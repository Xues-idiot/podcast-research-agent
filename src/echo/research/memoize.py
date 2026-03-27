"""记忆化工具"""

from typing import Callable, Dict, Any, Optional


class Memoize:
    _instance: Optional["Memoize"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_cache"):
            self._cache: Dict[str, Any] = {}

    def memoize(self, func: Callable) -> Callable:
        def memoized(*args, **kwargs):
            key = str(args) + str(kwargs)
            if key not in self._cache:
                self._cache[key] = func(*args, **kwargs)
            return self._cache[key]
        return memoized


def get_memoize() -> Memoize:
    return Memoize()
