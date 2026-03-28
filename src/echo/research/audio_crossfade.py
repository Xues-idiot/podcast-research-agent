"""音频交叉淡入淡出工具"""

from typing import List, Optional


class AudioCrossfadeTool:
    _instance: Optional["AudioCrossfadeTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def crossfade(self, a: List[float], b: List[float], fade_points: int = 1000) -> List[float]:
        if not a or not b:
            return a or b
        fade_points = max(1, min(len(a), fade_points))
        result = a[:]
        for i in range(fade_points):
            t = i / fade_points
            idx = len(a) - fade_points + i
            if idx < len(result):
                result[idx] = a[idx] * (1 - t) + b[i] * t
        for i in range(fade_points, len(b)):
            idx = len(a) - fade_points + i
            if idx < len(result):
                result[idx] = b[i]
        return result


def get_audio_crossfade_tool() -> AudioCrossfadeTool:
    return AudioCrossfadeTool()