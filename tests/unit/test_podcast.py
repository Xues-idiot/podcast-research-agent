"""播客RSS解析测试"""

import pytest
from echo.tools.podcast import PodcastRSSParser, PodcastEpisode


class TestPodcastRSSParser:
    """播客RSS解析测试"""

    def test_parser_init(self):
        """测试初始化"""
        parser = PodcastRSSParser()
        assert parser is not None

    def test_podcast_episode_dataclass(self):
        """测试Episode数据类"""
        episode = PodcastEpisode(
            title="测试标题",
            url="https://example.com/episode",
            description="测试描述",
            published=None,
            duration="30:00",
            audio_url="https://example.com/audio.mp3",
        )
        assert episode.title == "测试标题"
        assert episode.duration == "30:00"
