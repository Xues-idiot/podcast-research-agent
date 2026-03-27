"""计数工具"""

from typing import Optional, List, Any


class CountTool:
    """计数工具"""

    def count(self, items: List[Any]) -> int:
        """计数"""
        return len(items)


_count_tool: Optional[CountTool] = None


def get_count_tool() -> CountTool:
    global _count_tool
    if _count_tool is None:
        _count_tool = CountTool()
    return _count_tool