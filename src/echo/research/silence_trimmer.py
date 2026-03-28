"""静音修剪工具"""

from typing import List, Optional, Tuple


class SilenceTrimmer:
    _instance: Optional["SilenceTrimmer"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def trim(self, signal: List[float], threshold: float = 0.01) -> Tuple[List[float], int, int]:
        start = 0
        end = len(signal) - 1
        for i in range(len(signal)):
            if abs(signal[i]) > threshold:
                start = i
                break
        for i in range(len(signal) - 1, -1, -1):
            if abs(signal[i]) > threshold:
                end = i
                break
        return signal[start:end + 1], start, end


def get_silence_trimmer() -> SilenceTrimmer:
    return SilenceTrimmer()
