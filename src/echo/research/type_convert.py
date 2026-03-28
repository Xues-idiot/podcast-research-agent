"""类型转换工具"""

from typing import Any, Optional


class TypeConvertTool:
    _instance: Optional["TypeConvertTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def to_int(self, value: Any) -> int:
        try:
            return int(value)
        except:
            return 0

    def to_float(self, value: Any) -> float:
        try:
            return float(value)
        except:
            return 0.0

    def to_str(self, value: Any) -> str:
        return str(value)

    def to_bool(self, value: Any) -> bool:
        if isinstance(value, bool):
            return value
        if isinstance(value, str):
            return value.lower() in ('true', '1', 'yes')
        return bool(value)


def get_type_convert_tool() -> TypeConvertTool:
    return TypeConvertTool()