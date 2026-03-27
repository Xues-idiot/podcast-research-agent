"""防抖工具"""

import time
from typing import Callable, Optional


class Debouncer:
    """函数防抖"""

    def __init__(self, wait_seconds: float = 0.5):
        self._wait = wait_seconds
        self._last_call = 0

    def debounce(self, func: Callable) -> Callable:
        """装饰器防抖"""
        def wrapped(*args, **kwargs):
            now = time.time()
            if now - self._last_call >= self._wait:
                self._last_call = now
                return func(*args, **kwargs)
            return None
        return wrapped


_debouncer: Optional[Debouncer] = None


def get_debouncer() -> Debouncer:
    global _debouncer
    if _debouncer is None:
        _debouncer = Debouncer()
    return _debouncer