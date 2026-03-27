"""缓存装饰器"""

import time
from typing import Optional, Callable


class CacheDecorator:
    """缓存装饰器"""

    def __init__(self):
        self._cache = {}

    def cached(self, ttl: int = 60):
        """缓存装饰器"""
        def decorator(func: Callable):
            def wrapper(*args, **kwargs):
                key = str(args) + str(kwargs)
                if key in self._cache:
                    cached_time, result = self._cache[key]
                    if time.time() - cached_time < ttl:
                        return result
                result = func(*args, **kwargs)
                self._cache[key] = (time.time(), result)
                return result
            return wrapper
        return decorator


_decorator: Optional[CacheDecorator] = None


def get_cache_decorator() -> CacheDecorator:
    global _decorator
    if _decorator is None:
        _decorator = CacheDecorator()
    return _decorator