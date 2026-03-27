"""柯里化工具"""

from typing import Optional, Callable, Any


class CurryTool:
    """柯里化工具"""

    def curry(self, func: Callable, arity: int = None) -> Callable:
        """柯里化"""
        if arity is None:
            arity = func.__code__.co_argcount

        def curried(*args):
            if len(args) >= arity:
                return func(*args)
            return curry_help(func, args, arity)
        return curried


def curry_help(func: Callable, args: tuple, arity: int) -> Callable:
    """辅助"""
    def curried(*more_args):
        return func(*(args + more_args))
    return curried


_curry: Optional[CurryTool] = None


def get_curry_tool() -> CurryTool:
    global _curry
    if _curry is None:
        _curry = CurryTool()
    return _curry