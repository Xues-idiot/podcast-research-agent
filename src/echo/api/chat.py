"""对话API - FastAPI路由"""

import uuid
from dataclasses import dataclass, field
from datetime import datetime
from typing import AsyncIterator, Optional

from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from echo.conversation import ConversationHandler, ChatMessage


router = APIRouter(prefix="/api/chat", tags=["chat"])


class ChatRequest(BaseModel):
    """聊天请求"""
    query: str
    conversation_id: Optional[str] = None
    stream: bool = True
    # 研究结果，用于提供对话上下文（可选，优先使用已有对话）
    research_result: Optional[dict] = None


class ChatResponse(BaseModel):
    """聊天响应"""
    answer: str
    conversation_id: str
    references: list[dict] = field(default_factory=list)


class MessageResponse(BaseModel):
    """单条消息响应"""
    type: str  # "text", "reference", "done", "error"
    content: str
    conversation_id: Optional[str] = None


# 存储活跃的对话处理器
_active_handlers: dict[str, ConversationHandler] = {}


def get_or_create_handler(
    conversation_id: Optional[str],
    research_result: dict
) -> tuple[ConversationHandler, str]:
    """获取或创建对话处理器"""
    if conversation_id and conversation_id in _active_handlers:
        return _active_handlers[conversation_id], conversation_id

    handler = ConversationHandler(research_result)
    new_id = conversation_id or handler.get_conversation_id()
    _active_handlers[new_id] = handler
    return handler, new_id


@router.post("/chat")
async def chat(request: ChatRequest):
    """对话接口

    Args:
        request: 聊天请求，包含 query, conversation_id, stream, research_result

    Returns:
        流式或非流式的回答
    """
    if not request.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")

    # 获取或创建处理器
    # 如果请求中有 research_result 且没有 conversation_id，使用新的研究结果
    research_data = request.research_result if request.research_result else {}
    handler, conversation_id = get_or_create_handler(
        request.conversation_id,
        research_data
    )

    if request.stream:
        # 流式响应
        async def event_generator():
            full_answer = ""

            try:
                async for response in handler.chat(request.query, stream=True):
                    full_answer += response.answer
                    yield f"data: {response.answer}\n\n"

                # 保存用户消息
                handler.history.add(ChatMessage(
                    role="user",
                    content=request.query
                ))
                handler.history.add(ChatMessage(
                    role="assistant",
                    content=full_answer
                ))

                yield f"data: [DONE] {conversation_id}\n\n"

            except Exception as e:
                yield f"data: [ERROR] {str(e)}\n\n"

        return StreamingResponse(
            event_generator(),
            media_type="text/plain",
            headers={
                "X-Conversation-ID": conversation_id,
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "Transfer-Encoding": "chunked"
            }
        )
    else:
        # 非流式响应
        response = None
        async for r in handler.chat(request.query, stream=False):
            response = r

        return ChatResponse(
            answer=response.answer if response else "",
            conversation_id=conversation_id,
            references=response.references if response else []
        )


@router.get("/conversations")
async def list_conversations():
    """获取所有对话列表"""
    return {
        "conversations": [
            {
                "id": conv_id,
                "message_count": len(handler.history.get_all()),
                "created_at": handler.history.get_all()[0].timestamp.isoformat() if handler.history.get_all() else None,
                "last_message": handler.history.get_all()[-1].content[:50] if handler.history.get_all() else None
            }
            for conv_id, handler in _active_handlers.items()
        ]
    }


@router.delete("/conversation/{conversation_id}")
    """删除对话"""
    if conversation_id in _active_handlers:
        handler = _active_handlers[conversation_id]
        handler.clear_history()
        del _active_handlers[conversation_id]
        return {"deleted": conversation_id}

    raise HTTPException(status_code=404, detail="Conversation not found")


@router.get("/conversation/{conversation_id}/history")
async def get_history(conversation_id: str):
    """获取对话历史"""
    if conversation_id not in _active_handlers:
        raise HTTPException(status_code=404, detail="Conversation not found")

    handler = _active_handlers[conversation_id]
    messages = handler.history.get_all()

    return {
        "conversation_id": conversation_id,
        "messages": [
            {
                "role": msg.role,
                "content": msg.content,
                "timestamp": msg.timestamp.isoformat(),
                "references": msg.references
            }
            for msg in messages
        ]
    }


@router.post("/conversation/{conversation_id}/export")
async def export_conversation(conversation_id: str, format: str = "markdown"):
    """导出对话

    Args:
        conversation_id: 对话ID
        format: 导出格式，支持 markdown, json
    """
    if conversation_id not in _active_handlers:
        raise HTTPException(status_code=404, detail="Conversation not found")

    handler = _active_handlers[conversation_id]

    if format == "markdown":
        content = handler.history.export_markdown()
        return {
            "format": "markdown",
            "content": content,
            "filename": f"conversation_{conversation_id}.md"
        }
    elif format == "json":
        messages = handler.history.get_all()
        return {
            "format": "json",
            "content": {
                "conversation_id": conversation_id,
                "messages": [
                    {
                        "role": msg.role,
                        "content": msg.content,
                        "timestamp": msg.timestamp.isoformat(),
                        "references": msg.references
                    }
                    for msg in messages
                ]
            },
            "filename": f"conversation_{conversation_id}.json"
        }
    else:
        raise HTTPException(status_code=400, detail=f"Unsupported format: {format}")
