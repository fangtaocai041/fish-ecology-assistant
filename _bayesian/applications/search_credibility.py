"""
SearchCredibility — 搜索验证层的贝叶斯可信度

将Thompson引擎选择、文献可信度评分、搜索结果质量判断
统一为 Beta 信念的贝叶斯更新。

工程化接口:
    # 引擎可信度
    engine_belief = SearchCredibility.engine_reliability("pubmed")
    engine_belief.update(successes=42, failures=5)

    # 文献可信度
    paper_belief = SearchCredibility.paper_credibility()
    paper_belief.update(successes=1, trials=1)  # 验证通过

    # 搜索质量
    quality = SearchCredibility.search_quality(prior="quick")
    quality.update(found_relevant=8, total_results=10)
"""

from __future__ import annotations

from typing import Optional

from ..engine import BetaBelief, NormalBelief
from ..self_check import SelfCheckReport, SelfCheckMixin


class SearchCredibility(SelfCheckMixin):
    """搜索可信度管理 — 搜索验证层的贝叶斯信念"""

    # 引擎默认先验 (基于历史表现)
    ENGINE_PRIORS = {
        "pubmed": {"alpha": 30, "beta": 5},       # 高可靠
        "crossref": {"alpha": 25, "beta": 8},      # 较高可靠
        "google_scholar": {"alpha": 20, "beta": 10}, # 中等
        "cnki": {"alpha": 15, "beta": 12},          # 中低
        "tavily": {"alpha": 12, "beta": 8},         # 较新引擎
        "semantic_scholar": {"alpha": 18, "beta": 7},
        "biorxiv": {"alpha": 10, "beta": 10},       # 预印本 = 先验中性
    }

    @staticmethod
    def engine_reliability(engine_name: str = "default") -> BetaBelief:
        """创建引擎可靠性的 Beta 信念

        参数:
          engine_name: 引擎名称，使用 ENGINE_PRIORS 中的先验
        """
        prior = SearchCredibility.ENGINE_PRIORS.get(
            engine_name, {"alpha": 5, "beta": 5}
        )
        return BetaBelief(alpha=prior["alpha"], beta=prior["beta"])

    @staticmethod
    def paper_credibility(
        prior_alpha: float = 1.0, prior_beta: float = 1.0
    ) -> BetaBelief:
        """创建文献可信度的 Beta 信念

        默认先验为 Beta(1,1) = 无信息先验。
        用 update(successes=1, trials=1) 代表一次验证通过。
        """
        return BetaBelief(alpha=prior_alpha, beta=prior_beta)

    @staticmethod
    def search_quality(prior: str = "standard") -> BetaBelief:
        """创建搜索质量的 Beta 信念

        参数:
          prior: "quick" → Beta(3,3) 少量信息
                 "standard" → Beta(8,4) 中等先验
                 "full" → Beta(15,5) 强先验
        """
        priors = {
            "quick": (3, 3),
            "standard": (8, 4),
            "full": (15, 5),
            "chinese": (6, 4),
            "preprint": (4, 6),
        }
        a, b = priors.get(prior, (5, 5))
        return BetaBelief(alpha=a, beta=b)

    @staticmethod
    def literature_volume(species_name: str) -> NormalBelief:
        """创建文献量的正态信念

        用于估计某物种的文献总量 (不确定的连续量)。
        """
        return NormalBelief(mu=50, sigma=30)

    def self_check(self) -> SelfCheckReport:
        """SearchCredibility 自检"""
        report = SelfCheckReport()

        # 检查所有引擎先验是否有效
        for name, prior in self.ENGINE_PRIORS.items():
            b = BetaBelief(alpha=prior["alpha"], beta=prior["beta"])
            ci = b.credible_interval()
            report.add(
                self._make_check_item(
                    name=f"引擎先验: {name}",
                    passed=ci[0] < ci[1] and 0 <= b.mean() <= 1,
                    detail=f"mean={b.mean():.3f}, CI=[{ci[0]:.3f},{ci[1]:.3f}]",
                )
            )

        return report

    @staticmethod
    def _make_check_item(name, passed, detail):
        from ..self_check import SelfCheckItem
        return SelfCheckItem(
            name=name, passed=passed, detail=detail,
            severity="error" if not passed else "info",
        )
