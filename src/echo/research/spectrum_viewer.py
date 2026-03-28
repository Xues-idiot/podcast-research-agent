"""频谱查看器"""

from typing import List, Optional


class SpectrumViewer:
    _instance: Optional["SpectrumViewer"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def view(self, spectrum: List[float]) -> str:
        return f"Spectrum: {len(spectrum)} bins"


def get_spectrum_viewer() -> SpectrumViewer:
    return SpectrumViewer()
