"""B站下载器"""

import asyncio
from pathlib import Path
from typing import Optional

import yt_dlp


class BilibiliDownloader:
    """
    B站视频下载器

    支持:
    - BV视频 (bilibili.com/video/BVxxx)
    - BV合集 (bilibili.com/video/BVxxx/?p=N)
    - 短链接 (b23.tv/xxx)
    """

    def __init__(self, output_dir: str = "./downloads"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    async def download(self, url: str) -> str:
        """
        下载B站视频并提取音频

        Args:
            url: B站视频URL

        Returns:
            音频文件路径 (mp3)
        """
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": str(self.output_dir / "bilibili_%(id)s.%(ext)s"),
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
            # B站特定选项
            "extractor_args": {
                "bilibili": {
                    "cookie": "cookies.txt",  # 可选，需要登录
                }
            },
        }

        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(
            None,
            lambda: self._download_sync(url, ydl_opts)
        )
        return result

    def _download_sync(self, url: str, ydl_opts: dict) -> str:
        """同步下载"""
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # 先获取信息
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            # mp3文件名
            mp3_name = Path(filename).stem + ".mp3"
            return str(self.output_dir / mp3_name)

    async def get_video_info(self, url: str) -> dict:
        """获取视频信息（不下载）"""
        ydl_opts = {
            "outtmpl": "%(id)s",
            "skip_download": True,
        }

        loop = asyncio.get_event_loop()
        info = await loop.run_in_executor(
            None,
            lambda: self._get_info_sync(url, ydl_opts)
        )
        return info

    def _get_info_sync(self, url: str, ydl_opts: dict) -> dict:
        """同步获取信息"""
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            return ydl.extract_info(url, download=False)
