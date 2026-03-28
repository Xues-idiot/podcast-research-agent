"""防抖调用工具"""

import time
from typing import Callable, Any, Optional


class DebounceCallTool:
    _instance: Optional["DebounceCallTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def debounce(self, func: Callable, delay: float) -> Callable:
        timer = [None]

        def debounced(*args, **kwargs):
            if timer[0]:
                timer[0].cancel()
            timer[0] = time.after(delay, lambda: func(*args, **kwargs))
        return debounced


def get_debounce_call_tool() -> DebounceCallTool:
    return DebounceCallTool()