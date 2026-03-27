"""分位数检测器"""

import statistics
from typing import List, Optional


class QuantileDetector:
    _instance: Optional["QuantileDetector"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def quartiles(self, data: List[float]) -> Optional[List[float]]:
        if len(data) < 4:
            return None
        try:
            return list(statistics.quantiles(data, n=4))
        except statistics.StatisticsError:
            return None

    def deciles(self, data: List[float]) -> Optional[List[float]]:
        if len(data) < 10:
            return None
        try:
            return list(statistics.quantiles(data, n=10))
        except statistics.StatisticsError:
            return None


def get_quantile_detector() -> QuantileDetector:
    return QuantileDetector()
