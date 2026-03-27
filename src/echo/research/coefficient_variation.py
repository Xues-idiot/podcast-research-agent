"""变异系数计算器"""

import statistics
from typing import List, Optional


class CoefficientVariation:
    _instance: Optional["CoefficientVariation"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def cv(self, data: List[float]) -> Optional[float]:
        if len(data) < 2:
            return None
        mean = statistics.mean(data)
        if mean == 0:
            return None
        stdev = statistics.stdev(data)
        return stdev / mean


def get_coefficient_variation() -> CoefficientVariation:
    return CoefficientVariation()
