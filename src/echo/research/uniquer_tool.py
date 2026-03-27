"""唯一化工具"""

from typing import Optional, List, Any


class UniquerTool:
    """唯一化工具"""

    def unique(self, items: List[Any]) -> List[Any]:
        """唯一化"""
        seen = set()
        result = []
        for item in items:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result


_uniquer_tool: Optional[UniquerTool] = None


def get_uniquer_tool() -> UniquerTool:
    global _uniquer_tool
    if _uniquer_tool is None:
        _uniquer_tool = UniquerTool()
    return _uniquer_tool