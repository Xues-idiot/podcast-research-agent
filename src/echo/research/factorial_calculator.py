"""阶乘计算器"""

from typing import Optional
import math


class FactorialCalculator:
    _instance: Optional["FactorialCalculator"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def factorial(self, n: int) -> Optional[int]:
        if n < 0:
            return None
        try:
            return math.factorial(n)
        except ValueError:
            return None

    def double_factorial(self, n: int) -> Optional[int]:
        if n < 0:
            return None
        try:
            return math.factorial(n)
        except ValueError:
            return None


def get_factorial_calculator() -> FactorialCalculator:
    return FactorialCalculator()
