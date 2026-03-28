"""简单时间拉伸工具"""

from typing import List, Optional


class TimeStretchSimple:
    _instance: Optional["TimeStretchSimple"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def stretch(self, signal: List[float], factor: float) -> List[float]:
        n = int(len(signal) / factor)
        result = []
        for i in range(n):
            src_idx = i * factor
            idx = int(src_idx)
            frac = src_idx - idx
            if idx + 1 < len(signal):
                result.append(signal[idx] * (1 - frac) + signal[idx + 1] * frac)
            else:
                result.append(signal[idx])
        return result


def get_time_stretch_simple() -> TimeStretchSimple:
    return TimeStretchSimple()
