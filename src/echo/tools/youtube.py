"""YouTube下载器"""

import asyncio
import logging
from pathlib import Path

import yt_dlp

logger = logging.getLogger(__name__)


class YouTubeDownloader:
    """
    YouTube视频下载器

    支持:
    - youtube.com/watch?v=xxx
    - youtu.be/xxx
    - youtube.com/playlist?list=xxx
    """

    def __init__(self, output_dir: str = "./downloads"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    async def download(self, url: str) -> str:
        """
        下载YouTube视频并提取音频

        Args:
            url: YouTube视频URL

        Returns:
            音频文件路径 (mp3)
        """
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": str(self.output_dir / "youtube_%(id)s.%(ext)s"),
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
        }

        result = await asyncio.run_in_executor(
            None,
            lambda: self._download_sync(url, ydl_opts)
        )
        return result

    def _download_sync(self, url: str, ydl_opts: dict) -> str:
        """同步下载"""
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                # 处理播放列表情况
                if isinstance(info, list):
                    info = info[0]
                filename = ydl.prepare_filename(info)
                mp3_name = Path(filename).stem + ".mp3"
                return str(self.output_dir / mp3_name)
        except yt_dlp.utils.DownloadError as e:
            raise RuntimeError(f"YouTube下载失败: {e}")
        except Exception as e:
            raise RuntimeError(f"YouTube下载时发生未知错误: {e}")

    async def get_video_info(self, url: str) -> dict:
        """获取视频信息（不下载）"""
        ydl_opts = {
            "outtmpl": "%(id)s",
            "skip_download": True,
        }

        return await asyncio.run_in_executor(
            None,
            lambda: self._get_info_sync(url, ydl_opts)
        )

    def _get_info_sync(self, url: str, ydl_opts: dict) -> dict:
        """同步获取信息"""
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                return ydl.extract_info(url, download=False)
        except Exception as e:
            raise RuntimeError(f"获取YouTube视频信息失败: {e}")
