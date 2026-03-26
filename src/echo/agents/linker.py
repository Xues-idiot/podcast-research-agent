"""知识关联Agent - 与已有知识库关联"""

import asyncio
from typing import List, Optional

from tavily import TavilyClient

from echo.config import TavilyConfig


class KnowledgeLinker:
    """
    知识关联Agent - 将要点与相关知识关联
    """

    def __init__(self, config: TavilyConfig):
        self.client = TavilyClient(api_key=config.api_key)

    async def link(self, keypoints: List[dict], max_results: int = 3) -> List[dict]:
        """
        为每个要点关联相关知识

        Args:
            keypoints: 要点列表
            max_results: 每个要点的最大关联数量

        Returns:
            知识卡片列表
        """
        knowledge_cards = []

        for kp in keypoints:
            content = kp.get("content", "")
            if not content:
                continue

            # 使用Tavily搜索相关知识 (使用 run_in_executor 避免阻塞)
            try:
                results = await asyncio.run_in_executor(
                    None,
                    lambda: self.client.search(
                        query=content,
                        max_results=max_results,
                        include_answer=True,
                    )
                )

                card = {
                    "keypoint": content,
                    "related": [],
                    "confidence": 0.0,
                }

                total_score = 0.0
                result_count = 0
                for r in results.get("results", []):
                    score = r.get("score", 0.0)
                    total_score += score
                    result_count += 1
                    card["related"].append({
                        "title": r.get("title", ""),
                        "url": r.get("url", ""),
                        "content": r.get("content", ""),
                        "score": score,
                    })

                # 使用平均相关性评分
                if result_count > 0:
                    card["confidence"] = total_score / result_count

                knowledge_cards.append(card)

            except Exception as e:
                # 搜索失败时跳过
                knowledge_cards.append({
                    "keypoint": content,
                    "related": [],
                    "confidence": 0.0,
                    "error": str(e),
                })

        return knowledge_cards

    async def search_related(self, query: str, max_results: int = 5) -> List[dict]:
        """
        搜索相关知识

        Args:
            query: 搜索查询
            max_results: 最大结果数

        Returns:
            搜索结果列表
        """
        try:
            results = await asyncio.run_in_executor(
                None,
                lambda: self.client.search(
                    query=query,
                    max_results=max_results,
                    include_answer=True,
                )
            )

            return results.get("results", [])

        except Exception:
            return []
