"""移动平均滤波器"""

from typing import List, Optional


class MovingAverageFilter:
    _instance: Optional["MovingAverageFilter"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def filter(self, data: List[float], window: int = 3) -> List[float]:
        if len(data) < window:
            return data
        result = []
        for i in range(len(data) - window + 1):
            result.append(sum(data[i:i+window]) / window)
        return result


def get_moving_average_filter() -> MovingAverageFilter:
    return MovingAverageFilter()
