"""格式转换工具"""

from typing import Any, Dict, List
import json


class FormatConvertTool:
    _instance: Any = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def dict_to_list(self, d: Dict, separator: str = "|") -> List[str]:
        """字典转列表字符串"""
        return [f"{k}{separator}{v}" for k, v in d.items()]

    def list_to_dict(self, items: List[str], separator: str = "|") -> Dict:
        """列表字符串转字典"""
        result = {}
        for item in items:
            if separator in item:
                parts = item.split(separator, 1)
                result[parts[0]] = parts[1]
        return result

    def flatten_dict(self, d: Dict, parent_key: str = "", sep: str = ".") -> Dict:
        """扁平化嵌套字典"""
        items = []
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(self.flatten_dict(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)

    def unflatten_dict(self, d: Dict, sep: str = ".") -> Dict:
        """反扁平化字典"""
        result = {}
        for key, value in d.items():
            parts = key.split(sep)
            current = result
            for part in parts[:-1]:
                if part not in current:
                    current[part] = {}
                current = current[part]
            current[parts[-1]] = value
        return result

    def list_to_string(self, items: List[Any], sep: str = ", ") -> str:
        """列表转字符串"""
        return sep.join(str(item) for item in items)

    def string_to_list(self, s: str, sep: str = ", ") -> List[str]:
        """字符串转列表"""
        if not s:
            return []
        return [item.strip() for item in s.split(sep)]


def get_format_convert_tool() -> FormatConvertTool:
    return FormatConvertTool()