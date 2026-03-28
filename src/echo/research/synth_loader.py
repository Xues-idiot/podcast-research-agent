"""合成器加载器"""

from typing import List, Optional, Dict


class SynthLoader:
    _instance: Optional["SynthLoader"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.synths: Dict[str, List[float]] = {}

    def register(self, name: str, data: List[float]) -> None:
        self.synths[name] = data

    def get(self, name: str) -> List[float]:
        return self.synths.get(name, [])


def get_synth_loader() -> SynthLoader:
    return SynthLoader()
