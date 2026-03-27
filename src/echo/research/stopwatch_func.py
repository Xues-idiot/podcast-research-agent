"""秒表工具"""

import time
from typing import Optional, List


class StopwatchFunc:
    _instance: Optional["StopwatchFunc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._start_time: Optional[float] = None
        self._laps: List[float] = []

    def start(self) -> None:
        self._start_time = time.time()
        self._laps = []

    def lap(self) -> float:
        if self._start_time is None:
            return 0
        lap_time = time.time() - self._start_time
        self._laps.append(lap_time)
        return lap_time

    def stop(self) -> float:
        if self._start_time is None:
            return 0
        return time.time() - self._start_time


def get_stopwatch_func() -> StopwatchFunc:
    return StopwatchFunc()
