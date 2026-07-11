"""
贝叶斯思想工程化框架 (Bayesian Engineering Framework)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
核心理念：信念有强弱，且随证据改变
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

本模块将贝叶斯更新从数学公式转化为工程化语言，为整个 fish_ecology
体系提供统一的信念管理基础设施。

设计原则:
1. 先验（Prior）  → 承认已知判断
2. 似然（Likelihood） → 量化新证据
3. 后验（Posterior） → 更新后的信念
4. 自检（Self-check）→ 验证信念是否合理

使用示例:
    from fish_ecology.core.bayesian import BetaBelief, NormalBelief, BayesianEngine

    # 搜索可信度的贝叶斯更新
    belief = BetaBelief(alpha=2, beta=2)  # 先验：对搜索结果持谨慎态度
    belief.update(successes=5, trials=6)   # 证据：6次检索5次成功
    print(f"可信度: {belief.posterior_mean:.2f}")  # 后验均值
    print(f"95% 可信区间: {belief.credible_interval()}")  # 不确定性量化
    report = belief.self_check()  # 自检
"""

from .engine import BayesianEngine, BetaBelief, NormalBelief, DirichletBelief
from .distributions import (
    BetaDistribution,
    NormalDistribution,
    GammaDistribution,
    DirichletDistribution,
)
from .inference import BayesianInference, conjugate_update
from .self_check import SelfCheckReport, SelfCheckMixin
from .applications import (
    SearchCredibility,
    KnowledgeUpdater,
    KnowledgeClaimBelief,
    ConflictResolver,
    ChangePointDetector,
    AgentBelief,
    SpeciesStatusBelief,
    MetaBayesian,
)

__all__ = [
    # 核心引擎
    "BayesianEngine",
    "BetaBelief",
    "NormalBelief",
    "DirichletBelief",
    # 概率分布
    "BetaDistribution",
    "NormalDistribution",
    "GammaDistribution",
    "DirichletDistribution",
    # 推理
    "BayesianInference",
    "conjugate_update",
    # 自检
    "SelfCheckReport",
    "SelfCheckMixin",
    # 领域应用
    "SearchCredibility",
    "KnowledgeUpdater",
    "KnowledgeClaimBelief",
    "ConflictResolver",
    "ChangePointDetector",
    "AgentBelief",
    "SpeciesStatusBelief",
    "MetaBayesian",
]
