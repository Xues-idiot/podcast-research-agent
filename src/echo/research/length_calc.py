"""长度工具"""

from typing import List, Any, Optional


class LengthCalcTool:
    _instance: Optional["LengthCalcTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def length(self, items: List[Any]) -> int:
        """获取长度"""
        return len(items)

    def count(self, items: List[Any], item: Any) -> int:
        """统计元素出现次数"""
        return items.count(item)

    def is_empty(self, items: List[Any]) -> bool:
        """是否为空"""
        return len(items) == 0

    def is_longer_than(self, items: List[Any], n: int) -> bool:
        """是否长于n"""
        return len(items) > n

    def is_shorter_than(self, items: List[Any], n: int) -> bool:
        """是否短于n"""
        return len(items) < n

    def word_count(self, text: str) -> int:
        """单词数"""
        return len(text.split())

    def char_count(self, text: str) -> int:
        """字符数"""
        return len(text)


_length_instance: Optional[LengthCalcTool] = None


def get_length_calc_tool() -> LengthCalcTool:
    global _length_instance
    if _length_instance is None:
        _length_instance = LengthCalcTool()
    return _length_instance