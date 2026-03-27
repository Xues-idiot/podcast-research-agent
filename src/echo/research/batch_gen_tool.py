"""批处理生成工具"""

from typing import Optional, List, Any, Callable


class BatchGenTool:
    """批处理生成工具"""

    def batch(self, items: List[Any], size: int) -> List[List[Any]]:
        """分批处理"""
        return [items[i:i+size] for i in range(0, len(items), size)]


_batch_gen_tool: Optional[BatchGenTool] = None


def get_batch_gen_tool() -> BatchGenTool:
    global _batch_gen_tool
    if _batch_gen_tool is None:
        _batch_gen_tool = BatchGenTool()
    return _batch_gen_tool