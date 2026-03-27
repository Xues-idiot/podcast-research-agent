"""威布尔分布工具"""

import math
from typing import Optional


class WeibullTool:
    _instance: Optional["WeibullTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def pdf(self, x: float, k: float, lam: float) -> float:
        if x < 0:
            return 0.0
        return (k / lam) * (x / lam) ** (k - 1) * math.exp(-(x / lam) ** k)

    def cdf(self, x: float, k: float, lam: float) -> float:
        if x < 0:
            return 0.0
        return 1 - math.exp(-(x / lam) ** k)


def get_weibull_tool() -> WeibullTool:
    return WeibullTool()
