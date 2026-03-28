"""硬剪辑工具"""

from typing import List, Optional


class HardClip:
    _instance: Optional["HardClip"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def clip(self, signal: List[float], threshold: float = 0.99) -> List[float]:
        return [max(-threshold, min(threshold, s)) for s in signal]


def get_hard_clip() -> HardClip:
    return HardClip()
