"""幂工具"""

from typing import Optional


class PowerTool:
    """幂工具"""

    def power(self, base: float, exponent: float) -> float:
        """幂运算"""
        return base ** exponent

    def sqrt(self, value: float) -> float:
        """平方根"""
        return value ** 0.5


_tool: Optional[PowerTool] = None


def get_power_tool() -> PowerTool:
    global _tool
    if _tool is None:
        _tool = PowerTool()
    return _tool