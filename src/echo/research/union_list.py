"""并集工具"""

from typing import List, Any, Optional


class UnionList:
    _instance: Optional["UnionList"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def union(self, *lists: List[Any]) -> List[Any]:
        result = []
        seen = set()
        for lst in lists:
            for item in lst:
                if item not in seen:
                    seen.add(item)
                    result.append(item)
        return result

    def union_by(self, *lists: List[Any], key: Any) -> List[Any]:
        seen = set()
        result = []
        for lst in lists:
            for item in lst:
                k = key(item)
                if k not in seen:
                    seen.add(k)
                    result.append(item)
        return result


def get_union_list() -> UnionList:
    return UnionList()
