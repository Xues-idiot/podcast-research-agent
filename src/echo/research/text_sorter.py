"""文本排序工具"""

from typing import Optional, Callable


class TextSorter:
    """文本排序工具"""

    def sort_lines(self, lines: list[str], reverse: bool = False) -> list[str]:
        """排序行"""
        return sorted(lines, reverse=reverse)

    def sort_by_length(self, lines: list[str], reverse: bool = False) -> list[str]:
        """按长度排序"""
        return sorted(lines, key=len, reverse=reverse)

    def sort_alphanumeric(self, lines: list[str], reverse: bool = False) -> list[str]:
        """字母数字排序"""
        import re
        def natural_key(s):
            return [int(c) if c.isdigit() else c.lower() for c in re.split(r'(\d+)', s)]
        return sorted(lines, key=natural_key, reverse=reverse)

    def sort_by_occurrence(self, items: list[str]) -> list[tuple[str, int]]:
        """按出现频率排序"""
        from collections import Counter
        counter = Counter(items)
        return counter.most_common()


_sorter: Optional[TextSorter] = None


def get_text_sorter() -> TextSorter:
    global _sorter
    if _sorter is None:
        _sorter = TextSorter()
    return _sorter