"""
KnowledgeUpdater — 知识供给层的贝叶斯更新

物种知识库中的每条知识声明 (KnowledgeClaim) 都应携带
一个贝叶斯信念，随证据积累而更新。

工程化接口:
    # 创建知识信念
    claim_belief = KnowledgeUpdater.claim_confidence("Coilia nasus 洄游路线")

    # 加入新证据
    claim_belief.add_evidence(source_credibility=0.8, source_count=3)
    claim_belief.add_evidence(contradictions=0, supporting_studies=5)

    # 获取后验
    confidence = claim_belief.confidence()      # 后验可信度
    interval = claim_belief.uncertainty()       # 不确定性
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional

from ..engine import BetaBelief, NormalBelief
from ..self_check import SelfCheckMixin, SelfCheckReport


class KnowledgeUpdater(SelfCheckMixin):
    """知识信念更新器"""

    # 知识来源的默认可信度 (可被下游覆盖)
    SOURCE_CREDIBILITY = {
        "peer_reviewed": 0.90,
        "book": 0.80,
        "report": 0.60,
        "preprint": 0.50,
        "conference": 0.55,
        "grey_literature": 0.35,
        "llm_generated": 0.20,
    }

    @staticmethod
    def claim_confidence(
        prior_alpha: float = 1.0, prior_beta: float = 1.0
    ) -> "KnowledgeClaimBelief":
        """创建一条知识声明的贝叶斯信念

        默认先验 Beta(1,1)：表示"不知道"，完全由证据驱动。
        """
        return KnowledgeClaimBelief(alpha=prior_alpha, beta=prior_beta)

    @staticmethod
    def validate_with_bayes(
        claim_text: str,
        supporting_count: int,
        contradicting_count: int,
        source_credibility: float = 1.0,
    ) -> dict:
        """贝叶斯验证一条知识声明

        返回:
          {
            "claim": str,
            "prior": "Beta(1,1)",
            "evidence": f"{supporting_count}支持/{contradicting_count}反对",
            "posterior_mean": float,
            "credible_interval": (float, float),
            "verdict": "confirmed" | "plausible" | "uncertain" | "contested"
          }
        """
        belief = BetaBelief(alpha=1.0, beta=1.0)
        # 每条支持/反对证据按其来源可信度加权
        belief.update(
            successes=supporting_count * source_credibility,
            failures=contradicting_count * source_credibility,
        )

        mean = belief.mean()
        lo, hi = belief.credible_interval()

        if mean > 0.8 and lo > 0.5:
            verdict = "confirmed"
        elif mean > 0.6:
            verdict = "plausible"
        elif mean > 0.3:
            verdict = "uncertain"
        else:
            verdict = "contested"

        return {
            "claim": claim_text,
            "prior": "Beta(1,1)",
            "evidence": f"{supporting_count}支持/{contradicting_count}反对",
            "posterior_mean": round(mean, 4),
            "credible_interval": (round(lo, 4), round(hi, 4)),
            "verdict": verdict,
            "weight": belief.weight(),
        }

    @staticmethod
    def species_trend(species_name: str) -> NormalBelief:
        """创建物种种群趋势的贝叶斯信念

        用于估计种群变化率 (正值=增长, 负值=下降)
        """
        return NormalBelief(mu=0.0, sigma=5.0)

    def self_check(self) -> SelfCheckReport:
        """KnowledgeUpdater 自检"""
        report = SelfCheckReport()

        # 测试一条声明的验证
        result = self.validate_with_bayes(
            "测试声明", supporting_count=10, contradicting_count=1,
            source_credibility=0.8
        )
        report.add(
            self._make_item(
                "知识声明验证",
                result["posterior_mean"] > 0.5,
                f"支持10/反对1, 后验={result['posterior_mean']:.3f}, "
                f"判定={result['verdict']}",
            )
        )

        # 测试高冲突场景
        conflict = self.validate_with_bayes(
            "争议声明", supporting_count=5, contradicting_count=5,
        )
        report.add(
            self._make_item(
                "冲突证据处理",
                conflict["verdict"] == "uncertain",
                f"支持5/反对5, 后验={conflict['posterior_mean']:.3f} (应≈0.5)",
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
class KnowledgeClaimBelief:
    """单条知识声明的贝叶斯信念状态"""

    alpha: float = 1.0
    beta: float = 1.0
    evidence_log: list[dict] = field(default_factory=list)

    def add_evidence(
        self,
        source_credibility: float = 0.5,
        supporting: bool = True,
        source_count: int = 1,
        contradictions: int = 0,
        supporting_studies: int = 0,
    ) -> "KnowledgeClaimBelief":
        """添加证据并更新信念

        参数:
          source_credibility: 来源可信度 0-1
          supporting: 是否支持该声明
          source_count: 独立来源数
        """
        weight = source_credibility * source_count
        if weight > 0:
            if supporting:
                self.alpha += weight
            else:
                self.beta += weight

        if contradictions > 0:
            self.beta += contradictions * source_credibility
        if supporting_studies > 0:
            self.alpha += supporting_studies * source_credibility

        self.evidence_log.append(
            {
                "source_credibility": source_credibility,
                "supporting": supporting,
                "weight": weight,
            }
        )
        return self

    def confidence(self) -> float:
        """后验可信度 (后验均值)"""
        total = self.alpha + self.beta
        return self.alpha / total if total > 0 else 0.5

    def uncertainty(self) -> float:
        """不确定性 (后验标准差)"""
        total = self.alpha + self.beta
        if total <= 1:
            return 0.5
        return ((self.alpha * self.beta) / (total * total * (total + 1))) ** 0.5

    def weight(self) -> float:
        """信念强度 (有效样本量)"""
        return self.alpha + self.beta
