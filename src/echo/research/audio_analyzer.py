"""音频分析器"""

from typing import List, Optional, Dict


class AudioAnalyzer:
    _instance: Optional["AudioAnalyzer"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def analyze(self, signal: List[float]) -> Dict[str, float]:
        if not signal:
            return {"rms": 0, "peak": 0, "crest": 0}
        rms = (sum(s ** 2 for s in signal) / len(signal)) ** 0.5
        peak = max(abs(s) for s in signal)
        crest = peak / rms if rms > 0 else 0
        return {"rms": rms, "peak": peak, "crest": crest}


def get_audio_analyzer() -> AudioAnalyzer:
    return AudioAnalyzer()
