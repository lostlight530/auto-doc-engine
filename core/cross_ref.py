"""
Quantum Entanglement Index — Cross-Document Reference Engine
[EXPERIMENTAL] Not integrated into main rendering chain.

Maps bidirectional semantic links between documents, enabling
holistic knowledge graph construction from isolated AST trees.

Real-world: Cross-document reference tracking and knowledge graph construction.
"""

import hashlib
import json
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set
from pathlib import Path


@dataclass
class CrossRefNode:
    """A node in the cross-document reference graph."""

    doc_id: str
    node_path: str
    content_hash: str
    refs: Set[str] = field(default_factory=set)


@dataclass
class EntanglementIndex:
    """Quantum-inspired bidirectional reference index."""

    index_path: str = "incremental/entanglement_index.json"
    nodes: Dict[str, CrossRefNode] = field(default_factory=dict)

    def build(self, docs_dir: str) -> None:
        """Build entanglement index from document directory."""
        docs_path = Path(docs_dir)
        for doc_file in docs_path.glob("**/*.md"):
            doc_id = str(doc_file.relative_to(docs_path))
            content = doc_file.read_text(encoding="utf-8")
            self._index_document(doc_id, content)

    def _index_document(self, doc_id: str, content: str) -> None:
        """Index a single document's cross-references."""
        lines = content.split("\n")
        for i, line in enumerate(lines):
            if line.startswith("#"):
                heading = line.lstrip("# ").strip()
                node_path = f"{doc_id}#heading[{i}]"
                content_hash = hashlib.sha256(heading.encode()).hexdigest()[:16]
                node = CrossRefNode(
                    doc_id=doc_id, node_path=node_path, content_hash=content_hash
                )
                self.nodes[node_path] = node

    def entangle(self, node_a: str, node_b: str) -> None:
        """Create bidirectional entanglement between two nodes."""
        if node_a in self.nodes and node_b in self.nodes:
            self.nodes[node_a].refs.add(node_b)
            self.nodes[node_b].refs.add(node_a)

    def save(self) -> None:
        """Persist entanglement index to disk."""
        data = {
            node_path: {
                "doc_id": node.doc_id,
                "node_path": node.node_path,
                "content_hash": node.content_hash,
                "refs": list(node.refs),
            }
            for node_path, node in self.nodes.items()
        }
        index_file = Path(self.index_path)
        index_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.index_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def load(self) -> None:
        """Load entanglement index from disk."""
        try:
            with open(self.index_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            for node_path, node_data in data.items():
                self.nodes[node_path] = CrossRefNode(
                    doc_id=node_data["doc_id"],
                    node_path=node_data["node_path"],
                    content_hash=node_data["content_hash"],
                    refs=set(node_data.get("refs", [])),
                )
        except FileNotFoundError:
            self.nodes = {}

    def query_entangled(self, node_path: str, depth: int = 1) -> List[str]:
        """Query all entangled nodes up to given depth."""
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
