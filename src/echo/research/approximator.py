"""近似工具"""

from typing import Optional


class Approximator:
    """近似工具"""

    def round_to(self, value: float, precision: int) -> float:
        """四舍五入到精度"""
        multiplier = 10 ** precision
        return round(value * multiplier) / multiplier

    def truncate_to(self, value: float, precision: int) -> float:
        """截断到精度"""
        multiplier = 10 ** precision
        return int(value * multiplier) / multiplier


_tool: Optional[Approximator] = None


def get_approximator() -> Approximator:
    global _tool
    if _tool is None:
        _tool = Approximator()
    return _tool