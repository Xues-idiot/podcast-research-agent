"""滑动窗口速率限制"""

import time
from typing import List


class SlidingWindowRateLimiter:
    _instance: Optional["SlidingWindowRateLimiter"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_timestamps"):
            self._timestamps: List[float] = []
            self._limit: int = 10
            self._window: float = 60.0

    def allow(self) -> bool:
        now = time.time()
        self._timestamps = [t for t in self._timestamps if now - t < self._window]
        if len(self._timestamps) < self._limit:
            self._timestamps.append(now)
            return True
        return False


def get_sliding_window_rate_limiter() -> SlidingWindowRateLimiter:
    return SlidingWindowRateLimiter()
