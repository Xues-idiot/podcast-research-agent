"""平均值计算器"""

from typing import List, Optional


class MeanCalc:
    _instance: Optional["MeanCalc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def mean(self, values: List[float]) -> float:
        return sum(values) / len(values) if values else 0.0

    def weighted_mean(self, values: List[float], weights: List[float]) -> float:
        if len(values) != len(weights) or not values:
            return 0.0
        return sum(v * w for v, w in zip(values, weights)) / sum(weights)


def get_mean_calc() -> MeanCalc:
    return MeanCalc()
