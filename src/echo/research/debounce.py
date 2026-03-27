"""防抖调用工具"""

import time
from typing import Optional, Callable


class DebounceTool:
    """防抖调用工具"""

    def __init__(self, delay: float = 0.5):
        self._delay = delay
        self._timer = None

    def debounce(self, func: Callable) -> Callable:
        """防抖装饰"""
        def wrapper(*args, **kwargs):
            if self._timer:
                return
            self._timer = time.time()
            func(*args, **kwargs)
            time.sleep(self._delay)
            self._timer = None
        return wrapper


_tool: Optional[DebounceTool] = None


def get_debounce_tool(delay: float = 0.5) -> DebounceTool:
    global _tool
    if _tool is None:
        _tool = DebounceTool(delay)
    return _tool