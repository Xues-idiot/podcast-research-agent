"""函数包装工具"""

from typing import Optional, Callable, Any


class FunctionWrapper:
    """函数包装工具"""

    def wrap(self, func: Callable) -> Callable:
        """包装函数"""
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper

    def before(self, func: Callable, before_func: Callable) -> Callable:
        """前置处理"""
        def wrapper(*args, **kwargs):
            before_func()
            return func(*args, **kwargs)
        return wrapper

    def after(self, func: Callable, after_func: Callable) -> Callable:
        """后置处理"""
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            after_func()
            return result
        return wrapper


_function_wrapper: Optional[FunctionWrapper] = None


def get_function_wrapper() -> FunctionWrapper:
    global _function_wrapper
    if _function_wrapper is None:
        _function_wrapper = FunctionWrapper()
    return _function_wrapper