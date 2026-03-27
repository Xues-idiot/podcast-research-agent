"""空操作工具"""

from typing import Callable, Any


class NoopFunc:
    _instance: Optional["NoopFunc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def noop(self, *args, **kwargs) -> None:
        pass


def get_noop_func() -> NoopFunc:
    return NoopFunc()
