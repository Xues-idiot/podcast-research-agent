"""归一化工具"""

from typing import List, Optional


class Normalizer:
    _instance: Optional["Normalizer"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def normalize(self, data: List[float]) -> Optional[List[float]]:
        if not data:
            return None
        min_val = min(data)
        max_val = max(data)
        if max_val == min_val:
            return [0.5] * len(data)
        return [(x - min_val) / (max_val - min_val) for x in data]


def get_normalizer() -> Normalizer:
    return Normalizer()
