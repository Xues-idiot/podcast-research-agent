"""幂计算器"""

import math
from typing import Optional


class PowerCalc:
    _instance: Optional["PowerCalc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def power(self, base: float, exp: float) -> float:
        return math.pow(base, exp)

    def square_root(self, n: float) -> float:
        return math.sqrt(n)

    def cube_root(self, n: float) -> float:
        return n ** (1/3)


def get_power_calc() -> PowerCalc:
    return PowerCalc()
