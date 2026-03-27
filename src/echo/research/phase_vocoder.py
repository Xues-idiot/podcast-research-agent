"""相位声码器"""

from typing import List, Optional


class PhaseVocoder:
    _instance: Optional["PhaseVocoder"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def phase_vocode(self, signal: List[float], stretch_factor: float) -> List[float]:
        from echo.research.resampler import get_resampler
        resampler = get_resampler()
        return resampler.upsample(signal, int(stretch_factor))


def get_phase_vocoder() -> PhaseVocoder:
    return PhaseVocoder()
