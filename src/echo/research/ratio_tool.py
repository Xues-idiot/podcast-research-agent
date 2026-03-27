"""比例工具"""

from typing import Optional


class RatioTool:
    """比例工具"""

    def calculate_ratio(self, a: float, b: float) -> float:
        """计算比例"""
        if b == 0:
            return 0.0
        return a / b

    def simplify_ratio(self, a: float, b: float) -> tuple:
        """简化比例"""
        if b == 0:
            return (a, b)
        import math
        g = math.gcd(int(a), int(b))
        return (a / g, b / g)

    def scale_ratio(self, a: float, b: float, factor: float) -> tuple:
        """按比例缩放"""
        return (a * factor, b * factor)


_ratio_tool: Optional[RatioTool] = None


def get_ratio_tool() -> RatioTool:
    global _ratio_tool
    if _ratio_tool is None:
        _ratio_tool = RatioTool()
    return _ratio_tool