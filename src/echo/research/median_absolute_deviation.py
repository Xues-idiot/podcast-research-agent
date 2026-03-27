"""中位数绝对偏差计算器"""

import statistics
from typing import List, Optional


class MedianAbsoluteDeviation:
    _instance: Optional["MedianAbsoluteDeviation"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def mad(self, data: List[float]) -> Optional[float]:
        if len(data) < 2:
            return None
        median = statistics.median(data)
        deviations = [abs(x - median) for x in data]
        return statistics.median(deviations)


def get_median_absolute_deviation() -> MedianAbsoluteDeviation:
    return MedianAbsoluteDeviation()
