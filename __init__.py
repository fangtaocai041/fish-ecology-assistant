"""
fangtao_fishlab — 主系统统一入口

一键调用全部适配器 + 贝叶斯体系。

用法:
    from fangtao_fishlab import BetaBelief, health_check_all, get_adapter

    # 贝叶斯
    b = BetaBelief(2, 2)
    b.update(successes=5, trials=10)

    # 一键健康检查
    report = health_check_all()

    # 获取任意项目的适配器
    cse = get_adapter("cognitive-search-engine")
    porpoise = get_adapter("porpoise-agent")
"""

import sys as _sys
from pathlib import Path as _Path

# 确保自身在 sys.path 中
_root = str(_Path(__file__).resolve().parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)

from _bayesian import (
    BetaBelief,
    NormalBelief,
    DirichletBelief,
    SelfCheckReport,
    SelfCheckMixin,
)
from _bayesian.applications import (
    SearchCredibility,
    KnowledgeUpdater,
    ConflictResolver,
    ChangePointDetector,
    AgentBelief,
    MetaBayesian,
)
from _shared.types import AdapterState, SearchResult, CheckReport

__version__ = "v8.0.0"
__all__ = [
    "BetaBelief", "NormalBelief", "DirichletBelief",
    "SelfCheckReport", "SelfCheckMixin",
    "SearchCredibility", "KnowledgeUpdater", "ConflictResolver",
    "ChangePointDetector", "AgentBelief", "MetaBayesian",
    "AdapterState", "SearchResult", "CheckReport",
    "health_check_all", "get_adapter", "query_library",
    "__version__",
]


def health_check_all() -> dict:
    """一键健康检查所有项目"""
    from .scripts.health_check_all import check_all as _check
    return _check()


def get_adapter(project_name: str):
    """获取指定项目的适配器实例"""
    from importlib import import_module

    adapters = {
        "cognitive-search-engine": "cognitive-search-engine.src.adapter.CognitiveSearchAdapter",
        "fish-ecology-assistant": "fish-ecology-assistant.src.adapter.FishEcologyAdapter",
        "eon-core": "eon-core.src.adapter.EonCoreAdapter",
        "conflict-arbiter": "conflict-arbiter.src.adapter.ConflictArbiterAdapter",
        "porpoise-agent": "porpoise-agent.src.adapter.PorpoiseAdapter",
        "coilia-agent": "coilia-agent.src.adapter.CoiliaAdapter",
        "culter-agent": "culter-agent.src.adapter.CulterAdapter",
        "infrastructure": "infrastructure",
        "san-sheng-wanwu-core": "san-sheng-wanwu-core.src",  # module-level, no class
    }

    if project_name not in adapters:
        raise ValueError("Unknown: {} (available: {})".format(project_name, list(adapters.keys())))

    path = adapters[project_name]
    try:
        if "." in path:
            mod_path, cls_name = path.rsplit(".", 1)
            if "-" in mod_path:
                # hyphens in module path -> file-based import
                import importlib.util
                # build adapter file path: project/src/adapter.py
                proj_name = mod_path.split(".")[0]
                _p = "D:/Reasonix/fangtao_fishlab/{}/src/adapter.py".format(proj_name)
                spec = importlib.util.spec_from_file_location(cls_name, _p)
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)
                return getattr(mod, cls_name)()
            else:
                mod = import_module(mod_path)
            return getattr(mod, cls_name)()
        else:
            mod = import_module(path.replace("-", "_"))
            return mod
    except Exception as e:
        raise ImportError("Cannot load adapter '{}': {}".format(project_name, e)) from e


def query_library(keyword: str, category: str = "species") -> list:
    """搜索方陶文库

    Args:
        keyword: 搜索关键词
        category: "species" | "theories" | "notes" | "papers"

    Returns:
        匹配的文件路径列表
    """
    from pathlib import Path
    _lib = Path(__file__).resolve().parent.parent / "fangtao_library"
    if not _lib.exists():
        return []  # graceful: no library = no results

    search_dirs = {
        "species": _lib / "species",
        "theories": _lib / "方陶文库" / "02-基础理论",
        "notes": _lib / "方陶文库" / "01-研究笔记",
        "papers": _lib / "方陶文库" / "04-文献分析报告",
        "ecology": _lib / "方陶文库" / "11-数量生态学",
        "db": _lib / "方陶文库" / "06-数据库",
        "architecture": _lib / "方陶文库" / "05-项目架构",
    }

    target = search_dirs.get(category)
    if target is None or not target.exists():
        # fallback: 搜索整个方陶文库子目录
        wenku = _lib / "方陶文库"
        if wenku.exists():
            target = wenku

    results = []
    for f in target.rglob("*"):
        if f.is_file() and keyword.lower() in f.name.lower():
            results.append(str(f.relative_to(_lib)))
    return results
