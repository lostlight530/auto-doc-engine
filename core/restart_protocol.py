"""Experimental event-log replay and checkpoint helper.

[EXPERIMENTAL] Not integrated into the canonical document pipeline.

The historical ``DeterministicRestartProtocol`` name is retained for API
continuity. Replay is deterministic only when registered handlers are
repeatable for the same state/payload and do not depend on hidden external
state, randomness or wall-clock time. This module now verifies recorded handler
result hashes during replay instead of reporting unconditional success.
"""

from __future__ import annotations

import hashlib
import json
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Dict, List


@dataclass
class Checkpoint:
    """An in-memory state checkpoint used as a replay starting point."""

    checkpoint_id: str
    state_hash: str
    state: Dict[str, Any]
    event_index: int
    timestamp: float = field(default_factory=time.time)


@dataclass
class LoggedEvent:
    """A recorded event plus the hash of its handler result when available."""

    event_id: int
    event_type: str
    payload: Dict[str, Any]
    timestamp: float = field(default_factory=time.time)
    result_hash: str = ""


class DeterministicRestartProtocol:
    """Replay helper whose determinism depends on caller-supplied handlers."""

    def __init__(
        self,
        log_path: str = "incremental/event_log.jsonl",
        checkpoint_interval: int = 50,
    ):
        if checkpoint_interval < 1:
            raise ValueError("checkpoint_interval must be >= 1")
        self.log_path = log_path
        self.checkpoint_interval = checkpoint_interval
        self._events: List[LoggedEvent] = []
        self._checkpoints: List[Checkpoint] = []
        self._state: Dict[str, Any] = {}
        self._event_handlers: Dict[str, Callable] = {}
        self._replaying = False
        self._last_replay_errors: List[str] = []

    @staticmethod
    def _hash_value(value: Any) -> str:
        if value is None:
            return ""
        canonical = json.dumps(value, sort_keys=True, ensure_ascii=False, default=str, separators=(",", ":"))
        return hashlib.sha256(canonical.encode("utf-8")).hexdigest()[:16]

    @staticmethod
    def _hash_state(state: Dict[str, Any]) -> str:
        canonical = json.dumps(state, sort_keys=True, ensure_ascii=False, default=str, separators=(",", ":"))
        return hashlib.sha256(canonical.encode("utf-8")).hexdigest()[:16]

    def register_handler(self, event_type: str, handler: Callable) -> None:
        """Register a state-transition handler for one event type."""
        self._event_handlers[event_type] = handler

    def process(self, event_type: str, payload: Dict[str, Any]) -> Any:
        """Apply a handler, record the event and capture result identity."""
        handler = self._event_handlers.get(event_type)
        result = handler(self._state, payload) if handler else None
        event = LoggedEvent(
            event_id=len(self._events),
            event_type=event_type,
            payload=payload,
            result_hash=self._hash_value(result),
        )
        self._events.append(event)
        if not self._replaying and len(self._events) % self.checkpoint_interval == 0:
            self._checkpoint()
        return result

    def _checkpoint(self) -> None:
        """Capture an in-memory state snapshot and its canonical SHA-256 identity."""
        checkpoint = Checkpoint(
            checkpoint_id=f"ckpt_{len(self._checkpoints)}",
            state_hash=self._hash_state(self._state),
            state=json.loads(json.dumps(self._state, default=str)),
            event_index=len(self._events) - 1,
        )
        self._checkpoints.append(checkpoint)

    def restart(self) -> bool:
        """Replay from the last in-memory checkpoint and verify recorded results."""
        self._replaying = True
        self._last_replay_errors = []
        try:
            if not self._checkpoints:
                self._state = {}
                events_to_replay = self._events
            else:
                checkpoint = self._checkpoints[-1]
                self._state = json.loads(json.dumps(checkpoint.state))
                if self._hash_state(self._state) != checkpoint.state_hash:
                    self._last_replay_errors.append(
                        f"checkpoint hash mismatch: {checkpoint.checkpoint_id}"
                    )
                events_to_replay = self._events[checkpoint.event_index + 1 :]

            for event in events_to_replay:
                handler = self._event_handlers.get(event.event_type)
                if handler is None:
                    self._last_replay_errors.append(
                        f"missing handler for event {event.event_id}:{event.event_type}"
                    )
                    continue
                result = handler(self._state, event.payload)
                replay_hash = self._hash_value(result)
                if event.result_hash and replay_hash != event.result_hash:
                    self._last_replay_errors.append(
                        f"result hash mismatch for event {event.event_id}:{event.event_type}"
                    )
            return not self._last_replay_errors
        finally:
            self._replaying = False

    def flush_log(self) -> None:
        """Persist the event log as JSONL; checkpoints remain in-memory only."""
        log_file = Path(self.log_path)
        log_file.parent.mkdir(parents=True, exist_ok=True)
        with log_file.open("w", encoding="utf-8") as handle:
            for event in self._events:
                handle.write(
                    json.dumps(
                        {
                            "event_id": event.event_id,
                            "event_type": event.event_type,
                            "payload": event.payload,
                            "timestamp": event.timestamp,
                            "result_hash": event.result_hash,
                        },
                        ensure_ascii=False,
                    )
                    + "\n"
                )

    def load_log(self) -> None:
        """Load persisted events, replacing the current in-memory event list."""
        path = Path(self.log_path)
        if not path.exists():
            self._events = []
            return
        events: List[LoggedEvent] = []
        with path.open("r", encoding="utf-8") as handle:
            for line_number, line in enumerate(handle, 1):
                if not line.strip():
                    continue
                record = json.loads(line)
                events.append(
                    LoggedEvent(
                        event_id=int(record.get("event_id", len(events))),
                        event_type=str(record["event_type"]),
                        payload=dict(record.get("payload") or {}),
                        timestamp=float(record.get("timestamp", 0)),
                        result_hash=str(record.get("result_hash") or ""),
                    )
                )
        self._events = events

    def get_state(self) -> Dict[str, Any]:
        """Return a shallow copy of current state."""
        return dict(self._state)

    def replay_errors(self) -> List[str]:
        """Return verification errors from the latest ``restart`` call."""
        return list(self._last_replay_errors)

    def stats(self) -> Dict[str, Any]:
        """Return bounded replay statistics."""
        return {
            "total_events": len(self._events),
            "total_checkpoints": len(self._checkpoints),
            "current_state_keys": len(self._state),
            "checkpoint_interval": self.checkpoint_interval,
            "last_checkpoint_event": self._checkpoints[-1].event_index if self._checkpoints else -1,
            "last_replay_error_count": len(self._last_replay_errors),
            "experimental": True,
        }
