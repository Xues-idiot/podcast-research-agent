"""缓存装饰器工具"""

import functools
from typing import Optional, Callable, Any


class CacheDecoratorTool:
    """缓存装饰器工具"""

    def memoize(self, func: Callable) -> Callable:
        """记忆化缓存"""
        @functools.lru_cache(maxsize=None)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper

    def cache_result(self, func: Callable) -> Callable:
        """缓存结果"""
        cache = {}

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = str(args) + str(kwargs)
            if key not in cache:
                cache[key] = func(*args, **kwargs)
            return cache[key]
        return wrapper


_cache_decorator_tool: Optional[CacheDecoratorTool] = None


def get_cache_decorator_tool() -> CacheDecoratorTool:
    global _cache_decorator_tool
    if _cache_decorator_tool is None:
        _cache_decorator_tool = CacheDecoratorTool()
    return _cache_decorator_tool