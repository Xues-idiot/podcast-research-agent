"""查找工具"""

from typing import Optional, List, Any, Callable


class FinderTool:
    """查找工具"""

    def find(self, items: List[Any], predicate: Callable) -> Any:
        """查找"""
        for item in items:
            if predicate(item):
                return item
        return None


_finder_tool: Optional[FinderTool] = None


def get_finder_tool() -> FinderTool:
    global _finder_tool
    if _finder_tool is None:
        _finder_tool = FinderTool()
    return _finder_tool