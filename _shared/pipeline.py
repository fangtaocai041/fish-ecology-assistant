"""
统一管线调度 — 借鉴 Haystack Pipeline.connect()

Usage:
    from _shared.pipeline import STANDARD_PIPELINE
    result = STANDARD_PIPELINE.run("鳤")
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class PipelineStep:
    name: str
    adapter: str   # 如 "cognitive-search-engine"
    method: str = "search"
    depends_on: list[str] = field(default_factory=list)


class Pipeline:
    def __init__(self, name: str, steps: list[PipelineStep]):
        self.name = name
        self.steps = steps

    def run(self, query: str) -> dict:
        import time
        results: dict[str, Any] = {}
        for step in self.steps:
            _t0 = time.time()
            for dep in step.depends_on:
                if dep not in results:
                    results[dep] = {"status": "skipped", "note": "dependency {} not ready".format(dep)}
            try:
                from fangtao_fishlab import get_adapter
                adapter = get_adapter(step.adapter)
                fn = getattr(adapter, step.method, lambda q, **kw: {"error": "method not found"})
                results[step.name] = fn(query)
            except Exception as e:
                results[step.name] = {"status": "error", "error": str(e)[:100]}
            if isinstance(results.get(step.name), dict):
                results[step.name]["step_duration_ms"] = round((time.time() - _t0) * 1000, 1)
        return results


# 预置管线
STANDARD_PIPELINE = Pipeline("standard", [
    PipelineStep(name="kb_lookup", adapter="fish-ecology-assistant", method="search"),
    PipelineStep(name="literature", adapter="cognitive-search-engine", method="search", depends_on=["kb_lookup"]),
])

FAST_PIPELINE = Pipeline("fast", [
    PipelineStep(name="kb_lookup", adapter="fish-ecology-assistant", method="fast_search"),
])

DOMAIN_PIPELINES = {
    "porpoise": Pipeline("porpoise_domain", [
        PipelineStep(name="kb", adapter="fish-ecology-assistant"),
        PipelineStep(name="search", adapter="cognitive-search-engine"),
        PipelineStep(name="specialist", adapter="porpoise-agent", depends_on=["search"]),
    ]),
    "coilia": Pipeline("coilia_domain", [
        PipelineStep(name="kb", adapter="fish-ecology-assistant"),
        PipelineStep(name="search", adapter="cognitive-search-engine"),
        PipelineStep(name="specialist", adapter="coilia-agent", depends_on=["search"]),
    ]),
    "culter": Pipeline("culter_domain", [
        PipelineStep(name="kb", adapter="fish-ecology-assistant"),
        PipelineStep(name="search", adapter="cognitive-search-engine"),
        PipelineStep(name="specialist", adapter="culter-agent", depends_on=["search"]),
    ]),
}
