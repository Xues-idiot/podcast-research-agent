"""相等工具"""

from typing import Optional, Any


class Equalizer:
    """相等工具"""

    def equals(self, a: Any, b: Any) -> bool:
        """相等"""
        return a == b


_equalizer: Optional[Equalizer] = None


def get_equalizer() -> Equalizer:
    global _equalizer
    if _equalizer is None:
        _equalizer = Equalizer()
    return _equalizer