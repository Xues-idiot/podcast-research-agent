"""音频压缩器"""

from typing import Optional


class AudioCompressor:
    _instance: Optional["AudioCompressor"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def compress(self, signal: list[float], threshold: float = 0.5, ratio: float = 4.0) -> list[float]:
        result = []
        for sample in signal:
            if abs(sample) > threshold:
                sign = 1 if sample > 0 else -1
                excess = abs(sample) - threshold
                compressed_excess = excess / ratio
                result.append(sign * (threshold + compressed_excess))
            else:
                result.append(sample)
        return result


def get_audio_compressor() -> AudioCompressor:
    return AudioCompressor()
