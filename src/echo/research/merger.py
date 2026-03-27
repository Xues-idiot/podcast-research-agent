"""字典合并工具"""

from typing import Optional, Any


class DictMerger:
    """字典合并工具"""

    def shallow_merge(self, dict1: dict, dict2: dict) -> dict:
        """浅合并"""
        result = dict1.copy()
        result.update(dict2)
        return result

    def deep_merge(self, dict1: dict, dict2: dict) -> dict:
        """深合并"""
        result = dict1.copy()
        for key, value in dict2.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = self.deep_merge(result[key], value)
            else:
                result[key] = value
        return result


_merger: Optional[DictMerger] = None


def get_dict_merger() -> DictMerger:
    global _merger
    if _merger is None:
        _merger = DictMerger()
    return _merger