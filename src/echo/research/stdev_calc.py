"""标准差计算器"""

import math
from typing import List, Optional


class StdevCalc:
    _instance: Optional["StdevCalc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def stdev(self, values: List[float]) -> float:
        if len(values) < 2:
            return 0.0
        mean = sum(values) / len(values)
        variance = sum((v - mean) ** 2 for v in values) / (len(values) - 1)
        return math.sqrt(variance)


def get_stdev_calc() -> StdevCalc:
    return StdevCalc()
