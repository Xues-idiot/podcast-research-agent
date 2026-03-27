"""幂工具"""

from typing import Optional


class PowerTool:
    """幂工具"""

    def power(self, base: float, exponent: float) -> float:
        """计算幂"""
        return base ** exponent

    def square(self, value: float) -> float:
        """平方"""
        return value ** 2

    def cube(self, value: float) -> float:
        """立方"""
        return value ** 3

    def sqrt(self, value: float) -> float:
        """平方根"""
        return value ** 0.5


_power_tool: Optional[PowerTool] = None


def get_power_tool() -> PowerTool:
    global _power_tool
    if _power_tool is None:
        _power_tool = PowerTool()
    return _power_tool