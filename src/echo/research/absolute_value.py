"""绝对值工具"""

from typing import Any, Optional


class AbsoluteValue:
    _instance: Optional["AbsoluteValue"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def abs(self, n: float) -> float:
        return abs(n)

    def abs_int(self, n: int) -> int:
        return abs(n)

    def sign(self, n: float) -> int:
        if n > 0:
            return 1
        elif n < 0:
            return -1
        return 0


def get_absolute_value() -> AbsoluteValue:
    return AbsoluteValue()
