"""音阶生成器"""

from typing import List, Optional


class ScaleGenerator:
    _instance: Optional["ScaleGenerator"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def generate_scale(self, root: float, scale_type: str, octaves: int = 1) -> List[float]:
        intervals = {
            "major": [0, 2, 4, 5, 7, 9, 11],
            "minor": [0, 2, 3, 5, 7, 8, 10],
            "harmonic_minor": [0, 2, 3, 5, 7, 8, 11],
            "pentatonic_major": [0, 2, 4, 7, 9],
            "pentatonic_minor": [0, 3, 5, 7, 10]
        }
        scale = intervals.get(scale_type, [0, 2, 4, 5, 7, 9, 11])
        result = []
        for octave in range(octaves):
            for interval in scale:
                freq = root * (2 ** ((octave * 12 + interval) / 12))
                result.append(freq)
        return result


def get_scale_generator() -> ScaleGenerator:
    return ScaleGenerator()
