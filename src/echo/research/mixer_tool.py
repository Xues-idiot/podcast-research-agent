"""混音工具"""

from typing import List, Optional


class MixerTool:
    _instance: Optional["MixerTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def mix(self, *signals: List[float]) -> List[float]:
        if not signals:
            return []
        max_len = max(len(s) for s in signals)
        result = [0.0] * max_len
        for signal in signals:
            for i in range(len(signal)):
                result[i] += signal[i]
        return result


def get_mixer_tool() -> MixerTool:
    return MixerTool()
