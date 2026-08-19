#!/usr/bin/env python3
"""Executable documentation tests — 可执行文档测试

Python code blocks embedded in the repository's Markdown documentation are
living examples: this suite parses each document through the same mistune AST
layer used at runtime, extracts every ```python fenced block, and executes it
in an isolated namespace with a temporary working directory. Examples that
rot (API drift, renamed symbols, wrong output) fail here instead of failing
the reader.

Conventions / 约定:
- Only blocks fenced as ```python are executed; other languages are ignored.
- A block whose first non-empty line is ``# doc-example: skip`` is documented
  but not executed (for examples that need external tools such as pandoc).
- Each block runs with the repository root already importable and ``os.chdir``
  pointed at a fresh temporary directory.
"""

import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from core.ast_engine import MarkdownParser, NodeType

REPO_ROOT = Path(__file__).resolve().parents[1]

#: Documentation files whose python blocks must stay executable.
DOCUMENTS = [
    "README.md",
    "README_zh.md",
    "ARCHITECTURE.md",
    "ARCHITECTURE_zh.md",
]

SKIP_MARKER = "# doc-example: skip"


def extract_python_blocks(markdown_text: str):
    """Yield python code blocks from a Markdown document via the AST layer."""
    parser = MarkdownParser()
    root = parser.parse(markdown_text)
    blocks = []

    def walk(node):
        if node.type == NodeType.CODE_BLOCK:
            lang = (node.attributes.get("language") or "").strip().lower()
            if lang == "python":
                blocks.append(node.content or "")
        for child in node.children:
            walk(child)

    walk(root)
    return blocks


class ExecutableDocExamplesTests(unittest.TestCase):
    def test_every_python_block_in_docs_executes(self):
        executed = 0
        for rel_path in DOCUMENTS:
            doc_path = REPO_ROOT / rel_path
            text = doc_path.read_text(encoding="utf-8")
            blocks = extract_python_blocks(text)
            for i, code in enumerate(blocks):
                first_line = next((l for l in code.splitlines() if l.strip()), "")
                if first_line.strip() == SKIP_MARKER:
                    continue
                label = f"{rel_path}#python[{i}]"
                with self.subTest(example=label):
                    with tempfile.TemporaryDirectory() as tmp:
                        cwd = os.getcwd()
                        namespace = {"__name__": "__doc_example__"}
                        try:
                            os.chdir(tmp)
                            exec(compile(code, label, "exec"), namespace)
                        finally:
                            os.chdir(cwd)
                    executed += 1
        self.assertGreater(
            executed, 0,
            "documentation must contain at least one executable python example",
        )


if __name__ == '__main__':
    unittest.main()
