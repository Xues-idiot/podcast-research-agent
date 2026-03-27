"""点计算器"""

import math
from typing import List, Optional, Tuple


class PointCalc:
    _instance: Optional["PointCalc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def midpoint(self, p1: Tuple[float, float], p2: Tuple[float, float]) -> Tuple[float, float]:
        return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

    def centroid(self, points: List[Tuple[float, float]]) -> Tuple[float, float]:
        if not points:
            return (0.0, 0.0)
        n = len(points)
        return (sum(p[0] for p in points) / n, sum(p[1] for p in points) / n)


def get_point_calc() -> PointCalc:
    return PointCalc()
