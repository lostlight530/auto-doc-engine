#!/usr/bin/env python3
"""
Frontmatter parsing and hand-written schema validation — Frontmatter 解析与模式校验

Documents may carry an optional YAML frontmatter block. This module parses it
with ``pyyaml`` (an existing runtime dependency) and validates it against a
small, explicit schema — no new third-party validation library is introduced.

文档可以携带可选的 YAML frontmatter。本模块用既有依赖 pyyaml 解析，并依据一
个小型显式 schema 做校验，不引入新的第三方校验库。

Supported fields / 受支持字段:
- ``title``   : non-empty string (optional)
- ``aliases`` : list of non-empty strings; also feeds near-miss link matching
- ``status``  : one of ``draft`` / ``active`` / ``archived`` / ``deprecated``
- ``updated`` : date string in ``YYYY-MM-DD`` form
- ``tags``    : list of non-empty strings

Boundaries / 边界:
- Frontmatter is optional; a document without it produces no issues.
- Unknown fields are warnings, not errors (forward compatibility).
- Type and enum violations are errors.
"""

import datetime
import re
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

import yaml

KNOWN_FIELDS = {"title", "aliases", "status", "updated", "tags"}
STATUSES = {"draft", "active", "archived", "deprecated"}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


class FrontmatterError(ValueError):
    """Raised when a frontmatter block exists but is not valid YAML mapping."""


@dataclass
class SchemaIssue:
    """A single frontmatter schema finding for one document."""

    doc_id: str
    field: str
    message: str
    severity: str  # "error" | "warning"

    def __str__(self) -> str:  # pragma: no cover - display helper
        return f"[{self.severity}] {self.doc_id}: {self.field}: {self.message}"


def split_frontmatter(text: str) -> Tuple[Optional[str], str]:
    """Split ``text`` into (raw YAML block, body). Returns (None, text) if absent."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, text
    for i in range(1, len(lines)):
        if lines[i].strip() in ("---", "..."):
            return "\n".join(lines[1:i]), "\n".join(lines[i + 1:])
    # Opening fence without a closing one: not a frontmatter block.
    return None, text


def parse_frontmatter(text: str) -> Optional[Dict[str, Any]]:
    """Parse the frontmatter block. None if absent; raises FrontmatterError if invalid."""
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
    issues = []
    for item in value:
        if not _is_non_empty_str(item):
            issues.append(SchemaIssue(doc_id, field, f"entry {item!r} must be a non-empty string", "error"))
    return issues


def validate_schema(doc_id: str, data: Dict[str, Any]) -> List[SchemaIssue]:
    """Validate parsed frontmatter data against the hand-written schema."""
    issues: List[SchemaIssue] = []
    for field, value in data.items():
        if field not in KNOWN_FIELDS:
            issues.append(SchemaIssue(doc_id, str(field), "unknown field", "warning"))
            continue
        if field == "title":
            if not _is_non_empty_str(value):
                issues.append(SchemaIssue(doc_id, field, "must be a non-empty string", "error"))
        elif field in ("aliases", "tags"):
            issues.extend(_validate_str_list(field, value, doc_id))
        elif field == "status":
            if value not in STATUSES:
                issues.append(SchemaIssue(
                    doc_id, field,
                    f"must be one of {sorted(STATUSES)}, got {value!r}", "error",
                ))
        elif field == "updated":
            # pyyaml turns unquoted YYYY-MM-DD into datetime.date; both forms
            # are accepted, anything else is an error.
            if not (isinstance(value, datetime.date)
                    or (isinstance(value, str) and DATE_RE.match(value))):
                issues.append(SchemaIssue(doc_id, field, "must be a date string YYYY-MM-DD", "error"))
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
    """Return the declared aliases of a document (empty list when none/invalid)."""
    try:
        data = parse_frontmatter(text)
    except FrontmatterError:
        return []
    if not data:
        return []
    aliases = data.get("aliases")
    if not isinstance(aliases, list):
        return []
    return [a for a in aliases if _is_non_empty_str(a)]


def demo() -> None:
    sample = "---\ntitle: 指南\naliases: [guide, 导引]\nstatus: active\nupdated: 2026-08-05\n---\n\n# 指南\n"
    print("=== frontmatter 校验演示 ===")
    print("aliases:", extract_aliases(sample))
    print("issues:", validate_document("guide.md", sample))
    bad = "---\nstatus: hidden\nupdated: 2026/08/05\n---\n"
    for issue in validate_document("bad.md", bad):
        print(issue)


if __name__ == '__main__':
    demo()
