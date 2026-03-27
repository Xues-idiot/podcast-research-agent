"""配置加载工具"""

import json
import os
from typing import Optional, Any


class ConfigLoader:
    """配置加载工具"""

    def load_json(self, path: str) -> dict:
        """加载JSON配置"""
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def save_json(self, path: str, data: dict, indent: int = 2):
        """保存JSON配置"""
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=indent, ensure_ascii=False)

    def get_env(self, key: str, default: str = None) -> str:
        """获取环境变量"""
        return os.environ.get(key, default)

    def set_env(self, key: str, value: str):
        """设置环境变量"""
        os.environ[key] = value


_loader: Optional[ConfigLoader] = None


def get_config_loader() -> ConfigLoader:
    global _loader
    if _loader is None:
        _loader = ConfigLoader()
    return _loader