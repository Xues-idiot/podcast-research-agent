"""变异系数计算器"""

import math
from typing import List, Optional


class CoefficientOfVariation:
    _instance: Optional["CoefficientOfVariation"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def cv(self, values: List[float]) -> float:
        if not values:
            return 0.0
        mean = sum(values) / len(values)
        if mean == 0:
            return 0.0
        std = math.sqrt(sum((x - mean) ** 2 for x in values) / len(values))
        return std / mean


def get_coefficient_of_variation() -> CoefficientOfVariation:
    return CoefficientOfVariation()
