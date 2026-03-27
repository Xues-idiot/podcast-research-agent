"""批处理工具"""

from typing import Optional, Callable, Any


class BatcherTool:
    """批处理工具"""

    def batch(self, items: list, size: int) -> list:
        """分批"""
        return [items[i:i+size] for i in range(0, len(items), size)]

    def process_batches(self, items: list, func: Callable, size: int) -> list:
        """处理每批"""
        results = []
        for batch in self.batch(items, size):
            results.append(func(batch))
        return results


_batcher: Optional[BatcherTool] = None


def get_batcher_tool() -> BatcherTool:
    global _batcher
    if _batcher is None:
        _batcher = BatcherTool()
    return _batcher