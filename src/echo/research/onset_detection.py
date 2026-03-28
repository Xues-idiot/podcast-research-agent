""" onset检测工具"""

from typing import List, Optional


class OnsetDetection:
    _instance: Optional["OnsetDetection"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def detect(self, signal: List[float], threshold: float = 0.5) -> List[int]:
        onsets = []
        energy = [abs(signal[i]) for i in range(len(signal))]
        for i in range(1, len(energy)):
            diff = energy[i] - energy[i - 1]
            if diff > threshold:
                onsets.append(i)
        return onsets


def get_onset_detection() -> OnsetDetection:
    return OnsetDetection()
