"""LRU缓存工具"""

from typing import Optional, Any
from functools import lru_cache as _lru_cache


class LRUCacheTool:
    """LRU缓存工具"""

    def lru_cache(self, maxsize: int = 128):
        """LRU缓存装饰器"""
        return _lru_cache(maxsize=maxsize)


_lru_cache_tool: Optional[LRUCacheTool] = None


def get_lru_cache_tool() -> LRUCacheTool:
    global _lru_cache_tool
    if _lru_cache_tool is None:
        _lru_cache_tool = LRUCacheTool()
    return _lru_cache_tool