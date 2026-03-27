"""单次执行工具"""

from typing import Optional, Callable, Any


class OnceTool:
    """单次执行工具"""

    def __init__(self):
        self._executed = False

    def once(self, func: Callable) -> Callable:
        """只执行一次"""
        def wrapper(*args, **kwargs):
            if not self._executed:
                self._executed = True
                return func(*args, **kwargs)
            return None
        return wrapper


_tool: Optional[OnceTool] = None


def get_once_tool() -> OnceTool:
    global _tool
    if _tool is None:
        _tool = OnceTool()
    return _tool