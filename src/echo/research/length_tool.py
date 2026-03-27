"""长度工具"""

from typing import Optional, List, Any


class LengthTool:
    """长度工具"""

    def length(self, items: List[Any]) -> int:
        """长度"""
        return len(items)


_length_tool: Optional[LengthTool] = None


def get_length_tool() -> LengthTool:
    global _length_tool
    if _length_tool is None:
        _length_tool = LengthTool()
    return _length_tool