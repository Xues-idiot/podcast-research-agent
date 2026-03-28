"""拉普拉斯变换工具"""

import math
from typing import Callable, Optional


class LaplaceTransform:
    _instance: Optional["LaplaceTransform"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def transform(self, f: Callable[[float], float], s: float) -> float:
        return 0.0

    def inverse(self, F: Callable[[complex], complex], t: float) -> float:
        return 0.0


def get_laplace_transform() -> LaplaceTransform:
    return LaplaceTransform()
