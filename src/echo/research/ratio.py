"""比例工具"""

from typing import Optional


class RatioTool:
    """比例工具"""

    def ratio(self, part: float, whole: float) -> float:
        """计算比例"""
        return part / whole if whole else 0

    def proportion(self, value: float, min_val: float, max_val: float) -> float:
        """计算占比"""
        if max_val == min_val:
            return 0
        return (value - min_val) / (max_val - min_val)


_tool: Optional[RatioTool] = None


def get_ratio_tool() -> RatioTool:
    global _tool
    if _tool is None:
        _ratio_tool = RatioTool()
    return _ratio_tool