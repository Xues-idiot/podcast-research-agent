"""模糊工具"""

from typing import List, Optional


class BlurTool:
    _instance: Optional["BlurTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def blur(self, signal: List[float], radius: int = 2) -> List[float]:
        result = []
        for i in range(len(signal)):
            total = 0.0
            count = 0
            for j in range(max(0, i - radius), min(len(signal), i + radius + 1)):
                total += signal[j]
                count += 1
            result.append(total / count if count > 0 else 0)
        return result


def get_blur_tool() -> BlurTool:
    return BlurTool()
