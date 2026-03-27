"""恒等函数工具"""

from typing import Callable, Any


class IdentityFunc:
    _instance: Optional["IdentityFunc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def identity(self, x: Any) -> Any:
        return x


def get_identity_func() -> IdentityFunc:
    return IdentityFunc()
