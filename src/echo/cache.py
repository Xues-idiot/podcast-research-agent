"""缓存模块 - 简单的文件缓存"""

import hashlib
import json
from pathlib import Path
from typing import Any, Optional


class Cache:
    """
    简单文件缓存

    用于缓存研究结果，避免重复处理
    """

    def __init__(self, cache_dir: str = ".cache"):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _get_key(self, url: str) -> str:
        """将URL转换为缓存key"""
        return hashlib.md5(url.encode()).hexdigest()

    def _get_path(self, key: str) -> Path:
        """获取缓存文件路径"""
        return self.cache_dir / f"{key}.json"

    def get(self, url: str) -> Optional[dict]:
        """
        获取缓存

        Args:
            url: 原始URL

        Returns:
            缓存的数据，如果不存在则返回None
        """
        key = self._get_key(url)
        path = self._get_path(key)

        if not path.exists():
            return None

        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return None

    def set(self, url: str, data: dict):
        """
        设置缓存

        Args:
            url: 原始URL
            data: 要缓存的数据
        """
        key = self._get_key(url)
        path = self._get_path(key)

        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except IOError:
            pass

    def delete(self, url: str):
        """
        删除缓存

        Args:
            url: 原始URL
        """
        key = self._get_key(url)
        path = self._get_path(key)

        if path.exists():
            path.unlink()

    def clear(self):
        """清空所有缓存"""
        for path in self.cache_dir.glob("*.json"):
            path.unlink()

    def exists(self, url: str) -> bool:
        """
        检查缓存是否存在

        Args:
            url: 原始URL

        Returns:
            是否存在缓存
        """
        key = self._get_key(url)
        path = self._get_path(key)
        return path.exists()


# 全局缓存实例
_default_cache: Optional[Cache] = None


def get_cache() -> Cache:
    """获取全局缓存实例"""
    global _default_cache
    if _default_cache is None:
        _default_cache = Cache()
    return _default_cache
