"""配对工具"""

from typing import Optional, Any


class PairMaker:
    """配对工具"""

    def pairs(self, items: list) -> list:
        """生成所有配对"""
        result = []
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                result.append((items[i], items[j]))
        return result

    def zip_with_index(self, items: list) -> list:
        """带索引配对"""
        return list(enumerate(items))


_maker: Optional[PairMaker] = None


def get_pair_maker() -> PairMaker:
    global _maker
    if _maker is None:
        _maker = PairMaker()
    return _maker