"""观察者模式"""

from typing import List, Optional


class Observer:
    """观察者基类"""

    def update(self, message: str):
        raise NotImplementedError


class Subject:
    """主题"""

    def __init__(self):
        self._observers: List[Observer] = []

    def attach(self, observer: Observer):
        """添加观察者"""
        self._observers.append(observer)

    def detach(self, observer: Observer):
        """移除观察者"""
        self._observers.remove(observer)

    def notify(self, message: str):
        """通知观察者"""
        for observer in self._observers:
            observer.update(message)