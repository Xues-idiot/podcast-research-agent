"""积分工具"""

from typing import List, Optional


class IntegrateTool:
    _instance: Optional["IntegrateTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def integrate(self, signal: List[float], dt: float = 1.0) -> List[float]:
        result = []
        total = 0.0
        for s in signal:
            total += s * dt
            result.append(total)
        return result


def get_integrate_tool() -> IntegrateTool:
    return IntegrateTool()
