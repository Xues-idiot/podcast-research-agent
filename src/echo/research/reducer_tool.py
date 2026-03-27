"""归约工具"""

from typing import Optional, Callable, Any


class ReducerTool:
    """归约工具"""

    def reduce(self, items: list, func: Callable, initial: Any = None) -> Any:
        """归约"""
        if not items:
            return initial
        if initial is None:
            return self._reduce(items, func)
        return self._reduce_with_initial(items, func, initial)

    def _reduce(self, items: list, func: Callable) -> Any:
        """无初始值归约"""
        result = items[0]
        for item in items[1:]:
            result = func(result, item)
        return result

    def _reduce_with_initial(self, items: list, func: Callable, initial: Any) -> Any:
        """有初始值归约"""
        result = initial
        for item in items:
            result = func(result, item)
        return result


_reducer: Optional[ReducerTool] = None


def get_reducer_tool() -> ReducerTool:
    global _reducer
    if _reducer is None:
        _reducer = ReducerTool()
    return _reducer