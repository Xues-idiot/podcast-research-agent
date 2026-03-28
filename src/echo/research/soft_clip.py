"""软剪辑工具"""

import math
from typing import List, Optional


class SoftClip:
    _instance: Optional["SoftClip"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def clip(self, signal: List[float], threshold: float = 0.9) -> List[float]:
        return [math.tanh(s / threshold) * threshold for s in signal]


def get_soft_clip() -> SoftClip:
    return SoftClip()
