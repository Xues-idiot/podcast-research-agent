"""截断平均计算器"""

from typing import List, Optional


class TruncatedMeanCalc:
    _instance: Optional["TruncatedMeanCalc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def truncated_mean(self, values: List[float], proportion: float = 0.1) -> float:
        if not values:
            return 0.0
        sorted_vals = sorted(values)
        n = len(sorted_vals)
        k = int(n * proportion)
        if k >= n / 2:
            return sum(sorted_vals) / n
        return sum(sorted_vals[k:n - k]) / (n - 2 * k)


def get_truncated_mean_calc() -> TruncatedMeanCalc:
    return TruncatedMeanCalc()
