"""伽马函数计算器"""

import math
from typing import Optional


class GammaCalculator:
    _instance: Optional["GammaCalculator"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def gamma(self, n: float) -> Optional[float]:
        if n <= 0:
            return None
        try:
            return math.gamma(n)
        except ValueError:
            return None

    def log_gamma(self, n: float) -> Optional[float]:
        if n <= 0:
            return None
        try:
            return math.lgamma(n)
        except ValueError:
            return None


def get_gamma_calculator() -> GammaCalculator:
    return GammaCalculator()
