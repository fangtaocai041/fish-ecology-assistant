"""
贝叶斯推理引擎 — 共轭更新 + 数值近似

提供无需 MCMC 的高效贝叶斯推理。
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional, Union

import numpy as np


def conjugate_update(
    prior_type: str,
    prior_params: dict,
    data: Union[list, dict],
) -> dict:
    """共轭先验更新 — 统一接口

    参数:
      prior_type: "beta" | "normal" | "dirichlet"
      prior_params: 先验参数字典
      data: 观测数据

    返回:
      后验参数字典
    """
    if prior_type == "beta":
        from .engine import BetaBelief

        b = BetaBelief(**prior_params)
        b.update(**data)
        return b.posterior()

    elif prior_type == "normal":
        from .engine import NormalBelief

        n = NormalBelief(**prior_params)
        n.update(**data)
        return n.posterior()

    elif prior_type == "dirichlet":
        from .engine import DirichletBelief

        d = DirichletBelief(**prior_params)
        d.update(**data)
        return d.posterior()

    else:
        raise ValueError(f"Unknown prior type: {prior_type}")


@dataclass
class BayesianInference:
    """贝叶斯推理 — 多步推理管线

    支持链式更新和多证据源融合。
    """

    prior_type: str
    prior_params: dict

    def __post_init__(self):
        self._steps: list[dict] = []
        self._result: Optional[dict] = None

    def add_evidence(self, data: dict, label: str = "") -> "BayesianInference":
        """添加一条证据"""
        self._steps.append({"data": data, "label": label or f"step_{len(self._steps)}"})
        return self

    def run(self) -> dict:
        """执行所有推理步"""
        current = dict(self.prior_params)
        for step in self._steps:
            current = conjugate_update(self.prior_type, current, step["data"])
            step["posterior"] = dict(current)
        self._result = current
        return current

    @property
    def steps(self) -> list[dict]:
        return self._steps

    @property
    def result(self) -> dict:
        if self._result is None:
            return self.run()
        return self._result
