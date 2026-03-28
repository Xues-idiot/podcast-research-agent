"""二项分布工具"""

import math
from typing import Optional


class BinomialDistribution:
    _instance: Optional["BinomialDistribution"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def pmf(self, k: int, n: int, p: float) -> float:
        if k < 0 or k > n:
            return 0.0
        return math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

    def mean(self, n: int, p: float) -> float:
        return n * p

    def variance(self, n: int, p: float) -> float:
        return n * p * (1 - p)


def get_binomial_distribution() -> BinomialDistribution:
    return BinomialDistribution()
