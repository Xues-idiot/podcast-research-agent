"""研究API - FastAPI路由"""

import asyncio
import time
import uuid
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from io import BytesIO
from typing import Any, AsyncIterator, Optional

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse, Response
from pydantic import BaseModel

from echo.client import EchoClient
from echo.graph.research_graph import ResearchGraph, get_research_graph


# 简单的内存限流器
class RateLimiter:
    """基于时间的简单限流器"""

    def __init__(self, max_requests: int = 10, window_seconds: int = 60):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self._requests: dict[str, list[float]] = {}

    def is_allowed(self, client_id: str) -> bool:
        """检查是否允许请求"""
        now = time.time()
        window_start = now - self.window_seconds

        # 获取或初始化客户端请求记录
        if client_id not in self._requests:
            self._requests[client_id] = []

        # 清理过期的请求记录
        self._requests[client_id] = [
            t for t in self._requests[client_id] if t > window_start
        ]

        # 检查是否超过限制
        if len(self._requests[client_id]) >= self.max_requests:
            return False

        # 记录本次请求
        self._requests[client_id].append(now)
        return True

    def get_retry_after(self, client_id: str) -> int:
        """获取重试间隔秒数"""
        if client_id not in self._requests or not self._requests[client_id]:
            return 0

        oldest = min(self._requests[client_id])
        elapsed = time.time() - oldest
        return max(0, int(self.window_seconds - elapsed))


# 全局限流器实例 (生产环境应使用Redis)
rate_limiter = RateLimiter(max_requests=10, window_seconds=60)


router = APIRouter(prefix="/api/research", tags=["research"])


@router.get("/status/health")
async def health_check():
    """健康检查端点"""
    return {"status": "healthy"}


class TaskStatus(str, Enum):
    """任务状态"""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class ResearchTask:
    """研究任务"""
    id: str
    url: str
    num_keypoints: int
    status: TaskStatus
    created_at: datetime
    result: dict | None = None
    error: str | None = None


# 任务存储 (生产环境应使用Redis等)
_tasks: dict[str, ResearchTask] = {}


class StartRequest(BaseModel):
    """开始请求"""
    url: str
    num_keypoints: int = 5


class StartResponse(BaseModel):
    """开始响应"""
    task_id: str
    status: str


class StatusResponse(BaseModel):
    """状态响应"""
    task_id: str
    status: str
    created_at: str | None = None
    error: str | None = None


@router.post("/start", response_model=StartResponse)
async def start_research(request: StartRequest, http_request: Request):
    """
    开始研究任务

    Args:
        request: 包含url和num_keypoints的请求体

    Returns:
        任务ID和状态

    限流: 每分钟最多10次请求
    """
    # 获取客户端标识
    client_ip = http_request.client.host if http_request.client else "unknown"
    forwarded = http_request.headers.get("x-forwarded-for")
    if forwarded:
        client_ip = forwarded.split(",")[0].strip()

    # 检查限流
    if not rate_limiter.is_allowed(client_ip):
        retry_after = rate_limiter.get_retry_after(client_ip)
        return JSONResponse(
            status_code=429,
            content={"error": "请求过于频繁，请稍后再试", "retry_after": retry_after},
            headers={"Retry-After": str(retry_after)},
        )

    task_id = str(uuid.uuid4())[:8]

    task = ResearchTask(
        id=task_id,
        url=request.url,
        num_keypoints=request.num_keypoints,
        status=TaskStatus.PENDING,
        created_at=datetime.now(),
    )
    _tasks[task_id] = task

    # 后台启动任务
    asyncio.create_task(_run_research(task_id, request.url, request.num_keypoints))

    return StartResponse(task_id=task_id, status="pending")


async def _run_research(task_id: str, url: str, num_keypoints: int):
    """后台运行研究"""
    task = _tasks.get(task_id)
    if not task:
        return

    task.status = TaskStatus.RUNNING

    try:
        async with EchoClient() as client:
            result = await client.research(url, num_keypoints)
            task.result = result
            task.status = TaskStatus.COMPLETED
    except Exception as e:
        task.error = str(e)
        task.status = TaskStatus.FAILED


@router.get("/status/{task_id}", response_model=StatusResponse)
async def get_status(task_id: str):
    """
    获取任务状态

    Args:
        task_id: 任务ID

    Returns:
        状态信息
    """
    task = _tasks.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return StatusResponse(
        task_id=task.id,
        status=task.status.value,
        created_at=task.created_at.isoformat(),
        error=task.error,
    )


@router.get("/result/{task_id}")
async def get_result(task_id: str):
    """
    获取任务结果

    Args:
        task_id: 任务ID

    Returns:
        研究结果
    """
    task = _tasks.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if task.status == TaskStatus.PENDING or task.status == TaskStatus.RUNNING:
        raise HTTPException(status_code=202, detail="Task not completed yet")

    if task.status == TaskStatus.FAILED:
        raise HTTPException(status_code=500, detail=task.error)

    return task.result


@router.get("/tasks")
async def list_tasks():
    """
    列出所有任务

    Returns:
        任务列表
    """
    return {
        "tasks": [
            {
                "task_id": t.id,
                "url": t.url,
                "status": t.status.value,
                "created_at": t.created_at.isoformat(),
            }
            for t in _tasks.values()
        ]
    }


@router.delete("/{task_id}")
async def delete_task(task_id: str):
    """
    删除任务

    Args:
        task_id: 任务ID
    """
    if task_id not in _tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    del _tasks[task_id]
    return {"deleted": task_id}


# 流式API - SSE (Server-Sent Events)
@router.post("/stream")
async def stream_research(request: StartRequest, http_request: Request):
    """
    流式研究（返回实时状态）

    使用Server-Sent Events实现流式输出，
    前端可以通过EventSource接收实时进度和结果

    限流: 每分钟最多10次请求
    """
    # 获取客户端标识 (使用 IP 或 X-Forwarded-For)
    client_ip = http_request.client.host if http_request.client else "unknown"
    forwarded = http_request.headers.get("x-forwarded-for")
    if forwarded:
        client_ip = forwarded.split(",")[0].strip()

    # 检查限流
    if not rate_limiter.is_allowed(client_ip):
        retry_after = rate_limiter.get_retry_after(client_ip)
        return JSONResponse(
            status_code=429,
            content={"error": "请求过于频繁，请稍后再试", "retry_after": retry_after},
            headers={"Retry-After": str(retry_after)},
        )
    from fastapi.responses import StreamingResponse
    import json
    import asyncio

    graph = get_research_graph()

    async def event_generator():
        """SSE事件生成器"""
        steps = ["download", "transcribe", "summarize", "keypoint", "mindmap", "link", "report", "qa"]

        try:
            async for state in graph.astream(request.url):
                # 确定当前步骤
                step = state.get("current_step", "")
                step_index = steps.index(step) if step in steps else 0
                progress = min((step_index / len(steps)) * 100, 99)

                # 发送进度更新
                yield f"data: {json.dumps({
                    'type': 'progress',
                    'step': step,
                    'progress': progress,
                    'error': state.get("error", None)
                })}\n\n"

                # 如果完成，发送最终结果
                if state.get("transcript") and state.get("summary"):
                    yield f"data: {json.dumps({
                        'type': 'complete',
                        'result': {
                            'transcript': state.get('transcript'),
                            'summary': state.get('summary'),
                            'keypoints': state.get('keypoints'),
                            'mindmap': state.get('mindmap'),
                            'knowledge_cards': state.get('knowledge_cards'),
                            'report': state.get('report'),
                            'qa_pairs': state.get('qa_pairs'),
                        }
                    })}\n\n"

                await asyncio.sleep(0.1)

        except Exception as e:
            yield f"data: {json.dumps({'type': 'error', 'error': str(e)})}\n\n"

        # 发送完成信号
        yield f"data: {json.dumps({'type': 'done'})}\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        }
    )


class ExportRequest(BaseModel):
    """导出请求"""
    result: dict
    format: str = "pdf"


@router.post("/export")
async def export_result(request: ExportRequest) -> Response:
    """
    导出研究结果为不同格式

    Args:
        request: 包含result和format的请求体

    Returns:
        文件下载响应
    """
    # 生成HTML内容
    html_content = _generate_html_from_result(request.result)

    if request.format == "pdf":
        # 使用weasyprint或html2pdf生成PDF
        try:
            from weasyprint import HTML
            pdf_buffer = BytesIO()
            HTML(string=html_content).write_pdf(pdf_buffer)
            pdf_buffer.seek(0)
            return Response(
                content=pdf_buffer.read(),
                media_type="application/pdf",
                headers={
                    "Content-Disposition": "attachment; filename=research-result.pdf"
                }
            )
        except ImportError:
            # 如果没有weasyprint，返回HTML
            return Response(
                content=html_content.encode("utf-8"),
                media_type="text/html",
                headers={
                    "Content-Disposition": "attachment; filename=research-result.html"
                }
            )
    else:
        return Response(
            content=html_content.encode("utf-8"),
            media_type="text/html",
            headers={
                "Content-Disposition": "attachment; filename=research-result.html"
            }
        )


def _generate_html_from_result(result: dict) -> str:
    """将研究结果生成为HTML"""
    title = result.get("summary", {}).get("title", "研究报告")
    summary_text = result.get("summary", {}).get("summary", "")
    highlights = result.get("summary", {}).get("highlights", [])
    keypoints = result.get("keypoints", [])
    mindmap = result.get("mindmap", {})
    qa_pairs = result.get("qa_pairs", [])
    report = result.get("report", {})

    html_parts = [
        "<!DOCTYPE html>",
        "<html lang='zh-CN'>",
        "<head>",
        "    <meta charset='UTF-8'>",
        "    <meta name='viewport' content='width=device-width, initial-scale=1.0'>",
        f"    <title>{title} - Echo</title>",
        "    <style>",
        "        * { box-sizing: border-box; margin: 0; padding: 0; }",
        "        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.6; color: #333; max-width: 900px; margin: 0 auto; padding: 20px; background: #fafafa; }",
        "        .card { background: white; border-radius: 12px; padding: 24px; margin-bottom: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }",
        "        h1 { color: #2C3E50; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid #E67E22; padding-bottom: 10px; }",
        "        h2 { color: #2C3E50; font-size: 1.4em; margin: 20px 0 10px; }",
        "        .highlight { background: #FFF3E0; border-left: 4px solid #E67E22; padding: 10px 15px; margin: 15px 0; border-radius: 0 8px 8px 0; }",
        "        ul { margin: 10px 0 10px 20px; }",
        "        li { margin: 5px 0; }",
        "        .tag { display: inline-block; background: #E67E22; color: white; padding: 2px 8px; border-radius: 4px; font-size: 0.75em; margin-left: 8px; }",
        "        .qa-card { background: #f8f9fa; border-radius: 8px; padding: 15px; margin: 10px 0; border: 1px solid #e0e0e0; }",
        "        .qa-question { font-weight: bold; color: #2C3E50; margin-bottom: 8px; }",
        "        .qa-answer { color: #555; margin-left: 15px; }",
        "        .report-content { white-space: pre-wrap; background: #f8f9fa; padding: 15px; border-radius: 8px; }",
        "        .footer { text-align: center; color: #888; font-size: 0.85em; margin-top: 30px; padding-top: 20px; border-top: 1px solid #e0e0e0; }",
        "    </style>",
        "</head>",
        "<body>",
        f"    <h1>{title}</h1>",
    ]

    # 摘要
    if summary_text:
        html_parts.extend([
            "    <div class='card'>",
            "        <h2>摘要</h2>",
            f"        <div class='highlight'>{summary_text}</div>",
            "    </div>",
        ])

    # 亮点
    if highlights:
        html_parts.append("    <div class='card'>")
        html_parts.append("        <h2>亮点</h2>")
        html_parts.append("        <ul>")
        for h in highlights:
            html_parts.append(f"            <li>{h}</li>")
        html_parts.extend(["        </ul>", "    </div>"])

    # 要点
    if keypoints:
        html_parts.append("    <div class='card'>")
        html_parts.append("        <h2>关键要点</h2>")
        html_parts.append("        <ul>")
        for kp in keypoints:
            content = kp.get("content", kp) if isinstance(kp, dict) else kp
            importance = kp.get("importance", "") if isinstance(kp, dict) else ""
            tag = f"<span class='tag'>{importance}</span>" if importance else ""
            html_parts.append(f"            <li><strong>{content}</strong>{tag}</li>")
        html_parts.extend(["        </ul>", "    </div>"])

    # 思维导图
    if mindmap and mindmap.get("root"):
        html_parts.extend([
            "    <div class='card'>",
            "        <h2>思维导图</h2>",
            f"        <div class='highlight'><strong>主题:</strong> {mindmap['root']}</div>",
        ])
        for branch in mindmap.get("branches", []):
            branch_title = branch.get("title", "")
            children = branch.get("children", [])
            html_parts.append(f"        <div style='margin-left: 20px; margin-top: 10px;'><strong>{branch_title}</strong>")
            if children:
                html_parts.append("            <ul>")
                for child in children:
                    html_parts.append(f"                <li>{child}</li>")
                html_parts.append("            </ul>")
            html_parts.append("        </div>")
        html_parts.append("    </div>")

    # 问答对
    if qa_pairs:
        html_parts.append("    <div class='card'>")
        html_parts.append("        <h2>问答对</h2>")
        for i, qa in enumerate(qa_pairs, 1):
            question = qa.get("question", "")
            answer = qa.get("answer", "")
            level = qa.get("level", "")
            level_name = qa.get("level_name", "")
            html_parts.extend([
                f"        <div class='qa-card'>",
                f"            <div class='qa-question'>Q{i}: {question}</div>",
                f"            <div class='qa-answer'>A: {answer}</div>",
            ])
            if level:
                html_parts.append(f"            <div style='font-size:0.85em; color:#888; margin-top:5px;'>认知层次: {level} - {level_name}</div>")
            html_parts.append("        </div>")
        html_parts.append("    </div>")

    # 报告
    if report:
        content = report.get("content", "")
        report_title = report.get("title", "报告")
        if content:
            html_parts.extend([
                "    <div class='card'>",
                f"        <h2>{report_title}</h2>",
                f"        <div class='report-content'>{content}</div>",
                "    </div>",
            ])

    # 页脚
    html_parts.extend([
        "    <div class='footer'>",
        f"        由 Echo 播客研究Agent生成 | {datetime.now().strftime('%Y-%m-%d')}",
        "    </div>",
        "</body>",
        "</html>",
    ])

    return "\n".join(html_parts)
