"""BPM检测器"""

from typing import List, Optional


class BpmDetector:
    _instance: Optional["BpmDetector"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def detect(self, signal: List[float], sample_rate: float = 44100) -> float:
        if not signal:
            return 120.0
        energy = [abs(signal[i]) for i in range(len(signal))]
        peaks = []
        for i in range(1, len(energy) - 1):
            if energy[i] > energy[i - 1] and energy[i] > energy[i + 1]:
                peaks.append(i)
        if len(peaks) < 2:
            return 120.0
        intervals = [peaks[i + 1] - peaks[i] for i in range(len(peaks) - 1)]
        avg_interval = sum(intervals) / len(intervals)
        bpm = 60 * sample_rate / avg_interval if avg_interval > 0 else 120.0
        return max(60, min(200, bpm))


def get_bpm_detector() -> BpmDetector:
    return BpmDetector()
