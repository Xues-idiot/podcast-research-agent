"""CSV工具"""

from typing import Any, List, Optional


class CsvTool:
    _instance: Optional["CsvTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def parse(self, text: str, delimiter: str = ",") -> List[List[str]]:
        lines = text.strip().split("\n")
        return [line.split(delimiter) for line in lines]

    def to_csv(self, data: List[List[str]], delimiter: str = ",") -> str:
        return "\n".join(delimiter.join(row) for row in data)


def get_csv_tool() -> CsvTool:
    return CsvTool()
