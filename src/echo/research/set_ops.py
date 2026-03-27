"""集合操作工具"""

from typing import Optional, Any


class SetOps:
    """集合操作工具"""

    def union(self, set1: set, set2: set) -> set:
        """并集"""
        return set1 | set2

    def intersection(self, set1: set, set2: set) -> set:
        """交集"""
        return set1 & set2

    def difference(self, set1: set, set2: set) -> set:
        """差集"""
        return set1 - set2


_ops: Optional[SetOps] = None


def get_set_ops() -> SetOps:
    global _ops
    if _ops is None:
        _ops = SetOps()
    return _ops