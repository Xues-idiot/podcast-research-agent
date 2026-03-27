"""平均值工具"""

from typing import Optional, List


class AveragerTool:
    """平均值工具"""

    def average(self, items: List[float]) -> float:
        """平均值"""
        return sum(items) / len(items) if items else 0


_averager_tool: Optional[AveragerTool] = None


def get_averager_tool() -> AveragerTool:
    global _averager_tool
    if _averager_tool is None:
        _averager_tool = AveragerTool()
    return _averager_tool