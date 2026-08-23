#!/usr/bin/env python3
"""Document-set diagnostics for Markdown research collections.

``doctor`` composes the repository's existing document-analysis modules into a
single inspectable report:

- orphan documents (no inbound links), via ``core/cross_ref.py``;
- classified unresolved-link diagnostics and recurring-target backlog;
- directed reference-cycle detection;
- frontmatter schema validation, via ``core/frontmatter.py``;
- readability metrics, via ``core/readability.py`` (heuristic warnings);
- graph node/edge counts.

Exit codes:
- ``0``: no error-level findings;
- ``1``: error-level findings, or any warning when ``--strict`` is requested;
- ``2``: usage error such as a missing document directory.

The exit status is a local runtime signal for callers. It is not a GitHub merge
policy, scientific-validity decision, or peer-review result.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Set

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from core.cross_ref import EntanglementIndex, LinkDiagnostic
from core.frontmatter import SchemaIssue, split_frontmatter, validate_document
from core.readability import ReadabilityReport, analyze

MAX_CYCLES = 20
PROFILE = "auto-doc-engine/doctor@1"


@dataclass
class ReadabilityFinding:
    """Per-document readability metrics plus threshold warnings."""

    doc_id: str
    report: ReadabilityReport


@dataclass
class DoctorReport:
    """Aggregated diagnostic findings for one document set."""

    docs_dir: str
    doc_count: int = 0
    node_count: int = 0
    edge_count: int = 0
    orphan_docs: List[str] = field(default_factory=list)
    link_diagnostics: List[LinkDiagnostic] = field(default_factory=list)
    recurring: Dict[str, List[str]] = field(default_factory=dict)
    cycles: List[List[str]] = field(default_factory=list)
    schema_issues: List[SchemaIssue] = field(default_factory=list)
    readability: List[ReadabilityFinding] = field(default_factory=list)

    def errors(self) -> List[str]:
        """Return error-level findings."""
        messages = [
            f"broken link in {d.doc_id} ({d.source_path}) -> {d.target} [{d.kind}]"
            for d in self.link_diagnostics
        ]
        messages += [
            f"{issue.doc_id}: {issue.field}: {issue.message}"
            for issue in self.schema_issues
            if issue.severity == "error"
        ]
        return messages

    def warnings(self) -> List[str]:
        """Return warning-level findings."""
        messages = [f"orphan document (no inbound links): {doc_id}" for doc_id in self.orphan_docs]
        messages += ["reference cycle: " + " -> ".join(cycle + [cycle[0]]) for cycle in self.cycles]
        messages += [
            f"{issue.doc_id}: {issue.field}: {issue.message}"
            for issue in self.schema_issues
            if issue.severity == "warning"
        ]
        for finding in self.readability:
            for warning in finding.report.warnings:
                messages.append(f"{finding.doc_id}: {warning}")
        return messages

    def exit_code(self, strict: bool = False) -> int:
        """Return the command-line status for the current finding set."""
        if self.errors():
            return 1
        if strict and self.warnings():
            return 1
        return 0

    def to_dict(self) -> dict:
        """Return a JSON-serializable view of the report."""
        return {
            "profile": PROFILE,
            "docs_dir": self.docs_dir,
            "doc_count": self.doc_count,
            "graph": {"nodes": self.node_count, "edges": self.edge_count},
            "orphan_docs": self.orphan_docs,
            "link_diagnostics": [
                {
                    "doc_id": d.doc_id,
                    "source_path": d.source_path,
                    "target": d.target,
                    "kind": d.kind,
                    "suggestions": d.suggestions,
                }
                for d in self.link_diagnostics
            ],
            "recurring_backlog": self.recurring,
            "cycles": [cycle + [cycle[0]] for cycle in self.cycles],
            "schema_issues": [
                {
                    "doc_id": issue.doc_id,
                    "field": issue.field,
                    "message": issue.message,
                    "severity": issue.severity,
                }
                for issue in self.schema_issues
            ],
            "readability": [
                {
                    "doc_id": finding.doc_id,
                    "coleman_liau": finding.report.coleman_liau,
                    "latin_avg_words_per_sentence": finding.report.latin_avg_words_per_sentence,
                    "cjk_avg_chars_per_sentence": finding.report.cjk_avg_chars_per_sentence,
                    "warnings": finding.report.warnings,
                }
                for finding in self.readability
            ],
            "errors": self.errors(),
            "warnings": self.warnings(),
            "semantics": {
                "readability": "heuristic",
                "strict": "warnings_affect_exit_status_only_when_requested",
                "scientific_validity": False,
            },
        }

    def render_text(self) -> str:
        """Render a human-readable report."""
        lines = [
            "=== auto-doc-engine doctor ===",
            f"docs: {self.doc_count} documents | graph: {self.node_count} nodes, {self.edge_count} edges",
            "",
        ]
        lines.append(f"[links] broken: {len(self.link_diagnostics)}")
        for diagnostic in self.link_diagnostics:
            hint = ""
            if diagnostic.suggestions:
                hint = f" | did you mean: {', '.join(diagnostic.suggestions)}?"
            lines.append(f"  - {diagnostic.doc_id} -> {diagnostic.target} [{diagnostic.kind}]{hint}")
        if self.recurring:
            lines.append("[links] recurring dangling targets (backlog):")
            for target, doc_ids in self.recurring.items():
                lines.append(f"  - {target} <- referenced by {len(doc_ids)} docs: {', '.join(doc_ids)}")
        lines.append(f"[orphans] {len(self.orphan_docs)} document(s) without inbound links")
        for doc_id in self.orphan_docs:
            lines.append(f"  - {doc_id}")
        lines.append(f"[cycles] {len(self.cycles)} reference cycle(s)")
        for cycle in self.cycles:
            lines.append("  - " + " -> ".join(cycle + [cycle[0]]))
        lines.append(f"[frontmatter] {len(self.schema_issues)} schema issue(s)")
        for issue in self.schema_issues:
            lines.append(f"  - {issue}")
        readability_warnings = sum(len(f.report.warnings) for f in self.readability)
        lines.append(
            f"[readability] {len(self.readability)} document(s) analyzed, {readability_warnings} warning(s)"
        )
        for finding in self.readability:
            for warning in finding.report.warnings:
                lines.append(f"  - {finding.doc_id}: {warning}")
        return "\n".join(lines)


def find_cycles(edges: Dict[str, Set[str]], limit: int = MAX_CYCLES) -> List[List[str]]:
    """Enumerate elementary directed cycles, deduplicated up to rotation."""
    cycles: List[List[str]] = []
    seen = set()

    def dfs(start: str, node: str, path: List[str]) -> None:
        if len(cycles) >= limit:
            return
        for nxt in sorted(edges.get(node, ())):
            if nxt == start:
                rotations = [tuple(path[i:] + path[:i]) for i in range(len(path))]
                signature = min(rotations)
                if signature not in seen:
                    seen.add(signature)
                    cycles.append(list(signature))
            elif nxt not in path:
                dfs(start, nxt, path + [nxt])

    for start in sorted(edges):
        if len(cycles) >= limit:
            break
        dfs(start, start, [start])
    return cycles


def run_doctor(docs_dir: str, with_readability: bool = True) -> DoctorReport:
    """Inspect a directory of Markdown documents and return a ``DoctorReport``."""
    docs_path = Path(docs_dir)
    index = EntanglementIndex(index_path=str(docs_path / ".doctor_index.json"))
    index.build(docs_dir)

    report = DoctorReport(docs_dir=str(docs_dir))
    stats = index.graph_stats()
    report.node_count = stats["nodes"]
    report.edge_count = stats["edges"]

    doc_ids = sorted(key for key, node in index.nodes.items() if node.node_path == node.doc_id)
    report.doc_count = len(doc_ids)

    inbound: Set[str] = set()
    for targets in index.out_links.values():
        inbound.update(targets)
    report.orphan_docs = [doc_id for doc_id in doc_ids if doc_id not in inbound]

    report.link_diagnostics = index.diagnose()
    report.recurring = index.recurring_targets()
    # Mutual two-document backlinks are common navigation, not reported cycles.
    report.cycles = [cycle for cycle in find_cycles(index.out_links) if len(cycle) != 2]

    for doc_id in doc_ids:
        text = (docs_path / doc_id).read_text(encoding="utf-8")
        report.schema_issues.extend(validate_document(doc_id, text))
        if with_readability:
            _, body = split_frontmatter(text)
            report.readability.append(ReadabilityFinding(doc_id, analyze(body)))
    return report


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        prog="doctor",
        description=(
            "Inspect a Markdown document set (links, graph structure, frontmatter and readability) "
            "and expose explicit exit status."
        ),
    )
    parser.add_argument("docs_dir", help="directory containing Markdown documents")
    parser.add_argument("--json", action="store_true", help="emit the report as JSON")
    parser.add_argument("--strict", action="store_true", help="also return status 1 when warnings exist")
    parser.add_argument("--no-readability", action="store_true", help="skip readability metrics")
    args = parser.parse_args(argv)

    if not Path(args.docs_dir).is_dir():
        print(f"doctor: docs directory not found: {args.docs_dir}", file=sys.stderr)
        return 2

    report = run_doctor(args.docs_dir, with_readability=not args.no_readability)
    if args.json:
        print(json.dumps(report.to_dict(), indent=2, ensure_ascii=False))
    else:
        print(report.render_text())
    return report.exit_code(strict=args.strict)


def demo() -> None:
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        docs = Path(tmp)
        (docs / "a.md").write_text(
            "---\ntitle: Doc A\nstatus: active\nupdated: 2026-08-23\n---\n\n"
            "# Doc A\n\nSee [Doc B](b.md) and the [plan](plan.md).\n",
            encoding="utf-8",
        )
        (docs / "b.md").write_text(
            "# Doc B\n\nBack to [Doc A](a.md). Also [typo](aa.md).\n",
            encoding="utf-8",
        )
        (docs / "c.md").write_text(
            "# Doc C\n\nReferences the [plan](plan.md) too.\n",
            encoding="utf-8",
        )
        code = main([tmp])
        print(f"\nexit code: {code}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        raise SystemExit(main())
    demo()
