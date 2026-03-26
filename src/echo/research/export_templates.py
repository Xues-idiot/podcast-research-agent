"""导出格式预设"""

from dataclasses import dataclass


@dataclass
class ExportPreset:
    """导出预设"""
    id: str
    name: str
    formats: list
    include_sections: list


PRESETS = [
    ExportPreset(
        id="full",
        name="完整导出",
        formats=["json", "markdown", "html"],
        include_sections=["summary", "keypoints", "qa", "mindmap", "knowledge_cards"],
    ),
    ExportPreset(
        id="summary_only",
        name="仅摘要",
        formats=["markdown", "txt"],
        include_sections=["summary"],
    ),
    ExportPreset(
        id="notes",
        name="学习笔记",
        formats=["markdown", "txt"],
        include_sections=["keypoints", "qa"],
    ),
    ExportPreset(
        id="anki",
        name="Anki卡片",
        formats=["json", "csv"],
        include_sections=["keypoints"],
    ),
]
