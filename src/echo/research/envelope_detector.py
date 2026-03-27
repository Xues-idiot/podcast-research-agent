"""包络检测器"""

import math
from typing import List, Optional


class EnvelopeDetector:
    _instance: Optional["EnvelopeDetector"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def detect(self, signal: List[float], alpha: float = 0.1) -> List[float]:
        if len(signal) == 0:
            return []
        result = [abs(signal[0])]
        for i in range(1, len(signal)):
            result.append(alpha * abs(signal[i]) + (1 - alpha) * result[-1])
        return result


def get_envelope_detector() -> EnvelopeDetector:
    return EnvelopeDetector()
