"""函数守卫"""

from typing import Callable, Any, Optional


class FunctionGuard:
    _instance: Optional["FunctionGuard"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def guard(self, func: Callable, pre: Callable = None, post: Callable = None) -> Callable:
        def guarded(*args, **kwargs):
            if pre and not pre(*args, **kwargs):
                return None
            result = func(*args, **kwargs)
            if post:
                post(result)
            return result
        return guarded


def get_function_guard() -> FunctionGuard:
    return FunctionGuard()
