"""克隆工具"""

import copy
from typing import Optional, Any


class Cloner:
    """克隆工具"""

    def shallow_clone(self, obj: Any) -> Any:
        """浅克隆"""
        if isinstance(obj, list):
            return list(obj)
        if isinstance(obj, dict):
            return dict(obj)
        return obj

    def deep_clone(self, obj: Any) -> Any:
        """深克隆"""
        return copy.deepcopy(obj)


_cloner: Optional[Cloner] = None


def get_cloner() -> Cloner:
    global _cloner
    if _cloner is None:
        _cloner = Cloner()
    return _cloner