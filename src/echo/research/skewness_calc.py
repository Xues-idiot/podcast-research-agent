"""偏度计算器"""

import math
from typing import List, Optional


class SkewnessCalc:
    _instance: Optional["SkewnessCalc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def skewness(self, values: List[float]) -> float:
        if len(values) < 3:
            return 0.0
        n = len(values)
        mean = sum(values) / n
        std = math.sqrt(sum((x - mean) ** 2 for x in values) / n)
        if std == 0:
            return 0.0
        return sum(((x - mean) / std) ** 3 for x in values) * n / ((n - 1) * (n - 2))


def get_skewness_calc() -> SkewnessCalc:
    return SkewnessCalc()
