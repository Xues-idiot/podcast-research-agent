"""音频噪声门工具"""

from typing import List, Optional


class AudioGateTool:
    _instance: Optional["AudioGateTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def gate(self, signal: List[float], threshold: float = 0.1) -> List[float]:
        if not signal:
            return []
        threshold = max(0.0, min(1.0, threshold))
        return [s if abs(s) > threshold else 0.0 for s in signal]


def get_audio_gate_tool() -> AudioGateTool:
    return AudioGateTool()