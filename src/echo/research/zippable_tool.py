"""Zip工具"""

from typing import Optional, List, Any, Tuple


class ZippableTool:
    """Zip工具"""

    def zip_lists(self, *lists: List[Any]) -> List[Tuple]:
        """Zip列表"""
        return list(zip(*lists))


_zippable_tool: Optional[ZippableTool] = None


def get_zippable_tool() -> ZippableTool:
    global _zippable_tool
    if _zippable_tool is None:
        _zippable_tool = ZippableTool()
    return _zippable_tool