"""几何分布工具"""

import random
from typing import Optional


class GeometricDistribution:
    _instance: Optional["GeometricDistribution"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def pmf(self, k: int, p: float) -> float:
        if k < 1:
            return 0.0
        return (1 - p) ** (k - 1) * p

    def sample(self, p: float) -> int:
        count = 1
        while random.random() >= p:
            count += 1
        return count


def get_geometric_distribution() -> GeometricDistribution:
    return GeometricDistribution()
