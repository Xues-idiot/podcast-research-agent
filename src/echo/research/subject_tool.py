"""订阅者工具"""

from typing import Callable, List, Optional, Any


class SubjectTool:
    _instance: Optional["SubjectTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._observers: List[Callable] = []

    def subscribe(self, observer: Callable) -> None:
        self._observers.append(observer)

    def unsubscribe(self, observer: Callable) -> None:
        self._observers.remove(observer)

    def notify(self, data: Any) -> None:
        for observer in self._observers:
            observer(data)


def get_subject_tool() -> SubjectTool:
    return SubjectTool()
