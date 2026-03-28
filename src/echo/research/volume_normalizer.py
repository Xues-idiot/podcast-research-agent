"""音量归一化工具"""

from typing import List, Optional


class VolumeNormalizer:
    _instance: Optional["VolumeNormalizer"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def normalize(self, signal: List[float], target_rms: float = 0.2) -> List[float]:
        if not signal:
            return signal
        current_rms = (sum(s * s for s in signal) / len(signal)) ** 0.5
        if current_rms == 0:
            return signal
        factor = target_rms / current_rms
        return [s * factor for s in signal]


def get_volume_normalizer() -> VolumeNormalizer:
    return VolumeNormalizer()
