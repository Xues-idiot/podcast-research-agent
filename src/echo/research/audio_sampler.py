"""音频采样工具"""

from typing import List, Optional


class AudioSamplerTool:
    _instance: Optional["AudioSamplerTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def sample(self, signal: List[float], rate: float = 1.0) -> List[float]:
        if not signal or rate <= 0:
            return []
        n = len(signal)
        result_len = int(n / rate)
        if result_len == 0:
            return []
        step = n / result_len
        result = []
        for i in range(result_len):
            idx = int(i * step)
            if idx < n:
                result.append(signal[idx])
        return result


def get_audio_sampler_tool() -> AudioSamplerTool:
    return AudioSamplerTool()