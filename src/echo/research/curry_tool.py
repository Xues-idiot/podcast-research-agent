"""柯里化工具"""

from typing import Optional, Callable


class CurryTool:
    """柯里化工具"""

    def curry(self, func: Callable) -> Callable:
        """柯里化"""
        def curried(*args):
            if len(args) >= func.__code__.co_argcount:
                return func(*args)
            def next_curry(*more_args):
                return curried(*(args + more_args))
            return next_curry
        return curried


_curry_tool: Optional[CurryTool] = None


def get_curry_tool() -> CurryTool:
    global _curry_tool
    if _curry_tool is None:
        _curry_tool = CurryTool()
    return _curry_tool