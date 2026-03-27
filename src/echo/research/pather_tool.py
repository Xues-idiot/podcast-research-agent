"""Pather tool for path manipulation"""

import os
from typing import Any, List, Optional


class PatherTool:
    _instance: Optional["PatherTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def join(self, *parts: str) -> str:
        """Join path parts"""
        return os.path.join(*parts)

    def split(self, path: str) -> List[str]:
        """Split path into parts"""
        parts = []
        while path:
            path, part = os.path.split(path)
            if part:
                parts.insert(0, part)
        return parts

    def parent(self, path: str) -> str:
        """Get parent directory"""
        return os.path.dirname(path)

    def name(self, path: str) -> str:
        """Get file/directory name"""
        return os.path.basename(path)

    def extension(self, path: str) -> str:
        """Get file extension"""
        return os.path.splitext(path)[1]

    def stem(self, path: str) -> str:
        """Get file name without extension"""
        return os.path.splitext(self.name(path))[0]

    def normalize(self, path: str) -> str:
        """Normalize path"""
        return os.path.normpath(path)

    def is_absolute(self, path: str) -> bool:
        """Check if path is absolute"""
        return os.path.isabs(path)

    def absolute(self, path: str) -> str:
        """Convert to absolute path"""
        return os.path.abspath(path)

    def relative(self, path: str, start: str) -> str:
        """Get relative path"""
        return os.path.relpath(path, start)

    def process(self, data: Any) -> Any:
        """Process path data"""
        return data


def get_pather_tool() -> PatherTool:
    return PatherTool()