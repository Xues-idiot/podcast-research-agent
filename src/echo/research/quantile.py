"""分位数工具"""

from typing import Optional, List


class QuantileTool:
    """分位数工具"""

    def percentile(self, values: List[float], percentile: float) -> float:
        """计算百分位数"""
        if not values:
            return 0
        sorted_vals = sorted(values)
        index = (len(sorted_vals) - 1) * percentile / 100
        floor = int(index)
        ceil = floor + 1
        if ceil >= len(sorted_vals):
            return sorted_vals[floor]
        return sorted_vals[floor] * (ceil - index) + sorted_vals[ceil] * (index - floor)


_tool: Optional[QuantileTool] = None


def get_quantile_tool() -> QuantileTool:
    global _tool
    if _tool is None:
        _tool = QuantileTool()
    return _tool