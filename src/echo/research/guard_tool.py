"""守卫工具"""

from typing import Callable, Optional, Any


class GuardTool:
    _instance: Optional["GuardTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def guard(self, func: Callable, default: Any = None) -> Callable:
        def guarded(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception:
                return default
        return guarded


def get_guard_tool() -> GuardTool:
    return GuardTool()
