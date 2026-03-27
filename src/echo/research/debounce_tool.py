"""防抖工具"""

import time
from typing import Callable, Optional, Any


class DebounceTool:
    _instance: Optional["DebounceTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def debounce(self, func: Callable, delay: float) -> Callable:
        last_call = [0]

        def debounced(*args, **kwargs):
            now = time.time()
            if now - last_call[0] >= delay:
                last_call[0] = now
                return func(*args, **kwargs)
        return debounced


def get_debounce_tool() -> DebounceTool:
    return DebounceTool()
