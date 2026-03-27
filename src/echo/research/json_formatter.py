"""JSON格式化工具"""

import json
from typing import Optional


class JsonFormatter:
    """JSON格式化工具"""

    def format(self, data: str, indent: int = 2) -> str:
        """格式化JSON"""
        try:
            parsed = json.loads(data)
            return json.dumps(parsed, indent=indent, ensure_ascii=False)
        except json.JSONDecodeError:
            return data

    def minify(self, data: str) -> str:
        """压缩JSON"""
        try:
            parsed = json.loads(data)
            return json.dumps(parsed, separators=(',', ':'), ensure_ascii=False)
        except json.JSONDecodeError:
            return data

    def validate(self, data: str) -> dict:
        """验证JSON"""
        try:
            parsed = json.loads(data)
            return {"valid": True, "parsed": parsed}
        except json.JSONDecodeError as e:
            return {"valid": False, "error": str(e)}


_formatter: Optional[JsonFormatter] = None


def get_json_formatter() -> JsonFormatter:
    global _formatter
    if _formatter is None:
        _formatter = JsonFormatter()
    return _formatter