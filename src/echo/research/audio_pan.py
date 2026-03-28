"""音频声像工具"""

import math
from typing import List, Optional


class AudioPanTool:
    _instance: Optional["AudioPanTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def pan(self, signal: List[float], pan: float) -> tuple[List[float], List[float]]:
        if not signal:
            return [], []
        pan = max(-1.0, min(1.0, pan))
        left_gain = math.cos((pan + 1.0) * math.pi / 4.0)
        right_gain = math.sin((pan + 1.0) * math.pi / 4.0)
        left = [s * left_gain for s in signal]
        right = [s * right_gain for s in signal]
        return left, right


def get_audio_pan_tool() -> AudioPanTool:
    return AudioPanTool()