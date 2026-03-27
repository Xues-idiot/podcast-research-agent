"""统计工具"""

from typing import Optional, List


class StatisticsTool:
    """统计工具"""

    def mean(self, values: List[float]) -> float:
        """平均值"""
        return sum(values) / len(values) if values else 0

    def median(self, values: List[float]) -> float:
        """中位数"""
        if not values:
            return 0
        sorted_vals = sorted(values)
        n = len(sorted_vals)
        if n % 2 == 0:
            return (sorted_vals[n//2-1] + sorted_vals[n//2]) / 2
        return sorted_vals[n//2]

    def std_dev(self, values: List[float]) -> float:
        """标准差"""
        if len(values) < 2:
            return 0
        m = self.mean(values)
        variance = sum((x - m) ** 2 for x in values) / len(values)
        return variance ** 0.5


_tool: Optional[StatisticsTool] = None


def get_statistics_tool() -> StatisticsTool:
    global _tool
    if _tool is None:
        _tool = StatisticsTool()
    return _tool