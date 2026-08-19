#!/usr/bin/env python3
"""Tests for classified broken-link diagnostics (core/cross_ref.py)."""

import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from core.cross_ref import EntanglementIndex, LinkDiagnostic


class DiagnosticsTestCase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.docs = Path(self._tmp.name)

    def write_doc(self, rel_path: str, content: str) -> None:
        path = self.docs / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def build_index(self) -> EntanglementIndex:
        index = EntanglementIndex(index_path=str(self.docs / "out" / "index.json"))
        index.build(str(self.docs))
        return index


class TestNearMissVsDangling(DiagnosticsTestCase):
    def test_typo_target_is_near_miss_with_suggestion(self):
        self.write_doc("getting-started.md", "# Getting Started\n")
        self.write_doc("a.md", "# A\n\nSee [guide](gettng-started.md).\n")
        index = self.build_index()

        diagnostics = index.diagnose()
        self.assertEqual(len(diagnostics), 1)
        diag = diagnostics[0]
        self.assertIsInstance(diag, LinkDiagnostic)
        self.assertEqual(diag.kind, "near_miss")
        self.assertIn("getting-started.md", diag.suggestions)

    def test_planned_target_is_dangling_without_suggestions(self):
        self.write_doc("a.md", "# A\n\nSee the [roadmap](roadmap-2027.md).\n")
        index = self.build_index()

        diagnostics = index.diagnose()
        self.assertEqual(len(diagnostics), 1)
        self.assertEqual(diagnostics[0].kind, "dangling")
        self.assertEqual(diagnostics[0].suggestions, [])

    def test_moved_file_suggested_via_basename(self):
        self.write_doc("sub/guide.md", "# Guide\n")
        self.write_doc("a.md", "# A\n\nSee [guide](guide.md).\n")
        index = self.build_index()

        diagnostics = index.diagnose()
        self.assertEqual(len(diagnostics), 1)
        self.assertEqual(diagnostics[0].kind, "near_miss")
        self.assertIn("sub/guide.md", diagnostics[0].suggestions)

    def test_frontmatter_alias_feeds_near_miss(self):
        self.write_doc(
            "internal/handbook.md",
            "---\ntitle: Handbook\naliases: [onboarding-guide]\n---\n\n# Handbook\n",
        )
        self.write_doc("a.md", "# A\n\nSee [onboarding](onbording-guide.md).\n")
        index = self.build_index()

        diagnostics = index.diagnose()
        self.assertEqual(len(diagnostics), 1)
        self.assertEqual(diagnostics[0].kind, "near_miss")
        self.assertIn("onboarding-guide", diagnostics[0].suggestions)
        # The alias resolves to the declaring document.
        self.assertEqual(index.aliases["onboarding-guide"], "internal/handbook.md")

    def test_clean_set_has_no_diagnostics(self):
        self.write_doc("a.md", "# A\n\nSee [B](b.md).\n")
        self.write_doc("b.md", "# B\n")
        index = self.build_index()
        self.assertEqual(index.diagnose(), [])


class TestRecurringBacklog(DiagnosticsTestCase):
    def test_target_referenced_by_two_docs_is_recurring(self):
        self.write_doc("a.md", "# A\n\nSee [plan](plan.md).\n")
        self.write_doc("b.md", "# B\n\nAlso [plan](plan.md).\n")
        self.write_doc("c.md", "# C\n\nOnly [ghost](ghost.md).\n")
        index = self.build_index()

        recurring = index.recurring_targets()
        self.assertEqual(recurring, {"plan.md": ["a.md", "b.md"]})

    def test_min_refs_threshold_is_respected(self):
        self.write_doc("a.md", "# A\n\nSee [plan](plan.md) and [p2](plan.md).\n")
        index = self.build_index()
        # Two links from the same document do not make a recurring target.
        self.assertEqual(index.recurring_targets(), {})


class TestGraphStatsAndOutLinks(DiagnosticsTestCase):
    def test_graph_stats_counts_nodes_and_undirected_edges(self):
        self.write_doc("a.md", "# A\n\nSee [B](b.md).\n")
        self.write_doc("b.md", "# B\n")
        index = self.build_index()

        stats = index.graph_stats()
        # 2 document nodes + 2 heading nodes; 1 bidirectional edge.
        self.assertEqual(stats["nodes"], 4)
        self.assertEqual(stats["edges"], 1)

    def test_out_links_records_directed_doc_level_edges(self):
        self.write_doc("a.md", "# A\n\nSee [B](b.md).\n")
        self.write_doc("b.md", "# B\n")
        index = self.build_index()

        self.assertEqual(index.out_links["a.md"], {"b.md"})
        self.assertEqual(index.out_links["b.md"], set())


if __name__ == '__main__':
    unittest.main()
