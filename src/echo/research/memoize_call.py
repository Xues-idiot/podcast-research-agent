"""记忆化工具"""

from functools import lru_cache
from typing import Callable, Any, Optional


class MemoizeCallTool:
    _instance: Optional["MemoizeCallTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def memoize(self, func: Callable) -> Callable:
        return lru_cache(maxsize=None)(func)


def get_memoize_call_tool() -> MemoizeCallTool:
    return MemoizeCallTool()