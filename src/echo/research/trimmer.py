"""字符串修剪工具"""

from typing import Optional


class Trimmer:
    """字符串修剪工具"""

    def trim(self, text: str) -> str:
        """去除首尾空白"""
        return text.strip()

    def trim_left(self, text: str) -> str:
        """去除左侧空白"""
        return text.lstrip()

    def trim_right(self, text: str) -> str:
        """去除右侧空白"""
        return text.rstrip()

    def trim_lines(self, text: str) -> str:
        """去除每行首尾空白"""
        return "\n".join(line.strip() for line in text.split("\n"))


_trimmer: Optional[Trimmer] = None


def get_trimmer() -> Trimmer:
    global _trimmer
    if _trimmer is None:
        _trimmer = Trimmer()
    return _trimmer