"""卡方分布计算器"""

import math
from typing import Optional


class ChiSquare:
    _instance: Optional["ChiSquare"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def pdf(self, x: float, k: int) -> float:
        if x <= 0 or k <= 0:
            return 0.0
        return (x ** (k/2 - 1) * math.exp(-x/2)) / (2 ** (k/2) * math.gamma(k/2))


def get_chi_square() -> ChiSquare:
    return ChiSquare()
