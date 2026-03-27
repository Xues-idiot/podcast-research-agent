"""交集工具"""

from typing import Optional, List, Any


class IntersectTool:
    """交集工具"""

    def intersect(self, list1: List[Any], list2: List[Any]) -> List[Any]:
        """计算交集"""
        set1, set2 = set(list1), set(list2)
        return list(set1 & set2)


_intersect_tool: Optional[IntersectTool] = None


def get_intersect_tool() -> IntersectTool:
    global _intersect_tool
    if _intersect_tool is None:
        _intersect_tool = IntersectTool()
    return _intersect_tool