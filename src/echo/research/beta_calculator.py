"""贝塔函数计算器"""

import math
from typing import Optional


class BetaCalculator:
    _instance: Optional["BetaCalculator"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def beta(self, a: float, b: float) -> Optional[float]:
        if a <= 0 or b <= 0:
            return None
        try:
            return math.gamma(a) * math.gamma(b) / math.gamma(a + b)
        except (ValueError, OverflowError):
            return None


def get_beta_calculator() -> BetaCalculator:
    return BetaCalculator()
