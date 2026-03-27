"""收集工具"""

from typing import Optional, Any, Callable


class CollectorTool:
    """收集工具"""

    def collect(self, items: list, predicate: Callable) -> list:
        """收集满足条件的"""
        return [item for item in items if predicate(item)]

    def collect_keys(self, data: dict) -> list:
        """收集所有键"""
        return list(data.keys())

    def collect_values(self, data: dict) -> list:
        """收集所有值"""
        return list(data.values())


_collector: Optional[CollectorTool] = None


def get_collector_tool() -> CollectorTool:
    global _collector
    if _collector is None:
        _collector = CollectorTool()
    return _collector