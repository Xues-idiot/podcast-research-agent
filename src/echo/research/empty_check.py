"""空值检查工具"""

from typing import Any, Optional


class EmptyCheckTool:
    _instance: Optional["EmptyCheckTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def is_empty(self, value: Any) -> bool:
        if value is None:
            return True
        if isinstance(value, str):
            return len(value.strip()) == 0
        if isinstance(value, (list, dict, tuple, set)):
            return len(value) == 0
        return False

    def is_not_empty(self, value: Any) -> bool:
        return not self.is_empty(value)


def get_empty_check_tool() -> EmptyCheckTool:
    return EmptyCheckTool()