"""Echo 客户端 - 异步上下文管理器"""

import asyncio
import hashlib
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
from echo.agents.rag_agent import ResearchRAGAgent, AgentConfig
from echo.tools.downloader import VideoDownloader
from echo.knowledge import EntryStore, TextSplitter
from echo.memory import MemoryUpdater, MemoryStore
from echo.audio_overview import AudioOverviewGenerator, AudioStyle


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

        # 知识库组件
        self.entry_store = EntryStore()
        self.splitter = TextSplitter(chunk_size=500, chunk_overlap=50)

        # RAG Agent (用于深度研究)
        self.research_rag_agent = ResearchRAGAgent(
            config=AgentConfig(model_name=config.minimax.model),
        )

        # 记忆系统
        self.memory_store = MemoryStore()
        self.memory_updater = MemoryUpdater(self.memory_store)

        # 音频概览生成器
        self.audio_overview_gen = AudioOverviewGenerator(config.minimax)

    async def research(self, url: str, num_keypoints: int = 5) -> dict:
        """
        研究播客/视频

        Args:
            url: 视频/播客链接
            num_keypoints: 生成的要点数量

        Returns:
            包含 transcript, summary, keypoints, mindmap, knowledge_cards, report, audio_overview, entries 的字典
        """
        podcast_id = self._extract_podcast_id(url)

        # 1. 下载音视频
        audio_path = await self.downloader.download(url)

        # 2. 转录
        transcript = await self.transcriber.transcribe(audio_path)

        # 3. 创建 Entry 用于知识检索
        entries = await self._create_entries(podcast_id, transcript)

        # 4. 摘要
        summary = await self.summarizer.summarize(transcript)

        # 5. 要点提取
        keypoints = await self.keypoint_gen.generate(transcript, num_keypoints)

        # 6. 思维导图
        mindmap = await self.mindmap_gen.generate(keypoints)

        # 7. 知识关联
        knowledge_cards = await self.linker.link(keypoints)

        # 8. 报告生成
        report = await self.report_gen.generate(summary, keypoints, mindmap)

        # 9. 问答生成
        qa_pairs = await self.qa_gen.generate(transcript, num_keypoints)

        # 10. 音频概览生成 (NotebookLM风格)
        audio_overview_script = await self.audio_overview_gen.generate(
            transcript=transcript,
            summary=summary,
            keypoints=keypoints,
        )
        # 转换为可序列化的字典格式
        audio_overview = {
            "title": audio_overview_script.title,
            "script": self.audio_overview_gen.script_to_text(audio_overview_script),
            "segments": [
                {
                    "speaker": seg.speaker,
                    "content": seg.content,
                    "duration_seconds": seg.duration_seconds,
                }
                for seg in audio_overview_script.segments
            ],
            "total_duration_seconds": audio_overview_script.total_duration_seconds,
            "style": audio_overview_script.style.value,
        }

        # 11. 更新记忆 (学习用户偏好)
        await self.memory_updater.learn_research_topic(
            user_id="default",
            topic=summary.get("title", "播客内容"),
        )

        return {
            "transcript": transcript,
            "summary": summary,
            "keypoints": keypoints,
            "mindmap": mindmap,
            "knowledge_cards": knowledge_cards,
            "report": report,
            "qa_pairs": qa_pairs,
            "audio_overview": audio_overview,
            "entries": [e.to_dict() for e in entries],
            "podcast_id": podcast_id,
        }

    async def _create_entries(self, podcast_id: str, transcript) -> list:
        """从转录创建知识库 Entry"""
        try:
            segments = transcript.get("segments", [])
            if not segments:
                return []

            # 使用 TextSplitter 分割转录
            entry_data = self.splitter.split_transcript(
                podcast_id=podcast_id,
                transcript_segments=segments,
                min_duration=30.0,
                max_duration=120.0,
            )

            # 添加到存储
            entries = self.entry_store.add_entries(podcast_id, entry_data)
            return entries
        except Exception as e:
            print(f"创建Entry失败: {e}")
            return []

    def _extract_podcast_id(self, url: str) -> str:
        """从URL提取播客ID"""
        return hashlib.md5(url.encode()).hexdigest()[:12]

    async def research_with_rag(
        self,
        query: str,
        podcast_content: str,
        podcast_id: str = None,
    ) -> dict:
        """
        使用 ResearchRAGAgent 进行研究查询

        Args:
            query: 研究查询
            podcast_content: 播客内容
            podcast_id: 播客ID

        Returns:
            研究响应
        """
        result = await self.research_rag_agent.research_query(
            query=query,
            podcast_content=podcast_content,
            podcast_id=podcast_id,
        )
        return {
            "answer": result.answer,
            "citations": result.citations,
            "sources": result.sources,
            "retrieved_context": result.retrieved_context,
        }

    async def get_entries(self, podcast_id: str) -> list:
        """获取播客的Entries"""
        return self.entry_store.get_entries(podcast_id)

    async def search_entries(self, podcast_id: str, query: str, top_k: int = 5) -> list:
        """搜索Entries"""
        entries = self.entry_store.get_entries(podcast_id)
        if not entries:
            return []

        # 使用 Bi-encoder 进行向量检索
        from echo.knowledge import BiEncoder
        encoder = BiEncoder()
        texts = [e.compiled for e in entries]
        results = encoder.search(query=query, entries=entries, top_k=top_k)
        return [(e.to_dict(), score) for e, score in results]

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
