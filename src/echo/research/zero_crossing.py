"""过零检测器"""

from typing import List, Optional


class ZeroCrossing:
    _instance: Optional["ZeroCrossing"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def find_crossings(self, signal: List[float]) -> List[int]:
        if len(signal) < 2:
            return []
        crossings = []
        for i in range(1, len(signal)):
            if (signal[i-1] >= 0 and signal[i] < 0) or (signal[i-1] < 0 and signal[i] >= 0):
                crossings.append(i)
        return crossings


def get_zero_crossing() -> ZeroCrossing:
    return ZeroCrossing()
