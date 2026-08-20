#!/usr/bin/env python3
"""Tests for the cross-document reference engine (core/cross_ref.py)."""

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from core.cross_ref import EntanglementIndex, BrokenReference


class CrossRefTestCase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.docs = Path(self._tmp.name)
        self.index_path = str(self.docs / "out" / "index.json")

    def write_doc(self, rel_path: str, content: str) -> None:
        path = self.docs / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def build_index(self) -> EntanglementIndex:
        index = EntanglementIndex(index_path=self.index_path)
        index.build(str(self.docs))
        return index


class TestHeadingIndexing(CrossRefTestCase):
    def test_document_and_heading_nodes_indexed(self):
        self.write_doc("guide.md", "# Intro\n\nText.\n\n## Setup\n\nMore.\n")
        index = self.build_index()

        self.assertIn("guide.md", index.nodes)
        self.assertIn("guide.md#heading[0]", index.nodes)
        self.assertIn("guide.md#heading[1]", index.nodes)
        self.assertEqual(index.nodes["guide.md#heading[0]"].title, "Intro")
        self.assertEqual(index.nodes["guide.md#heading[1]"].title, "Setup")
        for node in index.nodes.values():
            self.assertTrue(node.content_hash, "each node must carry a content hash")

    def test_subdirectory_doc_ids_use_posix_paths(self):
        self.write_doc("sub/deep.md", "# Deep\n")
        index = self.build_index()
        self.assertIn("sub/deep.md", index.nodes)


class TestCrossDocumentLinks(CrossRefTestCase):
    def test_markdown_link_creates_bidirectional_reference(self):
        self.write_doc("a.md", "# Doc A\n\nSee [Doc B](sub/b.md).\n")
        self.write_doc("sub/b.md", "# Doc B\n")
        index = self.build_index()

        # The link sits under "Doc A", so the heading node is the source.
        self.assertIn("sub/b.md", index.query_entangled("a.md#heading[0]"))
        self.assertIn("a.md#heading[0]", index.query_entangled("sub/b.md"))
        self.assertEqual(index.validate(), [])

    def test_link_before_any_heading_attributed_to_document_node(self):
        self.write_doc("a.md", "See [B](b.md).\n\n# Later\n")
        self.write_doc("b.md", "# B\n")
        index = self.build_index()

        self.assertIn("b.md", index.query_entangled("a.md"))

    def test_depth_limited_traversal(self):
        self.write_doc("a.md", "See [B](b.md).\n")
        self.write_doc("b.md", "See [C](c.md).\n")
        self.write_doc("c.md", "# C\n")
        index = self.build_index()

        self.assertEqual(index.query_entangled("a.md", depth=1), ["b.md"])
        deep = index.query_entangled("a.md", depth=2)
        self.assertIn("b.md", deep)
        self.assertIn("c.md", deep)

    def test_external_and_non_markdown_links_ignored(self):
        self.write_doc(
            "a.md",
            "# A\n\n[site](https://example.com/x.md) "
            "[mail](mailto:a@b.c) [img](pic.png)\n",
        )
        index = self.build_index()

        self.assertEqual(index.query_entangled("a.md#heading[0]"), [])
        self.assertEqual(index.validate(), [])

    def test_broken_markdown_link_reported_by_validate(self):
        self.write_doc("a.md", "# A\n\nSee [missing](missing.md).\n")
        index = self.build_index()

        broken = index.validate()
        self.assertEqual(len(broken), 1)
        self.assertIsInstance(broken[0], BrokenReference)
        self.assertEqual(broken[0].doc_id, "a.md")
        self.assertEqual(broken[0].source_path, "a.md#heading[0]")
        self.assertEqual(broken[0].target, "missing.md")
        # A broken link must not create a graph edge.
        self.assertEqual(index.query_entangled("a.md#heading[0]"), [])


class TestPersistence(CrossRefTestCase):
    def test_save_load_roundtrip_preserves_refs(self):
        self.write_doc("a.md", "See [B](b.md).\n")
        self.write_doc("b.md", "# B\n")
        index = self.build_index()
        index.save()

        with open(self.index_path, "r", encoding="utf-8") as f:
            raw = json.load(f)
        self.assertIn("a.md", raw)
        self.assertEqual(raw["a.md"]["refs"], ["b.md"])

        restored = EntanglementIndex(index_path=self.index_path)
        restored.load()
        self.assertEqual(restored.query_entangled("a.md"), ["b.md"])
        self.assertEqual(restored.query_entangled("b.md"), ["a.md"])

    def test_load_missing_index_yields_empty_graph(self):
        index = EntanglementIndex(index_path=self.index_path)
        index.load()
        self.assertEqual(index.nodes, {})


if __name__ == '__main__':
    unittest.main()
