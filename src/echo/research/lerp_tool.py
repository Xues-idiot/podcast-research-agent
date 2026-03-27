"""线性插值工具"""

from typing import Optional


class LerpTool:
    _instance: Optional["LerpTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def lerp(self, a: float, b: float, t: float) -> float:
        return a + (b - a) * t

    def inverse_lerp(self, a: float, b: float, value: float) -> Optional[float]:
        if b == a:
            return None
        return (value - a) / (b - a)


def get_lerp_tool() -> LerpTool:
    return LerpTool()
