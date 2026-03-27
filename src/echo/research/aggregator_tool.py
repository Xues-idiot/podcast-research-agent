"""聚合工具"""

from typing import Optional, List, Any


class AggregatorTool:
    """聚合工具"""

    def aggregate(self, items: List[Any], key: str) -> dict:
        """聚合"""
        result = {}
        for item in items:
            if isinstance(item, dict):
                k = item.get(key)
                if k not in result:
                    result[k] = []
                result[k].append(item)
        return result


_aggregator_tool: Optional[AggregatorTool] = None


def get_aggregator_tool() -> AggregatorTool:
    global _aggregator_tool
    if _aggregator_tool is None:
        _aggregator_tool = AggregatorTool()
    return _aggregator_tool