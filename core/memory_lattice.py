"""Experimental structured node store with graph links and numeric indexes.

[EXPERIMENTAL] Not integrated into the canonical document pipeline.

The historical "memory lattice" name is retained for API continuity. The
implementation is a local JSON-persisted node map with bidirectional links and
rounded numeric-dimension indexes; it is not a vector database, semantic memory
system or mathematical lattice.
"""

from __future__ import annotations

import hashlib
import json
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple


@dataclass
class LatticeNode:
    """One stored node with byte-identity metadata and explicit links."""

    node_id: str
    content_hash: str
    data: Dict[str, Any]
    dimensions: Dict[str, float] = field(default_factory=dict)
    neighbors: Set[str] = field(default_factory=set)
    created_at: float = field(default_factory=time.time)
    last_accessed: float = field(default_factory=time.time)
    access_count: int = 0


class MemoryLatticeVault:
    """Local structured node store with rounded numeric indexes."""

    def __init__(self, vault_path: str = "incremental/memory_lattice.json"):
        self.vault_path = vault_path
        self._nodes: Dict[str, LatticeNode] = {}
        self._dimension_index: Dict[str, Dict[str, Set[str]]] = {}

    @staticmethod
    def _content_hash(data: Dict[str, Any]) -> str:
        canonical = json.dumps(data, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
        return hashlib.sha256(canonical.encode("utf-8")).hexdigest()[:16]

    def _remove_from_dimension_index(self, node_id: str) -> None:
        for buckets in self._dimension_index.values():
            for node_ids in buckets.values():
                node_ids.discard(node_id)

    def _index_node(self, node: LatticeNode) -> None:
        for dimension, value in node.dimensions.items():
            bucket = self._bucket_value(value)
            self._dimension_index.setdefault(dimension, {}).setdefault(bucket, set()).add(node.node_id)

    def _rebuild_dimension_index(self) -> None:
        self._dimension_index = {}
        for node in self._nodes.values():
            self._index_node(node)

    def store(
        self,
        node_id: str,
        data: Dict[str, Any],
        dimensions: Optional[Dict[str, float]] = None,
    ) -> LatticeNode:
        """Store or replace a node and keep numeric indexes consistent."""
        if not node_id:
            raise ValueError("node_id must be non-empty")
        self._remove_from_dimension_index(node_id)
        previous = self._nodes.get(node_id)
        node = LatticeNode(
            node_id=node_id,
            content_hash=self._content_hash(data),
            data=data,
            dimensions=dimensions or {},
            neighbors=set(previous.neighbors) if previous else set(),
            created_at=previous.created_at if previous else time.time(),
            access_count=previous.access_count if previous else 0,
        )
        self._nodes[node_id] = node
        self._index_node(node)
        return node

    def link(self, node_a: str, node_b: str) -> None:
        """Create a bidirectional link; both endpoints must exist."""
        if node_a not in self._nodes or node_b not in self._nodes:
            raise KeyError("both linked nodes must already exist")
        if node_a == node_b:
            return
        self._nodes[node_a].neighbors.add(node_b)
        self._nodes[node_b].neighbors.add(node_a)

    def retrieve(self, node_id: str) -> Optional[LatticeNode]:
        """Retrieve a node and update access metadata."""
        node = self._nodes.get(node_id)
        if node:
            node.last_accessed = time.time()
            node.access_count += 1
        return node

    def query_by_dimension(
        self, dimension: str, value_range: Tuple[float, float]
    ) -> List[str]:
        """Return indexed node IDs whose rounded bucket falls within a range."""
        if dimension not in self._dimension_index:
            return []
        minimum, maximum = value_range
        if minimum > maximum:
            raise ValueError("value_range minimum must be <= maximum")
        results: Set[str] = set()
        for bucket, node_ids in self._dimension_index[dimension].items():
            value = float(bucket)
            if minimum <= value <= maximum:
                results.update(node_ids)
        return sorted(results)

    def traverse(self, start_id: str, max_depth: int = 2) -> List[str]:
        """Breadth-first traversal over explicit neighbor links."""
        if start_id not in self._nodes or max_depth <= 0:
            return []
        visited = {start_id}
        current = {start_id}
        result: List[str] = []
        for _ in range(max_depth):
            next_level: Set[str] = set()
            for node_id in sorted(current):
                node = self._nodes.get(node_id)
                if not node:
                    continue
                for neighbor in sorted(node.neighbors):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        next_level.add(neighbor)
                        result.append(neighbor)
            current = next_level
            if not current:
                break
        return result

    @staticmethod
    def _bucket_value(value: float) -> str:
        return str(round(float(value), 2))

    def save(self) -> None:
        """Persist nodes to JSON. This is local persistence, not an append-only ledger."""
        data = {
            node_id: {
                "node_id": node.node_id,
                "content_hash": node.content_hash,
                "data": node.data,
                "dimensions": node.dimensions,
                "neighbors": sorted(node.neighbors),
                "created_at": node.created_at,
                "last_accessed": node.last_accessed,
                "access_count": node.access_count,
            }
            for node_id, node in sorted(self._nodes.items())
        }
        vault_file = Path(self.vault_path)
        vault_file.parent.mkdir(parents=True, exist_ok=True)
        vault_file.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    def load(self) -> None:
        """Load persisted nodes and rebuild derived numeric indexes."""
        try:
            raw = Path(self.vault_path).read_text(encoding="utf-8")
        except FileNotFoundError:
            self._nodes = {}
            self._dimension_index = {}
            return
        data = json.loads(raw)
        if not isinstance(data, dict):
            raise ValueError("memory lattice file must contain a JSON object")
        self._nodes = {}
        for node_id, node_data in data.items():
            self._nodes[node_id] = LatticeNode(
                node_id=node_data["node_id"],
                content_hash=node_data["content_hash"],
                data=node_data["data"],
                dimensions=node_data.get("dimensions", {}),
                neighbors=set(node_data.get("neighbors", [])),
                created_at=node_data.get("created_at", time.time()),
                last_accessed=node_data.get("last_accessed", time.time()),
                access_count=node_data.get("access_count", 0),
            )
        self._rebuild_dimension_index()

    def stats(self) -> Dict[str, Any]:
        """Return bounded implementation statistics."""
        return {
            "total_nodes": len(self._nodes),
            "total_links": sum(len(node.neighbors) for node in self._nodes.values()) // 2,
            "dimensions_indexed": len(self._dimension_index),
            "avg_access_count": sum(node.access_count for node in self._nodes.values())
            / max(len(self._nodes), 1),
            "experimental": True,
        }
