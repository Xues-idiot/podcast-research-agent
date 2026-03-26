"""研究模板系统 - 定义和保存研究模板"""

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


@dataclass
class ResearchTemplate:
    """研究模板"""
    id: str
    name: str
    description: str
    steps: list = field(default_factory=list)
    config: dict = field(default_factory=dict)
    is_default: bool = False


class TemplateStore:
    """模板存储"""

    DEFAULT_TEMPLATES = [
        ResearchTemplate(
            id="quick",
            name="快速研究",
            description="简短的播客摘要",
            steps=["transcribe", "summary"],
            is_default=True,
        ),
        ResearchTemplate(
            id="standard",
            name="标准研究",
            description="完整的播客研究流程",
            steps=["transcribe", "summary", "keypoints", "qa"],
            is_default=True,
        ),
        ResearchTemplate(
            id="deep",
            name="深度研究",
            description="包含思维导图和知识卡片",
            steps=["transcribe", "summary", "keypoints", "mindmap", "knowledge_cards", "qa"],
            is_default=True,
        ),
    ]

    def __init__(self, storage_path: Optional[str] = None):
        if storage_path:
            self.storage_path = Path(storage_path)
        else:
            self.storage_path = Path.home() / ".echo" / "templates"
        self.storage_path.mkdir(parents=True, exist_ok=True)
        self._templates_file = self.storage_path / "templates.json"
        self._templates: dict[str, ResearchTemplate] = {}
        self._load()

    def _load(self):
        if self._templates_file.exists():
            try:
                with open(self._templates_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    for tid, tdata in data.items():
                        self._templates[tid] = ResearchTemplate(**tdata)
            except:
                self._templates = {t.id: t for t in self.DEFAULT_TEMPLATES}
        else:
            self._templates = {t.id: t for t in self.DEFAULT_TEMPLATES}

    def _save(self):
        data = {tid: t.__dict__ for tid, t in self._templates.items()}
        with open(self._templates_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def list_all(self) -> list[ResearchTemplate]:
        return list(self._templates.values())

    def get(self, template_id: str) -> Optional[ResearchTemplate]:
        return self._templates.get(template_id)

    def add(self, template: ResearchTemplate) -> bool:
        if template.id in self._templates:
            return False
        self._templates[template.id] = template
        self._save()
        return True

    def remove(self, template_id: str) -> bool:
        t = self._templates.get(template_id)
        if not t or t.is_default:
            return False
        del self._templates[template_id]
        self._save()
        return True


_template_store: Optional[TemplateStore] = None

def get_template_store() -> TemplateStore:
    global _template_store
    if _template_store is None:
        _template_store = TemplateStore()
    return _template_store
