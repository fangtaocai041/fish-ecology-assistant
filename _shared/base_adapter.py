"""
BaseAdapter — 所有 adapter 的基类

消除 7 个 adapter 的重复代码：
  __init__ + _init_engine + info + health + import pattern

Usage:
    class MyAdapter(BaseAdapter):
        project_name = "my-project"
        _core_attr = "_engine"

        def _init_engine(self):
            self._engine = MyEngine()

        def search(self, query, **kwargs):
            return {"status": "ok", "result": self._engine.do(query)}
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Dict

# import fallback: _shared → scripts → object
try:
    from _shared.adapter_protocol import IProjectAdapter, BayesianAdapterMixin
except ImportError:
    try:
        from scripts.adapter_protocol import IProjectAdapter, BayesianAdapterMixin
    except ImportError:
        IProjectAdapter = object
        BayesianAdapterMixin = object


class BaseAdapter(IProjectAdapter, BayesianAdapterMixin):
    """标准适配器基类 — 所有项目继承此即可

    子类只需实现:
      - project_name (class var)
      - _core_attr (class var)
      - _init_engine() (instance method)
      - search() (instance method)
    其余: health / info / self_check / fast_search / deep_analyze 自动提供
    """

    project_name: str = "base"
    _core_attr: str = "_engine"
    version: str = "v8.0.0"

    def __init__(self, **kwargs):
        self._engine = None
        self._init_engine(**kwargs)

    def _init_engine(self, **kwargs):
        """子类在此初始化引擎"""

    def health(self) -> Dict[str, Any]:
        result = {
            "project": self.project_name,
            "version": self.version,
            "status": "HEALTHY" if self._engine else "DEGRADED",
        }
        # bayesian injection
        try:
            from _bayesian import BetaBelief
            b = BetaBelief(alpha=5, beta=5)
            if self._engine:
                b.update(successes=1, trials=1)
            result["bayesian_confidence"] = round(b.mean(), 4)
            result["bayesian_ci_95"] = [round(v, 4) for v in b.credible_interval()]
        except ImportError:
            pass
        return result

    def info(self) -> Dict[str, Any]:
        return {
            "project": self.project_name,
            "version": self.version,
            "role": getattr(self, "role", self.__class__.__name__),
            "capabilities": ["search", "health", "info", "self_check", "fast_search", "deep_analyze"],
        }
