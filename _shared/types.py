"""
统一状态类型 — Pydantic 模型，替代裸 dict

借鉴 LangGraph TypedDict + Haystack Component I/O contracts。
所有 adapter 的输入输出都必须符合这些模型，
使得 IDE 可自动补全、类型检查、序列化。

Usage:
    from fangtao_fishlab._shared.types import AdapterState, CheckReport, SearchResult
"""

from __future__ import annotations

from typing import Any, Optional
from pydantic import BaseModel, Field


class AdapterState(BaseModel):
    """适配器标准状态 — 所有 adapter.health() 必须返回此模型"""

    status: str = Field(default="HEALTHY", description="HEALTHY | DEGRADED | FAIL")
    core_loaded: bool = Field(default=False, description="核心引擎是否已加载")
    bayesian: str = Field(default="UNAVAILABLE", description="贝叶斯能力状态")
    bayesian_confidence: Optional[float] = Field(default=None, description="贝叶斯置信度 0-1")
    details: dict[str, Any] = Field(default_factory=dict, description="扩展详情")


class SearchResult(BaseModel):
    """搜索结果标准格式 — 所有 adapter.search() 必须返回此模型"""

    query: str = Field(default="")
    status: str = Field(default="ok", description="ok | error")
    papers_found: int = Field(default=0)
    mode: str = Field(default="fast", description="fast | standard | deep")
    duration_ms: float = Field(default=0.0)
    result: dict[str, Any] = Field(default_factory=dict)


class CheckItem(BaseModel):
    """单条自检项"""

    name: str
    passed: bool
    value: Any = None
    detail: str = ""


class CheckReport(BaseModel):
    """自检报告标准格式 — 替代裸 dict

    使用示例:
        report = CheckReport(checks={
            "engine_loaded": CheckItem(name="引擎", passed=True, value=True),
            "bayesian": CheckItem(name="贝叶斯", passed=True, value="OK(mean=0.714)"),
        })
        print(report.score)  # → 100
        print(report.is_healthy)  # → True
    """

    checks: dict[str, CheckItem] = Field(default_factory=dict)
    project: str = Field(default="", description="项目名称")
    version: str = Field(default="v8.0.0")

    @property
    def total(self) -> int:
        return len(self.checks)

    @property
    def passed_count(self) -> int:
        return sum(1 for c in self.checks.values() if c.passed)

    @property
    def score(self) -> float:
        """自检分数 0-100"""
        if self.total == 0:
            return 0.0
        return round(self.passed_count / self.total * 100, 1)

    @property
    def is_healthy(self) -> bool:
        return self.score >= 100.0

    def summary(self) -> dict:
        return {
            "project": self.project,
            "score": self.score,
            "total": self.total,
            "passed": self.passed_count,
            "healthy": self.is_healthy,
            "checks": {k: {"passed": v.passed, "detail": v.detail} for k, v in self.checks.items()},
        }

    def __repr__(self) -> str:
        items = ", ".join(
            f"{k}={'PASS' if v.passed else 'FAIL'}" for k, v in self.checks.items()
        )
        return f"CheckReport(score={self.score}/100, {items})"


class PipelineValidation(BaseModel):
    """管线验证结果"""

    valid: bool = True
    errors: list[str] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)

    def add_error(self, msg: str):
        self.errors.append(msg)
        self.valid = False

    def add_warning(self, msg: str):
        self.warnings.append(msg)
