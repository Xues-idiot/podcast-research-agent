"""协方差计算器"""

from typing import Any, List, Optional
import statistics


class CovarianceCalculator:
    _instance: Optional["CovarianceCalculator"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def covariance(self, x: List[float], y: List[float]) -> Optional[float]:
        if len(x) != len(y) or len(x) < 2:
            return None
        try:
            return statistics.covariance(x, y)
        except statistics.StatisticsError:
            return None

    def correlation(self, x: List[float], y: List[float]) -> Optional[float]:
        if len(x) != len(y) or len(x) < 2:
            return None
        try:
            return statistics.correlation(x, y)
        except statistics.StatisticsError:
            return None


def get_covariance_calculator() -> CovarianceCalculator:
    return CovarianceCalculator()
