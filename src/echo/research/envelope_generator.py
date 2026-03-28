"""包络生成器"""

from typing import List, Optional


class EnvelopeGenerator:
    _instance: Optional["EnvelopeGenerator"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def adsr(self, length: int, attack: float = 0.1, decay: float = 0.1, sustain: float = 0.7, release: float = 0.2) -> List[float]:
        a = int(length * attack)
        d = int(length * decay)
        r = int(length * release)
        s = length - a - d - r
        env = []
        for i in range(a):
            env.append(i / a)
        for i in range(d):
            env.append(1 - (1 - sustain) * (i / d))
        for i in range(s):
            env.append(sustain)
        for i in range(r):
            env.append(sustain * (1 - i / r))
        return env


def get_envelope_generator() -> EnvelopeGenerator:
    return EnvelopeGenerator()
