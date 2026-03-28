"""对数正态分布工具"""

import math
from typing import Optional


class LogNormalDistribution:
    _instance: Optional["LogNormalDistribution"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def pdf(self, x: float, mu: float = 0, sigma: float = 1) -> float:
        if x <= 0:
            return 0.0
        return math.exp(-((math.log(x) - mu) ** 2) / (2 * sigma ** 2)) / (x * sigma * math.sqrt(2 * math.pi))

    def mean(self, mu: float = 0, sigma: float = 1) -> float:
        return math.exp(mu + sigma ** 2 / 2)

    def variance(self, mu: float = 0, sigma: float = 1) -> float:
        return (math.exp(sigma ** 2) - 1) * math.exp(2 * mu + sigma ** 2)


def get_log_normal_distribution() -> LogNormalDistribution:
    return LogNormalDistribution()
