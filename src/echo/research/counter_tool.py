"""计数器工具"""

from typing import Optional, List, Any


class CounterTool:
    """计数器工具"""

    def count(self, items: List[Any]) -> int:
        """计数"""
        return len(items)


_counter_tool: Optional[CounterTool] = None


def get_counter_tool() -> CounterTool:
    global _counter_tool
    if _counter_tool is None:
        _counter_tool = CounterTool()
    return _counter_tool