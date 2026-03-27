"""信号微分器"""

from typing import List


class SignalDifferentiator:
    _instance: Optional["SignalDifferentiator"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def differentiate(self, signal: List[float], dt: float = 1.0) -> List[float]:
        if len(signal) < 2:
            return signal
        return [(signal[i] - signal[i-1]) / dt for i in range(1, len(signal))]


def get_signal_differentiator() -> SignalDifferentiator:
    return SignalDifferentiator()
