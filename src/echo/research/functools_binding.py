"""绑定工具"""

from typing import Callable, Any, Optional


class FunctoolsBinding:
    _instance: Optional["FunctoolsBinding"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def bind(self, func: Callable, *args: Any, **kwargs: Any) -> Callable:
        def bound(*a, **k):
            return func(*args, *a, **kwargs, **k)
        return bound

    def partial(self, func: Callable, *args: Any, **kwargs: Any) -> Callable:
        def partial_func(*a, **k):
            return func(*args, *a, **kwargs, **k)
        return partial_func


def get_functools_binding() -> FunctoolsBinding:
    return FunctoolsBinding()
