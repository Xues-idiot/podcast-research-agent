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
            raise RuntimeError(f"B站下载失败: {e}")
        except Exception as e:
            raise RuntimeError(f"B站下载时发生未知错误: {e}")

    async def get_video_info(self, url: str) -> dict:
        """获取视频信息（不下载）"""
        ydl_opts = {
            "outtmpl": "%(id)s",
            "skip_download": True,
        }

        info = await asyncio.run_in_executor(
            None,
            lambda: self._get_info_sync(url, ydl_opts)
        )
        return info

    def _get_info_sync(self, url: str, ydl_opts: dict) -> dict:
        """同步获取信息"""
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                return ydl.extract_info(url, download=False)
        except Exception as e:
            raise RuntimeError(f"获取B站视频信息失败: {e}")
