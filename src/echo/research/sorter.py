"""排序工具"""

from typing import Optional, Callable


class Sorter:
    """排序工具"""

    def sort_by_key(self, items: list, key: str, reverse: bool = False) -> list:
        """按键排序"""
        return sorted(items, key=lambda x: x.get(key, '') if isinstance(x, dict) else getattr(x, key, ''), reverse=reverse)

    def sort_naturally(self, items: list) -> list:
        """自然排序"""
        import re
        def natural_key(s):
            return [int(c) if c.isdigit() else c.lower() for c in re.split(r'(\d+)', str(s))]
        return sorted(items, key=natural_key)


_sorter: Optional[Sorter] = None


def get_sorter() -> Sorter:
    global _sorter
    if _sorter is None:
        _sorter = Sorter()
    return _sorter