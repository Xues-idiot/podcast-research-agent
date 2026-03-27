"""异常处理工具"""

from typing import Optional, Callable, Any


class TryCatchTool:
    """异常处理工具"""

    def try_catch(self, func: Callable, fallback: Any = None) -> Any:
        """尝试执行"""
        try:
            return func()
        except Exception:
            return fallback


_tool: Optional[TryCatchTool] = None


def get_try_catch_tool() -> TryCatchTool:
    global _tool
    if _tool is None:
        _tool = TryCatchTool()
    return _tool