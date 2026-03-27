"""缓存工具"""

import time
from typing import Optional, Any


class CacheManager:
    """简单缓存管理器"""

    def __init__(self):
        self._cache = {}
        self._ttl = {}

    def set(self, key: str, value: Any, ttl: int = 300):
        """设置缓存"""
        self._cache[key] = value
        self._ttl[key] = time.time() + ttl

    def get(self, key: str, default: Any = None) -> Any:
        """获取缓存"""
        if key not in self._cache:
            return default
        if key in self._ttl and time.time() > self._ttl[key]:
            del self._cache[key]
            del self._ttl[key]
            return default
        return self._cache[key]

    def delete(self, key: str):
        """删除缓存"""
        if key in self._cache:
            del self._cache[key]
        if key in self._ttl:
            del self._ttl[key]

    def clear(self):
        """清空缓存"""
        self._cache.clear()
        self._ttl.clear()


_cache: Optional[CacheManager] = None


def get_cache_manager() -> CacheManager:
    global _cache
    if _cache is None:
        _cache = CacheManager()
    return _cache