"""翻转函数工具"""

from typing import Callable, Any


class FlipFunc:
    _instance: Optional["FlipFunc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def flip(self, func: Callable) -> Callable:
        def flipped(*args, **kwargs):
            return func(*reversed(args), **kwargs)
        return flipped


def get_flip_func() -> FlipFunc:
    return FlipFunc()
