"""类型转换工具"""

from typing import Optional, Any


class TypeConverter:
    """类型转换工具"""

    def to_int(self, value: Any, default: int = 0) -> int:
        """转整数"""
        try:
            return int(value)
        except (ValueError, TypeError):
            return default

    def to_float(self, value: Any, default: float = 0.0) -> float:
        """转浮点数"""
        try:
            return float(value)
        except (ValueError, TypeError):
            return default

    def to_string(self, value: Any) -> str:
        """转字符串"""
        return str(value)

    def to_bool(self, value: Any) -> bool:
        """转布尔值"""
        if isinstance(value, bool):
            return value
        if isinstance(value, str):
            return value.lower() in ('true', '1', 'yes')
        return bool(value)


_converter: Optional[TypeConverter] = None


def get_type_converter() -> TypeConverter:
    global _converter
    if _converter is None:
        _converter = TypeConverter()
    return _converter