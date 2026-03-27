"""求和工具"""

from typing import Optional, List


class SumTool:
    """求和工具"""

    def sum_values(self, items: List[float]) -> float:
        """求和"""
        return sum(items)


_sum_tool: Optional[SumTool] = None


def get_sum_tool() -> SumTool:
    global _sum_tool
    if _sum_tool is None:
        _sum_tool = SumTool()
    return _sum_tool