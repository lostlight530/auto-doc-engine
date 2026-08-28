#!/usr/bin/env python3
"""Typed artifact-lineage handoff for auto-doc-engine.

The lineage record links one existing ``auto-doc-engine/artifact-record`` to
caller-declared predecessor/related artifacts without inheriting scientific
validity from any referenced object.

It is intentionally offline: local files may be hashed; URI/opaque references
are retained without dereferencing. Relation labels describe declared artifact
history, not semantic equivalence, correctness, novelty, or reproducibility.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Optional
from urllib.parse import urlsplit

PROFILE = "auto-doc-engine/artifact-lineage"
SOURCE_PROFILE = "auto-doc-engine/artifact-record"
RELATIONS = {"derived-from", "revision-of", "supersedes", "uses", "related-to"}


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _file_sha256(path: str | Path) -> str:
    candidate = Path(path)
    digest = hashlib.sha256()
    with candidate.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return "sha256:" + digest.hexdigest()


def _reference(value: str) -> dict:
    text = str(value).strip()
    record = {"ref": text, "basis": "caller-declared", "basis_inferred": False}
    candidate = Path(text)
    if candidate.is_file():
        record.update(
            {
                "resolution": "local-file",
                "file_sha256": _file_sha256(candidate),
                "size_bytes": candidate.stat().st_size,
            }
        )
    else:
        parsed = urlsplit(text)
        record["resolution"] = (
            "opaque-uri-not-dereferenced" if parsed.scheme else "opaque-reference-not-resolved"
        )
    return record


def _load_json(path: str | Path) -> dict:
    candidate = Path(path)
    data = json.loads(candidate.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("artifact record must be a JSON object")
    source_profile = data.get("profile")
    if source_profile != SOURCE_PROFILE:
        raise ValueError(
            f"artifact lineage requires source profile {SOURCE_PROFILE!r}, got {source_profile!r}"
        )
    return data


def _coverage(relations: list[dict]) -> dict:
    resolution_counts: dict[str, int] = {}
    relation_counts: dict[str, int] = {}
    for item in relations:
        resolution = str(item.get("target", {}).get("resolution") or "not-recorded")
        resolution_counts[resolution] = resolution_counts.get(resolution, 0) + 1
        relation = str(item.get("relation") or "unknown")
        relation_counts[relation] = relation_counts.get(relation, 0) + 1
    local_count = resolution_counts.get("local-file", 0)
    total = len(relations)
    return {
        "relation_count": total,
        "by_relation": relation_counts,
        "by_resolution": resolution_counts,
        "local_file_ratio": (local_count / total) if total else None,
        "aggregate_score": None,
        "semantics": (
            "descriptive lineage/reference coverage only; not semantic equivalence, provenance soundness, "
            "scientific validity, novelty, reproducibility, or probability"
        ),
    }


def build_artifact_lineage(
    artifact_record_path: str | Path,
    *,
    relations: Iterable[tuple[str, str]],
) -> dict:
    artifact_path = Path(artifact_record_path)
    artifact = _load_json(artifact_path)
    normalized: list[dict] = []
    seen: set[tuple[str, str]] = set()

    for relation, target in relations:
        relation_text = str(relation).strip()
        target_text = str(target).strip()
        if relation_text not in RELATIONS:
            raise ValueError(f"unsupported relation {relation_text!r}; choose from {sorted(RELATIONS)}")
        if not target_text:
            raise ValueError("lineage target must be non-empty")
        key = (relation_text, target_text)
        if key in seen:
            continue
        normalized.append(
            {
                "relation": relation_text,
                "relation_basis": "caller-declared",
                "target": _reference(target_text),
                "scientific_validity_inherited": False,
                "reproducibility_inherited": False,
            }
        )
        seen.add(key)

    return {
        "profile": PROFILE,
        "generated_at": _now(),
        "artifact_record": {
            "path": str(artifact_path),
            "file_sha256": _file_sha256(artifact_path),
            "artifact_id": artifact.get("artifact_id"),
            "source_profile": artifact.get("profile"),
            "basis": "runtime-observed-local-bytes",
        },
        "relations": normalized,
        "lineage_coverage": _coverage(normalized),
        "assertion_basis": {
            "artifact_identity": "runtime-observed-local-bytes",
            "relations": "caller-declared-with-optional-local-resolution",
            "basis_inferred": False,
        },
        "semantics": {
            "derived-from": "declared derivation relation; not proof of complete provenance",
            "revision-of": "declared revision relation; not semantic equivalence",
            "supersedes": "declared replacement intent; does not invalidate or erase history",
            "uses": "declared dependency/use relation; not evidence sufficiency",
            "related-to": "declared loose relation with no stronger inference",
        },
        "scientific_validity_claim": False,
        "source_credibility_claim": False,
        "semantic_equivalence_claim": False,
        "external_standard_conformance_claim": False,
    }


def write_artifact_lineage(record: dict, output: str | Path) -> Path:
    path = Path(output)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(temp, path)
    return path


def _parse_relation(value: str) -> tuple[str, str]:
    if "=" not in value:
        raise argparse.ArgumentTypeError("relation must be RELATION=REFERENCE")
    relation, target = value.split("=", 1)
    relation = relation.strip()
    target = target.strip()
    if relation not in RELATIONS or not target:
        raise argparse.ArgumentTypeError(
            f"relation must use one of {sorted(RELATIONS)} and a non-empty reference"
        )
    return relation, target


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Write a typed artifact-lineage handoff record")
    parser.add_argument("artifact_record", help="existing auto-doc-engine artifact-record JSON")
    parser.add_argument(
        "--relation",
        action="append",
        default=[],
        type=_parse_relation,
        metavar="RELATION=REFERENCE",
        help="declared lineage relation; may be repeated",
    )
    parser.add_argument("--output", required=True)
    args = parser.parse_args(argv)
    record = build_artifact_lineage(args.artifact_record, relations=args.relation)
    write_artifact_lineage(record, args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
