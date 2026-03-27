"""异常处理工具"""

from typing import Callable, Any, Optional


class ExceptionHandlerTool:
    _instance: Optional["ExceptionHandlerTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def handle(self, func: Callable, handler: Callable = None) -> Callable:
        def handled(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if handler:
                    return handler(e)
                return None
        return handled


def get_exception_handler_tool() -> ExceptionHandlerTool:
    return ExceptionHandlerTool()
