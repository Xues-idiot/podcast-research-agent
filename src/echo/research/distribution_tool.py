"""分布工具"""

from typing import Optional, List
import random


class DistributionTool:
    """分布工具"""

    def normal(self, mean: float, std_dev: float, count: int) -> List[float]:
        """正态分布"""
        return [random.gauss(mean, std_dev) for _ in range(count)]

    def uniform(self, low: float, high: float, count: int) -> List[float]:
        """均匀分布"""
        return [random.uniform(low, high) for _ in range(count)]


_distribution_tool: Optional[DistributionTool] = None


def get_distribution_tool() -> DistributionTool:
    global _distribution_tool
    if _distribution_tool is None:
        _distribution_tool = DistributionTool()
    return _distribution_tool