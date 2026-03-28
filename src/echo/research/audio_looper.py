"""音频循环工具"""

from typing import List, Optional


class AudioLooperTool:
    _instance: Optional["AudioLooperTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def loop(self, signal: List[float], start: int = 0, end: int = -1, count: int = 1) -> List[float]:
        if not signal:
            return []
        if end < 0 or end > len(signal):
            end = len(signal)
        if start >= end:
            return signal
        loop_chunk = signal[start:end]
        result = signal[:start]
        for _ in range(count):
            result.extend(loop_chunk)
        result.extend(signal[end:])
        return result


def get_audio_looper_tool() -> AudioLooperTool:
    return AudioLooperTool()