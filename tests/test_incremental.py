import unittest
from core.ast_engine import MarkdownParser
from core.incremental import DiffTracker

class TestIncrementalEngine(unittest.TestCase):
    def setUp(self):
        self.parser = MarkdownParser()
        self.tracker = DiffTracker(tracker_path=":memory:")

    def test_middle_insertion(self):
        old_doc = "# Header\n\nPara 1\n\nPara 2\n"
        new_doc = "# Header\n\nPara 1\n\nNew Para\n\nPara 2\n"

        old_ast = self.parser.parse(old_doc)
        new_ast = self.parser.parse(new_doc)

        changes = self.tracker.compute_diff('test', old_ast, new_ast)

        # In the recursive logic, Para 1 and Para 2 should be unchanged.
        # "New Para" and its surrounding blank lines should be 'add'.

        adds = [c for c in changes if c.action == 'add' and c.node_type == 'paragraph']
        modifies = [c for c in changes if c.action == 'modify']
        deletes = [c for c in changes if c.action == 'delete']

        self.assertEqual(len(adds), 1, "Should add exactly 1 paragraph")
        self.assertEqual(len(modifies), 0, "Should have 0 modifications when purely inserting")
        self.assertEqual(len(deletes), 0, "Should have 0 deletions when purely inserting")
        self.assertIn("New Para", adds[0].new_content)

    def test_modification(self):
        old_doc = "# Header\n\nPara 1\n\nPara 2\n"
        new_doc = "# Header\n\nPara 1 modified\n\nPara 2\n"

        old_ast = self.parser.parse(old_doc)
        new_ast = self.parser.parse(new_doc)

        changes = self.tracker.compute_diff('test', old_ast, new_ast)
        mod_paras = [c for c in changes if c.action == 'modify' and c.node_type == 'paragraph']

        self.assertEqual(len(mod_paras), 1, "Should modify exactly 1 paragraph")
        self.assertIn("Para 1 modified", mod_paras[0].new_content)

    def test_table_row_insertion(self):
        old_doc = "| A | B |\n|---|---|\n| 1 | 2 |\n"
        new_doc = "| A | B |\n|---|---|\n| 1 | 2 |\n| 3 | 4 |\n"

        old_ast = self.parser.parse(old_doc)
        new_ast = self.parser.parse(new_doc)

        changes = self.tracker.compute_diff('test', old_ast, new_ast)
        add_rows = [c for c in changes if c.action == 'add' and c.node_type == 'table_row']

        self.assertEqual(len(add_rows), 1, "Should add exactly 1 table row")
        self.assertIn("3", [c.new_content for c in changes if c.action == 'add' and c.node_type == 'text'])

if __name__ == '__main__':
    unittest.main()
