"""
贝叶斯信念引擎 — 工程化信念管理

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
信念有强弱，且随证据改变  (Bayesian Engineering)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

提供三类工程化信念原语:
  - BetaBelief:    二元结果信念 (可信/不可信、成功/失败)
  - NormalBelief:  连续量信念 (种群大小、生长率)
  - DirichletBelief: 多类别信念 (多源分类、多模型选择)

每个信念对象:
  1. 携带先验 (prior)
  2. 支持更新 (update)
  3. 给出后验 (posterior)
  4. 量化不确定性 (credible_interval)
  5. 可自检 (self_check)
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Any, Callable, Optional

import numpy as np

from .self_check import SelfCheckReport, SelfCheckMixin


# ═══════════════════════════════════════════════════════════
# 基类
# ═══════════════════════════════════════════════════════════


class BayesianEngine(SelfCheckMixin):
    """贝叶斯引擎基类 — 所有信念对象的共同祖先

    工程化契约:
      - prior()       → 返回先验参数
      - update(data)  → 用新证据更新信念
      - posterior()   → 返回后验分布参数
      - mean()        → 后验均值 (点估计)
      - credible_interval(prob) → 可信区间 (不确定性量化)
      - self_check()  → 自我检验报告
    """

    def prior(self) -> dict:
        raise NotImplementedError

    def update(self, data: Any) -> "BayesianEngine":
        raise NotImplementedError

    def posterior(self) -> dict:
        raise NotImplementedError

    def mean(self) -> float:
        raise NotImplementedError

    def credible_interval(self, prob: float = 0.95) -> tuple:
        raise NotImplementedError

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}("
            f"mean={self.mean():.4f}, "
            f"95% CI={self.credible_interval()}"
            f")"
        )


# ═══════════════════════════════════════════════════════════
# Beta 信念 — 二元结果 (成功/失败、可信/不可信、存在/不存在)
# ═══════════════════════════════════════════════════════════


@dataclass
class BetaBelief(BayesianEngine):
    """Beta 信念：二元结果的贝叶斯更新

    用于:
      - 搜索引擘可信度 (成功/失败)
      - 文献可信度 (可信/不可信)
      - 物种存在判断 (存在/不存在)
      - 冲突仲裁中的源可靠性

    工程化接口:
      >>> belief = BetaBelief(alpha=2, beta=2)    # 先验：均匀/谨慎
      >>> belief.update(successes=5, trials=6)    # 证据
      >>> belief.mean()                           # 后验均值 ≈ 0.7
      >>> belief.credible_interval()              # 可信区间
      >>> belief.self_check()                     # 自检

    属性:
      alpha: 先验"成功"计数
      beta:  先验"失败"计数
      prior_alpha, prior_beta: 先验参数 (用于自检)
    """

    alpha: float = 1.0
    beta: float = 1.0
    prior_alpha: float = field(default=1.0, init=False)
    prior_beta: float = field(default=1.0, init=False)

    def __post_init__(self):
        """初始化时记录先验参数 (用于自检)"""
        object.__setattr__(self, "prior_alpha", self.alpha)
        object.__setattr__(self, "prior_beta", self.beta)

    def prior(self) -> dict:
        return {"alpha": self.prior_alpha, "beta": self.prior_beta}

    def update(
        self,
        successes: float = 0,
        failures: float = 0,
        trials: Optional[float] = None,
    ) -> "BetaBelief":
        """贝叶斯更新：后验 = 先验 + 证据

        参数:
          successes: 成功次数 (正证据)
          failures:  失败次数 (负证据)
          trials:    总试验次数 (若提供则 failure = trials - successes)
        """
        if trials is not None:
            failures = trials - successes
        self.alpha += successes
        self.beta += failures
        return self

    def posterior(self) -> dict:
        return {"alpha": self.alpha, "beta": self.beta}

    def mean(self) -> float:
        """后验均值 = α / (α + β)"""
        total = self.alpha + self.beta
        if total == 0:
            return 0.5
        return self.alpha / total

    def variance(self) -> float:
        """后验方差"""
        total = self.alpha + self.beta
        if total <= 1:
            return 0.25
        return (self.alpha * self.beta) / (total * total * (total + 1))

    def credible_interval(self, prob: float = 0.95) -> tuple:
        """Beta 分布的可信区间 (基于正态近似)"""
        mean = self.mean()
        std = math.sqrt(self.variance())
        if std < 1e-10:
            return (mean, mean)
        from scipy.stats import beta as beta_dist  # type: ignore

        return (
            float(beta_dist.ppf((1 - prob) / 2, self.alpha, self.beta)),
            float(beta_dist.ppf(1 - (1 - prob) / 2, self.alpha, self.beta)),
        )

    def sample(self, n: int = 1000) -> np.ndarray:
        """从后验分布采样"""
        return np.random.beta(self.alpha, self.beta, size=n)

    def __add__(self, other: "BetaBelief") -> "BetaBelief":
        """信念融合：两个 Beta 信念合并"""
        return BetaBelief(
            alpha=self.alpha + other.alpha - self.prior_alpha,
            beta=self.beta + other.beta - self.prior_beta,
        )

    def weight(self) -> float:
        """证据权重：有效样本量 = α + β"""
        return self.alpha + self.beta


# ═══════════════════════════════════════════════════════════
# Normal 信念 — 连续量 (生长率、种群大小、环境参数)
# ═══════════════════════════════════════════════════════════


@dataclass
class NormalBelief(BayesianEngine):
    """Normal 信念：连续量的贝叶斯更新 (共轭先验)

    用于:
      - 生长率估计
      - 种群丰度
      - 环境参数均值

    工程化接口:
      >>> belief = NormalBelief(mu=0, sigma=10)     # 先验：均值0,不确定性大
      >>> belief.update(observations=[5.2, 4.8, 5.5])  # 证据
      >>> belief.mean()
      >>> belief.credible_interval()
    """

    mu: float = 0.0
    sigma: float = 10.0
    n: float = 1.0  # 先验有效样本量
    prior_mu: float = field(default=0.0, init=False)
    prior_sigma: float = field(default=10.0, init=False)
    prior_n: float = field(default=1.0, init=False)

    def __post_init__(self):
        object.__setattr__(self, "prior_mu", self.mu)
        object.__setattr__(self, "prior_sigma", self.sigma)
        object.__setattr__(self, "prior_n", self.n)

    def prior(self) -> dict:
        return {"mu": self.prior_mu, "sigma": self.prior_sigma, "n": self.prior_n}

    def update(
        self,
        observations: Optional[list[float]] = None,
        sample_mean: Optional[float] = None,
        sample_std: Optional[float] = None,
        sample_n: Optional[int] = None,
    ) -> "NormalBelief":
        """用观测数据更新正态信念

        参数:
          observations: 原始观测值列表
          sample_mean: 样本均值 (若已知)
          sample_std:  样本标准差 (若已知)
          sample_n:    样本量 (若已知)
        """
        if observations is not None:
            arr = np.array(observations, dtype=float)
            sample_mean = float(np.mean(arr))
            sample_std = float(np.std(arr, ddof=1)) if len(arr) > 1 else 1.0
            sample_n = len(arr)

        if sample_n is None or sample_mean is None:
            return self  # 无有效证据

        # 共轭更新: posterior precision = prior precision + sample precision
        prior_precision = self.n / (self.sigma**2 + 1e-10)
        if sample_std and sample_std > 0:
            sample_precision = sample_n / (sample_std**2 + 1e-10)
        else:
            sample_precision = sample_n / (1.0**2)

        posterior_precision = prior_precision + sample_precision
        posterior_mu = (
            prior_precision * self.mu + sample_precision * sample_mean
        ) / posterior_precision
        posterior_sigma = 1.0 / math.sqrt(posterior_precision + 1e-10)
        posterior_n = self.n + sample_n

        self.mu = posterior_mu
        self.sigma = posterior_sigma
        self.n = posterior_n
        return self

    def posterior(self) -> dict:
        return {"mu": self.mu, "sigma": self.sigma, "n": self.n}

    def mean(self) -> float:
        return self.mu

    def variance(self) -> float:
        return self.sigma**2

    def credible_interval(self, prob: float = 0.95) -> tuple:
        from scipy.stats import norm  # type: ignore

        z = norm.ppf(1 - (1 - prob) / 2)
        return (self.mu - z * self.sigma, self.mu + z * self.sigma)

    def sample(self, n: int = 1000) -> np.ndarray:
        return np.random.normal(self.mu, self.sigma, size=n)


# ═══════════════════════════════════════════════════════════
# Dirichlet 信念 — 多类别 (多源分类、多模型选择)
# ═══════════════════════════════════════════════════════════


@dataclass
class DirichletBelief(BayesianEngine):
    """Dirichlet 信念：多类别概率的贝叶斯更新

    用于:
      - 多源证据融合
      - 多模型选择
      - 多类别分类

    工程化接口:
      >>> belief = DirichletBelief(alphas=[1, 1, 1])  # 先验：三类等可能
      >>> belief.update(observations=[0, 1, 2, 1, 0])  # 证据：类别索引
      >>> belief.mean()           # [类0概率, 类1概率, 类2概率]
      >>> belief.credible_interval()  # 每个类的可信区间
    """

    alphas: list[float] = field(default_factory=lambda: [1.0, 1.0, 1.0])
    prior_alphas: list[float] = field(default_factory=lambda: [1.0, 1.0, 1.0], init=False)

    def __post_init__(self):
        if len(self.prior_alphas) == 3 and self.prior_alphas == [1.0, 1.0, 1.0]:
            object.__setattr__(self, "prior_alphas", list(self.alphas))
        total = sum(self.alphas)
        if total == 0:
            self.alphas = [1.0] * len(self.alphas)

    def prior(self) -> dict:
        return {"alphas": self.prior_alphas}

    def update(
        self,
        observations: Optional[list[int]] = None,
        counts: Optional[list[float]] = None,
    ) -> "DirichletBelief":
        """用观测数据更新 Dirichlet 信念

        参数:
          observations: 类别索引列表 (每个元素为类别编号)
          counts:       每个类别的计数列表 (与 observations 二选一)
        """
        k = len(self.alphas)
        if counts is not None:
            for i, c in enumerate(counts):
                if i < k:
                    self.alphas[i] += c
        elif observations is not None:
            for obs in observations:
                if 0 <= obs < k:
                    self.alphas[obs] += 1.0
        return self

    def posterior(self) -> dict:
        return {"alphas": self.alphas}

    def mean(self) -> list[float]:
        total = sum(self.alphas)
        if total == 0:
            return [1.0 / len(self.alphas)] * len(self.alphas)
        return [a / total for a in self.alphas]

    def variance(self) -> list[float]:
        total = sum(self.alphas)
        if total <= 1:
            return [0.25] * len(self.alphas)
        return [
            (a * (total - a)) / (total * total * (total + 1)) for a in self.alphas
        ]

    def credible_interval(self, prob: float = 0.95) -> list[tuple]:
        """每个类别的边际可信区间 (Beta 近似)"""
        total = sum(self.alphas)
        intervals = []
        for a in self.alphas:
            other = total - a
            # 边际 Beta(a, total-a)
            b = BetaBelief(alpha=a, beta=other)
            intervals.append(b.credible_interval(prob))
        return intervals

    def sample(self, n: int = 1000) -> np.ndarray:
        return np.random.dirichlet(self.alphas, size=n)

    @property
    def k(self) -> int:
        return len(self.alphas)
