"""并集工具"""

from typing import Optional, List, Any


class UnionTool:
    """并集工具"""

    def union(self, list1: List[Any], list2: List[Any]) -> List[Any]:
        """计算并集"""
        set1, set2 = set(list1), set(list2)
        return list(set1 | set2)


_union_tool: Optional[UnionTool] = None


def get_union_tool() -> UnionTool:
    global _union_tool
    if _union_tool is None:
        _union_tool = UnionTool()
    return _union_tool