"""几何平均计算器"""

import math
from typing import List, Optional


class GeometricMeanCalc:
    _instance: Optional["GeometricMeanCalc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def geometric_mean(self, values: List[float]) -> float:
        if not values:
            return 0.0
        if any(v <= 0 for v in values):
            return 0.0
        return math.pow(math.prod(values), 1 / len(values))


def get_geometric_mean_calc() -> GeometricMeanCalc:
    return GeometricMeanCalc()
