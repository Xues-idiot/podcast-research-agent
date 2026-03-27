"""JSON路径工具"""

from typing import Any, Dict, List, Optional


class JsonPath:
    _instance: Optional["JsonPath"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get(self, data: Dict, path: str) -> Any:
        keys = path.strip("$.").split(".")
        result = data
        for key in keys:
            if isinstance(result, dict):
                result = result.get(key)
            elif isinstance(result, list):
                try:
                    result = result[int(key)]
                except:
                    return None
            else:
                return None
        return result

    def set(self, data: Dict, path: str, value: Any) -> None:
        keys = path.strip("$.").split(".")
        current = data
        for key in keys[:-1]:
            if key not in current:
                current[key] = {}
            current = current[key]
        current[keys[-1]] = value


def get_json_path() -> JsonPath:
    return JsonPath()
