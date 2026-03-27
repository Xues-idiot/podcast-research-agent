"""打乱工具"""

import random
from typing import Optional, Any


class ShufflerTool:
    """打乱工具"""

    def shuffle(self, items: list) -> list:
        """打乱"""
        result = items.copy()
        random.shuffle(result)
        return result


_shuffler: Optional[ShufflerTool] = None


def get_shuffler_tool() -> ShufflerTool:
    global _shuffler
    if _shuffler is None:
        _shuffler = ShufflerTool()
    return _shuffler