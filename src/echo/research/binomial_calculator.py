"""二项分布计算器"""

import math
from typing import Optional


class BinomialCalculator:
    _instance: Optional["BinomialCalculator"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def binomial(self, n: int, p: float, k: int) -> float:
        if k < 0 or k > n:
            return 0.0
        return math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

    def expected_value(self, n: int, p: float) -> float:
        return n * p

    def variance(self, n: int, p: float) -> float:
        return n * p * (1 - p)


def get_binomial_calculator() -> BinomialCalculator:
    return BinomialCalculator()
