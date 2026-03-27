"""CSV转换工具"""

import csv
import io
from typing import Optional


class CsvConverter:
    """CSV转换工具"""

    def to_csv(self, data: list[dict], headers: Optional[list[str]] = None) -> str:
        """字典列表转CSV"""
        if not data:
            return ""

        if headers is None:
            headers = list(data[0].keys()) if data else []

        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
        return output.getvalue()

    def from_csv(self, csv_str: str) -> list[dict]:
        """CSV转字典列表"""
        input_io = io.StringIO(csv_str)
        reader = csv.DictReader(input_io)
        return list(reader)

    def to_tsv(self, data: list[dict]) -> str:
        """转TSV"""
        if not data:
            return ""
        headers = list(data[0].keys())
        lines = ['\t'.join(headers)]
        for row in data:
            lines.append('\t'.join(str(row.get(h, '')) for h in headers))
        return '\n'.join(lines)


_converter: Optional[CsvConverter] = None


def get_csv_converter() -> CsvConverter:
    global _converter
    if _converter is None:
        _converter = CsvConverter()
    return _converter