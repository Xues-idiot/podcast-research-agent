"""记忆化函数工具"""

from typing import Callable, Dict, Optional, Any


class MemoFunc:
    _instance: Optional["MemoFunc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def memoize(self, func: Callable) -> Callable:
        cache: Dict = {}

        def memoized(*args, **kwargs):
            key = str(args) + str(kwargs)
            if key not in cache:
                cache[key] = func(*args, **kwargs)
            return cache[key]
        return memoized


def get_memo_func() -> MemoFunc:
    return MemoFunc()
