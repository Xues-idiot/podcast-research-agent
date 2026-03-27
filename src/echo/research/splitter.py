"""分割工具"""

from typing import Optional


class Splitter:
    """分割工具"""

    def split_once(self, text: str, delimiter: str) -> tuple:
        """只分割一次"""
        parts = text.split(delimiter, 1)
        if len(parts) == 1:
            return (parts[0], '')
        return (parts[0], parts[1])

    def split_lines(self, text: str, strip: bool = True) -> list:
        """分割行"""
        lines = text.split('\n')
        if strip:
            lines = [l.strip() for l in lines if l.strip()]
        return lines


_splitter: Optional[Splitter] = None


def get_splitter() -> Splitter:
    global _splitter
    if _splitter is None:
        _splitter = Splitter()
    return _splitter