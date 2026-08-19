#!/usr/bin/env python3
"""
Cross-Document Reference Engine — 跨文档引用引擎

Built on the AST layer (``core/ast_engine.py``): documents are parsed with
``MarkdownParser`` instead of string scanning. Headings become addressable
index nodes, and Markdown links that point at other indexed ``.md`` files
become bidirectional references ("entanglements") in the graph.

Boundaries / 边界:
- Only Markdown links whose target is another indexed ``.md`` file create
  references; external URLs and non-Markdown targets are ignored.
- Link targets are resolved relative to the linking document's directory.
- ``validate()`` reports indexed links whose target file is not part of the
  document set (broken cross-references).
"""

import hashlib
import json
import posixpath
import sys
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set
from pathlib import Path, PurePosixPath

if __package__ in (None, ""):
    # 允许 `python core/cross_ref.py` 按 README 演示入口直接运行
    # Allow direct execution as a README demo entry point.
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from core.ast_engine import ASTNode, NodeType, MarkdownParser


@dataclass
class CrossRefNode:
    """A node in the cross-document reference graph."""

    doc_id: str
    node_path: str
    content_hash: str
    title: str = ""
    refs: Set[str] = field(default_factory=set)


@dataclass
class BrokenReference:
    """A Markdown link whose target is not part of the indexed document set."""

    doc_id: str
    source_path: str
    target: str


class EntanglementIndex:
    """Bidirectional cross-document reference index built from Markdown ASTs."""

    def __init__(self, index_path: str = "incremental/entanglement_index.json",
                 parser: Optional[MarkdownParser] = None):
        self.index_path = index_path
        self.parser = parser or MarkdownParser()
        self.nodes: Dict[str, CrossRefNode] = {}
        self.broken_refs: List[BrokenReference] = []

    def build(self, docs_dir: str) -> None:
        """Build the reference index from a directory of Markdown documents."""
        docs_path = Path(docs_dir)
        self.nodes = {}
        self.broken_refs = []

        contents: Dict[str, str] = {}
        for doc_file in sorted(docs_path.glob("**/*.md")):
            doc_id = doc_file.relative_to(docs_path).as_posix()
            contents[doc_id] = doc_file.read_text(encoding="utf-8")

        # Pass 1: index every document and its headings.
        for doc_id, content in contents.items():
            self._index_document(doc_id, content)

        # Pass 2: resolve cross-document links once all nodes exist.
        for doc_id, content in contents.items():
            self._link_document(doc_id, content)

    def _heading_text(self, heading: ASTNode) -> str:
        """Extract plain text from a heading node (same convention as ASTEngine)."""
        return ''.join(
            c.content or ''
            for c in heading.children
            if c.type in (NodeType.TEXT, NodeType.STRONG, NodeType.EMPHASIS)
        )

    def _find_nodes(self, node: ASTNode, node_type: NodeType) -> List[ASTNode]:
        results = []
        if node.type == node_type:
            results.append(node)
        for child in node.children:
            results.extend(self._find_nodes(child, node_type))
        return results

    def _index_document(self, doc_id: str, content: str) -> None:
        """Index a single document's node and its headings via the AST layer."""
        root = self.parser.parse(content)

        doc_hash = hashlib.sha256(content.encode("utf-8")).hexdigest()[:16]
        self.nodes[doc_id] = CrossRefNode(
            doc_id=doc_id, node_path=doc_id, content_hash=doc_hash
        )

        for i, heading in enumerate(self._find_nodes(root, NodeType.HEADING)):
            title = self._heading_text(heading)
            node_path = f"{doc_id}#heading[{i}]"
            content_hash = hashlib.sha256(title.encode("utf-8")).hexdigest()[:16]
            self.nodes[node_path] = CrossRefNode(
                doc_id=doc_id, node_path=node_path,
                content_hash=content_hash, title=title,
            )

    def _resolve_link(self, from_doc_id: str, url: str) -> Optional[str]:
        """Resolve a Markdown link target to a doc_id, or None if out of scope."""
        target = url.split('#', 1)[0].strip()
        if not target or '://' in target or target.startswith('mailto:'):
            return None
        if not target.endswith('.md'):
            return None
        base = PurePosixPath(from_doc_id).parent
        resolved = posixpath.normpath(posixpath.join(str(base), target))
        return resolved

    def _link_document(self, doc_id: str, content: str) -> None:
        """Entangle a document's link sources with their indexed targets."""
        root = self.parser.parse(content)

        # Walk top-level blocks in order, tracking the enclosing heading so
        # that a link is attributed to the section that contains it.
        heading_order = {
            id(h): i for i, h in enumerate(self._find_nodes(root, NodeType.HEADING))
        }
        current_source = doc_id
        for block in root.children:
            if block.type == NodeType.HEADING:
                current_source = f"{doc_id}#heading[{heading_order[id(block)]}]"
                continue
            for link in self._find_nodes(block, NodeType.LINK):
                url = link.attributes.get('url', '')
                resolved = self._resolve_link(doc_id, url)
                if resolved is None:
                    continue
                if resolved in self.nodes:
                    self.entangle(current_source, resolved)
                else:
                    self.broken_refs.append(BrokenReference(
                        doc_id=doc_id, source_path=current_source, target=resolved,
                    ))

    def entangle(self, node_a: str, node_b: str) -> None:
        """Create bidirectional reference between two nodes."""
        if node_a in self.nodes and node_b in self.nodes:
            self.nodes[node_a].refs.add(node_b)
            self.nodes[node_b].refs.add(node_a)

    def validate(self) -> List[BrokenReference]:
        """Return indexed links whose target file is outside the document set."""
        return list(self.broken_refs)

    def save(self) -> None:
        """Persist the reference index to disk."""
        data = {
            node_path: {
                "doc_id": node.doc_id,
                "node_path": node.node_path,
                "content_hash": node.content_hash,
                "title": node.title,
                "refs": sorted(node.refs),
            }
            for node_path, node in self.nodes.items()
        }
        index_file = Path(self.index_path)
        index_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.index_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def load(self) -> None:
        """Load the reference index from disk."""
        try:
            with open(self.index_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            for node_path, node_data in data.items():
                self.nodes[node_path] = CrossRefNode(
                    doc_id=node_data["doc_id"],
                    node_path=node_data["node_path"],
                    content_hash=node_data["content_hash"],
                    title=node_data.get("title", ""),
                    refs=set(node_data.get("refs", [])),
                )
        except FileNotFoundError:
            self.nodes = {}

    def query_entangled(self, node_path: str, depth: int = 1) -> List[str]:
        """Query all referenced nodes up to given depth (BFS)."""
        if node_path not in self.nodes:
            return []

        result = []
        visited = {node_path}
        current_level = {node_path}

        for _ in range(depth):
            next_level = set()
            for node in current_level:
                if node in self.nodes:
                    for ref in self.nodes[node].refs:
                        if ref not in visited:
                            visited.add(ref)
                            next_level.add(ref)
                            result.append(ref)
            current_level = next_level

        return result


def demo():
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        docs = Path(tmp)
        (docs / "a.md").write_text(
            "# Doc A\n\nSee [Doc B](b.md) for details.\n", encoding="utf-8"
        )
        (docs / "b.md").write_text(
            "# Doc B\n\nBack to [Doc A](a.md).\n", encoding="utf-8"
        )

        index = EntanglementIndex(index_path=str(docs / "index.json"))
        index.build(tmp)

        print("=== 跨文档引用演示 ===")
        print(f"索引节点数: {len(index.nodes)}")
        print(f"a.md 的引用: {index.query_entangled('a.md')}")
        print(f"断链: {index.validate()}")


if __name__ == '__main__':
    demo()
