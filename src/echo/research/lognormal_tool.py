"""对数正态分布工具"""

import math
from typing import Optional


class LognormalTool:
    _instance: Optional["LognormalTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def pdf(self, x: float, mu: float, sigma: float) -> float:
        if x <= 0:
            return 0.0
        return (1 / (x * sigma * math.sqrt(2 * math.pi))) * math.exp(-(math.log(x) - mu) ** 2 / (2 * sigma ** 2))


def get_lognormal_tool() -> LognormalTool:
    return LognormalTool()
