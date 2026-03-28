"""延迟效果器"""

from typing import List, Optional


class DelayEffect:
    _instance: Optional["DelayEffect"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def apply(self, signal: List[float], delay_ms: float = 200, feedback: float = 0.3, mix: float = 0.5, sample_rate: float = 44100) -> List[float]:
        delay_samples = int(delay_ms * sample_rate / 1000)
        output = list(signal)
        for i in range(len(signal)):
            if i - delay_samples >= 0:
                output[i] = signal[i] * (1 - mix) + (signal[i - delay_samples] + feedback * output[i - delay_samples]) * mix
        return output


def get_delay_effect() -> DelayEffect:
    return DelayEffect()
