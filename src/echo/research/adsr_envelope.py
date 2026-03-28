"""ADSR包络工具"""

from typing import List, Optional


class AdsrEnvelope:
    _instance: Optional["AdsrEnvelope"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def generate(self, total_samples: int, attack: float, decay: float, sustain: float, release: float) -> List[float]:
        a = int(total_samples * attack)
        d = int(total_samples * decay)
        r = int(total_samples * release)
        s = max(0, total_samples - a - d - r)
        env = []
        for i in range(a):
            env.append(i / a if a > 0 else 1)
        for i in range(d):
            env.append(1 - (1 - sustain) * (i / d) if d > 0 else sustain)
        for i in range(s):
            env.append(sustain)
        for i in range(r):
            env.append(sustain * (1 - i / r) if r > 0 else 0)
        return env


def get_adsr_envelope() -> AdsrEnvelope:
    return AdsrEnvelope()
