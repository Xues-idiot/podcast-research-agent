"""链式调用工具"""

from typing import Any, Callable, Optional


class ChainTool:
    _instance: Optional["ChainTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def chain(self, value: Any) -> "ChainWrapper":
        return ChainWrapper(value)

    def tap(self, value: Any, func: Callable) -> Any:
        func(value)
        return value


class ChainWrapper:
    def __init__(self, value: Any):
        self._value = value

    def pipe(self, func: Callable) -> "ChainWrapper":
        self._value = func(self._value)
        return self

    def value(self) -> Any:
        return self._value


def get_chain_tool() -> ChainTool:
    return ChainTool()
