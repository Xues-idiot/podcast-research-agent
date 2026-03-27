"""参数翻转工具"""

from typing import Optional, Callable


class FlipTool:
    """参数翻转工具"""

    def flip(self, func: Callable) -> Callable:
        """翻转参数顺序"""
        def flipped(*args):
            return func(*reversed(args))
        return flipped


_flip_tool: Optional[FlipTool] = None


def get_flip_tool() -> FlipTool:
    global _flip_tool
    if _flip_tool is None:
        _flip_tool = FlipTool()
    return _flip_tool