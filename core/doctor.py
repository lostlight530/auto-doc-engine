#!/usr/bin/env python3
"""
Doctor — 文档集体检命令 (health check for a Markdown document set)

Mature knowledge-base CLIs (neuron, Quartz, Obsidian vault linters) ship a
"doctor"-style command that audits a whole document set and exits non-zero so
CI can gate on it. This module provides that entry point on top of the
existing engines — no new runtime dependencies:

- orphan documents (no inbound links), via ``core/cross_ref.py``
- classified broken-link diagnostics (near-miss vs dangling, recurring backlog)
- reference-cycle detection on the directed doc-level link graph
- frontmatter schema validation, via ``core/frontmatter.py``
- readability report metrics, via ``core/readability.py`` (warnings only)
- graph node/edge counts

Exit codes / 退出码:
- ``0``: no error-level findings
- ``1``: error-level findings (broken links, schema errors), or any warning
  when ``--strict`` is given
- ``2``: usage error (e.g. docs directory does not exist)

Boundaries / 边界:
- Orphans, cycles and readability findings are warnings, not gates, unless
  ``--strict`` is passed.
- The cycle check walks the *directed* doc-level graph. Mutual two-document
  links are the normal backlink pattern and are *not* reported as cycles;
  self-links and cycles of length >= 3 are (capped, see MAX_CYCLES).
"""

import argparse
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Set

if __package__ in (None, ""):
    # 允许 `python core/doctor.py` 直接运行
    # Allow direct execution as a script.
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from core.cross_ref import EntanglementIndex, LinkDiagnostic
from core.frontmatter import SchemaIssue, split_frontmatter, validate_document
from core.readability import ReadabilityReport, analyze

#: Cap on enumerated elementary cycles, so pathological graphs stay cheap.
MAX_CYCLES = 20


@dataclass
class ReadabilityFinding:
    """Per-document readability metrics plus any threshold warnings."""

    doc_id: str
    report: ReadabilityReport


@dataclass
class DoctorReport:
    """Aggregated health findings for one document set."""

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
        """Error-level findings (gate CI by default)."""
        msgs = [
            f"broken link in {d.doc_id} ({d.source_path}) -> {d.target} [{d.kind}]"
            for d in self.link_diagnostics
        ]
        msgs += [
            f"{i.doc_id}: {i.field}: {i.message}"
            for i in self.schema_issues if i.severity == "error"
        ]
        return msgs

    def warnings(self) -> List[str]:
        """Warning-level findings (gate CI only under --strict)."""
        msgs = [f"orphan document (no inbound links): {d}" for d in self.orphan_docs]
        msgs += ["reference cycle: " + " -> ".join(c + [c[0]]) for c in self.cycles]
        msgs += [
            f"{i.doc_id}: {i.field}: {i.message}"
            for i in self.schema_issues if i.severity == "warning"
        ]
        for finding in self.readability:
            for w in finding.report.warnings:
                msgs.append(f"{finding.doc_id}: {w}")
        return msgs

    def exit_code(self, strict: bool = False) -> int:
        if self.errors():
            return 1
        if strict and self.warnings():
            return 1
        return 0

    def to_dict(self) -> dict:
        """JSON-serializable view of the report."""
        return {
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
            "cycles": [c + [c[0]] for c in self.cycles],
            "schema_issues": [
                {
                    "doc_id": i.doc_id,
                    "field": i.field,
                    "message": i.message,
                    "severity": i.severity,
                }
                for i in self.schema_issues
            ],
            "readability": [
                {
                    "doc_id": f.doc_id,
                    "coleman_liau": f.report.coleman_liau,
                    "latin_avg_words_per_sentence": f.report.latin_avg_words_per_sentence,
                    "cjk_avg_chars_per_sentence": f.report.cjk_avg_chars_per_sentence,
                    "warnings": f.report.warnings,
                }
                for f in self.readability
            ],
            "errors": self.errors(),
            "warnings": self.warnings(),
        }

    def render_text(self) -> str:
        """Human-readable report."""
        lines = [
            "=== auto-doc-engine doctor ===",
            f"docs: {self.doc_count} documents | graph: {self.node_count} nodes, "
            f"{self.edge_count} edges",
            "",
        ]
        lines.append(f"[links] broken: {len(self.link_diagnostics)}")
        for d in self.link_diagnostics:
            hint = ""
            if d.suggestions:
                resolved = ", ".join(d.suggestions)
                hint = f" | did you mean: {resolved}?"
            lines.append(f"  - {d.doc_id} -> {d.target} [{d.kind}]{hint}")
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
        lines.append(f"[readability] {len(self.readability)} document(s) analyzed, "
                     f"{readability_warnings} warning(s)")
        for finding in self.readability:
            for w in finding.report.warnings:
                lines.append(f"  - {finding.doc_id}: {w}")
        return "\n".join(lines)


def find_cycles(edges: Dict[str, Set[str]], limit: int = MAX_CYCLES) -> List[List[str]]:
    """Enumerate elementary cycles in the directed doc-level link graph.

    Cycles are deduplicated up to rotation; enumeration stops at ``limit``.
    """
    cycles: List[List[str]] = []
    seen = set()

    def dfs(start: str, node: str, path: List[str]) -> None:
        if len(cycles) >= limit:
            return
        for nxt in sorted(edges.get(node, ())):
            if nxt == start:
                # Canonical rotation makes A->B->A and B->A->B the same cycle.
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
    """Audit a directory of Markdown documents and return a DoctorReport."""
    docs_path = Path(docs_dir)
    index = EntanglementIndex(index_path=str(docs_path / ".doctor_index.json"))
    index.build(docs_dir)

    report = DoctorReport(docs_dir=str(docs_dir))
    stats = index.graph_stats()
    report.node_count = stats["nodes"]
    report.edge_count = stats["edges"]

    doc_ids = sorted(k for k, n in index.nodes.items() if n.node_path == n.doc_id)
    report.doc_count = len(doc_ids)

    # Orphans: documents no other document links to.
    inbound: Set[str] = set()
    for targets in index.out_links.values():
        inbound.update(targets)
    report.orphan_docs = [d for d in doc_ids if d not in inbound]

    report.link_diagnostics = index.diagnose()
    report.recurring = index.recurring_targets()
    # Mutual two-document links are idiomatic backlinks, not health issues.
    report.cycles = [c for c in find_cycles(index.out_links) if len(c) != 2]

    # Frontmatter schema + readability per document.
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
        description="Audit a Markdown document set (links, orphans, cycles, "
                    "frontmatter schema, readability) and exit non-zero on findings.",
    )
    parser.add_argument("docs_dir", help="directory containing Markdown documents")
    parser.add_argument("--json", action="store_true", help="emit the report as JSON")
    parser.add_argument("--strict", action="store_true",
                        help="exit non-zero on warnings too (orphans, cycles, readability)")
    parser.add_argument("--no-readability", action="store_true",
                        help="skip readability metrics")
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
            "---\ntitle: Doc A\nstatus: active\nupdated: 2026-08-05\n---\n\n"
            "# Doc A\n\nSee [Doc B](b.md) and the [plan](plan.md).\n",
            encoding="utf-8",
        )
        (docs / "b.md").write_text(
            "# Doc B\n\nBack to [Doc A](a.md). Also [typo](aa.md).\n",
            encoding="utf-8",
        )
        (docs / "c.md").write_text("# Doc C\n\nReferences the [plan](plan.md) too.\n",
                                   encoding="utf-8")
        code = main([tmp])
        print(f"\nexit code: {code}")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        sys.exit(main())
    demo()
