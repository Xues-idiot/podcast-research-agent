"""享元模式工厂"""

from typing import Optional, Any


class FlyweightFactory:
    """享元工厂"""

    def __init__(self):
        self._pool = {}

    def get(self, key: str, factory: callable) -> Any:
        """获取享元对象"""
        if key not in self._pool:
            self._pool[key] = factory()
        return self._pool[key]

    def clear(self):
        """清空池"""
        self._pool.clear()


_factory: Optional[FlyweightFactory] = None


def get_flyweight_factory() -> FlyweightFactory:
    global _factory
    if _factory is None:
        _factory = FlyweightFactory()
    return _factory