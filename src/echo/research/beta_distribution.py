"""Beta分布工具"""

import math
from typing import Optional


class BetaDistribution:
    _instance: Optional["BetaDistribution"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def pdf(self, x: float, alpha: float, beta: float) -> float:
        if x <= 0 or x >= 1:
            return 0.0
        return (x ** (alpha - 1) * (1 - x) ** (beta - 1)) / math.gamma(alpha) * math.gamma(beta) / math.gamma(alpha + beta)

    def mean(self, alpha: float, beta: float) -> float:
        return alpha / (alpha + beta)

    def variance(self, alpha: float, beta: float) -> float:
        return (alpha * beta) / ((alpha + beta) ** 2 * (alpha + beta + 1))


def get_beta_distribution() -> BetaDistribution:
    return BetaDistribution()
