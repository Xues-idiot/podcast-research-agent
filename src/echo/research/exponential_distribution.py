"""指数分布计算器"""

import math
from typing import Optional


class ExponentialDistribution:
    _instance: Optional["ExponentialDistribution"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def pdf(self, x: float, lambda_val: float) -> float:
        if x < 0 or lambda_val <= 0:
            return 0.0
        return lambda_val * math.exp(-lambda_val * x)

    def cdf(self, x: float, lambda_val: float) -> float:
        if x < 0 or lambda_val <= 0:
            return 0.0
        return 1 - math.exp(-lambda_val * x)


def get_exponential_distribution() -> ExponentialDistribution:
    return ExponentialDistribution()
