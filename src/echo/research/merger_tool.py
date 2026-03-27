"""Merger tool module - merges data from multiple sources"""

from typing import Any, Callable, Dict, List, Optional, TypeVar

T = TypeVar('T')


class MergerTool:
    _instance: Optional["MergerTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def merge(self, *dicts: Dict[str, Any]) -> Dict[str, Any]:
        """Merge multiple dictionaries"""
        result = {}
        for d in dicts:
            result.update(d)
        return result

    def merge_with(self, *dicts: Dict[str, Any], combiner: Callable[[Any, Any], Any]) -> Dict[str, Any]:
        """Merge dictionaries with custom value combination"""
        result: Dict[str, Any] = {}
        for d in dicts:
            for key, value in d.items():
                if key in result:
                    result[key] = combiner(result[key], value)
                else:
                    result[key] = value
        return result

    def merge_lists(self, *lists: List[T]) -> List[T]:
        """Merge multiple lists"""
        result = []
        for lst in lists:
            result.extend(lst)
        return result

    def merge_unique(self, *lists: List[T]) -> List[T]:
        """Merge lists keeping only unique values"""
        seen = set()
        result = []
        for lst in lists:
            for item in lst:
                if item not in seen:
                    seen.add(item)
                    result.append(item)
        return result

    def deep_merge(self, *dicts: Dict[str, Any]) -> Dict[str, Any]:
        """Deep merge nested dictionaries"""
        result = {}
        for d in dicts:
            self._deep_merge_dict(result, d)
        return result

    def _deep_merge_dict(self, base: Dict[str, Any], update: Dict[str, Any]) -> None:
        """Helper for deep merge"""
        for key, value in update.items():
            if key in base and isinstance(base[key], dict) and isinstance(value, dict):
                self._deep_merge_dict(base[key], value)
            else:
                base[key] = value


def get_merger_tool() -> MergerTool:
    return MergerTool()
