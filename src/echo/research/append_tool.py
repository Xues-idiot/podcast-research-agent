"""追加工具"""

from typing import Optional, List, Any


class AppendTool:
    """追加工具"""

    def append(self, items: List[Any], item: Any) -> List[Any]:
        """追加元素"""
        return items + [item]


_append_tool: Optional[AppendTool] = None


def get_append_tool() -> AppendTool:
    global _append_tool
    if _append_tool is None:
        _append_tool = AppendTool()
    return _append_tool