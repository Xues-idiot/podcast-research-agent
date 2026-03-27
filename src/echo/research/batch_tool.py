"""批处理工具"""

from typing import Optional, List, Any


class BatchTool:
    """批处理工具"""

    def batch(self, items: List[Any], size: int) -> List[List[Any]]:
        """批处理"""
        return [items[i:i+size] for i in range(0, len(items), size)]


_batch_tool: Optional[BatchTool] = None


def get_batch_tool() -> BatchTool:
    global _batch_tool
    if _batch_tool is None:
        _batch_tool = BatchTool()
    return _batch_tool