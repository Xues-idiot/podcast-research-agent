"""Echo 客户端 - 异步上下文管理器"""

import asyncio
from contextlib import asynccontextmanager
from typing import AsyncIterator

from echo.config import config
from echo.agents.transcriber import Transcriber
from echo.agents.summarizer import Summarizer
from echo.agents.keypoint import KeyPointGenerator
from echo.agents.linker import KnowledgeLinker
from echo.agents.mindmap import MindMapGenerator
from echo.agents.report import ReportGenerator
from echo.agents.qa import QAGenerator
from echo.tools.downloader import VideoDownloader


class EchoClient:
    """
    Echo 播客研究Agent主客户端

    使用方式:
        async with EchoClient() as client:
            result = await client.research("https://b23.tv/xxx")
    """

    def __init__(self):
        self.transcriber = Transcriber()
        self.summarizer = Summarizer(config.minimax)
        self.keypoint_gen = KeyPointGenerator(config.minimax)
        self.linker = KnowledgeLinker(config.tavily)
        self.mindmap_gen = MindMapGenerator(config.minimax)
        self.report_gen = ReportGenerator(config.minimax)
        self.qa_gen = QAGenerator(config.minimax)
        self.downloader = VideoDownloader()

    async def research(self, url: str, num_keypoints: int = 5) -> dict:
        """
        研究播客/视频

        Args:
            url: 视频/播客链接
            num_keypoints: 生成的要点数量

        Returns:
            包含 transcript, summary, keypoints, mindmap, knowledge_cards, report 的字典
        """
        # 1. 下载音视频
        audio_path = await self.downloader.download(url)

        # 2. 转录
        transcript = await self.transcriber.transcribe(audio_path)

        # 3. 摘要
        summary = await self.summarizer.summarize(transcript)

        # 4. 要点提取
        keypoints = await self.keypoint_gen.generate(transcript, num_keypoints)

        # 5. 思维导图
        mindmap = await self.mindmap_gen.generate(keypoints)

        # 6. 知识关联
        knowledge_cards = await self.linker.link(keypoints)

        # 7. 报告生成
        report = await self.report_gen.generate(summary, keypoints, mindmap)

        # 8. 问答生成
        qa_pairs = await self.qa_gen.generate(transcript, num_keypoints)

        return {
            "transcript": transcript,
            "summary": summary,
            "keypoints": keypoints,
            "mindmap": mindmap,
            "knowledge_cards": knowledge_cards,
            "report": report,
            "qa_pairs": qa_pairs,
        }

    async def close(self):
        """关闭客户端，清理资源"""
        await self.downloader.close()


@asynccontextmanager
async def EchoClientContext() -> AsyncIterator[EchoClient]:
    """Echo 客户端异步上下文管理器"""
    client = EchoClient()
    try:
        yield client
    finally:
        await client.close()
