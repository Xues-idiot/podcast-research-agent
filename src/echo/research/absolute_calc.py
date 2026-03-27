"""绝对值计算器"""

from typing import Optional


class AbsoluteCalc:
    _instance: Optional["AbsoluteCalc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def abs(self, value: float) -> float:
        return abs(value)

    def abs_diff(self, a: float, b: float) -> float:
        return abs(a - b)


def get_absolute_calc() -> AbsoluteCalc:
    return AbsoluteCalc()
