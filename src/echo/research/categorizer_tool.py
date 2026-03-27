"""Categorizer tool for categorizing items"""

from typing import Any, Callable, Dict, Hashable, List, Optional, Set


class CategorizerTool:
    _instance: Optional["CategorizerTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def categorize(self, items: List[Any], category_func: Callable[[Any], Hashable]) -> Dict[Hashable, List[Any]]:
        """Categorize items by a function"""
        categories: Dict[Hashable, List[Any]] = {}
        for item in items:
            category = category_func(item)
            if category not in categories:
                categories[category] = []
            categories[category].append(item)
        return categories

    def categorize_with_labels(self, items: List[Any], labels: List[str]) -> Dict[str, List[Any]]:
        """Categorize items with predefined labels"""
        categories = {label: [] for label in labels}
        for item in items:
            for label in labels:
                if label not in categories:
                    categories[label] = []
                categories[label].append(item)
        return categories

    def multi_categorize(self, items: List[Any], category_funcs: List[Callable[[Any], Hashable]]) -> List[Dict[Hashable, Any]]:
        """Apply multiple categorization functions"""
        results = []
        for item in items:
            item_categories = {}
            for func in category_funcs:
                item_categories[func.__name__] = func(item)
            results.append(item_categories)
        return results

    def filter_by_category(self, items: List[Any], categories: Set[Hashable], category_func: Callable[[Any], Hashable]) -> List[Any]:
        """Filter items belonging to specific categories"""
        return [item for item in items if category_func(item) in categories]

    def process(self, data: Any) -> Any:
        """Process data by categorizing"""
        return data


def get_categorizer_tool() -> CategorizerTool:
    return CategorizerTool()