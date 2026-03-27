"""事件总线"""

from typing import Callable, Dict, List, Optional


class EventBus:
    """事件总线"""

    def __init__(self):
        self._handlers: Dict[str, List[Callable]] = {}

    def subscribe(self, event: str, handler: Callable):
        """订阅事件"""
        if event not in self._handlers:
            self._handlers[event] = []
        self._handlers[event].append(handler)

    def publish(self, event: str, *args, **kwargs):
        """发布事件"""
        if event in self._handlers:
            for handler in self._handlers[event]:
                handler(*args, **kwargs)

    def unsubscribe(self, event: str, handler: Callable):
        """取消订阅"""
        if event in self._handlers:
            self._handlers[event].remove(handler)


_bus: Optional[EventBus] = None


def get_event_bus() -> EventBus:
    global _bus
    if _bus is None:
        _bus = EventBus()
    return _bus