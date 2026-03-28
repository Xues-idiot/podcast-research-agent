"""t分布工具"""

import math
from typing import Optional


class TDistribution:
    _instance: Optional["TDistribution"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def pdf(self, t: float, df: int) -> float:
        return math.gamma((df + 1) / 2) / (math.sqrt(df * math.pi) * math.gamma(df / 2)) * (1 + t ** 2 / df) ** (-(df + 1) / 2)

    def mean(self, df: int) -> float:
        return 0.0 if df > 1 else 0.0

    def variance(self, df: int) -> float:
        return df / (df - 2) if df > 2 else 0.0


def get_t_distribution() -> TDistribution:
    return TDistribution()
