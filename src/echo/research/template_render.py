"""模板渲染工具"""

from typing import Dict, Optional, Any
import re


class TemplateRenderTool:
    _instance: Optional["TemplateRenderTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def render(self, template: str, variables: Dict[str, Any]) -> str:
        """渲染模板"""
        result = template
        for key, value in variables.items():
            pattern = r"\{\{" + re.escape(key) + r"\}\}"
            result = re.sub(pattern, str(value), result)
        return result

    def render_list(self, template: str, items: list, item_var: str = "item") -> List[str]:
        """渲染列表模板"""
        results = []
        for item in items:
            results.append(self.render(template, {item_var: item}))
        return results

    def render_dict(self, template: str, data: Dict[str, Any]) -> str:
        """渲染字典模板"""
        return self.render(template, data)


_tpl_instance: Optional[TemplateRenderTool] = None


def get_template_render_tool() -> TemplateRenderTool:
    global _tpl_instance
    if _tpl_instance is None:
        _tpl_instance = TemplateRenderTool()
    return _tpl_instance