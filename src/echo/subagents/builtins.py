"""子Agent内置实现"""

import asyncio
from typing import Any

from echo.subagents import BaseSubAgent


class TranscriptionAgent(BaseSubAgent):
    """转录Agent - 专门负责音频转录"""

    @property
    def agent_type(self) -> str:
        return "transcription"

    async def execute(self, input_data: dict) -> dict:
        """执行转录

        Args:
            input_data: 包含 audio_path 的字典

        Returns:
            转录结果
        """
        from echo.agents.transcriber import Transcriber

        audio_path = input_data.get("audio_path")
        if not audio_path:
            raise ValueError("audio_path is required")

        transcriber = Transcriber()
        result = await transcriber.transcribe(audio_path)

        return result


class SummarizationAgent(BaseSubAgent):
    """摘要Agent - 专门负责生成摘要"""

    @property
    def agent_type(self) -> str:
        return "summarization"

    async def execute(self, input_data: dict) -> dict:
        """执行摘要生成

        Args:
            input_data: 包含 transcript 的字典

        Returns:
            摘要结果
        """
        from echo.agents.summarizer import Summarizer
        from echo.config import config

        transcript = input_data.get("transcript")
        if not transcript:
            raise ValueError("transcript is required")

        summarizer = Summarizer(config.minimax)
        result = await summarizer.summarize(transcript)

        return result


class KeyPointAgent(BaseSubAgent):
    """要点Agent - 专门负责提取要点"""

    @property
    def agent_type(self) -> str:
        return "keypoint"

    async def execute(self, input_data: dict) -> dict:
        """执行要点提取

        Args:
            input_data: 包含 transcript 和 num 的字典

        Returns:
            要点列表
        """
        from echo.agents.keypoint import KeyPointGenerator
        from echo.config import config

        transcript = input_data.get("transcript")
        if not transcript:
            raise ValueError("transcript is required")

        num = input_data.get("num", 5)

        keypoint_gen = KeyPointGenerator(config.minimax)
        result = await keypoint_gen.generate(transcript, num=num)

        return result


class MindMapAgent(BaseSubAgent):
    """思维导图Agent - 专门负责生成思维导图"""

    @property
    def agent_type(self) -> str:
        return "mindmap"

    async def execute(self, input_data: dict) -> dict:
        """执行思维导图生成

        Args:
            input_data: 包含 keypoints 的字典

        Returns:
            思维导图数据
        """
        from echo.agents.mindmap import MindMapGenerator
        from echo.config import config

        keypoints = input_data.get("keypoints")
        if not keypoints:
            raise ValueError("keypoints is required")

        mindmap_gen = MindMapGenerator(config.minimax)
        result = await mindmap_gen.generate(keypoints)

        return result


class KnowledgeLinkAgent(BaseSubAgent):
    """知识关联Agent - 专门负责知识关联"""

    @property
    def agent_type(self) -> str:
        return "knowledge_link"

    async def execute(self, input_data: dict) -> dict:
        """执行知识关联

        Args:
            input_data: 包含 keypoints 的字典

        Returns:
            知识卡片列表
        """
        from echo.agents.linker import KnowledgeLinker
        from echo.config import config

        keypoints = input_data.get("keypoints")
        if not keypoints:
            raise ValueError("keypoints is required")

        linker = KnowledgeLinker(config.tavily)
        result = await linker.link(keypoints)

        return result


class ReportAgent(BaseSubAgent):
    """报告Agent - 专门负责生成报告"""

    @property
    def agent_type(self) -> str:
        return "report"

    async def execute(self, input_data: dict) -> dict:
        """执行报告生成

        Args:
            input_data: 包含 summary, keypoints, mindmap 的字典

        Returns:
            报告内容
        """
        from echo.agents.report import ReportGenerator
        from echo.config import config

        summary = input_data.get("summary")
        keypoints = input_data.get("keypoints")
        mindmap = input_data.get("mindmap")

        if not all([summary, keypoints, mindmap]):
            raise ValueError("summary, keypoints, and mindmap are required")

        report_gen = ReportGenerator(config.minimax)
        result = await report_gen.generate(
            summary=summary,
            keypoints=keypoints,
            mindmap=mindmap,
        )

        return result


class QAAgent(BaseSubAgent):
    """问答Agent - 专门负责生成问答对"""

    @property
    def agent_type(self) -> str:
        return "qa"

    async def execute(self, input_data: dict) -> dict:
        """执行问答生成

        Args:
            input_data: 包含 transcript 和 num 的字典

        Returns:
            问答对列表
        """
        from echo.agents.qa import QAGenerator
        from echo.config import config

        transcript = input_data.get("transcript")
        if not transcript:
            raise ValueError("transcript is required")

        num = input_data.get("num", 5)

        qa_gen = QAGenerator(config.minimax)
        result = await qa_gen.generate(transcript, num=num)

        return result


class DownloadAgent(BaseSubAgent):
    """下载Agent - 专门负责音视频下载"""

    @property
    def agent_type(self) -> str:
        return "download"

    async def execute(self, input_data: dict) -> dict:
        """执行下载

        Args:
            input_data: 包含 url 的字典

        Returns:
            下载结果，包含 audio_path
        """
        from echo.tools.downloader import VideoDownloader

        url = input_data.get("url")
        if not url:
            raise ValueError("url is required")

        downloader = VideoDownloader()
        audio_path = await downloader.download(url)

        return {"audio_path": audio_path}


def register_builtin_agents(executor):
    """注册所有内置Agent

    Args:
        executor: SubAgentExecutor实例
    """
    executor.register_agent(TranscriptionAgent)
    executor.register_agent(SummarizationAgent)
    executor.register_agent(KeyPointAgent)
    executor.register_agent(MindMapAgent)
    executor.register_agent(KnowledgeLinkAgent)
    executor.register_agent(ReportAgent)
    executor.register_agent(QAAgent)
    executor.register_agent(DownloadAgent)
