"""转录Agent - 使用Whisper进行音频转文字"""

import asyncio
import whisper
from pathlib import Path


class Transcriber:
    """
    转录Agent - 将音频/视频转为文字

    使用OpenAI Whisper模型进行本地转录
    """

    def __init__(self, model_name: str = "base"):
        """
        初始化转录Agent

        Args:
            model_name: Whisper模型大小 (tiny, base, small, medium, large)
        """
        self.model_name = model_name
        self.model = None

    def _get_model(self):
        """懒加载Whisper模型"""
        if self.model is None:
            self.model = whisper.load_model(self.model_name)
        return self.model

    async def transcribe(self, audio_path: str) -> dict:
        """
        转录音频文件

        Args:
            audio_path: 音频文件路径

        Returns:
            包含 text, segments, language 的字典
        """
        model = self._get_model()
        # 使用 run_in_executor 避免阻塞事件循环
        result = await asyncio.run_in_executor(
            None,
            lambda: model.transcribe(str(audio_path), language="zh")
        )

        return {
            "text": result["text"],
            "segments": result.get("segments", []),
            "language": result.get("language", "zh"),
        }

    async def transcribe_from_url(self, url: str) -> dict:
        """
        从URL下载并转录

        Args:
            url: 视频URL

        Returns:
            转录结果
        """
        from echo.tools.downloader import AudioDownloader

        downloader = AudioDownloader()
        audio_path = await downloader.download(url)

        return await self.transcribe(audio_path)
