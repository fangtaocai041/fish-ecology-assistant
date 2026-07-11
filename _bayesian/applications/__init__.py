"""
贝叶斯应用模块 — 领域特化的贝叶斯推理

各模块将贝叶斯思想工程化到具体领域:
  - search_credibility:   搜索验证层 | Thompson采样 + 可信度
  - knowledge_updater:    知识供给层 | 信念更新 + 冲突检测
  - conflict_resolver:    冲突仲裁层 | 模型平均 + 贝叶斯因子
  - change_point_detector:涌现检测层 | 贝叶斯变点检测
  - agent_belief:         智能体层   | BDI 信念状态
  - meta_bayesian:        元框架层   | 元认知 + 自校准
"""

from .search_credibility import SearchCredibility
from .knowledge_updater import KnowledgeUpdater, KnowledgeClaimBelief
from .conflict_resolver import ConflictResolver
from .change_point_detector import ChangePointDetector, OnlineChangePoint, OfflineChangePoint
from .agent_belief import AgentBelief, SpeciesStatusBelief
from .meta_bayesian import MetaBayesian, MetaBeliefState, BeliefDriftDetector

__all__ = [
    "SearchCredibility",
    "KnowledgeUpdater",
    "KnowledgeClaimBelief",
    "ConflictResolver",
    "ChangePointDetector",
    "OnlineChangePoint",
    "OfflineChangePoint",
    "AgentBelief",
    "SpeciesStatusBelief",
    "MetaBayesian",
    "MetaBeliefState",
    "BeliefDriftDetector",
]
