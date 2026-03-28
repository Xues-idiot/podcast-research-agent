"""共振峰检测工具"""

from typing import List, Optional


class FormantDetect:
    _instance: Optional["FormantDetect"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def detect_formants(self, spectrum: List[float], sample_rate: float = 44100) -> List[float]:
        n = len(spectrum)
        formants = []
        for i in range(n // 2):
            freq = i * sample_rate / (2 * n)
            if 200 < freq < 4000 and spectrum[i] > 0.1:
                formants.append(freq)
        return formants[:5]


def get_formant_detect() -> FormantDetect:
    return FormantDetect()
