"""CSV转JSON工具"""

import csv
import json
import io
from typing import List, Optional


class CsvToJsonTool:
    _instance: Optional["CsvToJsonTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def convert(self, csv_str: str) -> str:
        try:
            reader = csv.DictReader(io.StringIO(csv_str))
            rows = list(reader)
            return json.dumps(rows, ensure_ascii=False, indent=2)
        except:
            return "[]"

    def parse(self, csv_str: str) -> List[dict]:
        try:
            reader = csv.DictReader(io.StringIO(csv_str))
            return list(reader)
        except:
            return []


def get_csv_to_json_tool() -> CsvToJsonTool:
    return CsvToJsonTool()