"""pytest配置和fixtures"""

import pytest


@pytest.fixture
def mock_transcript():
    """模拟转录结果"""
    return {
        "text": "这是测试转录文本。讨论了AI和机器学习的主题。",
        "segments": [
            {"start": 0, "end": 5, "text": "这是测试转录文本。"},
            {"start": 5, "end": 10, "text": "讨论了AI和机器学习的主题。"},
        ],
        "language": "zh",
    }


@pytest.fixture
def mock_summary():
    """模拟摘要结果"""
    return {
        "title": "测试摘要标题",
        "summary": "这是测试摘要内容，描述了主要讨论话题。",
        "highlights": ["亮点1", "亮点2", "亮点3"],
    }


@pytest.fixture
def mock_keypoints():
    """模拟要点结果"""
    return [
        {"id": 1, "content": "要点内容1", "importance": "high"},
        {"id": 2, "content": "要点内容2", "importance": "medium"},
        {"id": 3, "content": "要点内容3", "importance": "low"},
    ]


@pytest.fixture
def mock_mindmap():
    """模拟思维导图结果"""
    return {
        "root": "测试主题",
        "branches": [
            {"title": "分支1", "children": ["子节点1", "子节点2"]},
            {"title": "分支2", "children": ["子节点3"]},
        ],
    }


@pytest.fixture
def mock_research_result(mock_transcript, mock_summary, mock_keypoints, mock_mindmap):
    """模拟完整研究结果"""
    return {
        "transcript": mock_transcript,
        "summary": mock_summary,
        "keypoints": mock_keypoints,
        "mindmap": mock_mindmap,
        "knowledge_cards": [],
        "report": {},
    }
