"""包含检查工具"""

from typing import Optional, List, Any


class ContainsTool:
    """包含检查工具"""

    def contains(self, items: List[Any], item: Any) -> bool:
        """包含检查"""
        return item in items


_contains_tool: Optional[ContainsTool] = None


def get_contains_tool() -> ContainsTool:
    global _contains_tool
    if _contains_tool is None:
        _contains_tool = ContainsTool()
    return _contains_tool