"""组合函数工具"""

from typing import Callable, Any, Optional


class ComposeFunc:
    _instance: Optional["ComposeFunc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def compose(self, *funcs: Callable) -> Callable:
        def composed(x):
            result = x
            for func in reversed(funcs):
                result = func(result)
            return result
        return composed


def get_compose_func() -> ComposeFunc:
    return ComposeFunc()
