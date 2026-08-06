"""
Recursive Self-Observation Hook - Introspective AST Analysis
[EXPERIMENTAL] Not integrated into main rendering chain.

Enables the documentation engine to observe its own processing
behavior, creating a meta-layer where the engine can detect patterns
in how it renders documents and optimize itself.

Real-world: Self-monitoring and introspective logging system.
"""

import time
import json
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Callable, Any
from collections import defaultdict
from pathlib import Path


@dataclass
class ObservationRecord:
    """A single self-observation record."""

    timestamp: float
    event_type: str
    context: Dict[str, Any] = field(default_factory=dict)
    duration_ms: float = 0.0
    meta: Dict[str, Any] = field(default_factory=dict)


class SelfObservationHook:
    """Recursive self-observation system for the documentation engine."""

    def __init__(
        self, max_depth: int = 3, log_path: str = "incremental/self_observation.jsonl"
    ):
        self.max_depth = max_depth
        self.log_path = log_path
        self._observations: List[ObservationRecord] = []
        self._hooks: Dict[str, List[Callable]] = defaultdict(list)
        self._depth = 0
        self._pattern_counts: Dict[str, int] = defaultdict(int)

    def register_hook(self, event_type: str, callback: Callable) -> None:
        """Register a callback for a specific event type."""
        self._hooks[event_type].append(callback)

    def observe(self, event_type: str, context: Dict[str, Any] = None) -> None:
        """Record an observation and trigger hooks."""
        if self._depth >= self.max_depth:
            return

        self._depth += 1
        start_time = time.time()

        record = ObservationRecord(
            timestamp=start_time,
            event_type=event_type,
            context=context or {},
            duration_ms=0.0,
        )

        for callback in self._hooks.get(event_type, []):
            try:
                callback(record)
            except Exception as e:
                record.meta["hook_error"] = str(e)

        record.duration_ms = (time.time() - start_time) * 1000
        self._observations.append(record)
        self._pattern_counts[event_type] += 1

        self._depth -= 1

    def detect_patterns(self) -> Dict[str, Any]:
        """Detect recurring patterns in observations."""
        patterns = {
            "frequency": dict(self._pattern_counts),
            "avg_duration": {},
            "slow_events": [],
        }

        durations_by_type = defaultdict(list)
        for obs in self._observations:
            durations_by_type[obs.event_type].append(obs.duration_ms)

        for event_type, durations in durations_by_type.items():
            avg = sum(durations) / len(durations) if durations else 0
            patterns["avg_duration"][event_type] = avg
            if avg > 100:
                patterns["slow_events"].append({"event": event_type, "avg_ms": avg})

        return patterns

    def flush_to_disk(self) -> None:
        """Persist observations to disk as JSONL."""
        log_file = Path(self.log_path)
        log_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.log_path, "a", encoding="utf-8") as f:
            for obs in self._observations:
                record = {
                    "timestamp": obs.timestamp,
                    "event_type": obs.event_type,
                    "context": obs.context,
                    "duration_ms": obs.duration_ms,
                    "meta": obs.meta,
                }
                f.write(json.dumps(record, ensure_ascii=False) + "\n")
        self._observations.clear()

    def get_observations(self, event_type: str = None) -> List[ObservationRecord]:
        """Retrieve observations, optionally filtered by event type."""
        if event_type:
            return [o for o in self._observations if o.event_type == event_type]
        return list(self._observations)

    def clear(self) -> None:
        """Clear all observations."""
        self._observations.clear()
        self._pattern_counts.clear()
