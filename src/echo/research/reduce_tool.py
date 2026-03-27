"""归约工具"""

from typing import Optional, Any, Callable


class ReduceTool:
    """归约工具"""

    def reduce_items(self, items: List[Any], func: Callable, initial: Any = None) -> Any:
        """归约"""
        if not items:
            return initial
        result = initial if initial is not None else items[0]
        for item in items[1:] if initial is not None else items[1:]:
            result = func(result, item)
        return result


_reduce_tool: Optional[ReduceTool] = None


def get_reduce_tool() -> ReduceTool:
    global _reduce_tool
    if _reduce_tool is None:
        _reduce_tool = ReduceTool()
    return _reduce_tool