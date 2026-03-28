"""音频频谱分析工具"""

import math
from typing import List, Optional


class AudioSpectrumTool:
    _instance: Optional["AudioSpectrumTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def spectrum(self, signal: List[float]) -> List[float]:
        if not signal:
            return []
        n = len(signal)
        spectrum = []
        for k in range(n // 2):
            real = 0.0
            imag = 0.0
            for i in range(n):
                angle = 2 * math.pi * k * i / n
                real += signal[i] * math.cos(angle)
                imag -= signal[i] * math.sin(angle)
            spectrum.append(math.sqrt(real * real + imag * imag) / n)
        return spectrum


def get_audio_spectrum_tool() -> AudioSpectrumTool:
    return AudioSpectrumTool()