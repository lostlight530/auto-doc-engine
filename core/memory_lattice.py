"""
Memory Lattice Vault - Structured Knowledge Persistence

A lattice-based memory storage system that organizes document knowledge
into a crystalline structure - each node connected to its neighbors in
multiple dimensions, enabling efficient retrieval through graph traversal.

Real-world: Multi-dimensional knowledge graph with temporal tracking.
"""

import json
import time
import hashlib
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set, Tuple, Any
from pathlib import Path


@dataclass
class LatticeNode:
    """A node in the memory lattice."""
    node_id: str
    content_hash: str
    data: Dict[str, Any]
    dimensions: Dict[str, float] = field(default_factory=dict)
    neighbors: Set[str] = field(default_factory=set)
    created_at: float = field(default_factory=time.time)
    last_accessed: float = field(default_factory=time.time)
    access_count: int = 0


class MemoryLatticeVault:
    """Crystalline memory storage with multi-dimensional indexing."""
    
    def __init__(self, vault_path: str = "incremental/memory_lattice.json"):
        self.vault_path = vault_path
        self._nodes: Dict[str, LatticeNode] = {}
        self._dimension_index: Dict[str, Dict[str, Set[str]]] = {}
    
    def store(self, node_id: str, data: Dict[str, Any], dimensions: Dict[str, float] = None) -> LatticeNode:
        """Store data in the lattice with optional dimensional coordinates."""
        content_str = json.dumps(data, sort_keys=True)
        content_hash = hashlib.sha256(content_str.encode()).hexdigest()[:16]
        
        node = LatticeNode(
            node_id=node_id,
            content_hash=content_hash,
            data=data,
            dimensions=dimensions or {}
        )
        self._nodes[node_id] = node
        
        if dimensions:
            for dim_name, dim_value in dimensions.items():
                if dim_name not in self._dimension_index:
                    self._dimension_index[dim_name] = {}
                bucket = self._bucket_value(dim_value)
                if bucket not in self._dimension_index[dim_name]:
                    self._dimension_index[dim_name][bucket] = set()
                self._dimension_index[dim_name][bucket].add(node_id)
        
        return node
    
    def link(self, node_a: str, node_b: str) -> None:
        """Create a bidirectional link between two nodes."""
        if node_a in self._nodes and node_b in self._nodes:
            self._nodes[node_a].neighbors.add(node_b)
            self._nodes[node_b].neighbors.add(node_a)
    
    def retrieve(self, node_id: str) -> Optional[LatticeNode]:
        """Retrieve a node and update access tracking."""
        node = self._nodes.get(node_id)
        if node:
            node.last_accessed = time.time()
            node.access_count += 1
        return node
    
    def query_by_dimension(self, dimension: str, value_range: Tuple[float, float]) -> List[str]:
        """Find nodes within a value range on a specific dimension."""
        if dimension not in self._dimension_index:
            return []
        
        results = []
        min_val, max_val = value_range
        
        for bucket, node_ids in self._dimension_index[dimension].items():
            bucket_val = float(bucket)
            if min_val <= bucket_val <= max_val:
                results.extend(node_ids)
        
        return results
    
    def traverse(self, start_id: str, max_depth: int = 2) -> List[str]:
        """BFS traversal from a starting node."""
        if start_id not in self._nodes:
            return []
        
        visited = {start_id}
        current = {start_id}
        result = []
        
        for _ in range(max_depth):
            next_level = set()
            for node_id in current:
                node = self._nodes.get(node_id)
                if node:
                    for neighbor in node.neighbors:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            next_level.add(neighbor)
                            result.append(neighbor)
            current = next_level
        
        return result
    
    def _bucket_value(self, value: float) -> str:
        """Bucket a continuous value for indexing."""
        return str(round(value, 2))
    
    def save(self) -> None:
        """Persist the lattice to disk."""
        data = {
            node_id: {
                "node_id": node.node_id,
                "content_hash": node.content_hash,
                "data": node.data,
                "dimensions": node.dimensions,
                "neighbors": list(node.neighbors),
                "created_at": node.created_at,
                "last_accessed": node.last_accessed,
                "access_count": node.access_count
            }
            for node_id, node in self._nodes.items()
        }
        vault_file = Path(self.vault_path)
        vault_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.vault_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def load(self) -> None:
        """Load the lattice from disk."""
        try:
            with open(self.vault_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            for node_id, node_data in data.items():
                self._nodes[node_id] = LatticeNode(
                    node_id=node_data["node_id"],
                    content_hash=node_data["content_hash"],
                    data=node_data["data"],
                    dimensions=node_data.get("dimensions", {}),
                    neighbors=set(node_data.get("neighbors", [])),
                    created_at=node_data.get("created_at", time.time()),
                    last_accessed=node_data.get("last_accessed", time.time()),
                    access_count=node_data.get("access_count", 0)
                )
        except FileNotFoundError:
            self._nodes = {}
    
    def stats(self) -> Dict[str, Any]:
        """Get lattice statistics."""
        return {
            "total_nodes": len(self._nodes),
            "total_links": sum(len(n.neighbors) for n in self._nodes.values()) // 2,
            "dimensions_indexed": len(self._dimension_index),
            "avg_access_count": sum(n.access_count for n in self._nodes.values()) / max(len(self._nodes), 1)
        }
