#!/usr/bin/env python3
"""Tests for frontmatter parsing and schema validation (core/frontmatter.py)."""

import datetime
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from core.frontmatter import (
    FrontmatterError,
    extract_aliases,
    parse_frontmatter,
    split_frontmatter,
    validate_document,
    validate_schema,
)


class TestSplitAndParse(unittest.TestCase):
    def test_absent_frontmatter_returns_none(self):
        raw, body = split_frontmatter("# Just a heading\n")
        self.assertIsNone(raw)
        self.assertEqual(body, "# Just a heading\n")
        self.assertIsNone(parse_frontmatter("# Just a heading\n"))

    def test_frontmatter_block_is_separated_from_body(self):
        text = "---\ntitle: Guide\n---\n\n# Guide\n"
        raw, body = split_frontmatter(text)
        self.assertEqual(raw, "title: Guide")
        self.assertEqual(body.strip(), "# Guide")
        self.assertEqual(parse_frontmatter(text), {"title": "Guide"})

    def test_unclosed_fence_is_not_frontmatter(self):
        text = "---\ntitle: dangling\n\n# body\n"
        raw, _ = split_frontmatter(text)
        self.assertIsNone(raw)

    def test_invalid_yaml_raises_frontmatter_error(self):
        with self.assertRaises(FrontmatterError):
            parse_frontmatter("---\ntitle: [unclosed\n---\n")

    def test_non_mapping_frontmatter_raises(self):
        with self.assertRaises(FrontmatterError):
            parse_frontmatter("---\n- just\n- a\n- list\n---\n")

    def test_empty_frontmatter_parses_to_empty_mapping(self):
        self.assertEqual(parse_frontmatter("---\n---\n# Body\n"), {})


class TestSchemaValidation(unittest.TestCase):
    def test_valid_full_frontmatter_has_no_issues(self):
        data = {
            "title": "Guide",
            "aliases": ["guide", "handbook"],
            "status": "active",
            "updated": datetime.date(2026, 8, 5),  # pyyaml parses bare dates
            "tags": ["docs"],
        }
        self.assertEqual(validate_schema("guide.md", data), [])

    def test_updated_accepts_iso_date_string(self):
        self.assertEqual(
            validate_schema("d.md", {"updated": "2026-08-05"}), []
        )

    def test_unknown_field_is_warning_not_error(self):
        issues = validate_schema("d.md", {"mood": "happy"})
        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0].severity, "warning")

    def test_bad_status_is_error(self):
        issues = validate_schema("d.md", {"status": "hidden"})
        self.assertEqual([i.severity for i in issues], ["error"])
        self.assertIn("status", issues[0].field)

    def test_bad_updated_format_is_error(self):
        issues = validate_schema("d.md", {"updated": "2026/08/05"})
        self.assertEqual([i.severity for i in issues], ["error"])

    def test_aliases_must_be_non_empty_strings(self):
        issues = validate_schema("d.md", {"aliases": "not-a-list"})
        self.assertEqual([i.severity for i in issues], ["error"])
        issues = validate_schema("d.md", {"aliases": ["ok", 42]})
        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0].severity, "error")

    def test_title_must_be_non_empty_string(self):
        for bad in ("", "   ", 12):
            with self.subTest(bad=bad):
                issues = validate_schema("d.md", {"title": bad})
                self.assertEqual([i.severity for i in issues], ["error"])


class TestValidateDocument(unittest.TestCase):
    def test_document_without_frontmatter_is_clean(self):
        self.assertEqual(validate_document("d.md", "# No frontmatter\n"), [])

    def test_invalid_yaml_surfaces_as_error_issue(self):
        issues = validate_document("d.md", "---\ntitle: [unclosed\n---\n")
        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0].severity, "error")


class TestAliases(unittest.TestCase):
    def test_extract_aliases(self):
        text = "---\naliases: [guide, handbook]\n---\n# Guide\n"
        self.assertEqual(extract_aliases(text), ["guide", "handbook"])

    def test_extract_aliases_handles_missing_or_invalid(self):
        self.assertEqual(extract_aliases("# none\n"), [])
        self.assertEqual(extract_aliases("---\ntitle: [bad\n---\n"), [])
        self.assertEqual(extract_aliases("---\naliases: nope\n---\n"), [])


if __name__ == '__main__':
    unittest.main()
