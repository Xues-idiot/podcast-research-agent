#!/usr/bin/env python3
"""API 服务器入口 - 启动 FastAPI 服务器"""

import sys
from pathlib import Path

# 添加项目根目录到路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from echo.api.research import router as research_router
from echo.api.chat import router as chat_router
from echo.api.knowledge import router as knowledge_router
from echo.api.sources import router as sources_router
from echo.api.export import router as export_router
from echo.api.navigation import router as navigation_router
from echo.api.memory import router as memory_router


def create_app() -> FastAPI:
    """创建 FastAPI 应用"""
    app = FastAPI(
        title="Echo API",
        description="播客研究Agent API",
        version="0.1.0",
    )

    # CORS 中间件
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # 注册路由
    app.include_router(research_router)
    app.include_router(chat_router)
    app.include_router(knowledge_router)
    app.include_router(sources_router)
    app.include_router(export_router)
    app.include_router(navigation_router)
    app.include_router(memory_router)

    @app.get("/")
    async def root():
        return {"message": "Echo API", "version": "0.1.0"}

    @app.get("/health")
    async def health():
        return {"status": "healthy"}

    return app


def main():
    """启动服务器"""
    print("=" * 50)
    print("Echo API Server")
    print("=" * 50)
    print("Starting server on http://localhost:8002")
    print()

    uvicorn.run(
        "scripts.api_server:create_app",
        factory=True,
        host="0.0.0.0",
        port=8002,
        reload=True,
    )


if __name__ == "__main__":
    main()
