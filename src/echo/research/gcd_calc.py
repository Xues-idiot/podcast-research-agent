"""GCD计算器"""

import math
from typing import Optional


class GcdCalc:
    _instance: Optional["GcdCalc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def gcd(self, a: int, b: int) -> int:
        return math.gcd(a, b)

    def lcm(self, a: int, b: int) -> int:
        return abs(a * b) // math.gcd(a, b) if a and b else 0


def get_gcd_calc() -> GcdCalc:
    return GcdCalc()
