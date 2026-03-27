"""分布工具"""

from typing import Optional
import random


class DistributionTool:
    """分布工具"""

    def normal_random(self, mean: float = 0, std: float = 1) -> float:
        """正态分布随机"""
        return random.gauss(mean, std)

    def uniform_random(self, min_val: float, max_val: float) -> float:
        """均匀分布随机"""
        return random.uniform(min_val, max_val)


_tool: Optional[DistributionTool] = None


def get_distribution_tool() -> DistributionTool:
    global _tool
    if _tool is None:
        _tool = DistributionTool()
    return _tool