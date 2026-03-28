"""路径工具集合"""
import os
from pathlib import Path
from typing import List


def path_join(*parts: str) -> str:
    return os.path.join(*parts)


def path_split(path: str) -> List[str]:
    return path.split(os.sep)


def path_basename(path: str) -> str:
    return os.path.basename(path)


def path_dirname(path: str) -> str:
    return os.path.dirname(path)


def path_ext(path: str) -> str:
    return os.path.splitext(path)[1]


def path_stem(path: str) -> str:
    return os.path.splitext(path)[0]


def path_exists(path: str) -> bool:
    return os.path.exists(path)


def path_is_file(path: str) -> bool:
    return os.path.isfile(path)


def path_is_dir(path: str) -> bool:
    return os.path.isdir(path)


def path_abs(path: str) -> str:
    return os.path.abspath(path)


def path_norm(path: str) -> str:
    return os.path.normpath(path)
