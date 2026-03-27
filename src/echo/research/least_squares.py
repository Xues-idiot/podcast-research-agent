"""最小二乘法工具"""

import math
from typing import List, Optional, Tuple


class LeastSquares:
    _instance: Optional["LeastSquares"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def fit(self, x: List[float], y: List[float]) -> Optional[Tuple[float, float]]:
        if len(x) != len(y) or len(x) < 2:
            return None
        n = len(x)
        sum_x = sum(x)
        sum_y = sum(y)
        sum_xy = sum(xi * yi for xi, yi in zip(x, y))
        sum_x2 = sum(xi ** 2 for xi in x)
        denominator = n * sum_x2 - sum_x ** 2
        if denominator == 0:
            return None
        slope = (n * sum_xy - sum_x * sum_y) / denominator
        intercept = (sum_y - slope * sum_x) / n
        return (slope, intercept)


def get_least_squares() -> LeastSquares:
    return LeastSquares()
