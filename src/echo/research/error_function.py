"""误差函数计算器"""

import math
from typing import Optional


class ErrorFunction:
    _instance: Optional["ErrorFunction"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def erf(self, x: float) -> float:
        try:
            return math.erf(x)
        except ValueError:
            return 0.0

    def erfc(self, x: float) -> float:
        try:
            return math.erfc(x)
        except ValueError:
            return 1.0


def get_error_function() -> ErrorFunction:
    return ErrorFunction()
