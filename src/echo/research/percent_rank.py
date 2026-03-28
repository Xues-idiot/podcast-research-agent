"""百分比排名工具"""

from typing import List, Optional
import sortedcontainers


class PercentRankTool:
    _instance: Optional["PercentRankTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def percentile(self, values: List[float], p: float) -> float:
        """计算第p百分位数"""
        if not values:
            return 0.0
        sorted_vals = sorted(values)
        k = (len(sorted_vals) - 1) * p / 100
        f = int(k)
        c = f + 1 if f < len(sorted_vals) - 1 else f
        return sorted_vals[f] + (k - f) * (sorted_vals[c] - sorted_vals[f])

    def percentile_rank(self, values: List[float], v: float) -> float:
        """计算值的百分比排名"""
        if not values:
            return 0.0
        count_below = sum(1 for x in values if x < v)
        count_equal = sum(1 for x in values if x == v)
        return (count_below + 0.5 * count_equal) / len(values) * 100

    def quartiles(self, values: List[float]) -> tuple:
        """计算四分位数"""
        return (
            self.percentile(values, 25),
            self.percentile(values, 50),
            self.percentile(values, 75)
        )

    def iqr(self, values: List[float]) -> float:
        """计算四分位距"""
        q1, q3 = self.percentile(values, 25), self.percentile(values, 75)
        return q3 - q1


def get_percent_rank_tool() -> PercentRankTool:
    return PercentRankTool()