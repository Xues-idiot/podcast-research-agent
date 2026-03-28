"""色度特征工具"""

from typing import List, Optional


class ChromaFeatures:
    _instance: Optional["ChromaFeatures"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def compute(self, spectrum: List[float], sample_rate: float = 44100) -> List[float]:
        n = len(spectrum)
        chroma = [0.0] * 12
        for i in range(n):
            freq = i * sample_rate / (2 * n)
            if freq > 0:
                note = int(round(12 * (freq / 440.0) ** (1 / 12))) % 12
                chroma[note] += spectrum[i]
        return chroma


def get_chroma_features() -> ChromaFeatures:
    return ChromaFeatures()
