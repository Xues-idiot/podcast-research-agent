"""拉普拉斯变换工具"""

import math
from typing import Callable, Optional


class LaplaceTransform:
    _instance: Optional["LaplaceTransform"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def laplace(self, func: Callable, s: float) -> Optional[float]:
        try:
            return func(s)
        except:
            return None


def get_laplace_transform() -> LaplaceTransform:
    return LaplaceTransform()
