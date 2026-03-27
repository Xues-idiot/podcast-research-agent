"""方差计算器"""

from typing import List, Optional


class VarianceCalc:
    _instance: Optional["VarianceCalc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def variance(self, values: List[float]) -> float:
        if len(values) < 2:
            return 0.0
        mean = sum(values) / len(values)
        return sum((v - mean) ** 2 for v in values) / (len(values) - 1)


def get_variance_calc() -> VarianceCalc:
    return VarianceCalc()
