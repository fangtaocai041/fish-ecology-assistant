"""
ChangePointDetector — 涌现检测层的贝叶斯变点检测

用于检测生态系统中"涌现"行为的起点：何时一个生态指标
(如种群数量、分布范围、入侵速度) 发生了结构性变化。

基于贝叶斯变点检测 (Bayesian Change Point Detection):
  - 在线检测: 逐数据点更新，发现突变立即报警
  - 离线检测: 对整个时间序列回溯变点位置
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Any, Optional

import numpy as np

from ..engine import BetaBelief, NormalBelief
from ..self_check import SelfCheckMixin, SelfCheckReport


class ChangePointDetector(SelfCheckMixin):
    """贝叶斯变点检测器"""

    # 涌现信号阈值
    EMERGENCE_THRESHOLDS = {
        "strong": 0.95,
        "moderate": 0.80,
        "weak": 0.60,
    }

    @staticmethod
    def online(prior_mean: float = 0.0, prior_std: float = 1.0) -> "OnlineChangePoint":
        """创建在线变点检测器

        逐数据点更新，适合实时监测场景。
        """
        return OnlineChangePoint(
            prior_belief=NormalBelief(mu=prior_mean, sigma=prior_std)
        )

    @staticmethod
    def offline(time_series: list[float]) -> "OfflineChangePoint":
        """创建离线变点检测器

        对整个序列回溯分析，适合回顾性研究。
        """
        return OfflineChangePoint(data=time_series)

    @staticmethod
    def emergence_score(
        current_value: float,
        baseline_mean: float,
        baseline_std: float,
        n_baseline: int,
    ) -> dict:
        """计算涌现信号强度

        返回:
          {
            "z_score": float,        # 偏离程度 (标准差)
            "emergence_prob": float, # 涌现概率 (0-1)
            "signal": "strong"|"moderate"|"weak"|"none",
            "deviation": float       # 绝对偏离
          }
        """
        if baseline_std <= 0:
            return {
                "z_score": 0,
                "emergence_prob": 0,
                "signal": "none",
                "deviation": 0,
            }

        z = (current_value - baseline_mean) / baseline_std
        # 涌现强度 = 1 - p_value (p_value = 2*P(Z>|z|))
        # z越大 → p_value越小 → emergence_strength越接近1 → 涌现信号越强
        from scipy.stats import norm  # type: ignore
        p_value = 2 * (1 - norm.cdf(abs(z)))
        emergence_strength = 1 - p_value

        # 信号等级 (emergence_strength 越接近1信号越强)
        if emergence_strength > ChangePointDetector.EMERGENCE_THRESHOLDS["strong"]:
            signal = "strong"
        elif emergence_strength > ChangePointDetector.EMERGENCE_THRESHOLDS["moderate"]:
            signal = "moderate"
        elif emergence_strength > ChangePointDetector.EMERGENCE_THRESHOLDS["weak"]:
            signal = "weak"
        else:
            signal = "none"

        return {
            "z_score": round(z, 4),
            "p_value": round(p_value, 4),
            "emergence_strength": round(emergence_strength, 4),
            "signal": signal,
            "deviation": round(current_value - baseline_mean, 4),
        }

    def self_check(self) -> SelfCheckReport:
        """ChangePointDetector 自检"""
        report = SelfCheckReport()

        # 强涌现测试
        strong = self.emergence_score(
            current_value=10.0, baseline_mean=5.0, baseline_std=1.0, n_baseline=20
        )
        report.add(
            self._make_item(
                "强涌现检测",
                strong["signal"] == "strong",
                f"z={strong['z_score']:.2f}, strength={strong['emergence_strength']:.4f}",
            )
        )

        # 无涌现测试
        none = self.emergence_score(
            current_value=5.1, baseline_mean=5.0, baseline_std=1.0, n_baseline=20
        )
        report.add(
            self._make_item(
                "无涌现判别",
                none["signal"] == "none",
                f"z={none['z_score']:.2f}, strength={none['emergence_strength']:.4f}",
            )
        )

        # 在线检测器测试
        detector = self.online(prior_mean=0, prior_std=5)
        for _ in range(10):
            detector.update(1.0)
        report.add(
            self._make_item(
                "在线检测运行",
                detector.n_observations == 10,
                f"已处理 {detector.n_observations} 个数据点",
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
class OnlineChangePoint:
    """在线变点检测器

    使用累积偏差来检测分布变化。
    """

    prior_belief: NormalBelief
    n_observations: int = 0
    cumulative_deviation: float = 0.0
    change_points: list[int] = field(default_factory=list)

    def update(self, observation: float) -> dict:
        """输入一个新观测值，返回当前涌现信号"""
        self.n_observations += 1

        # 更新正态信念
        self.prior_belief.update(observations=[observation])

        # 计算偏离
        deviation = observation - self.prior_belief.prior_mu
        self.cumulative_deviation += deviation

        # 检测变点: 累积偏离超过阈值
        threshold = 3 * self.prior_belief.sigma
        if abs(self.cumulative_deviation) > threshold:
            self.change_points.append(self.n_observations)
            self.cumulative_deviation = 0  # 重置

        return {
            "step": self.n_observations,
            "observation": observation,
            "posterior_mean": self.prior_belief.mean(),
            "posterior_std": self.prior_belief.sigma,
            "cumulative_deviation": round(self.cumulative_deviation, 4),
            "is_change_point": len(self.change_points) > 0
            and self.change_points[-1] == self.n_observations,
        }


@dataclass
class OfflineChangePoint:
    """离线变点检测器

    使用滑动窗口 + 贝叶斯因子来检测变点。
    """

    data: list[float] = field(default_factory=list)
    window_size: int = 10

    def detect(self) -> list[dict]:
        """回溯检测所有变点"""
        if len(self.data) < self.window_size * 2:
            return []

        points = []
        for i in range(self.window_size, len(self.data) - self.window_size):
            left = self.data[i - self.window_size : i]
            right = self.data[i : i + self.window_size]

            left_mean = np.mean(left)
            right_mean = np.mean(right)
            left_std = np.std(left, ddof=1) or 0.1
            right_std = np.std(right, ddof=1) or 0.1

            # 贝叶斯因子: 两个窗口均值不同的证据
            pooled_std = math.sqrt(
                (left_std**2 + right_std**2) / 2
            )
            effect_size = abs(left_mean - right_mean) / (pooled_std + 1e-10)
            bf = math.exp(min(effect_size * 2, 10))  # 近似贝叶斯因子

            if bf > 3:  # 正证据
                points.append(
                    {
                        "index": i,
                        "bf": round(bf, 2),
                        "left_mean": round(left_mean, 4),
                        "right_mean": round(right_mean, 4),
                        "effect_size": round(effect_size, 4),
                    }
                )

        return points
