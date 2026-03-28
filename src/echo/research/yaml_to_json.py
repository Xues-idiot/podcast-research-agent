"""YAML转JSON工具"""

import json
import yaml
from typing import Optional


class YamlToJsonTool:
    _instance: Optional["YamlToJsonTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def convert(self, yaml_str: str) -> str:
        try:
            obj = yaml.safe_load(yaml_str)
            return json.dumps(obj, ensure_ascii=False, indent=2)
        except:
            return yaml_str


def get_yaml_to_json_tool() -> YamlToJsonTool:
    return YamlToJsonTool()