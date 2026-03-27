"""对象池"""

from typing import Optional, Any, List


class ObjectPool:
    """对象池"""

    def __init__(self, factory: callable):
        self._factory = factory
        self._pool: List[Any] = []

    def acquire(self) -> Any:
        """获取对象"""
        if self._pool:
            return self._pool.pop()
        return self._factory()

    def release(self, obj: Any):
        """归还对象"""
        self._pool.append(obj)

    def clear(self):
        """清空池"""
        self._pool.clear()


_pools = {}


def get_object_pool(name: str, factory: callable) -> ObjectPool:
    """获取对象池"""
    if name not in _pools:
        _pools[name] = ObjectPool(factory)
    return _pools[name]