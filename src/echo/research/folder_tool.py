"""Folder tool for folder operations"""

import os
import shutil
from typing import Any, List, Optional


class FolderTool:
    _instance: Optional["FolderTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def create(self, path: str) -> bool:
        """Create a folder"""
        try:
            os.makedirs(path, exist_ok=True)
            return True
        except Exception:
            return False

    def exists(self, path: str) -> bool:
        """Check if folder exists"""
        return os.path.isdir(path)

    def list_files(self, path: str, recursive: bool = False) -> List[str]:
        """List files in folder"""
        files = []
        if recursive:
            for root, _, filenames in os.walk(path):
                for filename in filenames:
                    files.append(os.path.join(root, filename))
        else:
            if os.path.isdir(path):
                for item in os.listdir(path):
                    full_path = os.path.join(path, item)
                    if os.path.isfile(full_path):
                        files.append(full_path)
        return files

    def list_folders(self, path: str, recursive: bool = False) -> List[str]:
        """List subfolders"""
        folders = []
        if recursive:
            for root, dirnames, _ in os.walk(path):
                for dirname in dirnames:
                    folders.append(os.path.join(root, dirname))
        else:
            if os.path.isdir(path):
                for item in os.listdir(path):
                    full_path = os.path.join(path, item)
                    if os.path.isdir(full_path):
                        folders.append(full_path)
        return folders

    def delete(self, path: str) -> bool:
        """Delete a folder"""
        try:
            if os.path.exists(path):
                shutil.rmtree(path)
                return True
            return False
        except Exception:
            return False

    def copy(self, src: str, dst: str) -> bool:
        """Copy a folder"""
        try:
            shutil.copytree(src, dst)
            return True
        except Exception:
            return False

    def move(self, src: str, dst: str) -> bool:
        """Move a folder"""
        try:
            shutil.move(src, dst)
            return True
        except Exception:
            return False

    def process(self, data: Any) -> Any:
        """Process folder data"""
        return data


def get_folder_tool() -> FolderTool:
    return FolderTool()