"""强制转换工具"""

from typing import Optional, Any


class CasterTool:
    """强制转换工具"""

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

    def to_str(self, value: Any) -> str:
        """转字符串"""
        return str(value)


_caster_tool: Optional[CasterTool] = None


def get_caster_tool() -> CasterTool:
    global _caster_tool
    if _caster_tool is None:
        _caster_tool = CasterTool()
    return _caster_tool