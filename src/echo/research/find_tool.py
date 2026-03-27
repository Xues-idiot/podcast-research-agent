"""查找工具"""

from typing import Optional, List, Any, Callable


class FindTool:
    """查找工具"""

    def find(self, items: List[Any], predicate: Callable) -> Any:
        """查找第一个匹配项"""
        for item in items:
            if predicate(item):
                return item
        return None


_find_tool: Optional[FindTool] = None


def get_find_tool() -> FindTool:
    global _find_tool
    if _find_tool is None:
        _find_tool = FindTool()
    return _find_tool