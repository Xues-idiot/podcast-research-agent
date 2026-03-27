"""享元工厂"""

from typing import Optional, Any, Dict


class FlyweightFactory:
    """享元工厂"""

    def __init__(self):
        self._flyweights: Dict[str, Any] = {}

    def get(self, key: str, factory: Callable) -> Any:
        """获取享元"""
        if key not in self._flyweights:
            self._flyweights[key] = factory()
        return self._flyweights[key]


_flyweight_factory: Optional[FlyweightFactory] = None


def get_flyweight_factory() -> FlyweightFactory:
    global _flyweight_factory
    if _flyweight_factory is None:
        _flyweight_factory = FlyweightFactory()
    return _flyweight_factory