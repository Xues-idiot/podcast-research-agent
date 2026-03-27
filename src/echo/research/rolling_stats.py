"""滚动统计工具"""

import statistics
from typing import List


class RollingStats:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def rolling_mean(self, data: List[float], window: int) -> List[float]:
        if window <= 0 or window > len(data):
            return []
        return [statistics.mean(data[i:i+window]) for i in range(len(data) - window + 1)]

    def rolling_std(self, data: List[float], window: int) -> List[float]:
        if window <= 0 or window > len(data):
            return []
        return [statistics.stdev(data[i:i+window]) for i in range(len(data) - window + 1)]


def get_rolling_stats() -> RollingStats:
    return RollingStats()
