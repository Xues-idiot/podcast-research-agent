"""收集器工具"""

from typing import Optional, List, Any


class CollectorTool:
    """收集器工具"""

    def collect(self, items: List[Any], condition: Any = None) -> List[Any]:
        """收集满足条件的项"""
        if condition is None:
            return list(items)
        return [item for item in items if item == condition]


_collector_tool: Optional[CollectorTool] = None


def get_collector_tool() -> CollectorTool:
    global _collector_tool
    if _collector_tool is None:
        _collector_tool = CollectorTool()
    return _collector_tool