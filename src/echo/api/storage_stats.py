"""存储统计API"""

from fastapi import APIRouter

from echo.research.storage_stats import get_storage_stats


router = APIRouter(prefix="/api/storage", tags=["storage"])


@router.get("/stats")
async def get_stats():
    stats = get_storage_stats()
    return stats.get_all_stats()


@router.post("/cleanup")
async def cleanup(days: int = 30):
    stats = get_storage_stats()
    removed = stats.cleanup_old_files(days=days)
    return {
        "removed_files": removed["files"],
        "freed_mb": round(removed["size_bytes"] / 1024 / 1024, 2),
    }
