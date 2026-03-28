"""频谱通量工具"""

from typing import List, Optional


class SpectralFlux:
    _instance: Optional["SpectralFlux"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def compute(self, spectrums: List[List[float]]) -> List[float]:
        if not spectrums:
            return []
        flux = []
        for i in range(1, len(spectrums)):
            diff = sum(max(0, spectrums[i][j] - spectrums[i - 1][j]) for j in range(len(spectrums[0])))
            flux.append(diff)
        return flux


def get_spectral_flux() -> SpectralFlux:
    return SpectralFlux()
