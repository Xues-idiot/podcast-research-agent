"""导出器测试"""

import json
import pytest
from pathlib import Path
from echo.agents.flashcard import Exporter


class TestExporter:
    """导出器测试"""

    @pytest.fixture
    def output_dir(self, tmp_path):
        """临时输出目录"""
        return str(tmp_path)

    @pytest.fixture
    def exporter(self, output_dir):
        """导出器实例"""
        return Exporter(output_dir)

    def test_export_json(self, exporter, mock_research_result):
        """测试JSON导出"""
        path = exporter.export_json(mock_research_result, "test.json")
        assert Path(path).exists()

        with open(path, encoding="utf-8") as f:
            data = json.load(f)
            assert "summary" in data

    def test_export_markdown(self, exporter, mock_research_result):
        """测试Markdown导出"""
        path = exporter.export_markdown(mock_research_result, "test.md")
        assert Path(path).exists()

        content = Path(path).read_text(encoding="utf-8")
        assert "测试摘要标题" in content
        assert "要点内容1" in content

    def test_export_csv(self, exporter, mock_research_result):
        """测试CSV导出"""
        path = exporter.export_csv(mock_research_result, "test.csv")
        assert Path(path).exists()

        content = Path(path).read_text(encoding="utf-8")
        assert "要点内容1" in content
        assert "high" in content

    def test_export_flashcards_json(self, exporter, mock_research_result):
        """测试闪卡JSON导出"""
        path = exporter.export_flashcards(mock_research_result, "cards.json", format="json")
        assert Path(path).exists()

        with open(path, encoding="utf-8") as f:
            data = json.load(f)
            assert len(data) > 0
            assert "front" in data[0]

    def test_export_flashcards_markdown(self, exporter, mock_research_result):
        """测试闪卡Markdown导出"""
        path = exporter.export_flashcards(mock_research_result, "cards.md", format="markdown")
        assert Path(path).exists()

        content = Path(path).read_text(encoding="utf-8")
        assert "闪卡" in content

    def test_export_flashcards_html(self, exporter, mock_research_result):
        """测试闪卡HTML导出"""
        path = exporter.export_flashcards(mock_research_result, "cards.html", format="html")
        assert Path(path).exists()

        content = Path(path).read_text(encoding="utf-8")
        assert "<html>" in content
        assert "flashcard" in content

    def test_export_mindmap_json(self, exporter, mock_research_result):
        """测试思维导图JSON导出"""
        path = exporter.export_mindmap_json(mock_research_result, "mindmap.json")
        assert Path(path).exists()

        with open(path, encoding="utf-8") as f:
            data = json.load(f)
            assert data["root"] == "测试主题"

    def test_export_all(self, exporter, mock_research_result):
        """测试导出所有格式"""
        paths = exporter.export_all(mock_research_result)

        assert "json" in paths
        assert "markdown" in paths
        assert "csv" in paths
        assert "mindmap" in paths
        assert "flashcards" in paths

        for path in paths.values():
            assert Path(path).exists()
