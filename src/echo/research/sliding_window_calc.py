"""滑动窗口计算器"""

from typing import Callable, List, Optional


class SlidingWindowCalc:
    _instance: Optional["SlidingWindowCalc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def sliding_window(self, data: List[float], window_size: int) -> List[float]:
        if window_size > len(data):
            return []
        return [sum(data[i:i + window_size]) / window_size for i in range(len(data) - window_size + 1)]

    def moving_average(self, data: List[float], window_size: int) -> List[float]:
        return self.sliding_window(data, window_size)


def get_sliding_window_calc() -> SlidingWindowCalc:
    return SlidingWindowCalc()
