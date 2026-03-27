"""秒表工具"""

import time
from typing import Optional


class TimerTool:
    """秒表工具"""

    def __init__(self):
        self._start = None

    def start(self) -> None:
        """开始计时"""
        self._start = time.time()

    def stop(self) -> float:
        """停止计时"""
        if self._start is None:
            return 0
        elapsed = time.time() - self._start
        self._start = None
        return elapsed

    def elapsed(self) -> float:
        """已过时间"""
        if self._start is None:
            return 0
        return time.time() - self._start


_timer_tool: Optional[TimerTool] = None


def get_timer_tool() -> TimerTool:
    global _timer_tool
    if _timer_tool is None:
        _timer_tool = TimerTool()
    return _timer_tool