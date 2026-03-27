"""对数计算器"""

from typing import Optional
import math


class LogarithmCalculator:
    _instance: Optional["LogarithmCalculator"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def log(self, x: float, base: float = math.e) -> Optional[float]:
        if x <= 0 or base <= 0 or base == 1:
            return None
        return math.log(x, base)

    def ln(self, x: float) -> Optional[float]:
        if x <= 0:
            return None
        return math.log(x)

    def log10(self, x: float) -> Optional[float]:
        if x <= 0:
            return None
        return math.log10(x)

    def log2(self, x: float) -> Optional[float]:
        if x <= 0:
            return None
        return math.log2(x)


def get_logarithm_calculator() -> LogarithmCalculator:
    return LogarithmCalculator()
