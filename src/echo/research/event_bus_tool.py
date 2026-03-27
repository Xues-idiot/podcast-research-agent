"""事件总线工具"""

from typing import Callable, Dict, List, Optional, Any


class EventBusTool:
    _instance: Optional["EventBusTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._listeners: Dict[str, List[Callable]] = {}

    def on(self, event: str, callback: Callable) -> None:
        if event not in self._listeners:
            self._listeners[event] = []
        self._listeners[event].append(callback)

    def emit(self, event: str, data: Any = None) -> None:
        if event in self._listeners:
            for callback in self._listeners[event]:
                callback(data)


def get_event_bus_tool() -> EventBusTool:
    return EventBusTool()
