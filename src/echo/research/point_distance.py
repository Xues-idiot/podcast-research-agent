"""点距离计算器"""

import math
from typing import Optional, Tuple


class PointDistance:
    _instance: Optional["PointDistance"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def euclidean(self, x1: float, y1: float, x2: float, y2: float) -> float:
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def manhattan(self, x1: float, y1: float, x2: float, y2: float) -> float:
        return abs(x2 - x1) + abs(y2 - y1)

    def chebyshev(self, x1: float, y1: float, x2: float, y2: float) -> float:
        return max(abs(x2 - x1), abs(y2 - y1))


def get_point_distance() -> PointDistance:
    return PointDistance()
