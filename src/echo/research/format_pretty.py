"""格式化输出工具"""

from typing import Any, List, Optional
import json


class FormatPrettyTool:
    _instance: Optional["FormatPrettyTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def pretty_json(self, data: Any, indent: int = 2) -> str:
        """格式化JSON"""
        return json.dumps(data, indent=indent, ensure_ascii=False)

    def pretty_list(self, items: List[Any], bullet: str = "- ") -> str:
        """格式化列表"""
        return "\n".join(f"{bullet}{item}" for item in items)

    def pretty_dict(self, d: dict, indent: int = 2) -> str:
        """格式化字典"""
        lines = []
        for k, v in d.items():
            if isinstance(v, dict):
                lines.append(f"{k}:")
                for kk, vv in v.items():
                    lines.append(f"{' ' * indent}{kk}: {vv}")
            else:
                lines.append(f"{k}: {v}")
        return "\n".join(lines)

    def table_format(self, headers: List[str], rows: List[List[Any]]) -> str:
        """表格格式化"""
        col_widths = [len(h) for h in headers]
        for row in rows:
            for i, cell in enumerate(row):
                col_widths[i] = max(col_widths[i], len(str(cell)))
        separator = "+" + "+".join("-" * (w + 2) for w in col_widths) + "+"
        header_line = "|" + "|".join(f" {h}{' ' * (col_widths[i] - len(h))}" for i, h in enumerate(headers)) + "|"
        result = [separator, header_line, separator]
        for row in rows:
            row_line = "|" + "|".join(f" {str(cell)}{' ' * (col_widths[i] - len(str(cell)))}" for i, cell in enumerate(row)) + "|"
            result.append(row_line)
        result.append(separator)
        return "\n".join(result)

    def truncate_middle(self, s: str, max_len: int = 50) -> str:
        """中间截断"""
        if len(s) <= max_len:
            return s
        left_len = (max_len - 3) // 2
        right_len = max_len - 3 - left_len
        return s[:left_len] + "..." + s[-right_len:]


_pretty_instance: Optional[FormatPrettyTool] = None


def get_format_pretty_tool() -> FormatPrettyTool:
    global _pretty_instance
    if _pretty_instance is None:
        _pretty_instance = FormatPrettyTool()
    return _pretty_instance