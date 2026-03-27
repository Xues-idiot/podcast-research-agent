"""字典更新工具"""

from typing import Optional, Any


class DictUpdater:
    """字典更新工具"""

    def update(self, data: dict, updates: dict) -> dict:
        """更新字典"""
        result = data.copy()
        result.update(updates)
        return result

    def deep_update(self, data: dict, updates: dict) -> dict:
        """深度更新"""
        result = data.copy()
        for key, value in updates.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = self.deep_update(result[key], value)
            else:
                result[key] = value
        return result


_updater: Optional[DictUpdater] = None


def get_dict_updater() -> DictUpdater:
    global _updater
    if _updater is None:
        _updater = DictUpdater()
    return _updater