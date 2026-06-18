"""
memory — MAGMA 四维正交图谱记忆

整合 MAGMA 四维图谱记忆到鱼类生态学知识供给引擎:
  语义图 (Semantic) — 物种/文献内容相似性
  时序图 (Temporal) — 时间关联
  因果图 (Causal)   — 因果关系链
  实体图 (Entity)   — 物种/栖息地/文献实体关系

整合自: san-sheng-wanwu-core (硅基生命体框架)
论文: MAGMA (arXiv 2601.03236)
"""

from .magma import (
    MagmaMemory, MemoryNode, Relation, RelationType,
    CharacterNgramEncoder, HuggingFaceEncoder, create_encoder,
)
from .consolidate import MemorySystem, MemoryItem, ebbinghaus_forgetting, reinforcement_boost

__all__ = [
    "MagmaMemory", "MemoryNode", "Relation", "RelationType",
    "CharacterNgramEncoder", "HuggingFaceEncoder", "create_encoder",
    "MemorySystem", "MemoryItem",
    "ebbinghaus_forgetting", "reinforcement_boost",
]
