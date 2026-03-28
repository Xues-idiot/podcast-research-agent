"""信号包络工具"""

import math
from typing import List, Optional


class SignalEnvelope:
    _instance: Optional["SignalEnvelope"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def envelope(self, signal: List[float]) -> List[float]:
        n = len(signal)
        result = []
        for i in range(n):
            peak = abs(signal[i])
            for j in range(max(0, i - 10), min(n, i + 11)):
                if abs(signal[j]) > peak:
                    peak = abs(signal[j])
            result.append(peak)
        return result

    def demodulate(self, signal: List[float]) -> List[float]:
        return self.envelope(signal)


def get_signal_envelope() -> SignalEnvelope:
    return SignalEnvelope()
