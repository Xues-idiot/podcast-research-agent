"""观察者模式"""

from typing import Optional, Callable, List


class Observer:
    """观察者"""

    def __init__(self):
        self._callbacks: List[Callable] = []

    def attach(self, callback: Callable) -> None:
        """附加观察者"""
        self._callbacks.append(callback)

    def notify(self, *args, **kwargs) -> None:
        """通知观察者"""
        for callback in self._callbacks:
            callback(*args, **kwargs)


_observer: Optional[Observer] = None


def get_observer() -> Observer:
    global _observer
    if _observer is None:
        _observer = Observer()
    return _observer