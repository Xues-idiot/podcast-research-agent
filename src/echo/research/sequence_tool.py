"""序列工具"""

from typing import Optional, List, Any


class SequenceTool:
    """序列工具"""

    def repeat(self, item: Any, count: int) -> List[Any]:
        """重复"""
        return [item] * count

    def cycle(self, items: List[Any], count: int) -> List[Any]:
        """循环"""
        result = []
        for _ in range(count):
            result.extend(items)
        return result


_sequence_tool: Optional[SequenceTool] = None


def get_sequence_tool() -> SequenceTool:
    global _sequence_tool
    if _sequence_tool is None:
        _sequence_tool = SequenceTool()
    return _sequence_tool