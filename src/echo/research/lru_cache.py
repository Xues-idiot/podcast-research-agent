"""LRU缓存"""

from collections import OrderedDict
from typing import Optional, Any


class LRUCache:
    """LRU缓存"""

    def __init__(self, max_size: int = 100):
        self._cache = OrderedDict()
        self._max_size = max_size

    def get(self, key: str) -> Any:
        """获取"""
        if key not in self._cache:
            return None
        self._cache.move_to_end(key)
        return self._cache[key]

    def set(self, key: str, value: Any):
        """设置"""
        if key in self._cache:
            self._cache.move_to_end(key)
        self._cache[key] = value
        if len(self._cache) > self._max_size:
            self._cache.popitem(last=False)


_cache: Optional[LRUCache] = None


def get_lru_cache(max_size: int = 100) -> LRUCache:
    global _cache
    if _cache is None:
        _cache = LRUCache(max_size)
    return _cache