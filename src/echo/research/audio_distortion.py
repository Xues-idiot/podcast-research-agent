"""音频失真效果工具"""

from typing import List, Optional


class AudioDistortionTool:
    _instance: Optional["AudioDistortionTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def distort(self, signal: List[float], drive: float = 0.5, mix: float = 0.5) -> List[float]:
        if not signal:
            return []
        drive = max(0.0, min(1.0, drive))
        threshold = 1.0 - drive * 0.99
        result = []
        for s in signal:
            distorted = s
            if abs(s) > threshold:
                distorted = threshold if s > 0 else -threshold
            result.append(distorted)
        return [signal[i] * (1 - mix) + result[i] * mix for i in range(len(signal))]


def get_audio_distortion_tool() -> AudioDistortionTool:
    return AudioDistortionTool()