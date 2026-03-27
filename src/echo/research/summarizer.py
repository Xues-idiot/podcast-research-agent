"""汇总工具"""

from typing import Optional, Any


class Summarizer:
    """汇总工具"""

    def frequencies(self, items: list) -> dict:
        """频率统计"""
        from collections import Counter
        return dict(Counter(items))

    def group_count(self, items: list) -> dict:
        """分组计数"""
        from collections import Counter
        return dict(Counter(items))


_tool: Optional[Summarizer] = None


def get_summarizer() -> Summarizer:
    global _tool
    if _tool is None:
        _tool = Summarizer()
    return _tool