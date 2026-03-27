"""循环工具"""

from typing import Optional, List, Any


class CycleTool:
    """循环工具"""

    def cycle(self, items: List[Any], times: int) -> List[Any]:
        """循环"""
        result = []
        for _ in range(times):
            result.extend(items)
        return result


_cycle_tool: Optional[CycleTool] = None


def get_cycle_tool() -> CycleTool:
    global _cycle_tool
    if _cycle_tool is None:
        _cycle_tool = CycleTool()
    return _cycle_tool