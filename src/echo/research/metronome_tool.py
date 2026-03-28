"""节拍器工具"""

import math
from typing import List, Optional


class MetronomeTool:
    _instance: Optional["MetronomeTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def tick(self, bpm: float, duration_ms: int, sample_rate: float = 44100) -> List[float]:
        tick_duration = int(0.05 * sample_rate)
        interval = int(60 * sample_rate / bpm)
        result = []
        for i in range(int(duration_ms * sample_rate / 1000)):
            if i % interval < tick_duration:
                result.append(math.sin(2 * math.pi * 1000 * (i % interval) / sample_rate))
            else:
                result.append(0.0)
        return result


def get_metronome_tool() -> MetronomeTool:
    return MetronomeTool()
