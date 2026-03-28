"""加权平均计算器"""

from typing import List, Optional


class WeightedAverageCalc:
    _instance: Optional["WeightedAverageCalc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def weighted_avg(self, values: List[float], weights: List[float]) -> float:
        if not values or not weights or len(values) != len(weights):
            return 0.0
        total_weight = sum(weights)
        if total_weight == 0:
            return 0.0
        return sum(v * w for v, w in zip(values, weights)) / total_weight


def get_weighted_average_calc() -> WeightedAverageCalc:
    return WeightedAverageCalc()
