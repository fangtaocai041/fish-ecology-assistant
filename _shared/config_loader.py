"""
统一配置加载器 — 从 YAML 读取而不硬编码

借鉴 CrewAI: 配置与代码分离，非开发者可调整参数。

Usage:
    from _shared.config_loader import get_config, get_agent_config

    cfg = get_config()
    agent = get_agent_config("cognitive-search-engine")
    print(agent["role"], agent["bayesian_methods"])
"""

from pathlib import Path
from typing import Any, Optional

import yaml

_CONFIG_DIR = Path(__file__).resolve().parent.parent / "config"
_CONFIG_CACHE: dict[str, dict] = {}


def _load_yaml(name: str) -> dict:
    """加载 YAML 配置（带缓存）"""
    if name in _CONFIG_CACHE:
        return _CONFIG_CACHE[name]

    path = _CONFIG_DIR / name
    if path.exists():
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
    else:
        data = {}

    _CONFIG_CACHE[name] = data
    return data


def get_config() -> dict:
    """获取基础配置"""
    return _load_yaml("agents.yaml")


def get_agent_config(agent_name: str) -> dict:
    """获取指定项目的配置

    Args:
        agent_name: e.g. "cognitive-search-engine", "porpoise-agent"

    Returns:
        {role, goal, backstory, core_attr, bayesian_methods}
    """
    cfg = _load_yaml("agents.yaml")
    agents = cfg.get("agents", {})
    return agents.get(agent_name, {})


def get_bayesian_priors() -> dict:
    """获取贝叶斯先验配置"""
    return _load_yaml("bayesian_priors.yaml")


def get_engine_prior(engine_name: str) -> Optional[dict]:
    """获取特定引擎的先验参数"""
    priors = get_bayesian_priors()
    engines = priors.get("engine_priors", {})
    return engines.get(engine_name)


def get_search_quality_prior(mode: str) -> Optional[dict]:
    """获取搜索质量先验"""
    priors = get_bayesian_priors()
    quality = priors.get("search_quality", {})
    return quality.get(mode)


def list_agents() -> list[str]:
    """列出所有已配置的项目名"""
    cfg = _load_yaml("agents.yaml")
    return list(cfg.get("agents", {}).keys())
