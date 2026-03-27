"""函数包装工具"""

from typing import Optional, Callable, Any


class FunctionWrapper:
    """函数包装工具"""

    def before(self, func: Callable, before_fn: Callable) -> Callable:
        """前置钩子"""
        def wrapper(*args, **kwargs):
            before_fn(*args, **kwargs)
            return func(*args, **kwargs)
        return wrapper

    def after(self, func: Callable, after_fn: Callable) -> Callable:
        """后置钩子"""
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            after_fn(result)
            return result
        return wrapper


_wrapper: Optional[FunctionWrapper] = None


def get_function_wrapper() -> FunctionWrapper:
    global _wrapper
    if _wrapper is None:
        _wrapper = FunctionWrapper()
    return _wrapper