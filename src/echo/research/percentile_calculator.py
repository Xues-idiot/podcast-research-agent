"""百分位数计算器"""

from typing import Any, List, Optional
import statistics


class PercentileCalculator:
    _instance: Optional["PercentileCalculator"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def percentile(self, items: List[float], p: float) -> Optional[float]:
        if not items:
            return None
        if p < 0 or p > 100:
            return None
        try:
            return statistics.quantiles(items, n=100)[int(p) - 1]
        except (IndexError, statistics.StatisticsError):
            return None

    def quantile(self, items: List[float], n: int) -> Optional[List[float]]:
        if not items:
            return None
        if n < 2:
            return None
        try:
            return list(statistics.quantiles(items, n=n))
        except statistics.StatisticsError:
            return None


def get_percentile_calculator() -> PercentileCalculator:
    return PercentileCalculator()
