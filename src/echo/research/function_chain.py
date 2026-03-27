"""函数链"""

from typing import Callable, Any, List


class FunctionChain:
    _instance: Optional["FunctionChain"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_funcs"):
            self._funcs: List[Callable] = []

    def add(self, func: Callable) -> "FunctionChain":
        self._funcs.append(func)
        return self

    def execute(self, value: Any) -> Any:
        result = value
        for func in self._funcs:
            result = func(result)
        return result


def get_function_chain() -> FunctionChain:
    return FunctionChain()
