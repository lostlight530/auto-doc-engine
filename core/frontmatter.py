#!/usr/bin/env python3
"""Frontmatter parsing and bounded research-metadata validation.

Documents may carry an optional YAML frontmatter block. The schema remains
small and hand-written so metadata semantics stay inspectable without adding a
second validation framework.

Supported fields:
- ``title`` / ``description``: non-empty strings
- ``aliases`` / ``tags``: lists of non-empty strings
- ``authors`` / ``sources``: lists of non-empty strings
- ``status``: ``draft`` / ``active`` / ``archived`` / ``deprecated``
- ``updated``: date in ``YYYY-MM-DD`` form
- ``license`` / ``doi`` / ``language`` / ``artifact_id``: non-empty strings

The added research fields are deliberately simple. They provide portable input
for evidence packaging and RO-Crate export without pretending to be a complete
bibliographic or domain ontology.

Boundaries:
- Frontmatter is optional; a document without it produces no issues.
- Unknown fields are warnings for forward compatibility.
- Type and enum violations are errors.
"""

from __future__ import annotations

import datetime
import re
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

import yaml

KNOWN_FIELDS = {
    "title",
    "description",
    "aliases",
    "status",
    "updated",
    "tags",
    "authors",
    "sources",
    "license",
    "doi",
    "language",
    "artifact_id",
}
STATUSES = {"draft", "active", "archived", "deprecated"}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
STRING_FIELDS = {"title", "description", "license", "doi", "language", "artifact_id"}
LIST_FIELDS = {"aliases", "tags", "authors", "sources"}


class FrontmatterError(ValueError):
    """Raised when an existing frontmatter block is not a YAML mapping."""


@dataclass
class SchemaIssue:
    """A single frontmatter schema finding for one document."""

    doc_id: str
    field: str
    message: str
    severity: str  # "error" | "warning"

    def __str__(self) -> str:
        return f"[{self.severity}] {self.doc_id}: {self.field}: {self.message}"


def split_frontmatter(text: str) -> Tuple[Optional[str], str]:
    """Split ``text`` into ``(raw_yaml, body)``; return ``(None, text)`` if absent."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, text
    for i in range(1, len(lines)):
        if lines[i].strip() in ("---", "..."):
            return "\n".join(lines[1:i]), "\n".join(lines[i + 1 :])
    return None, text


def parse_frontmatter(text: str) -> Optional[Dict[str, Any]]:
    """Parse the frontmatter mapping; return ``None`` when no block exists."""
    raw, _ = split_frontmatter(text)
    if raw is None:
        return None
    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError as exc:
        raise FrontmatterError(f"invalid YAML frontmatter: {exc}") from exc
    if data is None:
        return {}
    if not isinstance(data, dict):
        raise FrontmatterError("frontmatter must be a YAML mapping")
    return data


def _is_non_empty_str(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _validate_str_list(field: str, value: Any, doc_id: str) -> List[SchemaIssue]:
    if not isinstance(value, list):
        return [SchemaIssue(doc_id, field, "must be a list of strings", "error")]
    issues: List[SchemaIssue] = []
    for item in value:
        if not _is_non_empty_str(item):
            issues.append(
                SchemaIssue(doc_id, field, f"entry {item!r} must be a non-empty string", "error")
            )
    return issues


def validate_schema(doc_id: str, data: Dict[str, Any]) -> List[SchemaIssue]:
    """Validate parsed frontmatter against the repository's bounded schema."""
    issues: List[SchemaIssue] = []
    for field, value in data.items():
        if field not in KNOWN_FIELDS:
            issues.append(SchemaIssue(doc_id, str(field), "unknown field", "warning"))
            continue
        if field in STRING_FIELDS:
            if not _is_non_empty_str(value):
                issues.append(SchemaIssue(doc_id, field, "must be a non-empty string", "error"))
        elif field in LIST_FIELDS:
            issues.extend(_validate_str_list(field, value, doc_id))
        elif field == "status":
            if value not in STATUSES:
                issues.append(
                    SchemaIssue(
                        doc_id,
                        field,
                        f"must be one of {sorted(STATUSES)}, got {value!r}",
                        "error",
                    )
                )
        elif field == "updated":
            if not (
                isinstance(value, datetime.date)
                or (isinstance(value, str) and DATE_RE.match(value))
            ):
                issues.append(
                    SchemaIssue(doc_id, field, "must be a date string YYYY-MM-DD", "error")
                )
    return issues


def validate_document(doc_id: str, text: str) -> List[SchemaIssue]:
    """Validate one document's frontmatter; absent frontmatter yields no issues."""
    try:
        data = parse_frontmatter(text)
    except FrontmatterError as exc:
        return [SchemaIssue(doc_id, "<frontmatter>", str(exc), "error")]
    if data is None:
        return []
    return validate_schema(doc_id, data)


def extract_aliases(text: str) -> List[str]:
    """Return declared aliases, or an empty list when absent/invalid."""
    try:
        data = parse_frontmatter(text)
    except FrontmatterError:
        return []
    if not data:
        return []
    aliases = data.get("aliases")
    if not isinstance(aliases, list):
        return []
    return [a.strip() for a in aliases if _is_non_empty_str(a)]


def extract_research_metadata(text: str) -> Dict[str, Any]:
    """Return normalized supported research metadata for packaging layers.

    Invalid frontmatter returns an empty mapping here; callers that need error
    detail should use ``validate_document`` first.
    """
    try:
        data = parse_frontmatter(text)
    except FrontmatterError:
        return {}
    if not data:
        return {}

    result: Dict[str, Any] = {}
    for field in KNOWN_FIELDS:
        if field not in data:
            continue
        value = data[field]
        if isinstance(value, datetime.date):
            value = value.isoformat()
        result[field] = value
    return result


def demo() -> None:
    sample = (
        "---\n"
        "title: 指南\n"
        "description: 可追踪文档示例\n"
        "aliases: [guide, 导引]\n"
        "status: active\n"
        "updated: 2026-08-23\n"
        "authors: [lostlight530]\n"
        "sources: [https://www.researchobject.org/ro-crate/specification/1.3/]\n"
        "license: MIT\n"
        "---\n\n# 指南\n"
    )
    print("=== frontmatter 校验演示 ===")
    print("aliases:", extract_aliases(sample))
    print("metadata:", extract_research_metadata(sample))
    print("issues:", validate_document("guide.md", sample))


if __name__ == "__main__":
    demo()
