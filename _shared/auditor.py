"""
AuditTrail — 结构化步日志，借鉴 Prefect State

Usage:
    trail = AuditTrail("my-adapter")
    step = trail.start("search")
    result = do_search()
    trail.complete(step, metadata={"papers": 5})
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Optional


@dataclass
class StepLog:
    step: str
    status: str = "started"  # started | completed | failed
    started_at: str = ""
    duration_ms: float = 0
    error: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        if not self.started_at:
            self.started_at = datetime.now().isoformat()


class AuditTrail:
    """每个 adapter 持有一个 trail"""

    def __init__(self, name: str = ""):
        self.name = name
        self.steps: list[StepLog] = []
        self._timer: dict[str, float] = {}

    def start(self, step: str) -> StepLog:
        import time
        s = StepLog(step=step)
        self.steps.append(s)
        self._timer[step] = time.time()
        return s

    def complete(self, step: StepLog, metadata: dict | None = None):
        import time
        step.status = "completed"
        start = self._timer.pop(step.step, time.time())
        step.duration_ms = round((time.time() - start) * 1000, 1)
        if metadata:
            step.metadata.update(metadata)

    def fail(self, step: StepLog, error: str):
        import time
        step.status = "failed"
        step.error = error[:120]
        start = self._timer.pop(step.step, time.time())
        step.duration_ms = round((time.time() - start) * 1000, 1)

    def summary(self) -> dict:
        total = len(self.steps)
        failed = sum(1 for s in self.steps if s.status == "failed")
        completed = sum(1 for s in self.steps if s.status == "completed")
        avg_ms = round(sum(s.duration_ms for s in self.steps) / max(total, 1), 1)
        return {
            "name": self.name,
            "total_steps": total,
            "completed": completed,
            "failed": failed,
            "avg_duration_ms": avg_ms,
            "pass_rate": round((total - failed) / max(total, 1), 3),
        }
