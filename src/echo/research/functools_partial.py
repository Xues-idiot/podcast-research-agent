"""偏函数工具"""

from functools import partial
from typing import Callable, Any


class FunctoolsPartial:
    _instance: Optional["FunctoolsPartial"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def make_partial(self, func: Callable, *args: Any, **kwargs: Any) -> Callable:
        return partial(func, *args, **kwargs)


def get_functools_partial() -> FunctoolsPartial:
    return FunctoolsPartial()
