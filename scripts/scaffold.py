#!/usr/bin/env python3
"""
新项目脚手架 — 一键生成 adapter 模板

借鉴 CrewAI CLI: `crewai create crew`
用法:
    python scaffold.py new-agent <name>   # 生成新的 adapter
    python scaffold.py list              # 列出已有项目

示例:
    python scaffold.py new-agent turtle-agent
    → 生成 turtle-agent/src/adapter.py, __init__.py, config/agent.yaml
"""

import sys
import os
from pathlib import Path

TEMPLATE_ADAPTER = '''"""{}Adapter — fangtao_fishlab 标准适配器.

自动生成于 scaffold.py，基于 BayesianAdapterMixin。
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Dict, Optional

# Path setup
_reasonix = str(Path(__file__).resolve().parent.parent.parent.parent)
if _reasonix not in sys.path:
    sys.path.insert(0, _reasonix)
_workspace_root = str(Path(__file__).resolve().parent.parent.parent.parent.parent)
if _workspace_root not in sys.path:
    sys.path.insert(0, _workspace_root)

try:
    from scripts.adapter_protocol import IProjectAdapter, BayesianAdapterMixin
except ImportError:
    IProjectAdapter = object
    BayesianAdapterMixin = object


class {}Adapter(IProjectAdapter, BayesianAdapterMixin):
    """{} — 自动生成的 IProjectAdapter 实现"""

    project_name = "{0}"
    _core_attr = "_engine"

    def __init__(self):
        self._engine = None
        self._init_engine()

    def _init_engine(self):
        """初始化引擎（此处放你的初始化逻辑）"""
        pass

    def search(self, query: str, **kwargs) -> Dict[str, Any]:
        """执行领域搜索"""
        return {{"query": query, "status": "stub", "note": "implement search logic"}}

    def health(self) -> Dict[str, Any]:
        """健康检查"""
        result = {{
            "project": self.project_name,
            "status": "HEALTHY" if self._engine else "DEGRADED",
        }}
        # Bayesian health injection (auto)
        try:
            from _bayesian import BetaBelief
            b = BetaBelief(alpha=5, beta=5)
            if self._engine:
                b.update(successes=1, trials=1)
            result["bayesian_confidence"] = round(b.mean(), 4)
        except ImportError:
            pass
        return result

    def info(self) -> Dict[str, Any]:
        """能力信息"""
        return {{
            "project": self.project_name,
            "version": "v8.0.0",
            "role": "{0}",
        }}
'''

TEMPLATE_INIT = '''"""{} — fangtao_fishlab 子项目"""

import sys as _sys
from pathlib import Path as _Path

_PROJECT_ROOT = str(_Path(__file__).resolve().parent)
if _PROJECT_ROOT not in _sys.path:
    _sys.path.insert(0, _PROJECT_ROOT)

from .adapter import {}Adapter

__all__ = ["{}Adapter"]
'''


def new_agent(name: str):
    """创建新 agent"""
    root = Path(__file__).resolve().parent.parent
    agent_dir = root / name / "src"
    agent_dir.mkdir(parents=True, exist_ok=True)

    cls_name = "".join(w.capitalize() for w in name.replace("-", "_").split("_"))

    # adapter.py
    adapter_path = agent_dir / "adapter.py"
    if adapter_path.exists():
        print(f"SKIP: {adapter_path} already exists")
    else:
        with open(adapter_path, "w", encoding="utf-8") as f:
            f.write(TEMPLATE_ADAPTER.format(name, cls_name, name.replace("-", " ")))
        print(f"CREATED: {adapter_path}")

    # __init__.py
    init_path = agent_dir / "__init__.py"
    if init_path.exists():
        print(f"SKIP: {init_path} already exists")
    else:
        with open(init_path, "w", encoding="utf-8") as f:
            f.write(TEMPLATE_INIT.format(name, cls_name, cls_name))
        print(f"CREATED: {init_path}")

    # 更新 fangtao_fishlab/__init__.py
    main_init = root / "__init__.py"
    if main_init.exists():
        content = main_init.read_text(encoding="utf-8")
        if name not in content:
            # 在 get_adapter 的 adapters dict 中添加条目
            entry = f'        "{name}": "{name}.src.adapter.{cls_name}Adapter",\n'
            insert_marker = "        if project_name not in adapters:"
            if insert_marker in content:
                content = content.replace(
                    '        "san-sheng-wanwu-core": "san-sheng-wanwu-core.src",\n',
                    f'        "san-sheng-wanwu-core": "san-sheng-wanwu-core.src",\n{entry}'
                )
                main_init.write_text(content, encoding="utf-8")
                print(f"UPDATED: {main_init} (added {name} to get_adapter)")


def list_agents():
    """列出已有项目"""
    root = Path(__file__).resolve().parent.parent
    for d in sorted(root.iterdir()):
        if d.is_dir() and not d.name.startswith(("_", ".", "config", "scripts")):
            has_adapter = (d / "src" / "adapter.py").exists()
            tag = " [adapter]" if has_adapter else " [no-adapter]"
            print(f"  {d.name}{tag}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scaffold.py <list|new-agent <name>>")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "list":
        list_agents()
    elif cmd == "new-agent" and len(sys.argv) >= 3:
        new_agent(sys.argv[2])
    else:
        print("Unknown command. Use: list | new-agent <name>")
        sys.exit(1)
