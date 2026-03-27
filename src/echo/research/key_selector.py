"""键选择器"""

from typing import Optional, List, Any, Dict


class KeySelector:
    """键选择器"""

    def select_keys(self, item: Dict, keys: List[str]) -> Dict:
        """选择键"""
        return {k: item.get(k) for k in keys if k in item}


_key_selector: Optional[KeySelector] = None


def get_key_selector() -> KeySelector:
    global _key_selector
    if _key_selector is None:
        _key_selector = KeySelector()
    return _key_selector