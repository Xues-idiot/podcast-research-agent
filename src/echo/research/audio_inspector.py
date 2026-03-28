"""音频检查器"""

from typing import List, Optional


class AudioInspector:
    _instance: Optional["AudioInspector"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def inspect(self, signal: List[float]) -> dict:
        if not signal:
            return {"length": 0, "min": 0, "max": 0}
        return {
            "length": len(signal),
            "min": min(signal),
            "max": max(signal),
            "clipping": sum(1 for s in signal if abs(s) > 0.99)
        }


def get_audio_inspector() -> AudioInspector:
    return AudioInspector()
