"""参数翻转工具"""

from typing import Optional, Callable


class FlipTool:
    """参数翻转工具"""

    def flip(self, func: Callable) -> Callable:
        """翻转参数"""
        def flipped(a, b):
            return func(b, a)
        return flipped


_tool: Optional[FlipTool] = None


def get_flip_tool() -> FlipTool:
    global _tool
    if _tool is None:
        _tool = FlipTool()
    return _tool