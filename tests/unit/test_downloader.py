"""下载器测试"""

import pytest
from pathlib import Path
from echo.tools.downloader import VideoDownloader
from echo.tools.bilibili import BilibiliDownloader
from echo.tools.youtube import YouTubeDownloader


class TestVideoDownloader:
    """视频下载器测试"""

    def test_downloader_init(self):
        """测试初始化"""
        dl = VideoDownloader(output_dir="/tmp/test")
        assert dl.output_dir == Path("/tmp/test")
        assert dl.output_dir.exists()


class TestBilibiliDownloader:
    """B站下载器测试"""

    def test_bilibili_init(self):
        """测试初始化"""
        dl = BilibiliDownloader(output_dir="/tmp/test")
        assert dl.output_dir == Path("/tmp/test")


class TestYouTubeDownloader:
    """YouTube下载器测试"""

    def test_youtube_init(self):
        """测试初始化"""
        dl = YouTubeDownloader(output_dir="/tmp/test")
        assert dl.output_dir == Path("/tmp/test")
