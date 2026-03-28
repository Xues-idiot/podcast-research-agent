"""频谱带宽工具"""

from typing import List, Optional


class SpectralBandwidth:
    _instance: Optional["SpectralBandwidth"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def compute(self, spectrum: List[float], sample_rate: float = 44100, centroid: float = 0) -> float:
        n = len(spectrum)
        if centroid == 0:
            total = sum(spectrum)
            if total == 0:
                return 0.0
            centroid = sum(i * sample_rate / (2 * n) * spectrum[i] for i in range(n)) / total
        bandwidth = 0.0
        total = sum(spectrum)
        if total == 0:
            return 0.0
        for i in range(n):
            freq = i * sample_rate / (2 * n)
            bandwidth += abs(freq - centroid) * spectrum[i]
        return bandwidth / total


def get_spectral_bandwidth() -> SpectralBandwidth:
    return SpectralBandwidth()
