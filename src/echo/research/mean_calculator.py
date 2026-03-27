"""平均值计算器"""

from typing import Any, List, Optional
import statistics


class MeanCalculator:
    _instance: Optional["MeanCalculator"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def mean(self, items: List[float]) -> Optional[float]:
        if not items:
            return None
        try:
            return statistics.mean(items)
        except statistics.StatisticsError:
            return None

    def harmonic_mean(self, items: List[float]) -> Optional[float]:
        if not items:
            return None
        try:
            return statistics.harmonic_mean(items)
        except (statistics.StatisticsError, ValueError):
            return None

    def geometric_mean(self, items: List[float]) -> Optional[float]:
        if not items:
            return None
        try:
            return statistics.geometric_mean(items)
        except (statistics.StatisticsError, ValueError):
            return None


def get_mean_calculator() -> MeanCalculator:
    return MeanCalculator()
