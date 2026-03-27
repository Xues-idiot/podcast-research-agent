"""配置加载器"""

import json
import yaml
from typing import Any, Dict, Optional


class ConfigLoad:
    _instance: Optional["ConfigLoad"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def load_json(self, path: str) -> Dict[str, Any]:
        with open(path, "r") as f:
            return json.load(f)

    def load_yaml(self, path: str) -> Dict[str, Any]:
        with open(path, "r") as f:
            return yaml.safe_load(f)


def get_config_load() -> ConfigLoad:
    return ConfigLoad()
