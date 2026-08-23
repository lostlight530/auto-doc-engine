"""Experimental local observation hook for repository instrumentation.

[EXPERIMENTAL] Not integrated into the canonical document pipeline.

The historical self-observation name is retained, but the implementation is
ordinary instrumentation: it records caller-supplied event labels, callback
metadata and timing summaries. It does not autonomously optimize the engine,
infer causality, or inspect hidden model state.
"""

from __future__ import annotations

import json
import time
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional


@dataclass
class ObservationRecord:
    """One explicitly emitted observation."""

    timestamp: float
    event_type: str
    context: Dict[str, Any] = field(default_factory=dict)
    duration_ms: float = 0.0
    meta: Dict[str, Any] = field(default_factory=dict)


class SelfObservationHook:
    """Bounded event instrumentation with callback timing summaries."""

    def __init__(
        self, max_depth: int = 3, log_path: str = "incremental/self_observation.jsonl"
    ):
        if max_depth < 1:
            raise ValueError("max_depth must be >= 1")
        self.max_depth = max_depth
        self.log_path = log_path
        self._observations: List[ObservationRecord] = []
        self._hooks: Dict[str, List[Callable]] = defaultdict(list)
        self._depth = 0
        self._pattern_counts: Dict[str, int] = defaultdict(int)

    def register_hook(self, event_type: str, callback: Callable) -> None:
        """Register a callback for one caller-defined event label."""
        self._hooks[event_type].append(callback)

    def observe(self, event_type: str, context: Optional[Dict[str, Any]] = None) -> bool:
        """Record an event and trigger callbacks; return ``False`` at depth limit."""
        if self._depth >= self.max_depth:
            return False
        self._depth += 1
        wall_time = time.time()
        start = time.perf_counter()
        record = ObservationRecord(
            timestamp=wall_time,
            event_type=event_type,
            context=dict(context or {}),
        )
        try:
            for callback in self._hooks.get(event_type, []):
                try:
                    callback(record)
                except Exception as exc:
                    record.meta.setdefault("hook_errors", []).append(str(exc))
        finally:
            record.duration_ms = (time.perf_counter() - start) * 1000
            self._observations.append(record)
            self._pattern_counts[event_type] += 1
            self._depth -= 1
        return True

    def detect_patterns(self, slow_threshold_ms: float = 100.0) -> Dict[str, Any]:
        """Summarize frequencies and observed callback durations.

        These are descriptive statistics only; the method does not infer
        semantic patterns or performance causes.
        """
        if slow_threshold_ms < 0:
            raise ValueError("slow_threshold_ms must be >= 0")
        durations_by_type: Dict[str, List[float]] = defaultdict(list)
        for observation in self._observations:
            durations_by_type[observation.event_type].append(observation.duration_ms)

        averages: Dict[str, float] = {}
        slow_events: List[dict] = []
        for event_type, durations in durations_by_type.items():
            average = sum(durations) / len(durations) if durations else 0.0
            averages[event_type] = average
            if average > slow_threshold_ms:
                slow_events.append({"event": event_type, "avg_ms": average})
        return {
            "frequency": dict(self._pattern_counts),
            "avg_duration": averages,
            "slow_events": sorted(slow_events, key=lambda item: item["event"]),
            "semantics": "descriptive_instrumentation_only",
        }

    def flush_to_disk(self) -> int:
        """Append buffered observations as JSONL and return the number written."""
        if not self._observations:
            return 0
        path = Path(self.log_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        count = len(self._observations)
        with path.open("a", encoding="utf-8") as handle:
            for observation in self._observations:
                handle.write(
                    json.dumps(
                        {
                            "timestamp": observation.timestamp,
                            "event_type": observation.event_type,
                            "context": observation.context,
                            "duration_ms": observation.duration_ms,
                            "meta": observation.meta,
                        },
                        ensure_ascii=False,
                    )
                    + "\n"
                )
        self._observations.clear()
        return count

    def get_observations(self, event_type: Optional[str] = None) -> List[ObservationRecord]:
        """Return buffered observations, optionally filtered by event type."""
        if event_type is not None:
            return [item for item in self._observations if item.event_type == event_type]
        return list(self._observations)

    def clear(self) -> None:
        """Clear buffered observations and frequency summaries."""
        self._observations.clear()
        self._pattern_counts.clear()
