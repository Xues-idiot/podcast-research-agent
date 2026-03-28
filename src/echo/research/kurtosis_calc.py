"""峰度计算器"""

import math
from typing import List, Optional


class KurtosisCalc:
    _instance: Optional["KurtosisCalc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def kurtosis(self, values: List[float]) -> float:
        if len(values) < 4:
            return 0.0
        n = len(values)
        mean = sum(values) / n
        std = math.sqrt(sum((x - mean) ** 2 for x in values) / n)
        if std == 0:
            return 0.0
        return sum(((x - mean) / std) ** 4 for x in values) * n * (n + 1) / ((n - 1) * (n - 2) * (n - 3)) - 3 * (n - 1) ** 2 / ((n - 2) * (n - 3))


def get_kurtosis_calc() -> KurtosisCalc:
    return KurtosisCalc()
