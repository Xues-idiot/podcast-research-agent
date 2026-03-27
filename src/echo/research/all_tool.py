"""所有检查工具"""

from typing import Optional, List, Callable, Any


class AllTool:
    """所有检查工具"""

    def all_match(self, items: List[Any], predicate: Callable) -> bool:
        """所有匹配"""
        return all(predicate(item) for item in items)


_all_tool: Optional[AllTool] = None


def get_all_tool() -> AllTool:
    global _all_tool
    if _all_tool is None:
        _all_tool = AllTool()
    return _all_tool