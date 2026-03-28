"""节拍网格工具"""

from typing import List, Optional


class BeatGrid:
    _instance: Optional["BeatGrid"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def create_grid(self, bpm: float, duration_ms: int, sample_rate: float = 44100) -> List[int]:
        beat_duration_ms = 60000 / bpm
        grid = []
        t = 0
        while t < duration_ms:
            grid.append(int(t * sample_rate / 1000))
            t += beat_duration_ms
        return grid


def get_beat_grid() -> BeatGrid:
    return BeatGrid()
