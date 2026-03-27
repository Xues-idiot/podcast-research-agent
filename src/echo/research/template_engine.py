"""模板引擎工具"""

from typing import Any, Dict, Optional


class TemplateEngine:
    _instance: Optional["TemplateEngine"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def render(self, template: str, context: Dict[str, Any]) -> str:
        result = template
        for key, value in context.items():
            result = result.replace("{{" + key + "}}", str(value))
        return result

    def render_if(self, template: str, condition: bool, true_val: str, false_val: str = "") -> str:
        return true_val if condition else false_val


def get_template_engine() -> TemplateEngine:
    return TemplateEngine()
