"""Beta二项分布工具"""

import math
from typing import Optional


class BetaBinomial:
    _instance: Optional["BetaBinomial"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def pmf(self, k: int, n: int, alpha: float, beta: float) -> float:
        if k < 0 or k > n:
            return 0.0
        coef = math.comb(n, k)
        beta_k = math.gamma(alpha + k) * math.gamma(beta + n - k) / math.gamma(alpha + beta + n)
        beta_total = math.gamma(alpha) * math.gamma(beta) / math.gamma(alpha + beta)
        return coef * (beta_k / beta_total)


def get_beta_binomial() -> BetaBinomial:
    return BetaBinomial()
