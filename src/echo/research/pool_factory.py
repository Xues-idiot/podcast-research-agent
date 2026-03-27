"""对象池工具"""

from typing import Callable, Dict, Optional, Any


class PoolFactory:
    _instance: Optional["PoolFactory"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._pools: Dict[str, Any] = {}

    def get_pool(self, name: str, factory: Callable, max_size: int = 10) -> List[Any]:
        if name not in self._pools:
            self._pools[name] = {
                "items": [factory() for _ in range(max_size)],
                "factory": factory
            }
        return self._pools[name]["items"]


def get_pool_factory() -> PoolFactory:
    return PoolFactory()
