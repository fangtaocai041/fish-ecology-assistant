"""
概率分布封装 — 工程化概率分布

提供常用概率分布的工程化接口，作为贝叶斯推理的构件。
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Any, Optional, Union

import numpy as np


@dataclass
class BetaDistribution:
    """Beta 分布 — 二元结果的概率分布

    参数:
      alpha: 形状参数 α (成功计数)
      beta:  形状参数 β (失败计数)
    """

    alpha: float
    beta: float

    @property
    def mean(self) -> float:
        total = self.alpha + self.beta
        return self.alpha / total if total > 0 else 0.0

    @property
    def variance(self) -> float:
        total = self.alpha + self.beta
        if total <= 1:
            return 0.25
        return (self.alpha * self.beta) / (total * total * (total + 1))

    @property
    def mode(self) -> float:
        if self.alpha > 1 and self.beta > 1:
            return (self.alpha - 1) / (self.alpha + self.beta - 2)
        return self.mean

    def pdf(self, x: Union[float, np.ndarray]) -> Union[float, np.ndarray]:
        """概率密度函数"""
        from scipy.stats import beta as beta_dist  # type: ignore

        return beta_dist.pdf(x, self.alpha, self.beta)

    def ppf(self, q: float) -> float:
        """分位点函数"""
        from scipy.stats import beta as beta_dist  # type: ignore

        return float(beta_dist.ppf(q, self.alpha, self.beta))

    def credible_interval(self, prob: float = 0.95) -> tuple[float, float]:
        return (self.ppf((1 - prob) / 2), self.ppf(1 - (1 - prob) / 2))

    def sample(self, n: int = 1000) -> np.ndarray:
        return np.random.beta(self.alpha, self.beta, size=n)


@dataclass
class NormalDistribution:
    """正态分布 — 连续量的概率分布"""

    mu: float
    sigma: float

    @property
    def mean(self) -> float:
        return self.mu

    @property
    def variance(self) -> float:
        return self.sigma**2

    def pdf(self, x: Union[float, np.ndarray]) -> Union[float, np.ndarray]:
        from scipy.stats import norm  # type: ignore

        return norm.pdf(x, self.mu, self.sigma)

    def ppf(self, q: float) -> float:
        from scipy.stats import norm  # type: ignore

        return float(norm.ppf(q, self.mu, self.sigma))

    def credible_interval(self, prob: float = 0.95) -> tuple[float, float]:
        z = 1.96 if prob == 0.95 else float(norm.ppf(1 - (1 - prob) / 2))
        return (self.mu - z * self.sigma, self.mu + z * self.sigma)

    def sample(self, n: int = 1000) -> np.ndarray:
        return np.random.normal(self.mu, self.sigma, size=n)


@dataclass
class GammaDistribution:
    """Gamma 分布 — 正值的概率分布 (率参数、精度参数)"""

    shape: float  # α (形状)
    rate: float  # β (速率), 1/scale

    @property
    def mean(self) -> float:
        return self.shape / self.rate if self.rate > 0 else float("inf")

    @property
    def variance(self) -> float:
        return self.shape / (self.rate**2) if self.rate > 0 else float("inf")

    def sample(self, n: int = 1000) -> np.ndarray:
        return np.random.gamma(self.shape, 1.0 / self.rate, size=n)


@dataclass
class DirichletDistribution:
    """Dirichlet 分布 — 多类别概率分布"""

    alphas: list[float]

    @property
    def mean(self) -> list[float]:
        total = sum(self.alphas)
        return [a / total for a in self.alphas]

    def sample(self, n: int = 1000) -> np.ndarray:
        return np.random.dirichlet(self.alphas, size=n)

    @property
    def k(self) -> int:
        return len(self.alphas)
