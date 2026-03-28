"""节拍检测工具"""

from typing import List, Optional


class TempoDetection:
    _instance: Optional["TempoDetection"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def detect(self, onsets: List[int], sample_rate: float = 44100) -> float:
        if len(onsets) < 2:
            return 0.0
        intervals = [onsets[i + 1] - onsets[i] for i in range(len(onsets) - 1)]
        avg_interval = sum(intervals) / len(intervals)
        bpm = 60.0 * sample_rate / avg_interval if avg_interval > 0 else 0.0
        return bpm


def get_tempo_detection() -> TempoDetection:
    return TempoDetection()
