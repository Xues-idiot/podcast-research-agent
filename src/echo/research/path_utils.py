"""路径工具"""

import os
from typing import Optional


class PathUtils:
    """路径工具"""

    def get_extension(self, path: str) -> str:
        """获取扩展名"""
        return os.path.splitext(path)[1].lstrip('.')

    def get_filename(self, path: str) -> str:
        """获取文件名"""
        return os.path.basename(path)

    def get_basename(self, path: str) -> str:
        """获取不含扩展名的文件名"""
        return os.path.splitext(os.path.basename(path))[0]

    def join(self, *parts: str) -> str:
        """拼接路径"""
        return os.path.join(*parts)

    def normalize(self, path: str) -> str:
        """标准化路径"""
        return os.path.normpath(path)


_utils: Optional[PathUtils] = None


def get_path_utils() -> PathUtils:
    global _utils
    if _utils is None:
        _utils = PathUtils()
    return _utils