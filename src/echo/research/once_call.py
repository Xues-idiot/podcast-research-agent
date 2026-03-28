"""单次调用工具"""

from typing import Callable, Any, Optional


class OnceCallTool:
    _instance: Optional["OnceCallTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def once(self, func: Callable) -> Callable:
        called = [False]
        result = [None]

        def wrapper(*args, **kwargs):
            if not called[0]:
                called[0] = True
                result[0] = func(*args, **kwargs)
            return result[0]
        return wrapper


def get_once_call_tool() -> OnceCallTool:
    return OnceCallTool()