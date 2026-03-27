"""查找工具"""

from typing import Optional, Callable, Any


class FinderTool:
    """查找工具"""

    def find(self, items: list, predicate: Callable) -> Any:
        """查找第一个匹配"""
        for item in items:
            if predicate(item):
                return item
        return None

    def find_index(self, items: list, predicate: Callable) -> int:
        """查找索引"""
        for i, item in enumerate(items):
            if predicate(item):
                return i
        return -1


_finder: Optional[FinderTool] = None


def get_finder_tool() -> FinderTool:
    global _finder
    if _finder is None:
        _finder = FinderTool()
    return _finder