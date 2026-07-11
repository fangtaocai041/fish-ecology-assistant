"""
MetaBayesian — 元框架层的贝叶斯元学习

在 meta/ssww (三生万物核心/硅基生命体) 层面:
  - 元认知: 知道"自己知道/不知道什么"
  - 信念演化: 跟踪自身信念的变化轨迹
  - 元参数调优: 贝叶斯优化核心超参数
  - 异常信念检测: 发现与预期不符的信念突变

这是整个体系的"元认知"层 — 思想的思考。
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional

import numpy as np

from ..engine import BetaBelief, NormalBelief
from ..self_check import SelfCheckMixin, SelfCheckReport


class MetaBayesian(SelfCheckMixin):
    """元贝叶斯引擎 — 硅基生命体的自我认知层"""

    @staticmethod
    def meta_awareness(n_dimensions: int = 3) -> "MetaBeliefState":
        """创建元认知信念状态

        跟踪系统对自身知识状态的认知。
        """
        return MetaBeliefState(
            dimensions=[f"dim_{i}" for i in range(n_dimensions)]
        )

    @staticmethod
    def belief_drift_detector(window: int = 20) -> "BeliefDriftDetector":
        """创建信念漂移检测器

        检测某一信念是否发生了显著变化 (漂移)。
        """
        return BeliefDriftDetector(window_size=window)

    @staticmethod
    def calibrate_prior(
        historical_performance: list[dict],
    ) -> dict:
        """基于历史表现校准先验

        参数:
          historical_performance: [{"success": bool, "confidence": float}, ...]

        返回:
          {"calibrated_alpha": float, "calibrated_beta": float, "calibration_score": float}
        """
        if not historical_performance:
            return {"calibrated_alpha": 1, "calibrated_beta": 1, "calibration_score": 0}

        # 统计过自信/不自信
        overconfident = 0
        underconfident = 0
        total = 0

        for h in historical_performance:
            total += 1
            actual = 1.0 if h.get("success", False) else 0.0
            predicted = h.get("confidence", 0.5)
            error = abs(actual - predicted)
            if predicted >= 0.8 and error > 0.3:
                overconfident += 1
            elif predicted < 0.2 and error > 0.3:
                underconfident += 1

        # 校准分数: 0=完全不准, 1=完全校准
        calibration_score = max(0, 1 - (overconfident + underconfident) / max(total, 1))

        return {
            "calibrated_alpha": 1 + total * calibration_score * 0.5,
            "calibrated_beta": 1 + total * (1 - calibration_score) * 0.5,
            "calibration_score": round(calibration_score, 4),
            "overconfident_count": overconfident,
            "underconfident_count": underconfident,
        }

    @staticmethod
    def cross_validate_belief(
        belief: BetaBelief,
        test_data: list[tuple[int, int]],
    ) -> dict:
        """交叉验证信念的预测能力

        参数:
          belief: 要验证的 Beta 信念
          test_data: [(successes, trials), ...] 多组测试数据
        """
        log_likelihood = 0
        n_tests = len(test_data)

        for successes, trials in test_data:
            if trials <= 0:
                continue
            p = belief.mean()
            # 二项分布 log-likelihood
            from math import comb, log
            likelihood = comb(trials, successes) * (p**successes) * ((1 - p) ** (trials - successes))
            if likelihood > 0:
                log_likelihood += log(likelihood)

        return {
            "log_likelihood": round(log_likelihood, 4),
            "n_tests": n_tests,
            "avg_log_likelihood": round(log_likelihood / max(n_tests, 1), 4),
        }

    def self_check(self) -> SelfCheckReport:
        """MetaBayesian 自检"""
        report = SelfCheckReport()

        # 元认知
        meta = self.meta_awareness(3)
        report.add(
            self._make_item(
                "元认知信念",
                len(meta.dimensions) == 3,
                f"维度: {meta.dimensions}",
            )
        )

        # 校准
        calib = self.calibrate_prior(
            [
                {"success": True, "confidence": 0.85},
                {"success": True, "confidence": 0.90},
                {"success": False, "confidence": 0.30},
                {"success": False, "confidence": 0.80},  # 过自信
            ]
        )
        report.add(
            self._make_item(
                "信念校准",
                calib["calibration_score"] > 0,
                f"校准分数={calib['calibration_score']:.3f}",
            )
        )

        # 信念漂移检测
        drift = self.belief_drift_detector(5)
        for v in [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]:
            drift.record(v)
        before = drift.is_drifting()
        drift.record(0.9)
        drift.record(0.95)
        drift.record(0.98)
        after = drift.is_drifting()
        report.add(
            self._make_item(
                "信念漂移检测",
                not before and after,
                f"漂移前={before} → 漂移后={after}",
            )
        )

        return report

    @staticmethod
    def _make_item(name, passed, detail):
        from ..self_check import SelfCheckItem
        return SelfCheckItem(
            name=name, passed=passed, detail=detail,
            severity="error" if not passed else "info",
        )


@dataclass
class MetaBeliefState:
    """元认知信念状态 — 系统对自身知识的认知"""

    dimensions: list[str]
    confidences: dict[str, BetaBelief] = field(default_factory=dict)

    def __post_init__(self):
        for d in self.dimensions:
            self.confidences[d] = BetaBelief(alpha=2, beta=2)

    def update_confidence(self, dimension: str, correct: bool):
        """更新某维度的自信度"""
        if dimension in self.confidences:
            if correct:
                self.confidences[dimension].update(successes=1)
            else:
                self.confidences[dimension].update(failures=1)

    def self_awareness_score(self) -> float:
        """自认知分数: 信念的校准程度"""
        scores = [b.mean() for b in self.confidences.values()]
        return float(np.mean(scores)) if scores else 0.5

    def knows_unknown(self, threshold: float = 0.3) -> list[str]:
        """知道自己不知道什么 (不确定性高的维度)"""
        return [
            d for d, b in self.confidences.items()
            if b.variance() > threshold
        ]


@dataclass
class BeliefDriftDetector:
    """信念漂移检测器

    检测某一信念在时间序列上是否发生了结构性变化。
    """

    window_size: int = 20
    values: list[float] = field(default_factory=list)

    def record(self, value: float):
        """记录一个新的信念值"""
        self.values.append(value)

    def is_drifting(self, threshold: float = 2.0) -> bool:
        """检测是否发生漂移"""
        if len(self.values) < self.window_size * 2:
            return False

        recent = self.values[-self.window_size:]
        earlier = self.values[-(self.window_size * 2) : -self.window_size]

        recent_mean = np.mean(recent)
        earlier_mean = np.mean(earlier)
        earlier_std = np.std(earlier, ddof=1) or 0.01

        z = abs(recent_mean - earlier_mean) / (earlier_std / math.sqrt(self.window_size))
        return z > threshold

    def drift_magnitude(self) -> float:
        """漂移幅度"""
        if len(self.values) < self.window_size * 2:
            return 0.0
        recent = np.mean(self.values[-self.window_size:])
        earlier = np.mean(self.values[:self.window_size])
        return float(abs(recent - earlier))


import math  # noqa: E402
