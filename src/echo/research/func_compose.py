"""函数组合工具"""

from typing import Callable, Optional


class FuncCompose:
    _instance: Optional["FuncCompose"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def compose(self, *funcs: Callable) -> Callable:
        def composed(x):
            for func in reversed(funcs):
                x = func(x)
            return x
        return composed


def get_func_compose() -> FuncCompose:
    return FuncCompose()
