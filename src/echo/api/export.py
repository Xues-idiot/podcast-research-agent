"""导出API - 多种格式导出路由"""

from io import BytesIO
from fastapi import APIRouter, HTTPException
from fastapi.responses import Response, JSONResponse
from pydantic import BaseModel

from echo.exporters import KnowledgeCardExporter


router = APIRouter(prefix="/api/export", tags=["export"])


class ExportRequest(BaseModel):
    """导出请求"""
    result: dict
    format: str = "json"  # json, markdown, html, pdf
    entries: list = []


@router.post("/knowledge-cards")
async def export_knowledge_cards(request: ExportRequest):
    """导出知识卡片

    Args:
        request: 包含 result, format, entries 的请求

    Returns:
        文件下载响应
    """
    exporter = KnowledgeCardExporter()

    if request.format == "json":
        cards = exporter.build_cards_from_result(request.result, request.entries)
        data = exporter.export_json(cards)
        return Response(
            content=open(data, "rb").read(),
            media_type="application/json",
            headers={"Content-Disposition": "attachment; filename=knowledge_cards.json"},
        )

    elif request.format == "markdown":
        cards = exporter.build_cards_from_result(request.result, request.entries)
        data = exporter.export_markdown(cards)
        return Response(
            content=open(data, "rb").read(),
            media_type="text/markdown",
            headers={"Content-Disposition": "attachment; filename=knowledge_cards.md"},
        )

    elif request.format == "html":
        cards = exporter.build_cards_from_result(request.result, request.entries)
        title = request.result.get("summary", {}).get("title", "知识卡片")
        data = exporter.export_html(cards, title=title)
        return Response(
            content=open(data, "rb").read(),
            media_type="text/html",
            headers={"Content-Disposition": "attachment; filename=knowledge_cards.html"},
        )

    elif request.format == "pdf":
        # 生成HTML然后转换为PDF
        cards = exporter.build_cards_from_result(request.result, request.entries)
        title = request.result.get("summary", {}).get("title", "知识卡片")
        html_path = exporter.export_html(cards, title=title)

        try:
            from weasyprint import HTML
            pdf_buffer = BytesIO()
            HTML(filename=html_path).write_pdf(pdf_buffer)
            pdf_buffer.seek(0)
            return Response(
                content=pdf_buffer.read(),
                media_type="application/pdf",
                headers={"Content-Disposition": "attachment; filename=knowledge_cards.pdf"},
            )
        except ImportError:
            raise HTTPException(
                status_code=501,
                detail="PDF export requires weasyprint. Returning HTML instead.",
            )

    elif request.format == "anki":
        cards = exporter.build_cards_from_result(request.result, request.entries)
        data = exporter.export_anki(cards)
        return Response(
            content=open(data, "rb").read(),
            media_type="text/tab-separated-values",
            headers={"Content-Disposition": "attachment; filename=knowledge_cards.tsv"},
        )

    else:
        raise HTTPException(status_code=400, detail=f"Unknown format: {request.format}")


@router.post("/knowledge-cards/all")
async def export_knowledge_cards_all(request: ExportRequest):
    """导出所有格式的知识卡片

    Args:
        request: 包含 result, entries 的请求

    Returns:
        各格式的文件路径
    """
    exporter = KnowledgeCardExporter()
    paths = exporter.export_all_formats(
        result=request.result,
        entries=request.entries,
        base_filename="knowledge_cards"
    )

    return JSONResponse(content={
        "status": "exported",
        "formats": {
            fmt: {"path": path}
            for fmt, path in paths.items()
        }
    })
