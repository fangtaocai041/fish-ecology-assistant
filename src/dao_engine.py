"""
Dao Engine — 工程语言化·代码化·落地执行层

用法:
  python dao_engine.py "珠星三块鱼"
  python dao_engine.py "Tribolodon hakonensis"
  python dao_engine.py "鳤"

哲学链 → 代码映射:
  道 (Dao)     → DaoQuery        — 外部研究问题, 结构化输入
  一 (One)     → OneEntry        — 统一入口, 命令进入系统
  二 (Two)     → YinYangDuality  — 太极生两仪: S(阴/静/知识) ↔ V(阳/动/验证)
  三 (Three)   → TriangleCore    — 矛盾统一的密闭三元组
  万物 (Myriad)→ MyriadManifest  — 三角赋能后的一切输出
"""

from __future__ import annotations

import sys
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any, Dict, List, Optional


# ═══════════════════════════════════════════════════
# L0: 道 Dao — 外部世界
# ═══════════════════════════════════════════════════

class DaoSource(str, Enum):
    CLI = "cli"
    API = "api"
    SKILL = "skill"
    DELEGATE = "delegate"


@dataclass
class DaoQuery:
    """结构化研究问题 (道)."""
    source: DaoSource
    query: str
    chinese_name: str = ""
    context: Dict[str, Any] = field(default_factory=dict)


# ═══════════════════════════════════════════════════
# L1: 一 One — 统一入口
# ═══════════════════════════════════════════════════

@dataclass
class OneEntry:
    """统一入口 — one entry point."""
    query: DaoQuery
    result: Optional[Any] = None


# ═══════════════════════════════════════════════════
# L2: 二 Two — 阴阳二象性
# ═══════════════════════════════════════════════════

@dataclass
class YinYangDuality:
    """太极生两仪 — S(知识供给) ↔ V(验证搜索).

    Attributes:
        yin: 知识 (S / fish-ecology-assistant)
        yang: 验证 (V / cognitive-search-engine)
        harmony: 是否和谐运转
    """
    yin: Dict[str, Any]
    yang: Dict[str, Any]
    harmony: bool = False


# ═══════════════════════════════════════════════════
# L3: 三 Three — 三角核心
# ═══════════════════════════════════════════════════

@dataclass
class TriangleCore:
    """矛盾统一的密闭三元组.

    三角核心的三个顶点:
      S (fish-ecology-assistant): 知识供给
      V (cognitive-search-engine): 搜索验证
      T (eon-core): 三角核心 / 演化引擎

    Attributes:
        complete: 三个顶点是否全部可用
        vertices: 各顶点健康状态
    """
    complete: bool = False
    vertices: Dict[str, bool] = field(default_factory=dict)


# ═══════════════════════════════════════════════════
# L4+: 万物 Myriad — 三角赋能后的一切输出
# ═══════════════════════════════════════════════════

@dataclass
class MyriadManifest:
    """万物展现 — 所有可能的输出."""
    species_profile: Optional[Dict[str, Any]] = None
    search_results: Optional[List[Dict[str, Any]]] = None
    credibility_report: Optional[Dict[str, Any]] = None
    delegated_tasks: List[str] = field(default_factory=list)


# ═══════════════════════════════════════════════════
# 执行链
# ═══════════════════════════════════════════════════

def execute(entry: OneEntry) -> MyriadManifest:
    """道→一→二→三→万物的完整执行链。"""
    hub = None
    try:
        from .project_hub import get_hub
        hub = get_hub()
    except ImportError:
        pass

    # L0: 已收到 DaoQuery
    # L1: 已创建 OneEntry
    # L2: 检查 S↔V 二象性
    if hub:
        triangle = hub.triangle_status()
        yinyang = YinYangDuality(
            yin=triangle.get("fish", {}),
            yang=triangle.get("cognitive", {}),
            harmony=all(m.get("available", False) for m in [triangle.get("fish", {}), triangle.get("cognitive", {})]),
        )
    else:
        yinyang = YinYangDuality(yin={}, yang={})

    # L3: 检查三角核心密闭性
    triangle_complete = hub.is_triangle_complete() if hub else False
    core = TriangleCore(
        complete=triangle_complete,
        vertices={m.key: m.available for m in hub.triangle} if hub else {},
    )

    # L4+: 执行 KB-First 搜索
    result = MyriadManifest()
    try:
        from .orchestrator import get_orchestrator
        orch = get_orchestrator()
        kb_result = orch.kb_first_lookup(entry.query.query, entry.query.chinese_name)
        result.species_profile = {
            "found": kb_result.found,
            "scientific_name": kb_result.scientific_name,
            "chinese_name": kb_result.chinese_name,
            "summary": kb_result.summary_text,
        }
    except ImportError:
        pass

    return result


# ═══════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════

def main() -> None:
    """CLI entry point."""
    if len(sys.argv) < 2:
        print("用法: python dao_engine.py <物种名>")
        print("示例: python dao_engine.py 鳤")
        sys.exit(1)

    query_str = " ".join(sys.argv[1:])
    query = DaoQuery(source=DaoSource.CLI, query=query_str)
    entry = OneEntry(query=query)
    result = execute(entry)

    if result.species_profile:
        print(result.species_profile.get("summary", "无结果"))
    else:
        print(f"未找到: {query_str}")


if __name__ == "__main__":
    main()
