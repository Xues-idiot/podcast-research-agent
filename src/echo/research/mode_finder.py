"""众数查找器"""

from typing import Any, List, Optional
import statistics


class ModeFinder:
    _instance: Optional["ModeFinder"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def mode(self, items: List[Any]) -> Optional[Any]:
        if not items:
            return None
        try:
            return statistics.mode(items)
        except statistics.StatisticsError:
            return None

    def multimode(self, items: List[Any]) -> List[Any]:
        if not items:
            return []
        try:
            return statistics.multimode(items)
        except statistics.StatisticsError:
            return []


def get_mode_finder() -> ModeFinder:
    return ModeFinder()
