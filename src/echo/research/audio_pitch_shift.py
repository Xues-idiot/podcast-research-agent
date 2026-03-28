"""音频音高变换工具"""

from typing import List, Optional


class AudioPitchShiftTool:
    _instance: Optional["AudioPitchShiftTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def pitch_shift(self, signal: List[float], semitones: float = 0.0) -> List[float]:
        if not signal or semitones == 0:
            return signal
        factor = 2.0 ** (semitones / 12.0)
        n = len(signal)
        result = []
        for i in range(int(n / factor)):
            src_idx = int(i * factor)
            if src_idx < n:
                result.append(signal[src_idx])
        while len(result) < n:
            result.append(0.0)
        return result[:n]


def get_audio_pitch_shift_tool() -> AudioPitchShiftTool:
    return AudioPitchShiftTool()