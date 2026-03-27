"""采样工具"""

from typing import Optional, List, Any
import random


class SampleTool:
    """采样工具"""

    def sample(self, items: List[Any], count: int) -> List[Any]:
        """随机采样"""
        return random.sample(items, min(count, len(items)))


_sample_tool: Optional[SampleTool] = None


def get_sample_tool() -> SampleTool:
    global _sample_tool
    if _sample_tool is None:
        _sample_tool = SampleTool()
    return _sample_tool