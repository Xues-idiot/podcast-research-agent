"""中值滤波器"""

from typing import List
import statistics


class MedianFilter:
    _instance: Optional["MedianFilter"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def filter(self, data: List[float], window: int = 3) -> List[float]:
        if len(data) == 0:
            return []
        result = []
        half = window // 2
        for i in range(len(data)):
            start = max(0, i - half)
            end = min(len(data), i + half + 1)
            result.append(statistics.median(data[start:end]))
        return result


def get_median_filter() -> MedianFilter:
    return MedianFilter()
