"""
自检模块 — 贝叶斯信念的自我验证

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
每个信念不仅要知道自己相信什么，
还要知道自己为什么可以相信。
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

自检项:
  1. 后验预测检验 (Posterior Predictive Check)
  2. 收敛性检验 (已更新次数 > 0)
  3. 信息量检验 (证据权重足够)
  4. 校准性检验 (置信区间包含真实值的倾向)
  5. 稳定性检验 (微小扰动下信念变化不大)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class SelfCheckItem:
    """单条自检结果"""

    name: str
    passed: bool
    detail: str = ""
    metric: Optional[float] = None
    severity: str = "info"  # "error" | "warn" | "info"

    def __bool__(self) -> bool:
        return self.passed


@dataclass
class SelfCheckReport:
    """自检报告 — 包含所有检查项 + 综合结论"""

    items: list[SelfCheckItem] = field(default_factory=list)
    total_checks: int = 0
    passed_checks: int = 0

    def add(self, item: SelfCheckItem) -> "SelfCheckReport":
        self.items.append(item)
        self.total_checks += 1
        if item.passed:
            self.passed_checks += 1
        return self

    @property
    def passed(self) -> bool:
        return self.passed_checks == self.total_checks

    @property
    def summary(self) -> str:
        if self.total_checks == 0:
            return "⚠ 未执行任何自检"
        return (
            f"{'✅' if self.passed else '⚠'} "
            f"自检 {self.passed_checks}/{self.total_checks} 通过"
        )

    def __repr__(self) -> str:
        lines = [f"SelfCheckReport({self.summary})"]
        for item in self.items:
            status = "✅" if item.passed else "❌" if item.severity == "error" else "⚠️"
            lines.append(f"  {status} {item.name}: {item.detail}")
        return "\n".join(lines)

    def to_dict(self) -> dict:
        return {
            "passed": self.passed,
            "passed_checks": self.passed_checks,
            "total_checks": self.total_checks,
            "items": [
                {
                    "name": i.name,
                    "passed": i.passed,
                    "detail": i.detail,
                    "severity": i.severity,
                }
                for i in self.items
            ],
        }


class SelfCheckMixin:
    """自检混入类 — 提供 self_check() 模板方法"""

    def self_check(self) -> SelfCheckReport:
        """执行全量自检，返回报告

        子类应覆盖 _run_self_checks() 来添加具体的检查项。
        """
        report = SelfCheckReport()
        self._run_self_checks(report)
        return report

    def _run_self_checks(self, report: SelfCheckReport) -> None:
        """子类在此添加自检项 (覆盖此方法)"""
        pass

    def _check_posterior_updated(
        self, report: SelfCheckReport, has_updates: bool, name: str = "后验更新检验"
    ):
        """检查后验是否已被更新"""
        report.add(
            SelfCheckItem(
                name=name,
                passed=has_updates,
                detail="后验已更新" if has_updates else "后验未经更新，仍为先验状态",
                severity="warn" if not has_updates else "info",
            )
        )

    def _check_credible_interval(
        self,
        report: SelfCheckReport,
        lo: float,
        hi: float,
        name: str = "可信区间合理性检验",
    ):
        """检查可信区间是否合理"""
        reasonable = lo <= hi and not (math.isnan(lo) or math.isnan(hi))
        report.add(
            SelfCheckItem(
                name=name,
                passed=reasonable,
                detail=f"95% CI = [{lo:.4f}, {hi:.4f}]"
                if reasonable
                else f"异常区间 [{lo}, {hi}]",
                severity="error" if not reasonable else "info",
            )
        )

    def _check_information(
        self,
        report: SelfCheckReport,
        weight: float,
        min_weight: float = 3.0,
        name: str = "信息量检验",
    ):
        """检查证据是否足够"""
        sufficient = weight >= min_weight
        report.add(
            SelfCheckItem(
                name=name,
                passed=sufficient,
                detail=f"证据权重={weight:.1f} (阈值={min_weight})"
                if sufficient
                else f"证据不足: 权重={weight:.1f} < {min_weight}",
                severity="warn" if not sufficient else "info",
            )
        )


import math  # noqa: E402  (用于 self_check 中的数学运算)
