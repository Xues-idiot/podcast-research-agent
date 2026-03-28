"""波形分析器"""

import math
from typing import List, Optional


class WaveformAnalyzer:
    _instance: Optional["WaveformAnalyzer"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def analyze(self, signal: List[float]) -> dict:
        if not signal:
            return {"min": 0, "max": 0, "mean": 0, "std": 0}
        n = len(signal)
        mean = sum(signal) / n
        variance = sum((s - mean) ** 2 for s in signal) / n
        return {
            "min": min(signal),
            "max": max(signal),
            "mean": mean,
            "std": math.sqrt(variance)
        }


def get_waveform_analyzer() -> WaveformAnalyzer:
    return WaveformAnalyzer()
