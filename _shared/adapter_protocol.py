"""
IProjectAdapter + BayesianAdapterMixin

Canonical: D:/Reasonix/scripts/adapter_protocol.py
Local copy: D:/Reasonix/fangtao_fishlab/_shared/adapter_protocol.py
Keep both in sync.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict


class IProjectAdapter(ABC):
    """标准适配器接口"""

    project_name: str = ""

    @abstractmethod
    def search(self, query: str, **kwargs) -> Dict[str, Any]:
        ...

    @abstractmethod
    def health(self) -> Dict[str, Any]:
        ...

    @abstractmethod
    def info(self) -> Dict[str, Any]:
        ...


class BayesianAdapterMixin:
    """贝叶斯适配器混入 — 标准化自检、两速模式、贝叶斯健康

    配置热接入: from_config() 从 YAML 读取 core_attr。
    """

    _core_attr: str = "_engine"

    @classmethod
    def from_config(cls):
        """从 config/agents.yaml 读取配置创建实例"""
        try:
            from _shared.config_loader import get_agent_config
            cfg = get_agent_config(getattr(cls, "project_name", ""))
            if cfg:
                cls._core_attr = cfg.get("core_attr", cls._core_attr)
        except ImportError:
            pass
        return cls()

    # ── health 归一化 ──

    def normalize_health(self, raw: dict) -> dict:
        out = dict(raw)
        if "project" not in out:
            out["project"] = getattr(self, "project_name", "unknown")
        if "status" not in out:
            out["status"] = "HEALTHY" if raw else "DEGRADED"
        if "core_loaded" not in out:
            core = getattr(self, self._core_attr, None)
            out["core_loaded"] = core is not None
        if "bayesian_confidence" not in out:
            try:
                out.update(self.bayesian_health())
            except Exception:
                pass
        return out

    # ── self_check ──

    def self_check(self):
        from _shared.types import CheckItem, CheckReport
        items = {}
        core_val = getattr(self, self._core_attr, None)
        items["core_loaded"] = CheckItem(
            name="核心引擎", passed=core_val is not None,
            value=core_val is not None,
            detail="loaded" if core_val else "not loaded"
        )
        try:
            from _bayesian import BetaBelief
            _b = BetaBelief(alpha=2, beta=2)
            _b.update(successes=5, trials=10)
            _ci = _b.credible_interval()
            items["bayesian"] = CheckItem(
                name="贝叶斯", passed=True, value=_b.mean(),
                detail="mean={:.3f}, CI=[{:.3f},{:.3f}]".format(_b.mean(), _ci[0], _ci[1])
            )
        except ImportError:
            items["bayesian"] = CheckItem(name="贝叶斯", passed=False, detail="unavailable")
        try:
            h = self.health()
            status = h.get("status", "?") if isinstance(h, dict) else getattr(h, "status", "?")
            items["health"] = CheckItem(
                name="健康", passed=status == "HEALTHY", value=status, detail="status=" + status
            )
        except Exception as e:
            items["health"] = CheckItem(name="健康", passed=False, detail=str(e)[:60])
        return CheckReport(
            project=getattr(self, "project_name", "unknown"), checks=items
        )

    def fast_search(self, query: str) -> Dict[str, Any]:
        try:
            return self.search(query)
        except Exception as e:
            return {"query": query, "mode": "fast", "error": str(e)[:60]}

    def deep_analyze(self, query: str) -> Dict[str, Any]:
        try:
            return self.search(query)
        except Exception as e:
            return {"query": query, "mode": "deep", "error": str(e)[:60]}

    def bayesian_health(self) -> Dict[str, Any]:
        try:
            from _bayesian import BetaBelief
            b = BetaBelief(alpha=5, beta=5)
            try:
                h = self.health()
                if h.get("status") == "HEALTHY":
                    b.update(successes=1, trials=1)
            except Exception:
                pass
            return {
                "bayesian_confidence": round(b.mean(), 4),
                "bayesian_ci_95": [round(v, 4) for v in b.credible_interval()],
            }
        except ImportError:
            return {"bayesian_confidence": 0.5}
