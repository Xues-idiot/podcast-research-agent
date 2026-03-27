"""加权平均计算器"""

from typing import List, Optional


class WeightedMean:
    _instance: Optional["WeightedMean"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def weighted_mean(self, values: List[float], weights: List[float]) -> Optional[float]:
        if len(values) != len(weights) or len(values) == 0:
            return None
        total_weight = sum(weights)
        if total_weight == 0:
            return None
        return sum(v * w for v, w in zip(values, weights)) / total_weight


def get_weighted_mean() -> WeightedMean:
    return WeightedMean()
