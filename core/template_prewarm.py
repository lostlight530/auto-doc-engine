"""Experimental in-memory template-result LRU cache.

[EXPERIMENTAL] Not integrated into the canonical renderer.

The historical template-prewarm name is retained for continuity. The module
stores caller-provided rendered objects keyed by a truncated SHA-256 digest of
the template text. It does not itself precompile Jinja2 templates, remove
parsing cost universally, or measure any notion of "rendering entropy".
"""

from __future__ import annotations

import hashlib
import time
from collections import OrderedDict
from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class PrewarmedTemplate:
    """One cached object keyed by template-text identity."""

    template_hash: str
    rendered_ast: object
    created_at: float
    access_count: int = 0
    last_accessed: float = 0.0


class TemplatePrewarmCache:
    """Bounded LRU cache for caller-produced template results."""

    def __init__(self, max_size: int = 128):
        if max_size < 1:
            raise ValueError("max_size must be >= 1")
        self.max_size = max_size
        self._cache: OrderedDict[str, PrewarmedTemplate] = OrderedDict()
        self._hit_count = 0
        self._miss_count = 0

    @staticmethod
    def _hash_template(template_str: str) -> str:
        """Return a short SHA-256 identity used only as the local cache key."""
        return hashlib.sha256(template_str.encode("utf-8")).hexdigest()[:16]

    def prewarm(self, template_str: str, rendered_ast: object) -> None:
        """Insert or replace a cached caller-produced result."""
        template_hash = self._hash_template(template_str)
        now = time.time()
        if template_hash in self._cache:
            entry = self._cache[template_hash]
            entry.rendered_ast = rendered_ast
            entry.created_at = now
            entry.last_accessed = now
            self._cache.move_to_end(template_hash)
            return
        self._cache[template_hash] = PrewarmedTemplate(
            template_hash=template_hash,
            rendered_ast=rendered_ast,
            created_at=now,
            last_accessed=now,
        )
        if len(self._cache) > self.max_size:
            self._cache.popitem(last=False)

    def retrieve(self, template_str: str) -> Optional[object]:
        """Return a cached result and update LRU/access metadata."""
        template_hash = self._hash_template(template_str)
        entry = self._cache.get(template_hash)
        if entry is None:
            self._miss_count += 1
            return None
        self._hit_count += 1
        entry.access_count += 1
        entry.last_accessed = time.time()
        self._cache.move_to_end(template_hash)
        return entry.rendered_ast

    def hit_rate(self) -> float:
        total = self._hit_count + self._miss_count
        return self._hit_count / total if total else 0.0

    def evict_stale(self, max_age: float = 3600) -> int:
        """Evict entries not accessed within ``max_age`` seconds."""
        if max_age < 0:
            raise ValueError("max_age must be >= 0")
        now = time.time()
        stale = [
            key
            for key, entry in self._cache.items()
            if now - entry.last_accessed > max_age
        ]
        for key in stale:
            del self._cache[key]
        return len(stale)

    def stats(self) -> Dict[str, Any]:
        """Return cache counters without claiming performance improvement."""
        return {
            "size": len(self._cache),
            "max_size": self.max_size,
            "hits": self._hit_count,
            "misses": self._miss_count,
            "hit_rate": self.hit_rate(),
            "experimental": True,
        }
