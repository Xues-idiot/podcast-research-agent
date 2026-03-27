"""秒表工具"""

import time
from typing import Optional


class StopwatchTool:
    """秒表工具"""

    def __init__(self):
        self._start = None
        self._laps = []

    def start(self):
        """开始"""
        self._start = time.time()
        self._laps = []

    def lap(self) -> float:
        """计圈"""
        if self._start is None:
            return 0
        lap_time = time.time() - self._start
        self._laps.append(lap_time)
        return lap_time

    def total(self) -> float:
        """总时间"""
        if self._start is None:
            return 0
        return time.time() - self._start


_tool: Optional[StopwatchTool] = None


def get_stopwatch_tool() -> StopwatchTool:
    global _tool
    if _tool is None:
        _tool = StopwatchTool()
    return _tool