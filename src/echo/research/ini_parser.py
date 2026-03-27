"""INI解析器工具"""

from typing import Any, Dict, Optional


class IniParser:
    _instance: Optional["IniParser"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def parse(self, text: str) -> Dict[str, Dict[str, str]]:
        result = {}
        current_section = "default"
        result[current_section] = {}
        for line in text.strip().split("\n"):
            line = line.strip()
            if line.startswith("[") and line.endswith("]"):
                current_section = line[1:-1]
                result[current_section] = {}
            elif "=" in line:
                key, value = line.split("=", 1)
                result[current_section][key.strip()] = value.strip()
        return result


def get_ini_parser() -> IniParser:
    return IniParser()
