"""选择工具"""

from typing import Optional, List, Any


class SelectTool:
    """选择工具"""

    def select(self, items: List[Any], indices: List[int]) -> List[Any]:
        """按索引选择"""
        return [items[i] for i in indices if 0 <= i < len(items)]


_select_tool: Optional[SelectTool] = None


def get_select_tool() -> SelectTool:
    global _select_tool
    if _select_tool is None:
        _select_tool = SelectTool()
    return _select_tool