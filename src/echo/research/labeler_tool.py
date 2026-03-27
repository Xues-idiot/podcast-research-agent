"""Labeler tool for labeling items"""

from typing import Any, Callable, Dict, Hashable, List, Optional


class LabelerTool:
    _instance: Optional["LabelerTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def label(self, items: List[Any], label: str) -> List[Dict[str, Any]]:
        """Add a label to items"""
        return [{"item": item, "label": label} for item in items]

    def label_with_func(self, items: List[Any], label_func: Callable[[Any], str]) -> List[Dict[str, Any]]:
        """Label items using a function"""
        return [{"item": item, "label": label_func(item)} for item in items]

    def relabel(self, labeled_items: List[Dict[str, Any]], new_label: str) -> List[Dict[str, Any]]:
        """Change labels for all items"""
        return [{"item": t["item"], "label": new_label} for t in labeled_items]

    def filter_by_label(self, labeled_items: List[Dict[str, Any]], label: str) -> List[Any]:
        """Get items with specific label"""
        return [t["item"] for t in labeled_items if t.get("label") == label]

    def get_labels(self, labeled_items: List[Dict[str, Any]]) -> List[str]:
        """Get all unique labels"""
        seen = set()
        labels = []
        for t in labeled_items:
            label = t.get("label")
            if label and label not in seen:
                seen.add(label)
                labels.append(label)
        return labels

    def count_by_label(self, labeled_items: List[Dict[str, Any]]) -> Dict[str, int]:
        """Count items per label"""
        counts: Dict[str, int] = {}
        for t in labeled_items:
            label = t.get("label", "unknown")
            counts[label] = counts.get(label, 0) + 1
        return counts

    def process(self, data: Any) -> Any:
        """Process data by labeling"""
        return data


def get_labeler_tool() -> LabelerTool:
    return LabelerTool()