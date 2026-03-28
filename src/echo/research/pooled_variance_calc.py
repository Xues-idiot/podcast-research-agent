"""池化方差计算器"""

from typing import List, Optional


class PooledVarianceCalc:
    _instance: Optional["PooledVarianceCalc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def pooled_variance(self, *samples: List[float]) -> float:
        all_values = []
        for sample in samples:
            all_values.extend(sample)
        if not all_values:
            return 0.0
        n = len(all_values)
        mean = sum(all_values) / n
        return sum((x - mean) ** 2 for x in all_values) / n


def get_pooled_variance_calc() -> PooledVarianceCalc:
    return PooledVarianceCalc()
