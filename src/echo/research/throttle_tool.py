"""节流工具"""

import time
from typing import Optional, Callable


class ThrottleTool:
    """节流工具"""

    def __init__(self, interval: float):
        self._interval = interval
        self._last_call = 0

    def throttle(self, func: Callable) -> Callable:
        """节流装饰器"""
        def wrapper(*args, **kwargs):
            now = time.time()
            if now - self._last_call >= self._interval:
                self._last_call = now
                return func(*args, **kwargs)
        return wrapper


_throttle_tool: Optional[ThrottleTool] = None


def get_throttle_tool(interval: float = 1.0) -> ThrottleTool:
    global _throttle_tool
    if _throttle_tool is None:
        _throttle_tool = ThrottleTool(interval)
    return _throttle_tool