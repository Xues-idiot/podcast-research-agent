"""交叉合并列表工具"""

from typing import List, Any, Optional


class InterleaveListsTool:
    _instance: Optional["InterleaveListsTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def interleave(self, *lists: List[Any]) -> List[Any]:
        """交叉合并多个列表"""
        result = []
        max_len = max(len(lst) for lst in lists) if lists else 0
        for i in range(max_len):
            for lst in lists:
                if i < len(lst):
                    result.append(lst[i])
        return result

    def round_robin(self, *lists: List[Any]) -> List[Any]:
        """轮转合并"""
        return self.interleave(*lists)

    def intersperse(self, items: List[Any], value: Any) -> List[Any]:
        """在元素间插入值"""
        result = []
        for i, item in enumerate(items):
            if i > 0:
                result.append(value)
            result.append(item)
        return result


def get_interleave_lists_tool() -> InterleaveListsTool:
    return InterleaveListsTool()