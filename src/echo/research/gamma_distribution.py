"""Gamma分布工具"""

import math
from typing import Optional


class GammaDistribution:
    _instance: Optional["GammaDistribution"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def pdf(self, x: float, shape: float, scale: float = 1) -> float:
        if x <= 0:
            return 0.0
        return (x ** (shape - 1) * math.exp(-x / scale)) / (math.gamma(shape) * scale ** shape)

    def mean(self, shape: float, scale: float = 1) -> float:
        return shape * scale

    def variance(self, shape: float, scale: float = 1) -> float:
        return shape * scale ** 2


def get_gamma_distribution() -> GammaDistribution:
    return GammaDistribution()
