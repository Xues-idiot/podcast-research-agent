"""距离计算工具"""

import math
from typing import Optional


class DistanceCalculator:
    """距离计算工具"""

    def euclidean(self, x1: float, y1: float, x2: float, y2: float) -> float:
        """欧几里得距离"""
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def manhattan(self, x1: float, y1: float, x2: float, y2: float) -> float:
        """曼哈顿距离"""
        return abs(x2 - x1) + abs(y2 - y1)

    def haversine(self, lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """haversine公式计算球面距离(公里)"""
        R = 6371
        phi1, phi2 = math.radians(lat1), math.radians(lat2)
        dphi = math.radians(lat2 - lat1)
        dlambda = math.radians(lon2 - lon1)

        a = math.sin(dphi/2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        return R * c


_calculator: Optional[DistanceCalculator] = None


def get_distance_calculator() -> DistanceCalculator:
    global _calculator
    if _calculator is None:
        _calculator = DistanceCalculator()
    return _calculator