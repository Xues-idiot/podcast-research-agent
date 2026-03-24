"""并行研究流程图 - 使用LangGraph编排，支持子Agent并行"""

from typing import TypedDict, Optional
import asyncio

from echo.config import config
from echo.subagents import (
    SubAgentExecutor,
    SubAgentTask,
    TaskStatus,
    create_task,
    get_subagent_executor,
)
from echo.subagents.builtins import register_builtin_agents


class ParallelResearchState(TypedDict):
    """并行研究流程状态"""
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
    current_step: str | None
    # 并行任务ID
    parallel_tasks: dict[str, str]  # step_name -> task_id
    # 并行任务结果
    parallel_results: dict[str, dict]


class ParallelResearchGraph:
    """
    并行研究流程图 - 编排完整的研究流程，支持并行执行

    优化后的流程:
    - download -> transcribe (串行，因为有依赖)
    - summarize 和 keypoint (可以并行，都依赖transcript)
    - mindmap (依赖keypoint)
    - link (依赖keypoint，可以和mindmap并行)
    - report (依赖summary, keypoints, mindmap)
    - qa (依赖transcript)

    并行策略:
    - Phase 1: download -> transcribe (串行)
    - Phase 2: summarize || keypoint (并行)
    - Phase 3: mindmap || link (并行，都依赖keypoint)
    - Phase 4: report, qa (并行，依赖不同)
    """

    def __init__(self, max_concurrent: int = 3):
        """初始化并行研究图

        Args:
            max_concurrent: 最大并发子Agent数
        """
        # 初始化执行器
        self.executor = get_subagent_executor()
        self.executor.max_concurrent = max_concurrent

        # 注册内置Agent
        register_builtin_agents(self.executor)

        self.graph = self._build_graph()

    def _build_graph(self) -> "StateGraph":
        """构建流程图"""
        from langgraph.graph import StateGraph, END

        builder = StateGraph(ParallelResearchState)

        # 串行阶段
        builder.add_node("download", self._download_node)
        builder.add_node("transcribe", self._transcribe_node)

        # 并行阶段 1: summarize || keypoint
        builder.add_node("parallel_phase1", self._parallel_phase1_node)
        builder.add_node("summarize", self._summarize_node)
        builder.add_node("keypoint", self._keypoint_node)

        # 并行阶段 2: mindmap || link
        builder.add_node("parallel_phase2", self._parallel_phase2_node)
        builder.add_node("mindmap", self._mindmap_node)
        builder.add_node("link", self._link_node)

        # 最终阶段: report || qa
        builder.add_node("parallel_phase3", self._parallel_phase3_node)
        builder.add_node("report", self._report_node)
        builder.add_node("qa", self._qa_node)

        # 设置入口和边
        builder.set_entry_point("download")
        builder.add_edge("download", "transcribe")
        builder.add_edge("transcribe", "parallel_phase1")

        # Phase 1: summarize 和 keypoint 并行执行
        builder.add_edge("parallel_phase1", "summarize")
        builder.add_edge("parallel_phase1", "keypoint")
        builder.add_edge("summarize", "parallel_phase2")
        builder.add_edge("keypoint", "parallel_phase2")

        # Phase 2: mindmap 和 link 并行执行
        builder.add_edge("parallel_phase2", "mindmap")
        builder.add_edge("parallel_phase2", "link")
        builder.add_edge("mindmap", "parallel_phase3")
        builder.add_edge("link", "parallel_phase3")

        # Phase 3: report 和 qa 并行执行
        builder.add_edge("parallel_phase3", "report")
        builder.add_edge("parallel_phase3", "qa")
        builder.add_edge("report", END)
        builder.add_edge("qa", END)

        return builder.compile()

    async def _download_node(self, state: ParallelResearchState) -> ParallelResearchState:
        """下载节点"""
        state["current_step"] = "download"
        state["parallel_tasks"] = state.get("parallel_tasks", {})
        state["parallel_results"] = state.get("parallel_results", {})

        try:
            from echo.tools.downloader import VideoDownloader
            downloader = VideoDownloader()
            audio_path = await downloader.download(state["url"])
            state["audio_path"] = audio_path
            state["error"] = None
        except Exception as e:
            state["error"] = f"下载失败: {str(e)}"

        return state

    async def _transcribe_node(self, state: ParallelResearchState) -> ParallelResearchState:
        """转录节点"""
        state["current_step"] = "transcribe"

        try:
            audio_path = state.get("audio_path")
            if not audio_path:
                state["error"] = "没有音频文件路径"
                return state

            from echo.agents.transcriber import Transcriber
            transcriber = Transcriber()
            transcript = await transcriber.transcribe(audio_path)
            state["transcript"] = transcript
            state["error"] = None
        except Exception as e:
            state["error"] = f"转录失败: {str(e)}"

        return state

    async def _parallel_phase1_node(self, state: ParallelResearchState) -> ParallelResearchState:
        """并行阶段1节点 - 调度 summarize 和 keypoint 并行任务"""
        state["current_step"] = "parallel_phase1"

        transcript = state.get("transcript")
        if not transcript:
            state["error"] = "没有转录文本"
            return state

        # 创建并行任务
        summarize_task = create_task(
            name="summarize",
            description="生成播客摘要",
            agent_type="summarization",
            input_data={"transcript": transcript},
        )

        keypoint_task = create_task(
            name="keypoint",
            description="提取播客要点",
            agent_type="keypoint",
            input_data={"transcript": transcript, "num": 5},
        )

        # 提交任务
        summarize_id = await self.executor.submit(summarize_task)
        keypoint_id = await self.executor.submit(keypoint_task)

        state["parallel_tasks"]["summarize"] = summarize_id
        state["parallel_tasks"]["keypoint"] = keypoint_id

        return state

    async def _summarize_node(self, state: ParallelResearchState) -> ParallelResearchState:
        """摘要节点 - 从并行任务获取结果"""
        state["current_step"] = "summarize"

        task_id = state["parallel_tasks"].get("summarize")
        if not task_id:
            state["error"] = "没有摘要任务ID"
            return state

        try:
            result = await self.executor.wait_for(task_id)
            if result.status == TaskStatus.COMPLETED:
                state["summary"] = result.result
                state["error"] = None
            else:
                state["error"] = f"摘要任务失败: {result.error}"
        except Exception as e:
            state["error"] = f"获取摘要结果失败: {str(e)}"

        return state

    async def _keypoint_node(self, state: ParallelResearchState) -> ParallelResearchState:
        """要点节点 - 从并行任务获取结果"""
        state["current_step"] = "keypoint"

        task_id = state["parallel_tasks"].get("keypoint")
        if not task_id:
            state["error"] = "没有要点任务ID"
            return state

        try:
            result = await self.executor.wait_for(task_id)
            if result.status == TaskStatus.COMPLETED:
                state["keypoints"] = result.result
                state["error"] = None
            else:
                state["error"] = f"要点任务失败: {result.error}"
        except Exception as e:
            state["error"] = f"获取要点结果失败: {str(e)}"

        return state

    async def _parallel_phase2_node(self, state: ParallelResearchState) -> ParallelResearchState:
        """并行阶段2节点 - 调度 mindmap 和 link 并行任务"""
        state["current_step"] = "parallel_phase2"

        keypoints = state.get("keypoints")
        if not keypoints:
            state["error"] = "没有要点"
            return state

        # 创建并行任务
        mindmap_task = create_task(
            name="mindmap",
            description="生成思维导图",
            agent_type="mindmap",
            input_data={"keypoints": keypoints},
        )

        link_task = create_task(
            name="link",
            description="知识关联",
            agent_type="knowledge_link",
            input_data={"keypoints": keypoints},
        )

        # 提交任务
        mindmap_id = await self.executor.submit(mindmap_task)
        link_id = await self.executor.submit(link_task)

        state["parallel_tasks"]["mindmap"] = mindmap_id
        state["parallel_tasks"]["link"] = link_id

        return state

    async def _mindmap_node(self, state: ParallelResearchState) -> ParallelResearchState:
        """思维导图节点 - 从并行任务获取结果"""
        state["current_step"] = "mindmap"

        task_id = state["parallel_tasks"].get("mindmap")
        if not task_id:
            state["error"] = "没有思维导图任务ID"
            return state

        try:
            result = await self.executor.wait_for(task_id)
            if result.status == TaskStatus.COMPLETED:
                state["mindmap"] = result.result
                state["error"] = None
            else:
                state["error"] = f"思维导图任务失败: {result.error}"
        except Exception as e:
            state["error"] = f"获取思维导图结果失败: {str(e)}"

        return state

    async def _link_node(self, state: ParallelResearchState) -> ParallelResearchState:
        """知识关联节点 - 从并行任务获取结果"""
        state["current_step"] = "link"

        task_id = state["parallel_tasks"].get("link")
        if not task_id:
            state["error"] = "没有知识关联任务ID"
            return state

        try:
            result = await self.executor.wait_for(task_id)
            if result.status == TaskStatus.COMPLETED:
                state["knowledge_cards"] = result.result
                state["error"] = None
            else:
                state["error"] = f"知识关联任务失败: {result.error}"
        except Exception as e:
            state["error"] = f"获取知识关联结果失败: {str(e)}"

        return state

    async def _parallel_phase3_node(self, state: ParallelResearchState) -> ParallelResearchState:
        """并行阶段3节点 - 调度 report 和 qa 并行任务"""
        state["current_step"] = "parallel_phase3"

        summary = state.get("summary")
        keypoints = state.get("keypoints")
        mindmap = state.get("mindmap")
        transcript = state.get("transcript")

        if not all([summary, keypoints, mindmap]):
            state["error"] = "缺少报告生成所需素材"
            return state

        if not transcript:
            state["error"] = "没有转录文本"
            return state

        # 创建并行任务
        report_task = create_task(
            name="report",
            description="生成研究报告",
            agent_type="report",
            input_data={
                "summary": summary,
                "keypoints": keypoints,
                "mindmap": mindmap,
            },
        )

        qa_task = create_task(
            name="qa",
            description="生成问答对",
            agent_type="qa",
            input_data={"transcript": transcript, "num": 5},
        )

        # 提交任务
        report_id = await self.executor.submit(report_task)
        qa_id = await self.executor.submit(qa_task)

        state["parallel_tasks"]["report"] = report_id
        state["parallel_tasks"]["qa"] = qa_id

        return state

    async def _report_node(self, state: ParallelResearchState) -> ParallelResearchState:
        """报告节点 - 从并行任务获取结果"""
        state["current_step"] = "report"

        task_id = state["parallel_tasks"].get("report")
        if not task_id:
            state["error"] = "没有报告任务ID"
            return state

        try:
            result = await self.executor.wait_for(task_id)
            if result.status == TaskStatus.COMPLETED:
                state["report"] = result.result
                state["error"] = None
            else:
                state["error"] = f"报告任务失败: {result.error}"
        except Exception as e:
            state["error"] = f"获取报告结果失败: {str(e)}"

        return state

    async def _qa_node(self, state: ParallelResearchState) -> ParallelResearchState:
        """问答节点 - 从并行任务获取结果"""
        state["current_step"] = "qa"

        task_id = state["parallel_tasks"].get("qa")
        if not task_id:
            state["error"] = "没有问答任务ID"
            return state

        try:
            result = await self.executor.wait_for(task_id)
            if result.status == TaskStatus.COMPLETED:
                state["qa_pairs"] = result.result
                state["error"] = None
            else:
                state["error"] = f"问答任务失败: {result.error}"
        except Exception as e:
            state["error"] = f"获取问答结果失败: {str(e)}"

        return state

    async def astream(self, url: str):
        """
        异步流式执行流程

        Args:
            url: 视频URL
        """
        initial_state = ParallelResearchState(
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
            current_step=None,
            parallel_tasks={},
            parallel_results={},
        )

        async for state in self.graph.astream(initial_state):
            yield state

    async def run(self, url: str) -> ParallelResearchState:
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
_default_parallel_graph: ParallelResearchGraph | None = None


def get_parallel_research_graph(max_concurrent: int = 3) -> ParallelResearchGraph:
    """获取全局并行研究图实例"""
    global _default_parallel_graph
    if _default_parallel_graph is None:
        _default_parallel_graph = ParallelResearchGraph(max_concurrent)
    return _default_parallel_graph
