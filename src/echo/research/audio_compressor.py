"""音频压缩器工具"""

from typing import List, Optional


class AudioCompressorTool:
    _instance: Optional["AudioCompressorTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def compress(self, signal: List[float], threshold: float = 0.5, ratio: float = 4.0, makeup_gain: float = 1.0) -> List[float]:
        if not signal:
            return []
        result = []
        for s in signal:
            abs_val = abs(s)
            if abs_val > threshold:
                compressed = threshold + (abs_val - threshold) / ratio
                s = compressed * (1 if s > 0 else -1)
            result.append(s * makeup_gain)
        return result


def get_audio_compressor_tool() -> AudioCompressorTool:
    return AudioCompressorTool()