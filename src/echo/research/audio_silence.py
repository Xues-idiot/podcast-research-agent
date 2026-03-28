"""音频静音检测工具"""

from typing import List, Optional, Tuple


class AudioSilenceTool:
    _instance: Optional["AudioSilenceTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def detect_silence(self, signal: List[float], threshold: float = 0.01) -> List[Tuple[int, int]]:
        if not signal:
            return []
        silent_ranges = []
        in_silence = False
        start = 0
        for i, s in enumerate(signal):
            is_silent = abs(s) < threshold
            if is_silent and not in_silence:
                start = i
                in_silence = True
            elif not is_silent and in_silence:
                silent_ranges.append((start, i))
                in_silence = False
        if in_silence:
            silent_ranges.append((start, len(signal)))
        return silent_ranges


def get_audio_silence_tool() -> AudioSilenceTool:
    return AudioSilenceTool()