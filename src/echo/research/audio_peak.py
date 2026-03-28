"""音频峰值检测工具"""

from typing import List, Optional, Tuple


class AudioPeakTool:
    _instance: Optional["AudioPeakTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def peak(self, signal: List[float]) -> Tuple[float, int]:
        if not signal:
            return (0.0, -1)
        peak_val = max(abs(s) for s in signal)
        peak_idx = next((i for i, s in enumerate(signal) if abs(s) == peak_val), -1)
        return (peak_val, peak_idx)

    def peaks(self, signal: List[float], threshold: float = 0.8) -> List[Tuple[float, int]]:
        if not signal:
            return []
        peak_val, _ = self.peak(signal)
        threshold_val = peak_val * threshold
        return [(signal[i], i) for i in range(len(signal)) if abs(signal[i]) >= threshold_val]


def get_audio_peak_tool() -> AudioPeakTool:
    return AudioPeakTool()