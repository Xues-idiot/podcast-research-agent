"""正态分布计算器"""

import math
from typing import Optional


class NormalDistribution:
    _instance: Optional["NormalDistribution"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def pdf(self, x: float, mean: float = 0, stdev: float = 1) -> float:
        if stdev <= 0:
            return 0.0
        exp_val = -0.5 * ((x - mean) / stdev) ** 2
        return (1 / (stdev * math.sqrt(2 * math.pi))) * math.exp(exp_val)

    def cdf(self, x: float, mean: float = 0, stdev: float = 1) -> float:
        if stdev <= 0:
            return 0.0
        return 0.5 * (1 + math.erf((x - mean) / (stdev * math.sqrt(2))))


def get_normal_distribution() -> NormalDistribution:
    return NormalDistribution()
