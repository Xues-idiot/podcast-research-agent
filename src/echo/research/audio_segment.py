"""音频分段工具"""

from typing import List, Optional


class AudioSegment:
    _instance: Optional["AudioSegment"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def segment_by_silence(self, signal: List[float], threshold: float = 0.01) -> List[List[float]]:
        segments = []
        current = []
        for sample in signal:
            if abs(sample) > threshold:
                current.append(sample)
            elif current:
                segments.append(current)
                current = []
        if current:
            segments.append(current)
        return segments


def get_audio_segment() -> AudioSegment:
    return AudioSegment()
