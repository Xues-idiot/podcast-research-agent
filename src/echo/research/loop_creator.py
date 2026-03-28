"""循环创建工具"""

from typing import List, Optional


class LoopCreator:
    _instance: Optional["LoopCreator"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def create_loop(self, signal: List[float], num_times: int) -> List[float]:
        return signal * num_times


def get_loop_creator() -> LoopCreator:
    return LoopCreator()
