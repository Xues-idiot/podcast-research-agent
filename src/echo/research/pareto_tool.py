"""帕累托分布工具"""

import math
from typing import Optional


class ParetoTool:
    _instance: Optional["ParetoTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def pdf(self, x: float, alpha: float, xm: float = 1) -> float:
        if x < xm:
            return 0.0
        return alpha * (xm ** alpha) / (x ** (alpha + 1))

    def cdf(self, x: float, alpha: float, xm: float = 1) -> float:
        if x < xm:
            return 0.0
        return 1 - (xm / x) ** alpha


def get_pareto_tool() -> ParetoTool:
    return ParetoTool()
