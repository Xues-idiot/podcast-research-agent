"""计时器工具"""

import time
from typing import Optional


class Timer:
    """计时器工具"""

    def __init__(self):
        self._start_time = None
        self._end_time = None

    def start(self):
        """开始计时"""
        self._start_time = time.time()

    def stop(self) -> float:
        """停止计时"""
        self._end_time = time.time()
        return self.elapsed()

    def elapsed(self) -> float:
        """获取已过时间(秒)"""
        if self._start_time is None:
            return 0
        end = self._end_time if self._end_time else time.time()
        return round(end - self._start_time, 3)


_timer: Optional[Timer] = None


def get_timer() -> Timer:
    global _timer
    if _timer is None:
        _timer = Timer()
    return _timer