"""行过滤器"""

from typing import Optional


class LineFilter:
    """行过滤器"""

    def filter_empty_lines(self, lines: list[str]) -> list[str]:
        """过滤空行"""
        return [l for l in lines if l.strip()]

    def filter_by_length(self, lines: list[str], min_length: int = 1, max_length: int = 10000) -> list[str]:
        """按长度过滤"""
        return [l for l in lines if min_length <= len(l) <= max_length]

    def filter_by_pattern(self, lines: list[str], pattern: str, exclude: bool = False) -> list[str]:
        """按模式过滤"""
        import re
        compiled = re.compile(pattern)
        if exclude:
            return [l for l in lines if not compiled.search(l)]
        return [l for l in lines if compiled.search(l)]

    def filter_duplicates(self, lines: list[str], preserve_order: bool = True) -> list[str]:
        """过滤重复行"""
        if preserve_order:
            seen = set()
            result = []
            for line in lines:
                if line not in seen:
                    seen.add(line)
                    result.append(line)
            return result
        return list(dict.fromkeys(lines))


_filter: Optional[LineFilter] = None


def get_line_filter() -> LineFilter:
    global _filter
    if _filter is None:
        _filter = LineFilter()
    return _filter