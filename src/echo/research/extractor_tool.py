"""Extractor tool module - extracts values from data structures"""

from typing import Any, Callable, Dict, List, Optional, TypeVar

T = TypeVar('T')


class ExtractorTool:
    _instance: Optional["ExtractorTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def extract(self, data: Dict[str, Any], key: str) -> Optional[Any]:
        """Extract value from dictionary by key"""
        return data.get(key)

    def extract_nested(self, data: Dict[str, Any], keys: List[str]) -> Optional[Any]:
        """Extract nested value from dictionary"""
        result = data
        for key in keys:
            if isinstance(result, dict):
                result = result.get(key)
            else:
                return None
        return result

    def extract_all(self, data: List[Dict[str, Any]], key: str) -> List[Any]:
        """Extract values for a key from all items in a list"""
        return [item.get(key) for item in data if isinstance(item, dict) and key in item]

    def extract_with(self, data: Any, extractor: Callable[[Any], Any]) -> Any:
        """Extract value using a custom extractor function"""
        return extractor(data)

    def pluck(self, items: List[Dict[str, Any]], key: str) -> List[Any]:
        """Pluck values for a key from all dictionaries"""
        return self.extract_all(items, key)

    def pick(self, data: Dict[str, Any], keys: List[str]) -> Dict[str, Any]:
        """Pick specific keys from dictionary"""
        return {k: data.get(k) for k in keys if k in data}


def get_extractor_tool() -> ExtractorTool:
    return ExtractorTool()
