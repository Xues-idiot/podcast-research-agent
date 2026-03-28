"""失真效果器"""

import math
from typing import List, Optional


class Distortion:
    _instance: Optional["Distortion"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def apply(self, signal: List[float], drive: float = 0.5) -> List[float]:
        return [math.tanh(s * (1 + drive * 10)) for s in signal]


def get_distortion() -> Distortion:
    return Distortion()
