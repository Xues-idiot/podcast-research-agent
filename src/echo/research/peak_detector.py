"""峰值检测器"""

from typing import List, Optional, Tuple


class PeakDetector:
    _instance: Optional["PeakDetector"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def find_peaks(self, signal: List[float], threshold: float = 0.0) -> List[int]:
        if len(signal) < 3:
            return []
        peaks = []
        for i in range(1, len(signal) - 1):
            if signal[i] > signal[i-1] and signal[i] > signal[i+1] and signal[i] > threshold:
                peaks.append(i)
        return peaks


def get_peak_detector() -> PeakDetector:
    return PeakDetector()
