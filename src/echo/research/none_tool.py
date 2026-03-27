"""无匹配检查工具"""

from typing import Optional, List, Callable, Any


class NoneTool:
    """无匹配检查工具"""

    def none_match(self, items: List[Any], predicate: Callable) -> bool:
        """无匹配"""
        return not any(predicate(item) for item in items)


_none_tool: Optional[NoneTool] = None


def get_none_tool() -> NoneTool:
    global _none_tool
    if _none_tool is None:
        _none_tool = NoneTool()
    return _none_tool