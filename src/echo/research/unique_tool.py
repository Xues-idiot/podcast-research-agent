"""唯一工具"""

from typing import Optional, List, Any


class UniqueTool:
    """唯一工具"""

    def unique(self, items: List[Any]) -> List[Any]:
        """去重"""
        seen = set()
        result = []
        for item in items:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result


_unique_tool: Optional[UniqueTool] = None


def get_unique_tool() -> UniqueTool:
    global _unique_tool
    if _unique_tool is None:
        _unique_tool = UniqueTool()
    return _unique_tool