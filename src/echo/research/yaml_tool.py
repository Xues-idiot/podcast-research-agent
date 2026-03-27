"""YAML工具"""

import json
from typing import Optional


class YamlTool:
    """YAML工具"""

    def to_json(self, yaml_str: str) -> str:
        """YAML转JSON(简化实现)"""
        import re
        lines = yaml_str.strip().split('\n')
        result = {}
        stack = [(result, -1)]
        current_indent = 0

        for line in lines:
            if not line.strip():
                continue
            indent = len(line) - len(line.lstrip())
            key_val = line.strip().split(':', 1)

            if len(key_val) == 2:
                key = key_val[0].strip()
                val = key_val[1].strip()

                while len(stack) > 1 and stack[-1][1] >= indent:
                    stack.pop()

                if val:
                    stack[-1][0][key] = val
                else:
                    stack[-1][0][key] = {}
                    stack.append((stack[-1][0][key], indent))

        return json.dumps(result, indent=2, ensure_ascii=False)

    def from_json(self, json_str: str) -> str:
        """JSON转YAML(简化实现)"""
        data = json.loads(json_str)
        return self._dict_to_yaml(data, 0)


_yaml_tool: Optional[YamlTool] = None


def get_yaml_tool() -> YamlTool:
    global _yaml_tool
    if _yaml_tool is None:
        _yaml_tool = YamlTool()
    return _yaml_tool