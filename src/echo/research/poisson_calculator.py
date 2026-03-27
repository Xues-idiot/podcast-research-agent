"""泊松分布计算器"""

import math
from typing import Optional


class PoissonCalculator:
    _instance: Optional["PoissonCalculator"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def poisson(self, lambda_val: float, k: int) -> float:
        if k < 0 or lambda_val <= 0:
            return 0.0
        return (lambda_val ** k * math.exp(-lambda_val)) / math.factorial(k)

    def expected_value(self, lambda_val: float) -> float:
        return lambda_val

    def variance(self, lambda_val: float) -> float:
        return lambda_val


def get_poisson_calculator() -> PoissonCalculator:
    return PoissonCalculator()
