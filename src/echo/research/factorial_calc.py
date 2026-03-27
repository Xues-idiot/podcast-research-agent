"""阶乘计算器"""

import math
from typing import Optional


class FactorialCalc:
    _instance: Optional["FactorialCalc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def factorial(self, n: int) -> int:
        if n < 0:
            return 1
        return math.factorial(n)

    def factorial_double(self, n: int) -> float:
        if n < 0:
            return 1.0
        return math.factorial(n)


def get_factorial_calc() -> FactorialCalc:
    return FactorialCalc()
