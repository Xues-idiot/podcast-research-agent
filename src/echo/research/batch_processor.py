"""批处理工具"""

from typing import Callable, Any, Optional
from concurrent.futures import ThreadPoolExecutor
from typing import Optional


class BatchProcessor:
    """批处理工具"""

    def batch_process(self, items: list, func: Callable, batch_size: int = 10) -> list:
        """批量处理"""
        results = []
        for i in range(0, len(items), batch_size):
            batch = items[i:i+batch_size]
            results.extend(func(batch))
        return results

    def parallel_process(self, items: list, func: Callable, max_workers: int = 4) -> list:
        """并行处理"""
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            return list(executor.map(func, items))


_processor: Optional[BatchProcessor] = None


def get_batch_processor() -> BatchProcessor:
    global _processor
    if _processor is None:
        _processor = BatchProcessor()
    return _processor