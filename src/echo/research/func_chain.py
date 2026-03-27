"""函数链工具"""

from typing import Any, Callable, List, Optional


class FuncChain:
    _instance: Optional["FuncChain"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def chain(self, *funcs: Callable) -> Callable:
        def chained(value: Any) -> Any:
            result = value
            for func in funcs:
                result = func(result)
            return result
        return chained


def get_func_chain() -> FuncChain:
    return FuncChain()
