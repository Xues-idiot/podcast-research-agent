"""统计工具"""

from typing import Optional, List


class StatsTool:
    """统计工具"""

    def sum(self, items: List[float]) -> float:
        """求和"""
        return sum(items)

    def product(self, items: List[float]) -> float:
        """求积"""
        result = 1
        for item in items:
            result *= item
        return result

    def variance(self, items: List[float]) -> float:
        """方差"""
        if not items:
            return 0
        mean = sum(items) / len(items)
        return sum((x - mean) ** 2 for x in items) / len(items)

    def std_dev(self, items: List[float]) -> float:
        """标准差"""
        import math
        return math.sqrt(self.variance(items))


_stats_tool: Optional[StatsTool] = None


def get_stats_tool() -> StatsTool:
    global _stats_tool
    if _stats_tool is None:
        _stats_tool = StatsTool()
    return _stats_tool