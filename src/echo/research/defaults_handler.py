"""默认值处理工具"""

from typing import Optional, Any


class DefaultsHandler:
    """默认值处理工具"""

    def default(self, value: Any, default_val: Any) -> Any:
        """默认值"""
        return value if value is not None else default_val


_defaults_handler: Optional[DefaultsHandler] = None


def get_defaults_handler() -> DefaultsHandler:
    global _defaults_handler
    if _defaults_handler is None:
        _defaults_handler = DefaultsHandler()
    return _defaults_handler