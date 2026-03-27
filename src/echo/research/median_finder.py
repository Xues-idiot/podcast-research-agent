"""中位数查找器"""

from typing import Any, List, Optional
import statistics


class MedianFinder:
    _instance: Optional["MedianFinder"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def median(self, items: List[float]) -> Optional[float]:
        if not items:
            return None
        return statistics.median(items)

    def median_low(self, items: List[float]) -> Optional[float]:
        if not items:
            return None
        return statistics.median_low(items)

    def median_high(self, items: List[float]) -> Optional[float]:
        if not items:
            return None
        return statistics.median_high(items)


def get_median_finder() -> MedianFinder:
    return MedianFinder()
