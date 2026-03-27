"""中位数计算器"""

from typing import List, Optional


class MedianCalc:
    _instance: Optional["MedianCalc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def median(self, values: List[float]) -> float:
        if not values:
            return 0.0
        sorted_vals = sorted(values)
        n = len(sorted_vals)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2
        return sorted_vals[mid]


def get_median_calc() -> MedianCalc:
    return MedianCalc()
