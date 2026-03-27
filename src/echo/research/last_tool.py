"""最后一个元素工具"""

from typing import Optional, List, Any


class LastTool:
    """最后一个元素工具"""

    def last(self, items: List[Any]) -> Any:
        """最后一个元素"""
        return items[-1] if items else None


_last_tool: Optional[LastTool] = None


def get_last_tool() -> LastTool:
    global _last_tool
    if _last_tool is None:
        _last_tool = LastTool()
    return _last_tool