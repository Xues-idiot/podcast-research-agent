"""方差计算器"""

from typing import Any, List, Optional
import statistics


class VarianceCalculator:
    _instance: Optional["VarianceCalculator"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def variance(self, items: List[float]) -> Optional[float]:
        if len(items) < 2:
            return None
        try:
            return statistics.variance(items)
        except statistics.StatisticsError:
            return None

    def pvariance(self, items: List[float]) -> Optional[float]:
        if not items:
            return None
        try:
            return statistics.pvariance(items)
        except statistics.StatisticsError:
            return None


def get_variance_calculator() -> VarianceCalculator:
    return VarianceCalculator()
