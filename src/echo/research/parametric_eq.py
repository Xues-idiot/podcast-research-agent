"""参数均衡器"""

from typing import List, Optional


class ParametricEq:
    _instance: Optional["ParametricEq"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def eq(self, signal: List[float], freq: float, q: float, gain: float) -> List[float]:
        return signal


def get_parametric_eq() -> ParametricEq:
    return ParametricEq()
