"""过滤器工具"""

from typing import Optional, Callable, Any


class FilterTool:
    """过滤器工具"""

    def filter(self, items: list, predicate: Callable) -> list:
        """过滤"""
        return [item for item in items if predicate(item)]

    def reject(self, items: list, predicate: Callable) -> list:
        """排除"""
        return [item for item in items if not predicate(item)]


_filter: Optional[FilterTool] = None


def get_filter_tool() -> FilterTool:
    global _filter
    if _filter is None:
        _filter = FilterTool()
    return _filter