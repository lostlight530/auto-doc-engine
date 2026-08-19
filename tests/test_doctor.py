#!/usr/bin/env python3
"""Tests for the doctor health-check command (core/doctor.py)."""

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from core.doctor import DoctorReport, find_cycles, main, run_doctor


class DoctorTestCase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.docs = Path(self._tmp.name)

    def write_doc(self, rel_path: str, content: str) -> None:
        path = self.docs / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


class TestFindCycles(unittest.TestCase):
    def test_acyclic_graph_has_no_cycles(self):
        self.assertEqual(find_cycles({"a": {"b"}, "b": set()}), [])

    def test_mutual_links_form_one_cycle(self):
        cycles = find_cycles({"a": {"b"}, "b": {"a"}})
        self.assertEqual(len(cycles), 1)
        self.assertEqual(sorted(cycles[0]), ["a", "b"])

    def test_self_loop_is_a_cycle(self):
        cycles = find_cycles({"a": {"a"}})
        self.assertEqual(cycles, [["a"]])

    def test_rotation_duplicates_are_merged(self):
        cycles = find_cycles({"a": {"b"}, "b": {"c"}, "c": {"a"}})
        self.assertEqual(len(cycles), 1)

    def test_limit_caps_enumeration(self):
        edges = {str(i): {str((i + 1) % 10), str((i + 2) % 10)} for i in range(10)}
        self.assertLessEqual(len(find_cycles(edges, limit=3)), 3)


class TestRunDoctor(DoctorTestCase):
    def test_clean_set_reports_zero_exit_code(self):
        self.write_doc("a.md", "# A\n\nSee [B](b.md).\n")
        self.write_doc("b.md", "# B\n\nBack to [A](a.md).\n")
        report = run_doctor(str(self.docs))

        self.assertIsInstance(report, DoctorReport)
        self.assertEqual(report.doc_count, 2)
        self.assertEqual(report.link_diagnostics, [])
        self.assertEqual(report.orphan_docs, [])
        self.assertEqual(report.exit_code(), 0)
        self.assertEqual(report.exit_code(strict=True), 0)

    def test_broken_links_and_schema_errors_fail_the_gate(self):
        self.write_doc("a.md", "---\nstatus: hidden\n---\n\n# A\n\nSee [ghost](ghost.md).\n")
        report = run_doctor(str(self.docs))

        errors = report.errors()
        self.assertTrue(any("ghost.md" in e for e in errors))
        self.assertTrue(any("status" in e for e in errors))
        self.assertEqual(report.exit_code(), 1)

    def test_mutual_backlinks_are_not_reported_as_cycles(self):
        self.write_doc("a.md", "# A\n\nSee [B](b.md).\n")
        self.write_doc("b.md", "# B\n\nBack to [A](a.md).\n")
        report = run_doctor(str(self.docs))
        # A<->B is the normal backlink pattern, not a health issue.
        self.assertEqual(report.cycles, [])

    def test_orphans_and_cycles_are_warnings_only(self):
        self.write_doc("a.md", "# A\n\nSee [B](b.md).\n")
        self.write_doc("b.md", "# B\n\nSee [C](c.md).\n")
        self.write_doc("c.md", "# C\n\nBack to [A](a.md).\n")
        self.write_doc("lonely.md", "# Lonely\n")
        report = run_doctor(str(self.docs))

        self.assertEqual(report.orphan_docs, ["lonely.md"])
        self.assertEqual(len(report.cycles), 1)
        self.assertEqual(sorted(report.cycles[0]), ["a.md", "b.md", "c.md"])
        # Warnings do not fail by default, but do under strict mode.
        self.assertEqual(report.exit_code(), 0)
        self.assertEqual(report.exit_code(strict=True), 1)

    def test_recurring_backlog_reported(self):
        self.write_doc("a.md", "# A\n\nSee [plan](plan.md).\n")
        self.write_doc("b.md", "# B\n\nAlso [plan](plan.md).\n")
        report = run_doctor(str(self.docs))
        self.assertEqual(report.recurring, {"plan.md": ["a.md", "b.md"]})

    def test_readability_findings_collected_per_document(self):
        long_sentence = " ".join(["word"] * 40) + ". " + (" ".join(["word"] * 40) + ". ") * 2
        self.write_doc("verbose.md", f"# Verbose\n\n{long_sentence}\n")
        report = run_doctor(str(self.docs))

        self.assertEqual(len(report.readability), 1)
        finding = report.readability[0]
        self.assertEqual(finding.doc_id, "verbose.md")
        self.assertTrue(finding.report.warnings)
        # Readability warnings are warnings, not errors.
        self.assertEqual(report.errors(), [])
        self.assertEqual(report.exit_code(), 0)
        self.assertEqual(report.exit_code(strict=True), 1)

    def test_to_dict_is_json_serializable(self):
        self.write_doc("a.md", "# A\n\nSee [ghost](ghost.md).\n")
        report = run_doctor(str(self.docs))
        payload = json.loads(json.dumps(report.to_dict(), ensure_ascii=False))
        self.assertEqual(payload["doc_count"], 1)
        self.assertEqual(payload["link_diagnostics"][0]["target"], "ghost.md")
        self.assertIn("graph", payload)
        self.assertIn("errors", payload)


class TestDoctorCli(DoctorTestCase):
    def test_main_returns_zero_for_clean_set(self):
        self.write_doc("a.md", "# A\n\nSee [B](b.md).\n")
        self.write_doc("b.md", "# B\n\nBack to [A](a.md).\n")
        self.assertEqual(main([str(self.docs)]), 0)

    def test_main_returns_one_on_broken_links(self):
        self.write_doc("a.md", "# A\n\nSee [ghost](ghost.md).\n")
        self.assertEqual(main([str(self.docs)]), 1)

    def test_main_json_mode(self):
        self.write_doc("a.md", "# A\n")
        self.assertEqual(main([str(self.docs), "--json", "--strict"]), 1)

    def test_main_missing_directory_is_usage_error(self):
        self.assertEqual(main([str(self.docs / "nope")]), 2)


if __name__ == '__main__':
    unittest.main()
