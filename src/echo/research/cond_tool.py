"""条件表达式工具"""

from typing import Any, Callable, Optional


class CondTool:
    _instance: Optional["CondTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def if_(self, condition: bool, then_val: Any, else_val: Any) -> Any:
        return then_val if condition else else_val

    def when(self, condition: bool, then_func: Callable) -> Any:
        return then_func() if condition else None

    def when_else(self, condition: bool, then_func: Callable, else_func: Callable) -> Any:
        return then_func() if condition else else_func()


def get_cond_tool() -> CondTool:
    return CondTool()
