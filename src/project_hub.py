"""
ProjectHub — fish-ecology-assistant 宿主容器 / 多项目协调中枢。

统一加载三角核心（fish / cognitive / eon）和衍生项目（porpoise, coilia, conflict, ...）。
提供跨项目委托、健康状态聚合、能力清单查询。

Usage:
    from src.project_hub import get_hub

    hub = get_hub()
    print(hub.health_all())
    print(hub.is_triangle_complete())
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


# ── Triangle Members ──

@dataclass
class TriangleMember:
    """三角核心成员."""
    key: str
    name: str
    symbol: str      # 符号表示 (S/V/T)
    pole: str        # 角色: 知识/验证/三角
    path: str        # 相对路径
    available: bool = False


@dataclass
class DerivedMember:
    """衍生项目成员（万物层）."""
    key: str
    name: str
    parent: str      # 所属三角成员
    path: str
    available: bool = False


# ── 三角核心定义 ──

TRIANGLE: List[TriangleMember] = [
    TriangleMember("fish", "Fish Ecology Assistant", "S", "知识供给", "fish-ecology-assistant"),
    TriangleMember("cognitive", "Cognitive Search Engine", "V", "搜索验证", "cognitive-search-engine"),
    TriangleMember("eon", "Eon Taiji Core", "T", "三角核心", "eon-core"),
]

DERIVED: List[DerivedMember] = [
    DerivedMember("porpoise", "长江江豚助手", "cognitive", "porpoise-agent"),
    DerivedMember("coilia", "刀鲚助手", "fish", "coilia-agent"),
    DerivedMember("culter", "红鳍原鲌助手", "fish", "culter-agent"),
    DerivedMember("conflict", "冲突仲裁器", "eon", "conflict-arbiter"),
]


# ── ProjectHub ──

class ProjectHub:
    """宿主容器 — 统一协调中枢。

    功能:
      - health_all(): 全项目健康状态聚合
      - capabilities(): 能力清单
      - triangle_status(): 三角核心状态
      - is_triangle_complete(): 密闭性检查
      - relationship_map(): ASCII 关系图
      - delegate_to(target, payload): 跨项目委托
      - search_species(query): 统一搜索入口
    """

    def __init__(self) -> None:
        self.triangle = TRIANGLE
        self.derived = DERIVED
        self._check_availability()

    def _check_availability(self) -> None:
        """Check which projects are actually available on disk."""
        workspace = Path(__file__).resolve().parent.parent.parent
        for m in self.triangle:
            m.available = (workspace / m.path).is_dir()
        for m in self.derived:
            m.available = (workspace / m.path).is_dir()

    def health_all(self) -> Dict[str, Any]:
        """全项目健康状态聚合。"""
        return {
            "philosophy": "道生一 · 一生二 · 二生三 · 三生万物",
            "one": self.triangle_status(),
            "two": {"S(阴/知识)": "fish-ecology-assistant", "V(阳/验证)": "cognitive-search-engine"},
            "three": {"T(三角)": "eon-core"},
            "myriad": {m.key: m.available for m in self.derived},
            "triangle_complete": self.is_triangle_complete(),
        }

    def capabilities(self) -> Dict[str, Any]:
        """能力清单。"""
        caps = {}
        # Triangle
        caps["triangle"] = {
            m.key: {
                "name": m.name,
                "symbol": m.symbol,
                "pole": m.pole,
                "available": m.available,
            }
            for m in self.triangle
        }
        # Myriad
        caps["myriad"] = {
            m.key: {
                "name": m.name,
                "parent": m.parent,
                "available": m.available,
            }
            for m in self.derived
        }
        return caps

    def triangle_status(self) -> Dict[str, Any]:
        """三角核心状态。"""
        return {
            m.key: {
                "name": m.name,
                "symbol": m.symbol,
                "pole": m.pole,
                "available": m.available,
            }
            for m in self.triangle
        }

    def is_triangle_complete(self) -> bool:
        """检查三角核心是否完整（所有三角成员可用）。"""
        return all(m.available for m in self.triangle)

    @staticmethod
    def relationship_map() -> str:
        """返回 ASCII 关系图。"""
        return """\
╔══════════════════════════════════════════════╗
║           三角核心 · 万物生态               ║
║                                            ║
║            ┌───────────┐                    ║
║            │  Eon T    │                    ║
║            │ (三角核心) │                    ║
║            └─────┬─────┘                    ║
║                  │                          ║
║          ┌───────┴───────┐                  ║
║          │               │                  ║
║    ┌─────┴─────┐   ┌────┴─────┐             ║
║    │ Fish (S)  │   │ Cog (V)  │             ║
║    │ 知识供给  │   │ 搜索验证 │             ║
║    └─────┬─────┘   └────┬─────┘             ║
║          │               │                  ║
║    ┌─────┴─────┐   ┌────┴─────┐             ║
║    │ coilia    │   │ porpoise │             ║
║    │ culter    │   │ (others) │             ║
║    └───────────┘   └──────────┘             ║
║                                            ║
║    道生一 · 一生二 · 二生三 · 三生万物      ║
╚══════════════════════════════════════════════╝"""

    def delegate_to(self, target: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """跨项目委托协议。

        Args:
            target: 目标项目 key (如 "cognitive", "porpoise")
            payload: 传递给目标项目的参数

        Returns:
            委托结果字典。
        """
        return {
            "delegation_from": "fish-ecology-assistant",
            "delegation_to": target,
            "payload": payload,
            "status": "accepted",
            "note": f"委托给 {target} 处理 — 转到对应项目获取结果",
        }

    def search_species(self, query: str, chinese: str = "") -> Dict[str, Any]:
        """统一搜索入口 — 先查 KB，需全量搜索时委托给 cognitive。

        Args:
            query: 搜索关键词（学名/中文名）
            chinese: 可选中文名提示

        Returns:
            搜索结果字典，包含 KB 匹配和委托路由信息。
        """
        from .orchestrator import get_orchestrator

        orch = get_orchestrator()
        result = orch.kb_first_lookup(query, chinese)
        output = {
            "query": query,
            "kb_result": {
                "found": result.found,
                "scientific_name": result.scientific_name,
                "chinese_name": result.chinese_name,
                "family": result.family,
                "score": result.score,
                "summary": result.summary_text,
            },
            "recommendation": result.search_recommendation,
        }
        if result.search_recommendation == "continue_to_c":
            output["delegation"] = self.delegate_to(
                "cognitive",
                {"query": query, "chinese": chinese, "kb_found": result.found},
            )
        return output


# ── Module-level singleton ──

_hub_instance: Optional[ProjectHub] = None


def get_hub() -> ProjectHub:
    """获取（缓存的）ProjectHub 单例。"""
    global _hub_instance
    if _hub_instance is None:
        _hub_instance = ProjectHub()
    return _hub_instance


def reset_hub() -> None:
    """重置单例（测试用）。"""
    global _hub_instance
    _hub_instance = None
