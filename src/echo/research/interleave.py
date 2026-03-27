"""交错工具"""

from typing import List, Any, Optional


class Interleave:
    _instance: Optional["Interleave"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def interleave(self, *lists: List[Any]) -> List[Any]:
        result = []
        max_len = max(len(lst) for lst in lists)
        for i in range(max_len):
            for lst in lists:
                if i < len(lst):
                    result.append(lst[i])
        return result

    def interpose(self, items: List[Any], sep: Any) -> List[Any]:
        result = []
        for i, item in enumerate(items):
            if i > 0:
                result.append(sep)
            result.append(item)
        return result


def get_interleave() -> Interleave:
    return Interleave()
