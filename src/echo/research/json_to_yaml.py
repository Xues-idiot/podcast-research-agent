"""JSON转YAML工具"""

import json
import yaml
from typing import Optional


class JsonToYamlTool:
    _instance: Optional["JsonToYamlTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def convert(self, json_str: str) -> str:
        try:
            obj = json.loads(json_str)
            return yaml.dump(obj, allow_unicode=True, sort_keys=False)
        except:
            return json_str

    def parse(self, json_str: str) -> dict:
        try:
            return json.loads(json_str)
        except:
            return {}


def get_json_to_yaml_tool() -> JsonToYamlTool:
    return JsonToYamlTool()