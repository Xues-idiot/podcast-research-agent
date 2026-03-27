"""紧凑工具"""

from typing import Optional, List, Any


class CompactTool:
    """紧凑工具"""

    def compact(self, items: List[Any]) -> List[Any]:
        """移除空值"""
        return [item for item in items if item is not None]


_compact_tool: Optional[CompactTool] = None


def get_compact_tool() -> CompactTool:
    global _compact_tool
    if _compact_tool is None:
        _compact_tool = CompactTool()
    return _compact_tool