"""合并工具"""

from typing import Optional, List, Any


class MergeTool:
    """合并工具"""

    def merge(self, list1: List[Any], list2: List[Any]) -> List[Any]:
        """合并列表"""
        return list1 + list2


_merge_tool: Optional[MergeTool] = None


def get_merge_tool() -> MergeTool:
    global _merge_tool
    if _merge_tool is None:
        _merge_tool = MergeTool()
    return _merge_tool