"""版本比较工具"""

import re
from typing import Optional


class VersionComparator:
    """版本比较工具"""

    def parse_version(self, version: str) -> tuple:
        """解析版本号"""
        parts = re.findall(r'\d+', version)
        return tuple(int(p) for p in parts)

    def compare(self, v1: str, v2: str) -> int:
        """比较版本号: -1小于, 0等于, 1大于"""
        p1 = self.parse_version(v1)
        p2 = self.parse_version(v2)
        if p1 < p2:
            return -1
        elif p1 > p2:
            return 1
        return 0

    def is_compatible(self, current: str, required: str) -> bool:
        """检查是否兼容(主版本号相同)"""
        p1 = self.parse_version(current)
        p2 = self.parse_version(required)
        return p1[0] == p2[0] if p1 and p2 else False


_comparator: Optional[VersionComparator] = None


def get_version_comparator() -> VersionComparator:
    global _comparator
    if _comparator is None:
        _comparator = VersionComparator()
    return _comparator