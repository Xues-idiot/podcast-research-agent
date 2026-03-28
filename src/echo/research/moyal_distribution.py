"""Moyal分布工具"""

import math
from typing import Optional


class MoyalDistribution:
    _instance: Optional["MoyalDistribution"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def pdf(self, x: float, mu: float = 0, sigma: float = 1) -> float:
        if sigma <= 0:
            return 0.0
        z = (x - mu) / sigma
        return math.exp(-0.5 * (z + math.exp(-z))) / (sigma * math.sqrt(2 * math.pi))

    def mean(self, mu: float = 0, sigma: float = 1) -> float:
        return mu + sigma * 0.5772156649015329


def get_moyal_distribution() -> MoyalDistribution:
    return MoyalDistribution()
