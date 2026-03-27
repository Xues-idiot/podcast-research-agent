"""分位数工具"""

from typing import Optional, List


class QuantileTool:
    """分位数工具"""

    def percentile(self, items: List[float], percent: float) -> float:
        """百分位数"""
        if not items:
            return 0
        sorted_items = sorted(items)
        index = (len(sorted_items) - 1) * percent / 100
        floor = int(index)
        ceil = floor + 1
        if ceil >= len(sorted_items):
            return sorted_items[floor]
        return sorted_items[floor] + (sorted_items[ceil] - sorted_items[floor]) * (index - floor)


_quantile_tool: Optional[QuantileTool] = None


def get_quantile_tool() -> QuantileTool:
    global _quantile_tool
    if _quantile_tool is None:
        _quantile_tool = QuantileTool()
    return _quantile_tool