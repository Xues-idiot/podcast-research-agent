"""组合工具"""

from typing import Optional, Callable


class ComposeTool:
    """组合工具"""

    def compose(self, *funcs) -> Callable:
        """组合函数"""
        def composed(x):
            result = x
            for func in funcs:
                result = func(result)
            return result
        return composed


_compose_tool: Optional[ComposeTool] = None


def get_compose_tool() -> ComposeTool:
    global _compose_tool
    if _compose_tool is None:
        _compose_tool = ComposeTool()
    return _compose_tool