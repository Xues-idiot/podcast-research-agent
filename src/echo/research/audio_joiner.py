"""音频拼接工具"""

from typing import List, Optional


class AudioJoiner:
    _instance: Optional["AudioJoiner"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def join(self, *signals: List[float], crossfade_ms: int = 0, sample_rate: float = 44100) -> List[float]:
        if not signals:
            return []
        result = list(signals[0])
        for signal in signals[1:]:
            result.extend(signal)
        return result


def get_audio_joiner() -> AudioJoiner:
    return AudioJoiner()
