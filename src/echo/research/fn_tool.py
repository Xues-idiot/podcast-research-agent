"""函数工具"""

from typing import Any, Callable, Optional


class FnTool:
    _instance: Optional["FnTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def apply(self, func: Callable, args: tuple = (), kwargs: dict = None) -> Any:
        kwargs = kwargs or {}
        return func(*args, **kwargs)

    def juxt(self, *funcs: Callable) -> Callable:
        def juxtposed(*args, **kwargs):
            return [func(*args, **kwargs) for func in funcs]
        return juxtposed

    def complement(self, func: Callable) -> Callable:
        def complemented(*args, **kwargs):
            return not func(*args, **kwargs)
        return complemented


def get_fn_tool() -> FnTool:
    return FnTool()
