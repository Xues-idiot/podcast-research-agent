"""音频分割工具"""

from typing import List, Optional, Tuple


class AudioSplitter:
    _instance: Optional["AudioSplitter"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def split(self, signal: List[float], segment_length: int) -> List[List[float]]:
        return [signal[i:i + segment_length] for i in range(0, len(signal), segment_length)]


def get_audio_splitter() -> AudioSplitter:
    return AudioSplitter()
