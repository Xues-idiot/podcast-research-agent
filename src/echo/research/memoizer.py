"""记忆化工具"""

from typing import Optional, Callable, Dict


class Memoizer:
    """记忆化工具"""

    def __init__(self):
        self._cache: Dict = {}

    def memoize(self, func: Callable) -> Callable:
        """记忆化"""
        def wrapper(*args, **kwargs):
            key = str(args) + str(kwargs)
            if key not in self._cache:
                self._cache[key] = func(*args, **kwargs)
            return self._cache[key]
        return wrapper

    def clear(self):
        """清空缓存"""
        self._cache.clear()


_memoizer: Optional[Memoizer] = None


def get_memoizer() -> Memoizer:
    global _memoizer
    if _memoizer is None:
        _memoizer = Memoizer()
    return _memoizer