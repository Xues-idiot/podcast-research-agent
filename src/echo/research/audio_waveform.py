"""音频波形工具"""

from typing import List, Optional


class AudioWaveformTool:
    _instance: Optional["AudioWaveformTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def waveform(self, signal: List[float], bins: int = 100) -> List[float]:
        if not signal or bins <= 0:
            return []
        bin_size = len(signal) // bins
        if bin_size == 0:
            return signal
        result = []
        for i in range(bins):
            start = i * bin_size
            end = start + bin_size
            chunk = signal[start:end]
            result.append(max(abs(s) for s in chunk) if chunk else 0.0)
        return result


def get_audio_waveform_tool() -> AudioWaveformTool:
    return AudioWaveformTool()