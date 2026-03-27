"""差异工具"""

from typing import Optional, List, Any


class DiffTool:
    """差异工具"""

    def diff(self, list1: List[Any], list2: List[Any]) -> tuple:
        """计算差异"""
        set1, set2 = set(list1), set(list2)
        return (list(set1 - set2), list(set2 - set1))


_diff_tool: Optional[DiffTool] = None


def get_diff_tool() -> DiffTool:
    global _diff_tool
    if _diff_tool is None:
        _diff_tool = DiffTool()
    return _diff_tool