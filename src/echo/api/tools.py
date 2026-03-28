"""工具中心 API 路由"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List, Dict, Any

from echo.tools.metadata.categories import get_all_categories, get_categories_with_tools, get_category_by_id
from echo.tools.metadata.tools import (
    TOOL_REGISTRY,
    get_tool_by_id,
    get_tools_by_category,
    search_tools
)


router = APIRouter(prefix="/api/tools", tags=["tools"])


class ToolExecuteRequest(BaseModel):
    params: Dict[str, Any] = {}


class ToolSearchRequest(BaseModel):
    query: str


@router.get("/categories")
async def get_categories():
    """获取所有工具分类"""
    categories = get_categories_with_tools()
    return {
        "categories": categories,
        "total": len(categories)
    }


@router.get("/category/{category_id}")
async def get_category_tools(category_id: str):
    """获取指定分类下的所有工具"""
    category = get_category_by_id(category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    tools = get_tools_by_category(category_id)
    return {
        "category": category,
        "tools": tools,
        "total": len(tools)
    }


@router.get("/{tool_id}")
async def get_tool(tool_id: str):
    """获取指定工具的详细信息"""
    tool = get_tool_by_id(tool_id)
    if not tool:
        raise HTTPException(status_code=404, detail="Tool not found")
    return tool


@router.post("/search")
async def search(request: ToolSearchRequest):
    """搜索工具"""
    results = search_tools(request.query)
    return {
        "results": results,
        "total": len(results)
    }


@router.post("/{tool_id}/execute")
async def execute_tool(tool_id: str, request: ToolExecuteRequest):
    """执行指定工具"""
    tool = get_tool_by_id(tool_id)
    if not tool:
        raise HTTPException(status_code=404, detail="Tool not found")

    # 这里需要调用实际的研究模块
    # 目前返回模拟结果，后续需要与实际模块对接
    api_endpoint = tool.get("api_endpoint", "")

    return {
        "tool_id": tool_id,
        "tool_name": tool.get("name"),
        "api_endpoint": api_endpoint,
        "params": request.params,
        "status": "simulated",
        "message": f"Tool {tool_id} execution simulated. API endpoint: {api_endpoint}"
    }


@router.get("/")
async def list_all_tools():
    """获取所有工具列表"""
    return {
        "tools": list(TOOL_REGISTRY.values()),
        "total": len(TOOL_REGISTRY)
    }
