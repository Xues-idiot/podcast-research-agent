"""函数偏应用工具"""

from functools import partial
from typing import Callable, Optional, Any


class FuncPartial:
    _instance: Optional["FuncPartial"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def apply(self, func: Callable, *args, **kwargs) -> Callable:
        return partial(func, *args, **kwargs)


def get_func_partial() -> FuncPartial:
    return FuncPartial()
