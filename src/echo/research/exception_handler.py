"""异常处理工具"""

from typing import Optional, Callable, Any


class ExceptionHandler:
    """异常处理工具"""

    def handle(self, func: Callable, handler: Callable) -> Any:
        """处理异常"""
        try:
            return func()
        except Exception as e:
            return handler(e)


_exception_handler: Optional[ExceptionHandler] = None


def get_exception_handler() -> ExceptionHandler:
    global _exception_handler
    if _exception_handler is None:
        _exception_handler = ExceptionHandler()
    return _exception_handler