"""音频延迟效果工具"""

from typing import List, Optional


class AudioDelayTool:
    _instance: Optional["AudioDelayTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def delay(self, signal: List[float], delay_ms: float = 250.0, feedback: float = 0.3, mix: float = 0.5) -> List[float]:
        if not signal:
            return []
        delay_samples = int(delay_ms * len(signal) / 1000.0)
        result = signal[:]
        for iteration in range(4):
            for i in range(len(signal)):
                idx = i - delay_samples * (iteration + 1)
                if idx >= 0 and idx < len(signal):
                    result[i] += signal[idx] * (feedback ** (iteration + 1))
        return [signal[i] * (1 - mix) + result[i] * mix for i in range(len(signal))]


def get_audio_delay_tool() -> AudioDelayTool:
    return AudioDelayTool()