"""音频立体声扩展工具"""

import math
from typing import List, Optional, Tuple


class AudioStereoWidenTool:
    _instance: Optional["AudioStereoWidenTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def widen(self, left: List[float], right: List[float], amount: float = 0.5) -> Tuple[List[float], List[float]]:
        if not left or not right:
            return left, right
        amount = max(0.0, min(1.0, amount))
        mid = [(left[i] + right[i]) * 0.5 for i in range(len(left))]
        diff_l = [left[i] - mid[i] for i in range(len(left))]
        diff_r = [right[i] - mid[i] for i in range(len(right))]
        factor = 1.0 + amount
        new_l = [mid[i] + diff_l[i] * factor for i in range(len(left))]
        new_r = [mid[i] + diff_r[i] * factor for i in range(len(right))]
        return new_l, new_r


def get_audio_stereo_widen_tool() -> AudioStereoWidenTool:
    return AudioStereoWidenTool()