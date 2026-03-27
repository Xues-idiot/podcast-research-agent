"""聚合工具"""

from typing import Optional, Any


class AggregatorTool:
    """聚合工具"""

    def sum(self, items: list) -> float:
        """求和"""
        return sum(items)

    def product(self, items: list) -> float:
        """求积"""
        result = 1
        for item in items:
            result *= item
        return result

    def average(self, items: list) -> float:
        """平均值"""
        return sum(items) / len(items) if items else 0


_aggregator: Optional[AggregatorTool] = None


def get_aggregator_tool() -> AggregatorTool:
    global _aggregator
    if _aggregator is None:
        _aggregator = AggregatorTool()
    return _aggregator