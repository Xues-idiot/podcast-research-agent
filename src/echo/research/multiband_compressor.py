"""多频段压缩器"""

from typing import List, Optional


class MultibandCompressor:
    _instance: Optional["MultibandCompressor"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def compress(self, signal: List[float], bands: int = 4, threshold: float = 0.5, ratio: float = 4.0) -> List[float]:
        return signal


def get_multiband_compressor() -> MultibandCompressor:
    return MultibandCompressor()
