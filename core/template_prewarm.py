"""
Zero-Entropy Template Prewarm - Pre-rendered Template Cache
[EXPERIMENTAL] Not integrated into main rendering chain.

Pre-renders frequently used templates into a warm cache, eliminating
repeated AST parsing overhead and reducing rendering entropy.

Real-world: Template precompilation and LRU cache management.
"""

import time
import hashlib
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
from collections import OrderedDict


@dataclass
class PrewarmedTemplate:
    """A pre-rendered template stored in the warm cache."""

    template_hash: str
    rendered_ast: object
    created_at: float
    access_count: int = 0
    last_accessed: float = 0.0


class TemplatePrewarmCache:
    """LRU cache for pre-rendered templates."""

    def __init__(self, max_size: int = 128):
        self.max_size = max_size
        self._cache: OrderedDict[str, PrewarmedTemplate] = OrderedDict()
        self._hit_count = 0
        self._miss_count = 0

    def _hash_template(self, template_str: str) -> str:
        """Compute SHA-256 hash of template string."""
        return hashlib.sha256(template_str.encode("utf-8")).hexdigest()[:16]

    def prewarm(self, template_str: str, rendered_ast: object) -> None:
        """Add a pre-rendered template to the warm cache."""
        template_hash = self._hash_template(template_str)

        if template_hash in self._cache:
            self._cache.move_to_end(template_hash)
            self._cache[template_hash].rendered_ast = rendered_ast
            self._cache[template_hash].created_at = time.time()
        else:
            entry = PrewarmedTemplate(
                template_hash=template_hash,
                rendered_ast=rendered_ast,
                created_at=time.time(),
                last_accessed=time.time(),
            )
            self._cache[template_hash] = entry

            if len(self._cache) > self.max_size:
                self._cache.popitem(last=False)

    def retrieve(self, template_str: str) -> Optional[object]:
        """Retrieve a pre-rendered template from cache."""
        template_hash = self._hash_template(template_str)

        if template_hash in self._cache:
            self._hit_count += 1
            entry = self._cache[template_hash]
            entry.access_count += 1
            entry.last_accessed = time.time()
            self._cache.move_to_end(template_hash)
            return entry.rendered_ast

        self._miss_count += 1
        return None

    def hit_rate(self) -> float:
        """Calculate cache hit rate."""
        total = self._hit_count + self._miss_count
        if total == 0:
            return 0.0
        return self._hit_count / total

    def evict_stale(self, max_age: float = 3600) -> int:
        """Evict templates older than max_age seconds."""
        now = time.time()
        evicted = 0
        to_delete = []
        for key, entry in self._cache.items():
            if now - entry.last_accessed > max_age:
                to_delete.append(key)
        for key in to_delete:
            del self._cache[key]
            evicted += 1
        return evicted

    def stats(self) -> Dict[str, any]:
        """Return cache statistics."""
        return {
            "size": len(self._cache),
            "max_size": self.max_size,
            "hits": self._hit_count,
            "misses": self._miss_count,
            "hit_rate": self.hit_rate(),
        }
