"""电平表工具"""

from typing import List, Optional


class MeteringTool:
    _instance: Optional["MeteringTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def measure(self, signal: List[float]) -> dict:
        if not signal:
            return {"peak": 0, "rms": 0}
        import math
        peak = max(abs(s) for s in signal)
        rms = math.sqrt(sum(s ** 2 for s in signal) / len(signal))
        return {"peak": peak, "rms": rms}

    import math


def get_metering_tool() -> MeteringTool:
    return MeteringTool()
