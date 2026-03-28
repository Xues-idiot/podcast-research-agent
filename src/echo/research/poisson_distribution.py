"""泊松分布工具"""

import math
from typing import Optional


class PoissonDistribution:
    _instance: Optional["PoissonDistribution"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def pmf(self, k: int, lam: float) -> float:
        if k < 0:
            return 0.0
        return math.exp(-lam) * (lam ** k) / math.factorial(k)

    def mean(self, lam: float) -> float:
        return lam

    def variance(self, lam: float) -> float:
        return lam


def get_poisson_distribution() -> PoissonDistribution:
    return PoissonDistribution()
