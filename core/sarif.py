#!/usr/bin/env python3
"""SARIF 2.1.0 + Approved Errata 01 export for document diagnostics.

The exporter maps ``core.doctor`` findings into a conservative SARIF result
profile so generic SARIF consumers can ingest the same evidence. It does not
reclassify Markdown diagnostics as source-code analysis and does not imply
certification by any downstream service.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Dict, List, Optional

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from core.doctor import PROFILE as DOCTOR_PROFILE
from core.doctor import run_doctor

SARIF_VERSION = "2.1.0"
SARIF_SCHEMA = (
    "https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/"
    "schemas/sarif-schema-2.1.0.json"
)
SARIF_PROFILE = "auto-doc-engine/sarif"
FINGERPRINT_KEY = "autoDocFinding"
TOOL_NAME = "auto-doc-engine doctor"
TOOL_URI = "https://github.com/lostlight530/auto-doc-engine"


def _fingerprint(*parts: object) -> str:
    canonical = "\x1f".join(str(part) for part in parts)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def _location(uri: str) -> List[dict]:
    return [{"physicalLocation": {"artifactLocation": {"uri": uri}}}]


def _result(
    rule_id: str,
    level: str,
    message: str,
    uri: str,
    *identity: object,
    properties: Optional[dict] = None,
) -> dict:
    result = {
        "ruleId": rule_id,
        "level": level,
        "message": {"text": message},
        "locations": _location(uri),
        "partialFingerprints": {
            FINGERPRINT_KEY: _fingerprint(rule_id, uri, *identity),
        },
    }
    if properties:
        result["properties"] = properties
    return result


def report_to_sarif(report) -> dict:
    """Convert a ``DoctorReport`` into the repository SARIF profile."""
    results: List[dict] = []
    rules: Dict[str, dict] = {}

    def register(rule_id: str, name: str, description: str) -> None:
        rules.setdefault(
            rule_id,
            {
                "id": rule_id,
                "name": name,
                "shortDescription": {"text": description},
            },
        )

    for diagnostic in report.link_diagnostics:
        rule_id = f"doc.link.{diagnostic.kind}"
        register(rule_id, "Unresolved document link", "A local Markdown target cannot be resolved.")
        hint = (
            f" Suggestions: {', '.join(diagnostic.suggestions)}."
            if diagnostic.suggestions
            else ""
        )
        results.append(
            _result(
                rule_id,
                "error",
                f"Unresolved link target '{diagnostic.target}' ({diagnostic.kind}).{hint}",
                diagnostic.source_path,
                diagnostic.doc_id,
                diagnostic.target,
                properties={
                    "target": diagnostic.target,
                    "kind": diagnostic.kind,
                    "suggestions": list(diagnostic.suggestions),
                },
            )
        )

    for issue in report.schema_issues:
        rule_id = f"doc.frontmatter.{issue.severity}"
        register(
            rule_id,
            "Frontmatter schema",
            "YAML frontmatter violates or extends the repository metadata schema.",
        )
        level = "error" if issue.severity == "error" else "warning"
        results.append(
            _result(
                rule_id,
                level,
                f"{issue.field}: {issue.message}",
                issue.doc_id,
                issue.field,
                issue.message,
                properties={"field": issue.field, "severity": issue.severity},
            )
        )

    register("doc.graph.orphan", "Orphan document", "A document has no inbound document links.")
    for doc_id in report.orphan_docs:
        results.append(
            _result(
                "doc.graph.orphan",
                "warning",
                "Document has no inbound links.",
                doc_id,
                doc_id,
            )
        )

    register("doc.graph.cycle", "Reference cycle", "The directed document graph contains a reported cycle.")
    for cycle in report.cycles:
        if not cycle:
            continue
        chain = cycle + [cycle[0]]
        results.append(
            _result(
                "doc.graph.cycle",
                "warning",
                "Reference cycle: " + " -> ".join(chain),
                cycle[0],
                *cycle,
                properties={"cycle": chain},
            )
        )

    register(
        "doc.readability.warning",
        "Readability signal",
        "A descriptive readability heuristic exceeded a project threshold.",
    )
    for finding in report.readability:
        for warning in finding.report.warnings:
            results.append(
                _result(
                    "doc.readability.warning",
                    "warning",
                    warning,
                    finding.doc_id,
                    warning,
                    properties={"semantics": "heuristic"},
                )
            )

    return {
        "version": SARIF_VERSION,
        "$schema": SARIF_SCHEMA,
        "runs": [
            {
                "tool": {
                    "driver": {
                        "name": TOOL_NAME,
                        "informationUri": TOOL_URI,
                        "rules": [rules[key] for key in sorted(rules)],
                    }
                },
                "results": results,
                "properties": {
                    "docsDir": report.docs_dir,
                    "documentCount": report.doc_count,
                    "graph": {"nodes": report.node_count, "edges": report.edge_count},
                    "profile": SARIF_PROFILE,
                    "sourceProfile": DOCTOR_PROFILE,
                    "scientificValidityClaim": False,
                },
            }
        ],
    }


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Export document diagnostics as SARIF 2.1.0")
    parser.add_argument("docs_dir", help="directory containing Markdown documents")
    parser.add_argument("-o", "--output", help="write SARIF JSON here; stdout when omitted")
    parser.add_argument("--strict", action="store_true", help="return non-zero on warnings as well as errors")
    parser.add_argument("--no-readability", action="store_true", help="skip readability findings")
    args = parser.parse_args(argv)

    if not Path(args.docs_dir).is_dir():
        print(f"sarif: docs directory not found: {args.docs_dir}", file=sys.stderr)
        return 2

    report = run_doctor(args.docs_dir, with_readability=not args.no_readability)
    rendered = json.dumps(report_to_sarif(report), ensure_ascii=False, indent=2) + "\n"
    if args.output:
        path = Path(args.output)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return report.exit_code(strict=args.strict)


if __name__ == "__main__":
    raise SystemExit(main())
