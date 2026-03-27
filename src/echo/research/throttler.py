"""节流工具"""

import time
from typing import Optional


class Throttler:
    """函数节流"""

    def __init__(self, interval_seconds: float = 1.0):
        self._interval = interval_seconds
        self._last_call = 0

    def should_proceed(self) -> bool:
        """是否应该继续"""
        now = time.time()
        if now - self._last_call >= self._interval:
            self._last_call = now
            return True
        return False


_throttler: Optional[Throttler] = None


def get_throttler() -> Throttler:
    global _throttler
    if _throttler is None:
        _throttler = Throttler()
    return _throttler