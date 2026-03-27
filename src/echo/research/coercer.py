"""强制转换工具"""

from typing import Optional, Any


class CoercerTool:
    """强制转换工具"""

    def to_int(self, value: Any, default: int = 0) -> int:
        """转整数"""
        try:
            return int(value)
        except (ValueError, TypeError):
            return default

    def to_float(self, value: Any, default: float = 0.0) -> float:
        """转浮点"""
        try:
            return float(value)
        except (ValueError, TypeError):
            return default

    def to_str(self, value: Any) -> str:
        """转字符串"""
        return str(value)


_tool: Optional[CoercerTool] = None


def get_coercer_tool() -> CoercerTool:
    global _tool
    if _tool is None:
        _tool = CoercerTool()
    return _tool