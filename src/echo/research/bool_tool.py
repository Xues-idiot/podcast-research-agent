"""布尔工具"""

from typing import Any, Optional


class BoolTool:
    _instance: Optional["BoolTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def and_(self, a: bool, b: bool) -> bool:
        return a and b

    def or_(self, a: bool, b: bool) -> bool:
        return a or b

    def not_(self, a: bool) -> bool:
        return not a

    def xor(self, a: bool, b: bool) -> bool:
        return bool(a) != bool(b)

    def to_bool(self, a: Any) -> bool:
        return bool(a)


def get_bool_tool() -> BoolTool:
    return BoolTool()
