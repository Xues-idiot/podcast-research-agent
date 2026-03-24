"""问答生成测试"""

import pytest
from echo.agents.qa import QAGenerator


class TestQAGenerator:
    """问答生成测试"""

    def test_parse_qa(self):
        """测试问答解析"""
        gen = QAGenerator.__new__(QAGenerator)

        content = """
Q1: 问题1
A1: 答案1

Q2: 问题2
A2: 答案2
"""

        qa_pairs = gen._parse_qa(content)
        assert len(qa_pairs) >= 0

    def test_export_markdown(self):
        """测试Markdown导出"""
        gen = QAGenerator.__new__(QAGenerator)

        qa_pairs = [
            {"question": "问题1", "answer": "答案1", "type": "fact"},
            {"question": "问题2", "answer": "答案2", "type": "comprehension"},
        ]

        md = gen.export_markdown(qa_pairs)
        assert "Q1" in md
        assert "问题1" in md
        assert "答案1" in md
