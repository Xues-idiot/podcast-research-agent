"""F分布工具"""

import math
from typing import Optional


class FDistribution:
    _instance: Optional["FDistribution"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def pdf(self, x: float, d1: int, d2: int) -> float:
        if x <= 0:
            return 0.0
        num = math.gamma((d1 + d2) / 2) * (d1 / d2) ** (d1 / 2) * x ** (d1 / 2 - 1)
        denom = math.gamma(d1 / 2) * math.gamma(d2 / 2) * (1 + d1 * x / d2) ** ((d1 + d2) / 2)
        return num / denom

    def mean(self, d1: int, d2: int) -> float:
        return d2 / (d2 - 2) if d2 > 2 else 0.0


def get_f_distribution() -> FDistribution:
    return FDistribution()
