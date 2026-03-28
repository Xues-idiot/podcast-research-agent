"""音频包络工具"""

from typing import List, Optional


class AudioEnvelopeTool:
    _instance: Optional["AudioEnvelopeTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def envelope(self, signal: List[float], attack: float = 0.01, release: float = 0.1) -> List[float]:
        n = len(signal)
        if n == 0:
            return []
        attack_samples = int(attack * n)
        release_samples = int(release * n)
        result = []
        for i in range(n):
            if i < attack_samples:
                env = i / attack_samples if attack_samples > 0 else 1.0
            else:
                env = 1.0
            result.append(signal[i] * env)
        return result

    def attack_release(self, signal: List[float], attack: float, release: float, sample_rate: float = 44100) -> List[float]:
        n = len(signal)
        if n == 0:
            return []
        attack_samples = max(1, int(attack * sample_rate))
        release_samples = max(1, int(release * sample_rate))
        result = []
        for i in range(n):
            if i < attack_samples:
                env = i / attack_samples
            elif i >= n - release_samples:
                env = (n - i) / release_samples
            else:
                env = 1.0
            result.append(signal[i] * env)
        return result


def get_audio_envelope_tool() -> AudioEnvelopeTool:
    return AudioEnvelopeTool()