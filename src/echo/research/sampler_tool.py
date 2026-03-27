"""采样工具"""

import random
from typing import Optional, Any


class SamplerTool:
    """采样工具"""

    def sample(self, items: list, count: int) -> list:
        """采样"""
        return random.sample(items, min(count, len(items)))


_sampler: Optional[SamplerTool] = None


def get_sampler_tool() -> SamplerTool:
    global _sampler
    if _sampler is None:
        _sampler = SamplerTool()
    return _sampler