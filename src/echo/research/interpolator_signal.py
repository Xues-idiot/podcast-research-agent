"""信号插值工具"""

from typing import List, Optional


class SignalInterpolator:
    _instance: Optional["SignalInterpolator"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def interpolate(self, signal: List[float], factor: int) -> List[float]:
        if factor <= 1:
            return signal
        n = len(signal)
        result = []
        for i in range(n - 1):
            result.append(signal[i])
            for j in range(1, factor):
                t = j / factor
                result.append(signal[i] * (1 - t) + signal[i + 1] * t)
        result.append(signal[-1])
        return result


def get_signal_interpolator() -> SignalInterpolator:
    return SignalInterpolator()
