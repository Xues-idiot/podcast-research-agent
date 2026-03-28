"""频谱质心工具"""

from typing import List, Optional


class SpectralCentroid:
    _instance: Optional["SpectralCentroid"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def compute(self, spectrum: List[float], sample_rate: float = 44100) -> float:
        n = len(spectrum)
        weighted_sum = 0.0
        magnitude_sum = 0.0
        for i in range(n):
            freq = i * sample_rate / (2 * n)
            magnitude_sum += spectrum[i]
            weighted_sum += freq * spectrum[i]
        return weighted_sum / magnitude_sum if magnitude_sum > 0 else 0.0


def get_spectral_centroid() -> SpectralCentroid:
    return SpectralCentroid()
