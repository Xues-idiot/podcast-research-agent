"""平均值工具"""

from typing import Optional, List


class AvgTool:
    """平均值工具"""

    def average(self, items: List[float]) -> float:
        """平均值"""
        return sum(items) / len(items) if items else 0


_avg_tool: Optional[AvgTool] = None


def get_avg_tool() -> AvgTool:
    global _avg_tool
    if _avg_tool is None:
        _avg_tool = AvgTool()
    return _avg_tool