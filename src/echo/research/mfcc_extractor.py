"""MFCC特征提取器"""

from typing import List, Optional
import math


class MfccExtractor:
    _instance: Optional["MfccExtractor"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def extract(self, spectrum: List[float], n_mfcc: int = 13) -> List[float]:
        n = len(spectrum)
        mfcc = [0.0] * n_mfcc
        for k in range(n_mfcc):
            for n_bin in range(n):
                mfcc[k] += spectrum[n_bin] * math.cos(math.pi * k * (n_bin + 0.5) / n)
        return mfcc


def get_mfcc_extractor() -> MfccExtractor:
    return MfccExtractor()
