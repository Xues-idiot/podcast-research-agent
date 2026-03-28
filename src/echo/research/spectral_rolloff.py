"""频谱滚降点工具"""

from typing import Optional


class SpectralRolloff:
    _instance: Optional["SpectralRolloff"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def compute(self, spectrum: List[float], sample_rate: float = 44100, rolloff_percent: float = 0.85) -> float:
        total_energy = sum(spectrum)
        if total_energy == 0:
            return 0.0
        threshold = total_energy * rolloff_percent
        cumulative = 0.0
        n = len(spectrum)
        for i in range(n):
            freq = i * sample_rate / (2 * n)
            cumulative += spectrum[i]
            if cumulative >= threshold:
                return freq
        return sample_rate / 2


def get_spectral_rolloff() -> SpectralRolloff:
    return SpectralRolloff()
