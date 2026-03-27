"""幂计算器"""

from typing import Optional
import math


class PowerCalculator:
    _instance: Optional["PowerCalculator"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def power(self, base: float, exp: float) -> float:
        return base ** exp

    def sqrt(self, n: float) -> Optional[float]:
        if n < 0:
            return None
        return math.sqrt(n)

    def cbrt(self, n: float) -> float:
        return n ** (1 / 3)

    def is_power_of(self, n: int, base: int) -> bool:
        if base <= 1:
            return False
        if n <= 0:
            return False
        current = 1
        while current < n:
            current *= base
        return current == n


def get_power_calculator() -> PowerCalculator:
    return PowerCalculator()
