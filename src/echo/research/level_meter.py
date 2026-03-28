"""电平计量器"""

from typing import List, Optional


class LevelMeter:
    _instance: Optional["LevelMeter"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def meter(self, signal: List[float]) -> float:
        if not signal:
            return -60.0
        import math
        peak = max(abs(s) for s in signal)
        db = 20 * math.log10(peak) if peak > 0 else -60.0
        return db


def get_level_meter() -> LevelMeter:
    return LevelMeter()

import math
