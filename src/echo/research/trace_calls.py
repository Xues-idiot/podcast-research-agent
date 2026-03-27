"""跟踪调用工具"""

from typing import Callable, List, Any


class TraceCalls:
    _instance: Optional["TraceCalls"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_traces"):
            self._traces: List[str] = []

    def trace(self, name: str) -> None:
        self._traces.append(name)

    def get_traces(self) -> List[str]:
        return self._traces[:]


def get_trace_calls() -> TraceCalls:
    return TraceCalls()
