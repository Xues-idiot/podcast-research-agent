"""时间序列工具"""

from typing import Any, List, Optional, Tuple
from datetime import datetime


class TimeSeries:
    _instance: Optional["TimeSeries"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def create_point(self, timestamp: int, value: float) -> Tuple[int, float]:
        return (timestamp, value)

    def create_series(self, points: List[Tuple[int, float]]) -> List[Tuple[int, float]]:
        return sorted(points, key=lambda x: x[0])

    def resample(self, series: List[Tuple[int, float]], interval: int) -> List[Tuple[int, float]]:
        if not series:
            return []
        result = []
        start = series[0][0]
        end = series[-1][0]
        current = start
        while current <= end:
            result.append((current, None))
            current += interval
        return result


def get_time_series() -> TimeSeries:
    return TimeSeries()
