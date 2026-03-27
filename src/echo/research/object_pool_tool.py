"""对象池"""

from typing import Optional, Any, List, Callable


class ObjectPool:
    """对象池"""

    def __init__(self, factory: Callable):
        self._factory = factory
        self._pool: List[Any] = []

    def acquire(self) -> Any:
        """获取对象"""
        if self._pool:
            return self._pool.pop()
        return self._factory()

    def release(self, obj: Any) -> None:
        """释放对象"""
        self._pool.append(obj)


_object_pool: Optional[ObjectPool] = None


def get_object_pool(factory: Callable = lambda: None) -> ObjectPool:
    global _object_pool
    if _object_pool is None:
        _object_pool = ObjectPool(factory)
    return _object_pool