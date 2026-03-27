"""合并处理工具"""

from typing import Optional, Any


class CoalesceHandler:
    """合并处理工具"""

    def coalesce(self, *values) -> Any:
        """合并"""
        for value in values:
            if value is not None:
                return value
        return None


_coalesce_handler: Optional[CoalesceHandler] = None


def get_coalesce_handler() -> CoalesceHandler:
    global _coalesce_handler
    if _coalesce_handler is None:
        _coalesce_handler = CoalesceHandler()
    return _coalesce_handler