"""惰性计算工具"""

from typing import Any, Callable, Optional


class LazyTool:
    _instance: Optional["LazyTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def lazy(self, func: Callable) -> Callable:
        result = None
        computed = False
        def wrapper(*args, **kwargs):
            nonlocal result, computed
            if not computed:
                result = func(*args, **kwargs)
                computed = True
            return result
        return wrapper

    def memoize(self, func: Callable) -> Callable:
        cache = {}
        def wrapper(*args, **kwargs):
            key = str(args) + str(kwargs)
            if key not in cache:
                cache[key] = func(*args, **kwargs)
            return cache[key]
        return wrapper


def get_lazy_tool() -> LazyTool:
    return LazyTool()
