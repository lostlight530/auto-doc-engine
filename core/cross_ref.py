#!/usr/bin/env python3
"""Cross-document Markdown reference indexing and diagnostics.

Documents are parsed through ``core.ast_engine.MarkdownParser``. Document and
heading nodes become an inspectable reference graph; only local Markdown-file
links participate. External URLs and non-Markdown targets are intentionally out
of scope.

Near-miss suggestions are heuristics based on ``difflib`` and aliases. They are
repair hints, not semantic equivalence claims.
"""

from __future__ import annotations

import difflib
import hashlib
import json
import posixpath
import sys
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath
from typing import Dict, List, Optional, Set
from urllib.parse import unquote, urlsplit

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from core.ast_engine import ASTNode, MarkdownParser, NodeType
from core.frontmatter import extract_aliases, split_frontmatter

RECURRING_MIN_REFS = 2


@dataclass
class CrossRefNode:
    doc_id: str
    node_path: str
    content_hash: str
    title: str = ""
    refs: Set[str] = field(default_factory=set)


@dataclass
class BrokenReference:
    doc_id: str
    source_path: str
    target: str


@dataclass
class LinkDiagnostic:
    doc_id: str
    source_path: str
    target: str
    kind: str  # near_miss | dangling
    suggestions: List[str] = field(default_factory=list)


class EntanglementIndex:
    """Historical name for the repository's bidirectional local-reference index."""

    def __init__(
        self,
        index_path: str = "incremental/entanglement_index.json",
        parser: Optional[MarkdownParser] = None,
    ):
        self.index_path = index_path
        self.parser = parser or MarkdownParser()
        self.nodes: Dict[str, CrossRefNode] = {}
        self.broken_refs: List[BrokenReference] = []
        self.aliases: Dict[str, str] = {}
        self.out_links: Dict[str, Set[str]] = {}

    def build(self, docs_dir: str) -> None:
        """Build the index from all Markdown files under ``docs_dir``."""
        docs_path = Path(docs_dir)
        if not docs_path.is_dir():
            raise FileNotFoundError(docs_dir)
        self.nodes = {}
        self.broken_refs = []
        self.aliases = {}
        self.out_links = {}
        contents = {
            path.relative_to(docs_path).as_posix(): path.read_text(encoding="utf-8")
            for path in sorted(docs_path.glob("**/*.md"))
        }
        for doc_id, content in contents.items():
            self._index_document(doc_id, content)
        for doc_id, content in contents.items():
            self._link_document(doc_id, content)

    def _plain_text(self, node: ASTNode) -> str:
        if node.type == NodeType.TEXT and not node.children:
            return node.content or ""
        if node.type == NodeType.IMAGE:
            return "".join(self._plain_text(child) for child in node.children)
        return "".join(self._plain_text(child) for child in node.children)

    def _heading_text(self, heading: ASTNode) -> str:
        return self._plain_text(heading).strip()

    def _find_nodes(self, node: ASTNode, node_type: NodeType) -> List[ASTNode]:
        results = [node] if node.type == node_type else []
        for child in node.children:
            results.extend(self._find_nodes(child, node_type))
        return results

    def _index_document(self, doc_id: str, content: str) -> None:
        _, body = split_frontmatter(content)
        root = self.parser.parse(body)
        digest = hashlib.sha256(content.encode("utf-8")).hexdigest()[:16]
        self.nodes[doc_id] = CrossRefNode(doc_id=doc_id, node_path=doc_id, content_hash=digest)
        self.out_links.setdefault(doc_id, set())
        for alias in extract_aliases(content):
            self.aliases.setdefault(alias, doc_id)
        for index, heading in enumerate(self._find_nodes(root, NodeType.HEADING)):
            title = self._heading_text(heading)
            node_path = f"{doc_id}#heading[{index}]"
            self.nodes[node_path] = CrossRefNode(
                doc_id=doc_id,
                node_path=node_path,
                content_hash=hashlib.sha256(title.encode("utf-8")).hexdigest()[:16],
                title=title,
            )

    def _resolve_link(self, from_doc_id: str, url: str) -> Optional[str]:
        """Normalize a local Markdown-file link to a document-set relative ID."""
        split = urlsplit(url.strip())
        if split.scheme or split.netloc:
            return None
        target = unquote(split.path).strip()
        if not target or not target.lower().endswith(".md"):
            return None
        if target.startswith("/"):
            return posixpath.normpath(target.lstrip("/"))
        base = PurePosixPath(from_doc_id).parent
        return posixpath.normpath(posixpath.join(str(base), target))

    def _link_document(self, doc_id: str, content: str) -> None:
        _, body = split_frontmatter(content)
        root = self.parser.parse(body)
        heading_order = {
            id(heading): index
            for index, heading in enumerate(self._find_nodes(root, NodeType.HEADING))
        }
        current_source = doc_id
        for block in root.children:
            if block.type == NodeType.HEADING:
                current_source = f"{doc_id}#heading[{heading_order[id(block)]}]"
                continue
            for link in self._find_nodes(block, NodeType.LINK):
                resolved = self._resolve_link(doc_id, str(link.attributes.get("url", "")))
                if resolved is None:
                    continue
                if resolved in self.nodes:
                    self.entangle(current_source, resolved)
                    self.out_links.setdefault(doc_id, set()).add(resolved)
                else:
                    self.broken_refs.append(
                        BrokenReference(doc_id=doc_id, source_path=current_source, target=resolved)
                    )

    def entangle(self, node_a: str, node_b: str) -> None:
        """Create a bidirectional graph edge when both nodes are indexed."""
        if node_a not in self.nodes or node_b not in self.nodes:
            raise KeyError("both reference nodes must exist")
        self.nodes[node_a].refs.add(node_b)
        self.nodes[node_b].refs.add(node_a)

    def validate(self) -> List[BrokenReference]:
        return list(self.broken_refs)

    def _near_miss_candidates(self) -> Dict[str, str]:
        candidates: Dict[str, str] = {}
        for key, node in self.nodes.items():
            if node.node_path == node.doc_id:
                candidates[key[:-3] if key.endswith(".md") else key] = key
        for alias in self.aliases:
            candidates.setdefault(alias, alias)
        return candidates

    def diagnose(self, cutoff: float = 0.6) -> List[LinkDiagnostic]:
        """Classify unresolved links with bounded lexical near-miss hints."""
        if not 0 <= cutoff <= 1:
            raise ValueError("cutoff must be between 0 and 1")
        candidates = self._near_miss_candidates()
        diagnostics: List[LinkDiagnostic] = []
        for ref in self.broken_refs:
            target_key = ref.target[:-3] if ref.target.endswith(".md") else ref.target
            matched = difflib.get_close_matches(target_key, list(candidates), n=3, cutoff=cutoff)
            target_base = PurePosixPath(target_key).name
            for key in candidates:
                if PurePosixPath(key).name == target_base and key not in matched:
                    matched.append(key)
            suggestions = list(dict.fromkeys(candidates[key] for key in matched))
            diagnostics.append(
                LinkDiagnostic(
                    doc_id=ref.doc_id,
                    source_path=ref.source_path,
                    target=ref.target,
                    kind="near_miss" if suggestions else "dangling",
                    suggestions=suggestions,
                )
            )
        return diagnostics

    def recurring_targets(self, min_refs: int = RECURRING_MIN_REFS) -> Dict[str, List[str]]:
        if min_refs < 1:
            raise ValueError("min_refs must be >= 1")
        refs_by_target: Dict[str, Set[str]] = {}
        for ref in self.broken_refs:
            refs_by_target.setdefault(ref.target, set()).add(ref.doc_id)
        return {
            target: sorted(doc_ids)
            for target, doc_ids in sorted(refs_by_target.items())
            if len(doc_ids) >= min_refs
        }

    def graph_stats(self) -> Dict[str, int]:
        edges = sum(len(node.refs) for node in self.nodes.values()) // 2
        return {"nodes": len(self.nodes), "edges": edges}

    def save(self) -> None:
        """Persist the resolved node/ref graph; diagnostic state is rebuilt from sources."""
        data = {
            node_path: {
                "doc_id": node.doc_id,
                "node_path": node.node_path,
                "content_hash": node.content_hash,
                "title": node.title,
                "refs": sorted(node.refs),
            }
            for node_path, node in sorted(self.nodes.items())
        }
        path = Path(self.index_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    def load(self) -> None:
        """Load a persisted node/ref graph; aliases and diagnostics are not reconstructed."""
        path = Path(self.index_path)
        if not path.exists():
            self.nodes = {}
            return
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError("cross-reference index must be a JSON object")
        self.nodes = {
            node_path: CrossRefNode(
                doc_id=node_data["doc_id"],
                node_path=node_data["node_path"],
                content_hash=node_data["content_hash"],
                title=node_data.get("title", ""),
                refs=set(node_data.get("refs", [])),
            )
            for node_path, node_data in data.items()
        }

    def query_entangled(self, node_path: str, depth: int = 1) -> List[str]:
        """Breadth-first traversal of explicit reference edges."""
        if depth < 0:
            raise ValueError("depth must be >= 0")
        if node_path not in self.nodes or depth == 0:
            return []
        result: List[str] = []
        visited = {node_path}
        current_level = {node_path}
        for _ in range(depth):
            next_level: Set[str] = set()
            for current in sorted(current_level):
                for ref in sorted(self.nodes[current].refs):
                    if ref not in visited:
                        visited.add(ref)
                        next_level.add(ref)
                        result.append(ref)
            current_level = next_level
            if not current_level:
                break
        return result


def demo() -> None:
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        docs = Path(tmp)
        (docs / "a.md").write_text("# **Doc A**\n\nSee [Doc B](b.md).\n", encoding="utf-8")
        (docs / "b.md").write_text("# Doc B\n\nBack to [Doc A](a.md).\n", encoding="utf-8")
        index = EntanglementIndex(index_path=str(docs / "index.json"))
        index.build(tmp)
        print("=== 跨文档引用演示 ===")
        print("stats:", index.graph_stats())
        print("a.md refs:", index.query_entangled("a.md"))


if __name__ == "__main__":
    demo()
