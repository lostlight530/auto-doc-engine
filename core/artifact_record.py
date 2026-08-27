#!/usr/bin/env python3
"""Portable research-artifact records for auto-doc-engine.

``auto-doc-engine/artifact-record`` is a small project-owned handoff profile
for one source document and its declared/generated derivatives. It sits between
frontmatter metadata and larger packaging formats such as RO-Crate:

- frontmatter describes the document;
- the artifact record binds that metadata to concrete byte identities,
  diagnostics, process disclosure and derivative files;
- RO-Crate may package the resulting files as a broader Research Object.

The profile is intentionally conservative. It does not claim source
credibility, authorship proof, peer review, scientific validity, semantic
identity, publisher compliance, or independent reproduction.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, Mapping, Optional
from urllib.parse import urlsplit

if __package__ in (None, ""):
    import sys

    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from core.frontmatter import extract_research_metadata, validate_document

PROFILE = "auto-doc-engine/artifact-record"
PROCESS_DISCLOSURE_PROFILE = "auto-doc-engine/process-disclosure"
REPRODUCIBILITY_LEVELS = {"R0", "R1", "R2", "R3"}


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def file_sha256(path: str | Path) -> str:
    candidate = Path(path)
    if not candidate.is_file():
        raise ValueError(f"artifact file does not exist: {candidate}")
    digest = hashlib.sha256()
    with candidate.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return "sha256:" + digest.hexdigest()


def canonical_sha256(value: Any) -> str:
    payload = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        default=str,
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def _reference(value: Any, *, kind: str = "reference") -> Optional[dict]:
    """Normalize a local file or opaque URI/reference without network access."""
    if value is None:
        return None
    text = str(value).strip()
    if not text:
        return None

    record = {"kind": kind, "ref": text}
    candidate = Path(text)
    if candidate.is_file():
        record.update(
            {
                "resolution": "local-file",
                "file_sha256": file_sha256(candidate),
                "size_bytes": candidate.stat().st_size,
            }
        )
        return record

    parsed = urlsplit(text)
    record["resolution"] = (
        "opaque-uri-not-dereferenced" if parsed.scheme else "opaque-reference-not-resolved"
    )
    return record


def _string_list(value: Any) -> list[str]:
    if not isinstance(value, (list, tuple, set)):
        return []
    result: list[str] = []
    seen = set()
    for item in value:
        text = str(item).strip()
        if text and text not in seen:
            result.append(text)
            seen.add(text)
    return result


def _process_disclosure(metadata: Mapping[str, Any]) -> dict:
    disclosure_ref = _reference(metadata.get("disclosure_ref"), kind="disclosure")
    result = {
        "profile": PROCESS_DISCLOSURE_PROFILE,
        "ai_assistance": metadata.get("ai_assistance", "not_declared"),
        "ai_tools": _string_list(metadata.get("ai_tools")),
        "human_review": metadata.get("human_review", "not_declared"),
        "semantics": (
            "declared preparation/review context only; not authorship proof, peer review, "
            "model validation, scientific validity, or publisher-policy compliance"
        ),
    }
    if disclosure_ref:
        result["disclosure_ref"] = disclosure_ref
    return result


def _validation_summary(source_path: Path, text: str) -> dict:
    issues = validate_document(source_path.as_posix(), text)
    serialized = [
        {
            "field": issue.field,
            "severity": issue.severity,
            "message": issue.message,
        }
        for issue in issues
    ]
    counts = {"error": 0, "warning": 0}
    for issue in serialized:
        severity = issue["severity"]
        counts[severity] = counts.get(severity, 0) + 1
    status = "error" if counts.get("error", 0) else (
        "warning" if counts.get("warning", 0) else "clean"
    )
    return {
        "profile": "auto-doc-engine/frontmatter-validation",
        "status": status,
        "counts": counts,
        "issues": serialized,
        "semantics": (
            "bounded frontmatter/schema diagnostics only; not factual, scientific, "
            "authorship, accessibility, or peer-review validation"
        ),
    }


def _file_record(kind: str, path: str | Path) -> dict:
    candidate = Path(path)
    if not candidate.is_file():
        raise ValueError(f"declared {kind} file does not exist: {candidate}")
    return {
        "kind": kind,
        "path": str(candidate),
        "file_sha256": file_sha256(candidate),
        "size_bytes": candidate.stat().st_size,
    }


def _normalize_derivatives(
    derivatives: Optional[Mapping[str, str | Path] | Iterable[str | Path]],
) -> list[dict]:
    if derivatives is None:
        return []

    records: list[dict] = []
    seen: set[tuple[str, str]] = set()
    if isinstance(derivatives, Mapping):
        items = derivatives.items()
    else:
        items = (("derivative", path) for path in derivatives)

    for kind, path in items:
        kind_text = str(kind).strip() or "derivative"
        candidate = Path(path)
        key = (kind_text, str(candidate))
        if key in seen:
            continue
        records.append(_file_record(kind_text, candidate))
        seen.add(key)
    return records


def build_artifact_record(
    source_path: str | Path,
    *,
    derivatives: Optional[Mapping[str, str | Path] | Iterable[str | Path]] = None,
    generated_with: Optional[str] = None,
    configuration_ref: Optional[str] = None,
    provenance_ref: Optional[str] = None,
    validation_ref: Optional[str] = None,
    reproducibility_level: str = "R0",
    execution_context: Optional[Mapping[str, Any]] = None,
) -> dict:
    """Build one bounded research-artifact record.

    ``R3`` is accepted only as caller-declared metadata. This function does not
    execute a rerun and therefore never upgrades a record to R3 by itself.
    """
    if reproducibility_level not in REPRODUCIBILITY_LEVELS:
        raise ValueError(
            f"reproducibility_level must be one of {sorted(REPRODUCIBILITY_LEVELS)}"
        )

    source = Path(source_path)
    if not source.is_file():
        raise ValueError(f"source document does not exist: {source}")
    text = source.read_text(encoding="utf-8")
    metadata = extract_research_metadata(text)
    derivatives_record = _normalize_derivatives(derivatives)

    declared_sources = [
        ref
        for ref in (
            _reference(value, kind="declared-source")
            for value in _string_list(metadata.get("sources"))
        )
        if ref
    ]

    authors = _string_list(metadata.get("authors"))
    core_metadata = {
        key: metadata.get(key)
        for key in (
            "title",
            "description",
            "status",
            "updated",
            "license",
            "doi",
            "language",
            "artifact_id",
            "tags",
        )
        if metadata.get(key) is not None
    }

    lineage = {
        "generated_with": generated_with,
        "configuration": _reference(configuration_ref, kind="configuration"),
        "provenance": _reference(provenance_ref, kind="provenance"),
        "validation": _reference(validation_ref, kind="validation"),
        "execution_context": dict(execution_context or {}),
        "semantics": (
            "declared generation/context references; local file hashes identify recorded bytes, "
            "while opaque references are not dereferenced or externally verified"
        ),
    }

    return {
        "profile": PROFILE,
        "generated_at": _now(),
        "artifact_id": str(metadata.get("artifact_id") or source.stem),
        "source_artifact": _file_record("source-document", source),
        "derivatives": derivatives_record,
        "metadata": core_metadata,
        "declared_authors": authors,
        "declared_sources": declared_sources,
        "process_disclosure": _process_disclosure(metadata),
        "validation": _validation_summary(source, text),
        "lineage": lineage,
        "record_identity": {
            "metadata_canonical_sha256": canonical_sha256(core_metadata),
            "identity_semantics": (
                "file_sha256 identifies bytes; metadata_canonical_sha256 identifies the selected "
                "normalized metadata mapping; neither proves semantic equivalence or truth"
            ),
        },
        "reproducibility": {
            "level": reproducibility_level,
            "declared_by_caller": True,
            "semantics": (
                "R0-R3 are local project terms; this record does not execute or verify a rerun. "
                "R3 requires an actual separate rerun plus a declared comparison criterion"
            ),
        },
        "payloads_embedded": False,
        "scientific_validity_claim": False,
        "authorship_claim": False,
        "peer_review_claim": False,
        "source_credibility_claim": False,
        "external_standard_conformance_claim": False,
    }


def write_artifact_record(
    record: dict,
    *,
    output: str | Path,
) -> Path:
    """Atomically write an artifact record and return its path."""
    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    temp = output_path.with_suffix(output_path.suffix + ".tmp")
    temp.write_text(
        json.dumps(record, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    os.replace(temp, output_path)
    return output_path


def _parse_derivative(value: str) -> tuple[str, str]:
    if "=" in value:
        kind, path = value.split("=", 1)
        if kind.strip() and path.strip():
            return kind.strip(), path.strip()
    return "derivative", value


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Write an auto-doc-engine artifact record for a research document"
    )
    parser.add_argument("source", help="source Markdown document")
    parser.add_argument(
        "--derivative",
        action="append",
        default=[],
        metavar="[KIND=]PATH",
        help="generated derivative; may be repeated",
    )
    parser.add_argument("--generated-with", help="tool/profile identifier for the producing path")
    parser.add_argument("--configuration-ref", help="local path or opaque configuration reference")
    parser.add_argument("--provenance-ref", help="local path or opaque provenance reference")
    parser.add_argument("--validation-ref", help="local path or opaque validation reference")
    parser.add_argument(
        "--reproducibility-level",
        choices=sorted(REPRODUCIBILITY_LEVELS),
        default="R0",
    )
    parser.add_argument("--output", required=True, help="artifact record output path")
    args = parser.parse_args(argv)

    derivatives: Dict[str, str] = {}
    for index, value in enumerate(args.derivative):
        kind, path = _parse_derivative(value)
        unique_kind = kind if kind not in derivatives else f"{kind}-{index + 1}"
        derivatives[unique_kind] = path

    try:
        record = build_artifact_record(
            args.source,
            derivatives=derivatives,
            generated_with=args.generated_with,
            configuration_ref=args.configuration_ref,
            provenance_ref=args.provenance_ref,
            validation_ref=args.validation_ref,
            reproducibility_level=args.reproducibility_level,
        )
        output = write_artifact_record(record, output=args.output)
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"artifact-record: {exc}", file=__import__("sys").stderr)
        return 1

    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
