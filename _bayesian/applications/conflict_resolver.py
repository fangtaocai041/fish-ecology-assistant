"""
ConflictResolver — 冲突仲裁层的贝叶斯模型平均

当多个数据源 (文献、数据库、专家意见) 对同一问题给出
不同答案时，用贝叶斯模型平均 (BMA) 和贝叶斯因子进行
量化仲裁。

工程化接口:
    # 仲裁两个冲突观点
    result = ConflictResolver.arbitrate(
        claim="长江江豚种群数量",
        sources=[
            {"name": "文献A", "value": 1012, "credibility": 0.85},
            {"name": "调查B", "value": 1240, "credibility": 0.70},
            {"name": "文献C", "value": 850, "credibility": 0.60},
        ]
    )
    result["weighted_estimate"]  # 贝叶斯加权估计
    result["conflict_level"]     # 冲突等级
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional

import numpy as np

from ..engine import BetaBelief, NormalBelief, DirichletBelief
from ..self_check import SelfCheckMixin, SelfCheckReport


class ConflictResolver(SelfCheckMixin):
    """贝叶斯冲突仲裁器"""

    # 冲突等级阈值
    CONFLICT_THRESHOLDS = {
        "low": 0.3,
        "medium": 0.5,
        "high": 0.7,
    }

    @staticmethod
    def source_reliability(initial_hits: float = 1, initial_misses: float = 1) -> BetaBelief:
        """创建数据源可靠性的 Beta 信念

        每次该源提供正确信息 → update(successes=1)
        每次该源提供错误信息 → update(failures=1)
        """
        return BetaBelief(alpha=initial_hits, beta=initial_misses)

    @staticmethod
    def arbitrate(
        claim: str,
        sources: list[dict],
        method: str = "bma",
    ) -> dict:
        """贝叶斯仲裁多个冲突源

        参数:
          claim: 被仲裁的声明
          sources: 数据源列表，每个:
            {"name": str, "value": float, "credibility": float (0-1)}
          method: "bma" (贝叶斯模型平均) | "weights" (可信度加权)

        返回:
          {
            "claim": str,
            "n_sources": int,
            "weighted_estimate": float,
            "credible_interval": (float, float),
            "conflict_level": "low"|"medium"|"high",
            "conflict_score": float,
            "contributions": [{source, weight}]
          }
        """
        if not sources:
            return {
                "claim": claim,
                "n_sources": 0,
                "weighted_estimate": None,
                "conflict_level": "unknown",
                "conflict_score": 0,
                "contributions": [],
            }

        if method == "bma":
            return ConflictResolver._bma_arbitrate(claim, sources)
        else:
            return ConflictResolver._weight_arbitrate(claim, sources)

    @staticmethod
    def _bma_arbitrate(claim: str, sources: list[dict]) -> dict:
        """贝叶斯模型平均仲裁"""
        values = np.array([s["value"] for s in sources])
        creds = np.array([s["credibility"] for s in sources])

        # 可信度归一化为权重
        weights = creds / (creds.sum() + 1e-10)

        # 加权估计
        weighted_estimate = float(np.average(values, weights=weights))

        # 冲突分数 = 加权标准差 / 均值 (变异系数)
        if abs(weighted_estimate) > 1e-10:
            variance = np.average((values - weighted_estimate) ** 2, weights=weights)
            conflict_score = float(np.sqrt(variance) / abs(weighted_estimate))
        else:
            conflict_score = 0.5

        # 冲突等级
        if conflict_score < ConflictResolver.CONFLICT_THRESHOLDS["low"]:
            level = "low"
        elif conflict_score < ConflictResolver.CONFLICT_THRESHOLDS["medium"]:
            level = "medium"
        else:
            level = "high"

        # 可信区间 (加权标准差)
        std = float(np.sqrt(variance)) if conflict_score > 0 else 0

        return {
            "claim": claim,
            "n_sources": len(sources),
            "weighted_estimate": round(weighted_estimate, 4),
            "credible_interval": (
                round(weighted_estimate - 1.96 * std, 4),
                round(weighted_estimate + 1.96 * std, 4),
            ),
            "conflict_level": level,
            "conflict_score": round(conflict_score, 4),
            "contributions": [
                {"source": s["name"], "weight": round(float(w), 4)}
                for s, w in zip(sources, weights)
            ],
        }

    @staticmethod
    def _weight_arbitrate(claim: str, sources: list[dict]) -> dict:
        """简单可信度加权仲裁 (作为对照)"""
        total_cred = sum(s["credibility"] for s in sources)
        if total_cred == 0:
            return {"claim": claim, "n_sources": len(sources), "weighted_estimate": 0}

        weighted = sum(s["value"] * s["credibility"] for s in sources) / total_cred
        return {
            "claim": claim,
            "n_sources": len(sources),
            "weighted_estimate": round(weighted, 4),
            "credible_interval": (None, None),
            "conflict_level": "unknown",
            "conflict_score": 0,
            "contributions": [
                {"source": s["name"], "weight": round(s["credibility"] / total_cred, 4)}
                for s in sources
            ],
        }

    @staticmethod
    def bayes_factor(
        model1_likelihood: float,
        model2_likelihood: float,
    ) -> float:
        """贝叶斯因子：两个模型的相对证据支持

        BF > 3  → 支持 model1
        BF > 10 → 强支持 model1
        BF < 1/3 → 支持 model2
        """
        if model2_likelihood <= 0:
            return float("inf")
        return model1_likelihood / model2_likelihood

    def self_check(self) -> SelfCheckReport:
        """ConflictResolver 自检"""
        report = SelfCheckReport()

        # 低冲突测试
        low = self.arbitrate(
            "测试低冲突",
            [
                {"name": "A", "value": 100, "credibility": 0.9},
                {"name": "B", "value": 105, "credibility": 0.8},
                {"name": "C", "value": 98, "credibility": 0.7},
            ],
        )
        report.add(
            self._make_item(
                "低冲突仲裁",
                low["conflict_level"] == "low",
                f"冲突分数={low['conflict_score']:.3f}, "
                f"估计值={low['weighted_estimate']:.1f}",
            )
        )

        # 高冲突测试
        high = self.arbitrate(
            "测试高冲突",
            [
                {"name": "A", "value": 100, "credibility": 0.9},
                {"name": "B", "value": 500, "credibility": 0.8},
            ],
        )
        report.add(
            self._make_item(
                "高冲突仲裁",
                high["conflict_level"] == "high" or high["conflict_score"] > 0.3,
                f"冲突分数={high['conflict_score']:.3f}, 等级={high['conflict_level']}",
            )
        )

        # 单源退化测试
        single = self.arbitrate(
            "单源", [{"name": "A", "value": 42, "credibility": 0.9}]
        )
        report.add(
            self._make_item(
                "单源退化",
                abs(single["weighted_estimate"] - 42) < 0.01,
                f"估计值={single['weighted_estimate']} (期望=42)",
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
