"""类型检测工具"""

from typing import Any, Optional


class TypeCheckTool:
    _instance: Optional["TypeCheckTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_type(self, value: Any) -> str:
        return type(value).__name__

    def is_string(self, value: Any) -> bool:
        return isinstance(value, str)

    def is_number(self, value: Any) -> bool:
        return isinstance(value, (int, float))

    def is_bool(self, value: Any) -> bool:
        return isinstance(value, bool)

    def is_list(self, value: Any) -> bool:
        return isinstance(value, list)

    def is_dict(self, value: Any) -> bool:
        return isinstance(value, dict)


def get_type_check_tool() -> TypeCheckTool:
    return TypeCheckTool()