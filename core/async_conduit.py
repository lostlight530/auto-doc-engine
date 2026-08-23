"""Experimental bounded asynchronous document task conduit.

[EXPERIMENTAL] Not integrated into the canonical rendering/sync chain.

This module provides an in-memory priority queue, a concurrency ceiling and
stage callbacks. It does not itself parse, analyze, render or write documents;
callers must register those handlers. The queue-size limit is a bounded buffer,
not a complete streaming backpressure protocol.
"""

from __future__ import annotations

import asyncio
import time
from collections import deque
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Callable, Deque, Dict, List, Optional, Set


class RenderStage(Enum):
    QUEUED = "queued"
    PARSING = "parsing"
    ANALYZING = "analyzing"
    RENDERING = "rendering"
    WRITING = "writing"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class RenderTask:
    """A single queued task and its observable lifecycle state."""

    task_id: str
    source_path: str
    output_path: str
    priority: int = 0
    stage: RenderStage = RenderStage.QUEUED
    created_at: float = field(default_factory=time.time)
    completed_at: Optional[float] = None
    error: Optional[str] = None
    result: Optional[Dict[str, Any]] = None


class AsyncRenderConduit:
    """Bounded priority scheduling for caller-provided async/sync handlers."""

    def __init__(self, max_concurrent: int = 4, max_queue_size: int = 100):
        if max_concurrent < 1:
            raise ValueError("max_concurrent must be >= 1")
        if max_queue_size < 1:
            raise ValueError("max_queue_size must be >= 1")
        self.max_concurrent = max_concurrent
        self.max_queue_size = max_queue_size
        self._queue: Deque[RenderTask] = deque()
        self._active: Dict[str, RenderTask] = {}
        self._completed: List[RenderTask] = []
        self._stage_handlers: Dict[RenderStage, Callable] = {}
        self._workers: Set[asyncio.Task] = set()
        self._running = False

    def register_stage_handler(self, stage: RenderStage, handler: Callable) -> None:
        """Register a handler for one stage."""
        self._stage_handlers[stage] = handler

    def submit(self, task: RenderTask) -> bool:
        """Queue a unique task; return ``False`` when the buffer is full."""
        known_ids = {queued.task_id for queued in self._queue} | set(self._active)
        if task.task_id in known_ids:
            raise ValueError(f"duplicate task_id: {task.task_id}")
        if len(self._queue) >= self.max_queue_size:
            return False
        self._queue.append(task)
        self._queue = deque(sorted(self._queue, key=lambda item: -item.priority))
        return True

    async def process(self, task: RenderTask) -> None:
        """Run a task through registered stage handlers in canonical order."""
        for stage in (
            RenderStage.PARSING,
            RenderStage.ANALYZING,
            RenderStage.RENDERING,
            RenderStage.WRITING,
        ):
            task.stage = stage
            handler = self._stage_handlers.get(stage)
            if handler is not None:
                try:
                    if asyncio.iscoroutinefunction(handler):
                        await handler(task)
                    else:
                        result = handler(task)
                        if asyncio.iscoroutine(result):
                            await result
                except Exception as exc:
                    task.stage = RenderStage.FAILED
                    task.error = str(exc)
                    task.completed_at = time.time()
                    return
            await asyncio.sleep(0)
        task.stage = RenderStage.COMPLETED
        task.completed_at = time.time()

    async def run(self) -> None:
        """Schedule queued work until stopped and all active workers have drained."""
        self._running = True
        while self._running or self._workers:
            if self._running:
                while self._queue and len(self._workers) < self.max_concurrent:
                    task = self._queue.popleft()
                    self._active[task.task_id] = task
                    worker = asyncio.create_task(self._process_and_cleanup(task))
                    self._workers.add(worker)
                    worker.add_done_callback(self._workers.discard)
            if not self._workers and not self._queue:
                self._running = False
                break
            await asyncio.sleep(0.01)

    async def _process_and_cleanup(self, task: RenderTask) -> None:
        try:
            await self.process(task)
        finally:
            self._active.pop(task.task_id, None)
            self._completed.append(task)

    def stop(self) -> None:
        """Stop scheduling new queued work; already active tasks are allowed to drain."""
        self._running = False

    def stats(self) -> Dict[str, Any]:
        """Return current scheduler counts."""
        return {
            "queued": len(self._queue),
            "active": len(self._active),
            "completed": len(self._completed),
            "failed": sum(task.stage == RenderStage.FAILED for task in self._completed),
            "max_concurrent": self.max_concurrent,
            "experimental": True,
        }
