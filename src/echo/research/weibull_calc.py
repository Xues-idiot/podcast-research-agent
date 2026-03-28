"""威布尔分布工具"""

import math
from typing import Optional


class WeibullDistribution:
    _instance: Optional["WeibullDistribution"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def pdf(self, x: float, shape: float, scale: float = 1) -> float:
        if x <= 0:
            return 0.0
        return (shape / scale) * (x / scale) ** (shape - 1) * math.exp(-(x / scale) ** shape)

    def cdf(self, x: float, shape: float, scale: float = 1) -> float:
        if x <= 0:
            return 0.0
        return 1 - math.exp(-(x / scale) ** shape)


def get_weibull_distribution() -> WeibullDistribution:
    return WeibullDistribution()
