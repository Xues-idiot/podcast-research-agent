"""节拍同步工具"""

from typing import List, Optional


class BeatSync:
    _instance: Optional["BeatSync"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def sync_to_grid(self, signal: List[float], bpm: float, sample_rate: float = 44100) -> List[float]:
        beat_samples = int(60 * sample_rate / bpm)
        result = []
        for i in range(len(signal)):
            grid_pos = (i // beat_samples) * beat_samples
            if i == grid_pos:
                result.append(signal[i])
            else:
                result.append(0.0)
        return result


def get_beat_sync() -> BeatSync:
    return BeatSync()
