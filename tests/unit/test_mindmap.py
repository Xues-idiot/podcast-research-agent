"""思维导图测试"""

import json
import pytest
from echo.agents.mindmap import MindMapGenerator


class TestMindMapGenerator:
    """思维导图生成测试"""

    def test_export_json(self):
        """测试JSON导出"""
        gen = MindMapGenerator.__new__(MindMapGenerator)

        mindmap = {
            "root": "测试主题",
            "branches": [
                {"title": "分支1", "children": ["子节点1", "子节点2"]}
            ]
        }

        result = gen.export_json(mindmap)
        assert isinstance(result, str)

        parsed = json.loads(result)
        assert parsed["root"] == "测试主题"
