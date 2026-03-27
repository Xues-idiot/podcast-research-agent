"""节流调用工具"""

import time
from typing import Optional, Callable


class ThrottleTool:
    """节流调用工具"""

    def __init__(self, interval: float = 1.0):
        self._interval = interval
        self._last_call = 0

    def throttle(self, func: Callable) -> Callable:
        """节流装饰"""
        def wrapper(*args, **kwargs):
            now = time.time()
            if now - self._last_call >= self._interval:
                self._last_call = now
                return func(*args, **kwargs)
        return wrapper


_tool: Optional[ThrottleTool] = None


def get_throttle_tool(interval: float = 1.0) -> ThrottleTool:
    global _tool
    if _tool is None:
        _tool = ThrottleTool(interval)
    return _tool