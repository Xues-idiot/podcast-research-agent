"""报告生成测试"""

import pytest
from echo.agents.report import ReportGenerator


class TestReportGenerator:
    """报告生成测试"""

    def test_format_mindmap(self):
        """测试思维导图格式化"""
        gen = ReportGenerator.__new__(ReportGenerator)

        mindmap = {
            "root": "测试主题",
            "branches": [
                {"title": "分支1", "children": ["子节点1", "子节点2"]},
                {"title": "分支2", "children": ["子节点3"]},
            ]
        }

        result = gen._format_mindmap(mindmap)
        assert "测试主题" in result
        assert "分支1" in result
        assert "子节点1" in result

    def test_export_markdown(self):
        """测试Markdown导出"""
        gen = ReportGenerator.__new__(ReportGenerator)

        report = {
            "title": "测试报告",
            "summary": {
                "title": "测试摘要",
                "summary": "这是摘要内容",
                "highlights": ["亮点1", "亮点2"],
            },
            "keypoints": [
                {"id": 1, "content": "要点1"},
                {"id": 2, "content": "要点2"},
            ],
            "content": "报告正文内容",
        }

        md = gen.export_markdown(report)
        assert "# 测试报告" in md
        assert "## 摘要" in md
        assert "## 亮点" in md
        assert "## 关键要点" in md
