"""批处理制造工具"""

from typing import Optional, List, Any


class BatchMaker:
    """批处理制造工具"""

    def make_batch(self, items: List[Any], size: int) -> List[List[Any]]:
        """制造批处理"""
        return [items[i:i+size] for i in range(0, len(items), size)]


_batch_maker: Optional[BatchMaker] = None


def get_batch_maker() -> BatchMaker:
    global _batch_maker
    if _batch_maker is None:
        _batch_maker = BatchMaker()
    return _batch_maker