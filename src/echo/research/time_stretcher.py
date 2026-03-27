"""时间拉伸工具"""

from typing import List


class TimeStretcher:
    _instance: Optional["TimeStretcher"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def stretch(self, signal: List[float], factor: float) -> List[float]:
        if factor == 1.0:
            return signal
        if factor <= 0:
            return []
        n = int(len(signal) / factor)
        result = []
        for i in range(n):
            idx = int(i * factor)
            if idx < len(signal):
                result.append(signal[idx])
        return result


def get_time_stretcher() -> TimeStretcher:
    return TimeStretcher()
