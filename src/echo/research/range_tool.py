"""范围工具"""

from typing import Optional, List


class RangeTool:
    """范围工具"""

    def range(self, start: int, stop: int, step: int = 1) -> List[int]:
        """范围"""
        return list(range(start, stop, step))


_range_tool: Optional[RangeTool] = None


def get_range_tool() -> RangeTool:
    global _range_tool
    if _range_tool is None:
        _range_tool = RangeTool()
    return _range_tool