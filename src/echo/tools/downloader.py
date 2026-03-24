"""视频下载器 - 统一下载接口"""

import asyncio
from pathlib import Path
from urllib.parse import urlparse

import yt_dlp

from echo.tools.bilibili import BilibiliDownloader
from echo.tools.youtube import YouTubeDownloader
from echo.tools.douyin import DouyinDownloader
from echo.tools.wechat import WechatDownloader
from echo.tools.xiaohongshu import XiaohongshuDownloader


class VideoDownloader:
    """
    统一视频下载器 - 根据URL类型调用对应下载器

    支持平台:
    - B站 (bilibili.com, b23.tv)
    - YouTube (youtube.com, youtu.be)
    - 抖音/火山 (douyin.com, huoshan.com)
    - 微信 (mp.weixin.qq.com, channels.weixin.qq.com)
    - 小红书 (xiaohongshu.com, xhslink.com)
    - 通用RSS
    """

    def __init__(self, output_dir: str = "./downloads"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.downloaders = {
            "bilibili": BilibiliDownloader(output_dir),
            "youtube": YouTubeDownloader(output_dir),
            "douyin": DouyinDownloader(output_dir),
            "wechat": WechatDownloader(output_dir),
            "xiaohongshu": XiaohongshuDownloader(output_dir),
        }

    async def download(self, url: str) -> str:
        """
        下载视频/音频

        Args:
            url: 视频URL

        Returns:
            下载后的音频文件路径
        """
        parsed = urlparse(url)
        domain = parsed.netloc.lower()

        # B站
        if "bilibili.com" in domain or "b23.tv" in domain:
            return await self.downloaders["bilibili"].download(url)

        # YouTube
        if "youtube.com" in domain or "youtu.be" in domain:
            return await self.downloaders["youtube"].download(url)

        # 抖音/火山
        if "douyin.com" in domain or "huoshan.com" in domain:
            return await self.downloaders["douyin"].download(url)

        # 微信
        if "weixin.qq.com" in domain or "channels.weixin.qq.com" in domain:
            return await self.downloaders["wechat"].download(url)

        # 小红书
        if "xiaohongshu.com" in domain or "xhslink.com" in domain:
            return await self.downloaders["xiaohongshu"].download(url)

        # 通用下载
        return await self._generic_download(url)

    async def _generic_download(self, url: str) -> str:
        """通用下载（使用yt-dlp）"""
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": str(self.output_dir / "%(title)s.%(ext)s"),
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
            }],
        }

        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(
            None,
            lambda: self._download_sync(url, ydl_opts)
        )
        return result

    def _download_sync(self, url: str, ydl_opts: dict) -> str:
        """同步下载（在线程池中运行）"""
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            # 转换后的mp3文件名
            mp3_name = Path(filename).stem + ".mp3"
            return str(self.output_dir / mp3_name)

    async def close(self):
        """关闭下载器"""
        pass  # 目前无需清理
