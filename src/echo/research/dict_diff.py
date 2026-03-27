"""字典差异工具"""

from typing import Optional, Any


class DictDiffer:
    """字典差异工具"""

    def diff(self, dict1: dict, dict2: dict) -> dict:
        """比较差异"""
        added = set(dict2.keys()) - set(dict1.keys())
        removed = set(dict1.keys()) - set(dict2.keys())
        modified = {k for k in set(dict1.keys()) & set(dict2.keys()) if dict1[k] != dict2[k]}
        return {
            "added": list(added),
            "removed": list(removed),
            "modified": list(modified)
        }


_differ: Optional[DictDiffer] = None


def get_dict_differ() -> DictDiffer:
    global _differ
    if _differ is None:
        _differ = DictDiffer()
    return _differ