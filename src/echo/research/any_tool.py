"""任意检查工具"""

from typing import Optional, List, Callable, Any


class AnyTool:
    """任意检查工具"""

    def any_match(self, items: List[Any], predicate: Callable) -> bool:
        """任意匹配"""
        return any(predicate(item) for item in items)


_any_tool: Optional[AnyTool] = None


def get_any_tool() -> AnyTool:
    global _any_tool
    if _any_tool is None:
        _any_tool = AnyTool()
    return _any_tool