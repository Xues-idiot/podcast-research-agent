"""要点生成测试"""

import pytest
from echo.agents.keypoint import KeyPointGenerator


class TestKeyPointGenerator:
    """要点生成测试"""

    def test_parse_keypoints(self):
        """测试要点解析"""
        gen = KeyPointGenerator.__new__(KeyPointGenerator)

        content = """
1. 这是第一个要点
2. 这是第二个要点
3. 这是第三个要点
"""

        keypoints = gen._parse_keypoints(content, 3)
        assert len(keypoints) == 3
        assert keypoints[0]["content"] == "这是第一个要点"
        assert keypoints[1]["content"] == "这是第二个要点"
