"""波形查看器"""

from typing import List, Optional


class WaveformViewer:
    _instance: Optional["WaveformViewer"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def view(self, signal: List[float]) -> str:
        return f"Waveform: {len(signal)} samples"


def get_waveform_viewer() -> WaveformViewer:
    return WaveformViewer()
