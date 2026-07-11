"""
AgentBelief — 智能体层的贝叶斯信念状态

每个智能体 (Porpoise/Coilia/Culter) 的内部信念系统:
  - 对物种状态的信念 (种群趋势、威胁等级)
  - 对自身知识完备性的信念 (知道什么、不知道什么)
  - 对行动效果的信念 (某策略成功的概率)

基于 BDI (Belief-Desire-Intention) 架构中的 Belief 层。
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional

from ..engine import BetaBelief, NormalBelief, DirichletBelief
from ..self_check import SelfCheckMixin, SelfCheckReport


class AgentBelief(SelfCheckMixin):
    """智能体信念工厂"""

    @staticmethod
    def species_status(prior_confident: bool = False) -> "SpeciesStatusBelief":
        """创建物种状态信念

        参数:
          prior_confident: 是否在先验上更自信
        """
        if prior_confident:
            return SpeciesStatusBelief(
                population=NormalBelief(mu=1000, sigma=200),
                trend=BetaBelief(alpha=8, beta=4),  # 偏向增长
                threat=BetaBelief(alpha=3, beta=8),  # 偏向不威胁
            )
        else:
            return SpeciesStatusBelief(
                population=NormalBelief(mu=1000, sigma=500),
                trend=BetaBelief(alpha=2, beta=2),  # 无信息
                threat=BetaBelief(alpha=2, beta=2),
            )

    @staticmethod
    def knowledge_completeness(n_categories: int = 5) -> DirichletBelief:
        """创建知识完备性信念

        用于跟踪智能体在不同知识维度的覆盖程度。
        """
        return DirichletBelief(alphas=[1.0] * n_categories)

    @staticmethod
    def strategy_effectiveness(prior_alpha: float = 1, prior_beta: float = 1) -> BetaBelief:
        """创建策略有效性信念

        用于跟踪某种搜索/分析策略的成功率。
        """
        return BetaBelief(alpha=prior_alpha, beta=prior_beta)

    def self_check(self) -> SelfCheckReport:
        """AgentBelief 自检"""
        report = SelfCheckReport()

        # 物种状态信念
        status = self.species_status()
        report.add(
            self._make_item(
                "物种状态信念",
                status.population.mean() > 0,
                f"种群={status.population.mean():.0f}±{status.population.sigma:.0f}, "
                f"趋势={status.trend.mean():.3f}",
            )
        )

        # 知识完备性
        knowledge = self.knowledge_completeness(3)
        means = knowledge.mean()
        report.add(
            self._make_item(
                "知识完备性信念",
                len(means) == 3 and abs(sum(means) - 1.0) < 0.01,
                f"类别概率={[round(m, 3) for m in means]}",
            )
        )

        # 策略有效性更新
        strategy = self.strategy_effectiveness()
        strategy.update(successes=7, trials=10)
        report.add(
            self._make_item(
                "策略有效性更新",
                0.5 < strategy.mean() < 0.9,
                f"7/10成功 → 后验均值={strategy.mean():.3f}",
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
class SpeciesStatusBelief:
    """物种状态信念 — 智能体对某物种的综合认知

    包含:
      - population: 种群数量的正态信念
      - trend:      种群趋势的 Beta 信念 (增长概率)
      - threat:     威胁等级的 Beta 信念 (受威胁概率)
    """

    population: NormalBelief
    trend: BetaBelief
    threat: BetaBelief

    def update_population(self, estimate: float, uncertainty: float = 0):
        """更新种群数量信念"""
        self.population.update(
            observations=[estimate],
            sample_std=uncertainty or estimate * 0.2,
        )

    def update_trend(self, increasing: bool, confidence: float = 0.5):
        """更新趋势信念

        increasing=True → 种群增长
        """
        weight = max(confidence * 2, 0.1)
        if increasing:
            self.trend.update(successes=weight)
        else:
            self.trend.update(failures=weight)

    def update_threat(self, threatened: bool, confidence: float = 0.5):
        """更新威胁信念

        threatened=True → 受到威胁
        """
        weight = max(confidence * 2, 0.1)
        if threatened:
            self.threat.update(successes=weight)
        else:
            self.threat.update(failures=weight)

    def status_summary(self) -> dict:
        return {
            "population": {
                "estimate": round(self.population.mean(), 0),
                "ci_95": (
                    round(self.population.credible_interval()[0], 0),
                    round(self.population.credible_interval()[1], 0),
                ),
            },
            "trend_growing_prob": round(self.trend.mean(), 3),
            "threatened_prob": round(self.threat.mean(), 3),
            "knowledge_weight": round(self.trend.weight() + self.threat.weight(), 1),
        }
