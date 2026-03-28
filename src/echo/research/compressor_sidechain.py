"""侧链压缩器"""

from typing import List, Optional


class SidechainCompressor:
    _instance: Optional["SidechainCompressor"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def compress(self, signal: List[float], sidechain: List[float], threshold: float = 0.5, ratio: float = 4.0) -> List[float]:
        result = []
        for i in range(min(len(signal), len(sidechain))):
            if abs(sidechain[i]) > threshold:
                factor = threshold + (abs(sidechain[i]) - threshold) / ratio
                result.append(signal[i] * factor / abs(sidechain[i]) if abs(sidechain[i]) > 0 else signal[i])
            else:
                result.append(signal[i])
        return result


def get_sidechain_compressor() -> SidechainCompressor:
    return SidechainCompressor()
