"""去重工具"""

from typing import Optional, List, Any


class DistinctTool:
    """去重工具"""

    def distinct(self, items: List[Any]) -> List[Any]:
        """去重"""
        seen = set()
        result = []
        for item in items:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result


_distinct_tool: Optional[DistinctTool] = None


def get_distinct_tool() -> DistinctTool:
    global _distinct_tool
    if _distinct_tool is None:
        _distinct_tool = DistinctTool()
    return _distinct_tool