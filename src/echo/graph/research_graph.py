"""研究流程图 - 使用LangGraph编排"""

from typing import TypedDict

from echo.config import config
from echo.agents.transcriber import Transcriber
from echo.agents.summarizer import Summarizer
from echo.agents.keypoint import KeyPointGenerator
from echo.agents.linker import KnowledgeLinker
from echo.agents.mindmap import MindMapGenerator
from echo.agents.report import ReportGenerator
from echo.agents.qa import QAGenerator
from echo.tools.downloader import VideoDownloader


class ResearchState(TypedDict):
    """研究流程状态"""
    url: str
    audio_path: str | None
    transcript: dict | None
    summary: dict | None
    keypoints: list | None
    mindmap: dict | None
    knowledge_cards: list | None
    report: dict | None
    qa_pairs: list | None
    error: str | None


class ResearchGraph:
    """
    研究流程图 - 编排完整的研究流程

    流程:
    download -> transcribe -> summarize -> keypoint -> mindmap -> link -> report -> qa -> output
    """

    def __init__(self):
        # 初始化各组件
        self.transcriber = Transcriber()
        self.summarizer = Summarizer(config.minimax)
        self.keypoint_gen = KeyPointGenerator(config.minimax)
        self.linker = KnowledgeLinker(config.tavily)
        self.mindmap_gen = MindMapGenerator(config.minimax)
        self.report_gen = ReportGenerator(config.minimax)
        self.qa_gen = QAGenerator(config.minimax)
        self.downloader = VideoDownloader()

        self.graph = self._build_graph()

    def _build_graph(self) -> "StateGraph":
        """构建流程图"""
        from langgraph.graph import StateGraph, END

        builder = StateGraph(ResearchState)

        # 添加节点
        builder.add_node("download", self._download_node)
        builder.add_node("transcribe", self._transcribe_node)
        builder.add_node("summarize", self._summarize_node)
        builder.add_node("keypoint", self._keypoint_node)
        builder.add_node("mindmap", self._mindmap_node)
        builder.add_node("link", self._link_node)
        builder.add_node("report", self._report_node)
        builder.add_node("qa", self._qa_node)

        # 设置入口和结束
        builder.set_entry_point("download")
        builder.add_edge("download", "transcribe")
        builder.add_edge("transcribe", "summarize")
        builder.add_edge("summarize", "keypoint")
        builder.add_edge("keypoint", "mindmap")
        builder.add_edge("mindmap", "link")
        builder.add_edge("link", "report")
        builder.add_edge("report", "qa")
        builder.add_edge("qa", END)

        return builder.compile()

    async def _download_node(self, state: ResearchState) -> ResearchState:
        """下载节点"""
        try:
            url = state["url"]
            audio_path = await self.downloader.download(url)
            state["audio_path"] = audio_path
            state["error"] = None
        except Exception as e:
            state["error"] = f"下载失败: {str(e)}"
        return state

    async def _transcribe_node(self, state: ResearchState) -> ResearchState:
        """转录节点"""
        try:
            audio_path = state.get("audio_path")
            if not audio_path:
                state["error"] = "没有音频文件路径"
                return state

            transcript = await self.transcriber.transcribe(audio_path)
            state["transcript"] = transcript
            state["error"] = None
        except Exception as e:
            state["error"] = f"转录失败: {str(e)}"
        return state

    async def _summarize_node(self, state: ResearchState) -> ResearchState:
        """摘要节点"""
        try:
            transcript = state.get("transcript")
            if not transcript:
                state["error"] = "没有转录文本"
                return state

            summary = await self.summarizer.summarize(transcript)
            state["summary"] = summary
            state["error"] = None
        except Exception as e:
            state["error"] = f"摘要失败: {str(e)}"
        return state

    async def _keypoint_node(self, state: ResearchState) -> ResearchState:
        """要点节点"""
        try:
            transcript = state.get("transcript")
            if not transcript:
                state["error"] = "没有转录文本"
                return state

            keypoints = await self.keypoint_gen.generate(transcript, num=5)
            state["keypoints"] = keypoints
            state["error"] = None
        except Exception as e:
            state["error"] = f"要点提取失败: {str(e)}"
        return state

    async def _mindmap_node(self, state: ResearchState) -> ResearchState:
        """思维导图节点"""
        try:
            keypoints = state.get("keypoints")
            if not keypoints:
                state["error"] = "没有要点"
                return state

            mindmap = await self.mindmap_gen.generate(keypoints)
            state["mindmap"] = mindmap
            state["error"] = None
        except Exception as e:
            state["error"] = f"思维导图生成失败: {str(e)}"
        return state

    async def _link_node(self, state: ResearchState) -> ResearchState:
        """知识关联节点"""
        try:
            keypoints = state.get("keypoints")
            if not keypoints:
                state["error"] = "没有要点"
                return state

            knowledge_cards = await self.linker.link(keypoints)
            state["knowledge_cards"] = knowledge_cards
            state["error"] = None
        except Exception as e:
            state["error"] = f"知识关联失败: {str(e)}"
        return state

    async def _report_node(self, state: ResearchState) -> ResearchState:
        """报告生成节点"""
        try:
            summary = state.get("summary")
            keypoints = state.get("keypoints")
            mindmap = state.get("mindmap")

            if not summary or not keypoints or not mindmap:
                state["error"] = "缺少生成报告所需的素材"
                return state

            report = await self.report_gen.generate(
                summary=summary,
                keypoints=keypoints,
                mindmap=mindmap,
            )
            state["report"] = report
            state["error"] = None
        except Exception as e:
            state["error"] = f"报告生成失败: {str(e)}"
        return state

    async def _qa_node(self, state: ResearchState) -> ResearchState:
        """问答生成节点"""
        try:
            transcript = state.get("transcript")
            if not transcript:
                state["error"] = "没有转录文本"
                return state

            qa_pairs = await self.qa_gen.generate(transcript, num=5)
            state["qa_pairs"] = qa_pairs
            state["error"] = None
        except Exception as e:
            state["error"] = f"问答生成失败: {str(e)}"
        return state

    async def astream(self, url: str):
        """
        异步流式执行流程

        Args:
            url: 视频URL
        """
        initial_state = ResearchState(
            url=url,
            audio_path=None,
            transcript=None,
            summary=None,
            keypoints=None,
            mindmap=None,
            knowledge_cards=None,
            report=None,
            qa_pairs=None,
            error=None,
        )

        async for state in self.graph.astream(initial_state):
            yield state

    async def run(self, url: str) -> ResearchState:
        """
        执行完整流程

        Args:
            url: 视频URL

        Returns:
            最终状态
        """
        result = None
        async for state in self.astream(url):
            result = state

        return result or {}


# 全局实例
_default_graph: ResearchGraph | None = None


def get_research_graph() -> ResearchGraph:
    """获取全局研究图实例"""
    global _default_graph
    if _default_graph is None:
        _default_graph = ResearchGraph()
    return _default_graph
