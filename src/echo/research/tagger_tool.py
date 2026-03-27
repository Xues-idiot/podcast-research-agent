"""Tagger tool for tagging items"""

from typing import Any, Callable, Dict, Hashable, List, Optional, Set


class TaggerTool:
    _instance: Optional["TaggerTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def tag(self, item: Any, tags: Set[str]) -> Dict[str, Any]:
        """Add tags to an item"""
        return {"item": item, "tags": tags}

    def tag_with_func(self, items: List[Any], tag_func: Callable[[Any], Set[str]]) -> List[Dict[str, Any]]:
        """Tag items using a function"""
        return [{"item": item, "tags": tag_func(item)} for item in items]

    def add_tags(self, item: Any, new_tags: Set[str]) -> Dict[str, Any]:
        """Add additional tags to an item"""
        if isinstance(item, dict) and "tags" in item:
            item["tags"].update(new_tags)
            return item
        return {"item": item, "tags": new_tags}

    def remove_tags(self, item: Any, tags_to_remove: Set[str]) -> Dict[str, Any]:
        """Remove tags from an item"""
        if isinstance(item, dict) and "tags" in item:
            item["tags"] = item["tags"] - tags_to_remove
            return item
        return {"item": item, "tags": set()}

    def filter_by_tag(self, tagged_items: List[Dict[str, Any]], tag: str) -> List[Dict[str, Any]]:
        """Filter items by tag"""
        return [t for t in tagged_items if tag in t.get("tags", set())]

    def get_all_tags(self, tagged_items: List[Dict[str, Any]]) -> Set[str]:
        """Get all unique tags"""
        all_tags: Set[str] = set()
        for t in tagged_items:
            all_tags.update(t.get("tags", set()))
        return all_tags

    def process(self, data: Any) -> Any:
        """Process data by tagging"""
        return data


def get_tagger_tool() -> TaggerTool:
    return TaggerTool()