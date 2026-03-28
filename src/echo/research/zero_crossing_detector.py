"""过零检测工具"""

from typing import List, Optional


class ZeroCrossingDetector:
    _instance: Optional["ZeroCrossingDetector"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def find_crossings(self, signal: List[float]) -> List[int]:
        crossings = []
        for i in range(1, len(signal)):
            if (signal[i - 1] >= 0 and signal[i] < 0) or (signal[i - 1] < 0 and signal[i] >= 0):
                crossings.append(i)
        return crossings

    def count_crossings(self, signal: List[float]) -> int:
        return len(self.find_crossings(signal))


def get_zero_crossing_detector() -> ZeroCrossingDetector:
    return ZeroCrossingDetector()
