"""
Async Render Conduit - Non-Blocking Document Rendering Pipeline

Enables asynchronous, non-blocking rendering of documents through a
conduit-based pipeline. Documents flow through stages without blocking
the main thread, enabling concurrent multi-document processing.

Real-world: Async pipeline with backpressure and priority queuing.
"""

import asyncio
import time
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Callable, Any
from enum import Enum
from collections import deque


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
    """A single document rendering task."""
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
    """Non-blocking document rendering pipeline with priority queuing."""
    
    def __init__(self, max_concurrent: int = 4, max_queue_size: int = 100):
        self.max_concurrent = max_concurrent
        self.max_queue_size = max_queue_size
        self._queue: deque = deque()
        self._active: Dict[str, RenderTask] = {}
        self._completed: List[RenderTask] = []
        self._stage_handlers: Dict[RenderStage, Callable] = {}
        self._running = False
    
    def register_stage_handler(self, stage: RenderStage, handler: Callable) -> None:
        """Register a handler for a rendering stage."""
        self._stage_handlers[stage] = handler
    
    def submit(self, task: RenderTask) -> bool:
        """Submit a rendering task to the conduit."""
        if len(self._queue) >= self.max_queue_size:
            return False
        
        self._queue.append(task)
        self._queue = deque(sorted(self._queue, key=lambda t: -t.priority))
        return True
    
    async def process(self, task: RenderTask) -> None:
        """Process a single task through all stages."""
        stages = [
            RenderStage.PARSING,
            RenderStage.ANALYZING,
            RenderStage.RENDERING,
            RenderStage.WRITING
        ]
        
        for stage in stages:
            task.stage = stage
            handler = self._stage_handlers.get(stage)
            
            if handler:
                try:
                    if asyncio.iscoroutinefunction(handler):
                        await handler(task)
                    else:
                        handler(task)
                except Exception as e:
                    task.stage = RenderStage.FAILED
                    task.error = str(e)
                    return
            
            await asyncio.sleep(0)
        
        task.stage = RenderStage.COMPLETED
        task.completed_at = time.time()
    
    async def run(self) -> None:
        """Main conduit loop - process tasks with concurrency control."""
        self._running = True
        
        while self._running and (self._queue or self._active):
            while self._queue and len(self._active) < self.max_concurrent:
                task = self._queue.popleft()
                self._active[task.task_id] = task
                asyncio.create_task(self._process_and_cleanup(task))
            
            await asyncio.sleep(0.01)
    
    async def _process_and_cleanup(self, task: RenderTask) -> None:
        """Process a task and clean up."""
        await self.process(task)
        
        if task.task_id in self._active:
            del self._active[task.task_id]
        
        self._completed.append(task)
    
    def stop(self) -> None:
        """Stop the conduit after current tasks finish."""
        self._running = False
    
    def stats(self) -> Dict[str, Any]:
        """Get conduit statistics."""
        return {
            'queued': len(self._queue),
            'active': len(self._active),
            'completed': len(self._completed),
            'failed': len([t for t in self._completed if t.stage == RenderStage.FAILED]),
            'max_concurrent': self.max_concurrent
        }
