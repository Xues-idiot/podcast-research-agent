"""计时器工具"""

import time
from typing import Optional


class TimerFunc:
    _instance: Optional["TimerFunc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def start(self) -> float:
        return time.time()

    def elapsed(self, start: float) -> float:
        return time.time() - start


def get_timer_func() -> TimerFunc:
    return TimerFunc()
