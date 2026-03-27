"""Collection harvester module - harvests and collects items into a result"""

from typing import Any, Callable, List, Optional


class CollectionHarvester:
    _instance: Optional["CollectionHarvester"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._collected = []
        return cls._instance

    def harvest(self, item: Any) -> List[Any]:
        """Harvest a single item"""
        self._collected.append(item)
        return self._collected

    def harvest_many(self, items: List[Any]) -> List[Any]:
        """Harvest multiple items"""
        self._collected.extend(items)
        return self._collected

    def harvest_with(self, item: Any, predicate: Callable[[Any], bool]) -> List[Any]:
        """Harvest item only if predicate returns true"""
        if predicate(item):
            self._collected.append(item)
        return self._collected

    def get_harvest(self) -> List[Any]:
        """Get harvested items"""
        return self._collected.copy()

    def clear_harvest(self) -> None:
        """Clear harvested items"""
        self._collected.clear()


def get_collection_harvester() -> CollectionHarvester:
    return CollectionHarvester()
