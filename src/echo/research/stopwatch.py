"""秒表工具"""

import time
from typing import Optional


class Stopwatch:
    """秒表工具"""

    def __init__(self):
        self._start_time = None
        self._lap_times = []

    def start(self):
        """开始"""
        self._start_time = time.time()
        self._lap_times = []

    def lap(self) -> float:
        """计圈"""
        if self._start_time is None:
            return 0
        lap_time = round(time.time() - self._start_time, 3)
        self._lap_times.append(lap_time)
        return lap_time

    def total(self) -> float:
        """总时间"""
        if self._start_time is None:
            return 0
        return round(time.time() - self._start_time, 3)

    def reset(self):
        """重置"""
        self._start_time = None
        self._lap_times = []


_stopwatch: Optional[Stopwatch] = None


def get_stopwatch() -> Stopwatch:
    global _stopwatch
    if _stopwatch is None:
        _stopwatch = Stopwatch()
    return _stopwatch