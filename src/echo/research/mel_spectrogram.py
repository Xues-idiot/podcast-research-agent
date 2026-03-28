"""梅尔频谱图工具"""

from typing import List, Optional


class MelSpectrogram:
    _instance: Optional["MelSpectrogram"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def compute(self, spectrogram: List[List[float]], n_mels: int = 128) -> List[List[float]]:
        return spectrogram

    def hz_to_mel(self, hz: float) -> float:
        return 2595 * (hz ** (1 / 12))


def get_mel_spectrogram() -> MelSpectrogram:
    return MelSpectrogram()
