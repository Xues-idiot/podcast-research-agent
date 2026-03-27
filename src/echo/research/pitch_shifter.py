"""音高变换工具"""

from typing import List, Optional


class PitchShifter:
    _instance: Optional["PitchShifter"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def shift(self, signal: List[float], semitones: int) -> List[float]:
        factor = 2 ** (semitones / 12.0)
        from echo.research.resampler import get_resampler
        resampler = get_resampler()
        if semitones > 0:
            return resampler.downsample(signal, int(factor))
        return resampler.upsample(signal, int(1 / factor))


def get_pitch_shifter() -> PitchShifter:
    return PitchShifter()
