"""偏函数工具"""

from functools import partial
from typing import Callable, Any, Optional


class PartialFuncTool:
    _instance: Optional["PartialFuncTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def create_partial(self, func: Callable, *args, **kwargs) -> Callable:
        return partial(func, *args, **kwargs)


def get_partial_func_tool() -> PartialFuncTool:
    return PartialFuncTool()