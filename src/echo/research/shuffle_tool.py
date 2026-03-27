"""打乱工具"""

from typing import Optional, List, Any
import random


class ShuffleTool:
    """打乱工具"""

    def shuffle(self, items: List[Any]) -> List[Any]:
        """打乱顺序"""
        result = list(items)
        random.shuffle(result)
        return result


_shuffle_tool: Optional[ShuffleTool] = None


def get_shuffle_tool() -> ShuffleTool:
    global _shuffle_tool
    if _shuffle_tool is None:
        _shuffle_tool = ShuffleTool()
    return _shuffle_tool