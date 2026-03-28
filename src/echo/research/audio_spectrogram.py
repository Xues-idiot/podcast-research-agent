"""频谱图生成器"""

from typing import List, Optional


class SpectrogramGenerator:
    _instance: Optional["SpectrogramGenerator"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def generate(self, signal: List[float], window_size: int = 1024, hop_size: int = 512) -> List[List[float]]:
        n_frames = (len(signal) - window_size) // hop_size + 1
        spectrogram = []
        for i in range(n_frames):
            frame = signal[i * hop_size:i * hop_size + window_size]
            magnitudes = [abs(frame[j]) for j in range(window_size)]
            spectrogram.append(magnitudes)
        return spectrogram


def get_spectrogram_generator() -> SpectrogramGenerator:
    return SpectrogramGenerator()
