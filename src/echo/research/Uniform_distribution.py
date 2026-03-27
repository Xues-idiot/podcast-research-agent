"""均匀分布工具"""

import random
from typing import Optional


class UniformDistribution:
    _instance: Optional["UniformDistribution"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def pdf(self, x: float, a: float, b: float) -> float:
        if a <= x <= b:
            return 1 / (b - a)
        return 0.0

    def cdf(self, x: float, a: float, b: float) -> float:
        if x < a:
            return 0.0
        if x > b:
            return 1.0
        return (x - a) / (b - a)

    def sample(self, a: float, b: float) -> float:
        return random.uniform(a, b)


def get_uniform_distribution() -> UniformDistribution:
    return UniformDistribution()
