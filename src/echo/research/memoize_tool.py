"""记忆化工具"""

from typing import Optional, Callable, Any, Dict


class MemoizeTool:
    """记忆化工具"""

    def __init__(self):
        self._cache: Dict[str, Any] = {}

    def memoize(self, func: Callable, *args, **kwargs) -> Any:
        """记忆化调用"""
        key = str(args) + str(kwargs)
        if key not in self._cache:
            self._cache[key] = func(*args, **kwargs)
        return self._cache[key]

    def clear(self) -> None:
        """清空缓存"""
        self._cache.clear()


_memoize_tool: Optional[MemoizeTool] = None


def get_memoize_tool() -> MemoizeTool:
    global _memoize_tool
    if _memoize_tool is None:
        _memoize_tool = MemoizeTool()
    return _memoize_tool