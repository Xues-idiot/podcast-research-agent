"""节流调用工具"""

import time
from typing import Callable, Any, Optional


class ThrottleCallTool:
    _instance: Optional["ThrottleCallTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def throttle(self, func: Callable, interval: float) -> Callable:
        last_called = [0.0]

        def throttled(*args, **kwargs):
            now = time.time()
            if now - last_called[0] >= interval:
                last_called[0] = now
                return func(*args, **kwargs)
            return None
        return throttled


def get_throttle_call_tool() -> ThrottleCallTool:
    return ThrottleCallTool()