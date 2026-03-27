"""对数计算器"""

import math
from typing import Optional


class LogarithmCalc:
    _instance: Optional["LogarithmCalc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def log(self, n: float, base: float = math.e) -> float:
        if n <= 0:
            return 0.0
        return math.log(n, base)

    def log10(self, n: float) -> float:
        if n <= 0:
            return 0.0
        return math.log10(n)

    def log2(self, n: float) -> float:
        if n <= 0:
            return 0.0
        return math.log2(n)


def get_logarithm_calc() -> LogarithmCalc:
    return LogarithmCalc()
