"""Aggregation engine module - aggregates values from multiple sources"""

from typing import Any, Callable, Dict, List, Optional


class AggregationEngine:
    _instance: Optional["AggregationEngine"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def aggregate(self, values: List[Any], operation: Callable[[List[Any]], Any]) -> Any:
        """Aggregate values using a custom operation"""
        return operation(values)

    def sum_values(self, values: List[float]) -> float:
        """Sum all numeric values"""
        return sum(values)

    def avg_values(self, values: List[float]) -> float:
        """Calculate average of numeric values"""
        return sum(values) / len(values) if values else 0.0

    def max_value(self, values: List[Any], key: Optional[Callable[[Any], Any]] = None) -> Any:
        """Get maximum value"""
        return max(values, key=key) if values else None

    def min_value(self, values: List[Any], key: Optional[Callable[[Any], Any]] = None) -> Any:
        """Get minimum value"""
        return min(values, key=key) if values else None

    def group_aggregate(self, items: List[Dict[str, Any]], group_key: str, agg_key: str, operation: Callable[[List[Any]], Any]) -> Dict[str, Any]:
        """Group items and aggregate values within each group"""
        groups: Dict[str, List[Any]] = {}
        for item in items:
            group = item.get(group_key)
            if group not in groups:
                groups[group] = []
            groups[group].append(item.get(agg_key))
        return {k: operation(v) for k, v in groups.items()}


def get_aggregation_engine() -> AggregationEngine:
    return AggregationEngine()
