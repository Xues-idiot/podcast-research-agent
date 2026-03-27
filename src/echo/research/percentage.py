"""百分比工具"""

from typing import Optional


class PercentageTool:
    """百分比工具"""

    def calculate(self, part: float, total: float) -> float:
        """计算百分比"""
        if total == 0:
            return 0.0
        return (part / total) * 100

    def of(self, percent: float, total: float) -> float:
        """计算百分比的值"""
        return (percent / 100) * total

    def format(self, value: float, decimals: int = 2) -> str:
        """格式化百分比"""
        return f"{value:.{decimals}f}%"


_percentage_tool: Optional[PercentageTool] = None


def get_percentage_tool() -> PercentageTool:
    global _percentage_tool
    if _percentage_tool is None:
        _percentage_tool = PercentageTool()
    return _percentage_tool