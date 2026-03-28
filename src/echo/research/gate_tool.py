"""门限工具"""

from typing import List, Optional


class GateTool:
    _instance: Optional["GateTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def gate(self, signal: List[float], threshold: float = 0.01) -> List[float]:
        return [0.0 if abs(s) < threshold else s for s in signal]


def get_gate_tool() -> GateTool:
    return GateTool()
