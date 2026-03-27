"""元组操作工具"""

from typing import Optional, Any


class TupleOps:
    """元组操作工具"""

    def first(self, tuple_obj: tuple) -> Any:
        """第一个元素"""
        return tuple_obj[0] if tuple_obj else None

    def second(self, tuple_obj: tuple) -> Any:
        """第二个元素"""
        return tuple_obj[1] if len(tuple_obj) > 1 else None

    def last(self, tuple_obj: tuple) -> Any:
        """最后一个元素"""
        return tuple_obj[-1] if tuple_obj else None


_ops: Optional[TupleOps] = None


def get_tuple_ops() -> TupleOps:
    global _ops
    if _ops is None:
        _ops = TupleOps()
    return _ops