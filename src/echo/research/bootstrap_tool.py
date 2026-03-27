"""Bootstrap工具"""

import random
from typing import List, Callable, Optional


class BootstrapTool:
    _instance: Optional["BootstrapTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def bootstrap_mean(self, data: List[float], n_iterations: int = 1000) -> List[float]:
        if len(data) == 0:
            return []
        means = []
        for _ in range(n_iterations):
            sample = [random.choice(data) for _ in data]
            means.append(sum(sample) / len(sample))
        return means


def get_bootstrap_tool() -> BootstrapTool:
    return BootstrapTool()
