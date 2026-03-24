"""导出模块 - 多种格式导出"""

import csv
import json
from pathlib import Path
from typing import List

from echo.types import ResearchResult


class Exporter:
    """
    导出器 - 将研究结果导出为多种格式
    """

    def __init__(self, output_dir: str = "./output"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def export_json(self, result: dict, filename: str = "result.json") -> str:
        """
        导出为JSON

        Args:
            result: 研究结果
            filename: 文件名

        Returns:
            文件路径
        """
        path = self.output_dir / filename
        with open(path, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        return str(path)

    def export_markdown(self, result: dict, filename: str = "result.md") -> str:
        """
        导出为Markdown

        Args:
            result: 研究结果
            filename: 文件名

        Returns:
            文件路径
        """
        lines = []

        # 标题
        title = result.get("summary", {}).get("title", "无标题")
        lines.append(f"# {title}")
        lines.append("")

        # 摘要
        summary_text = result.get("summary", {}).get("summary", "")
        if summary_text:
            lines.append("## 摘要")
            lines.append(summary_text)
            lines.append("")

        # 亮点
        highlights = result.get("summary", {}).get("highlights", [])
        if highlights:
            lines.append("## 亮点")
            for h in highlights:
                lines.append(f"- {h}")
            lines.append("")

        # 要点
        keypoints = result.get("keypoints", [])
        if keypoints:
            lines.append("## 关键要点")
            for kp in keypoints:
                importance = kp.get("importance", "medium")
                lines.append(f"- [{importance.upper()}] {kp.get('content', '')}")
            lines.append("")

        # 思维导图
        mindmap = result.get("mindmap", {})
        if mindmap.get("root"):
            lines.append("## 思维导图")
            lines.append(f"**主题**: {mindmap['root']}")
            lines.append("")
            for branch in mindmap.get("branches", []):
                lines.append(f"### {branch.get('title', '')}")
                for child in branch.get("children", []):
                    lines.append(f"- {child}")
                lines.append("")

        # 知识卡片
        knowledge_cards = result.get("knowledge_cards", [])
        if knowledge_cards:
            lines.append("## 相关知识")
            for card in knowledge_cards:
                lines.append(f"### {card.get('keypoint', '')[:50]}...")
                for related in card.get("related", [])[:3]:
                    lines.append(f"- [{related.get('title', '')}]({related.get('url', '')})")
                lines.append("")

        # 转录摘要
        transcript = result.get("transcript", {})
        if transcript.get("text"):
            text = transcript["text"]
            lines.append("## 转录摘要")
            lines.append(f"*{text[:500]}...*" if len(text) > 500 else f"*{text}*")

        path = self.output_dir / filename
        path.write_text("\n".join(lines), encoding="utf-8")
        return str(path)

    def export_csv(self, result: dict, filename: str = "keypoints.csv") -> str:
        """
        导出要点为CSV

        Args:
            result: 研究结果
            filename: 文件名

        Returns:
            文件路径
        """
        keypoints = result.get("keypoints", [])

        path = self.output_dir / filename
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "要点内容", "重要性"])

            for kp in keypoints:
                writer.writerow([
                    kp.get("id", ""),
                    kp.get("content", ""),
                    kp.get("importance", ""),
                ])

        return str(path)

    def export_flashcards(
        self,
        result: dict,
        filename: str = "flashcards.json",
        format: str = "json"
    ) -> str:
        """
        导出为闪卡格式

        Args:
            result: 研究结果
            filename: 文件名
            format: 输出格式 (json, markdown, html)

        Returns:
            文件路径
        """
        keypoints = result.get("keypoints", [])
        flashcards = []

        for kp in keypoints:
            card = {
                "front": kp.get("content", ""),
                "back": f"重要性: {kp.get('importance', 'medium')}",
            }
            flashcards.append(card)

        if format == "json":
            return self._export_flashcards_json(flashcards, filename)
        elif format == "markdown":
            return self._export_flashcards_markdown(flashcards, filename)
        elif format == "html":
            return self._export_flashcards_html(flashcards, filename)
        else:
            raise ValueError(f"Unknown format: {format}")

    def _export_flashcards_json(self, flashcards: list, filename: str) -> str:
        """导出为JSON闪卡"""
        path = self.output_dir / filename
        with open(path, "w", encoding="utf-8") as f:
            json.dump(flashcards, f, ensure_ascii=False, indent=2)
        return str(path)

    def _export_flashcards_markdown(self, flashcards: list, filename: str) -> str:
        """导出为Markdown闪卡"""
        lines = ["# 闪卡", ""]

        for i, card in enumerate(flashcards, 1):
            lines.append(f"## 卡片 {i}")
            lines.append("")
            lines.append("**正面:**")
            lines.append(card["front"])
            lines.append("")
            lines.append("**背面:**")
            lines.append(card["back"])
            lines.append("")

        path = self.output_dir / filename
        path.write_text("\n".join(lines), encoding="utf-8")
        return str(path)

    def _export_flashcards_html(self, flashcards: list, filename: str) -> str:
        """导出为HTML闪卡"""
        cards_html = []

        for card in flashcards:
            cards_html.append(f"""
            <div class="flashcard">
                <div class="front">{card['front']}</div>
                <div class="back">{card['back']}</div>
            </div>
            """)

        html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Echo Flashcards</title>
    <style>
        .flashcard {{ border: 1px solid #ccc; margin: 10px; padding: 20px; border-radius: 8px; }}
        .front {{ font-weight: bold; font-size: 18px; }}
        .back {{ color: #666; margin-top: 10px; }}
    </style>
</head>
<body>
    <h1>Echo Flashcards</h1>
    {"".join(cards_html)}
</body>
</html>
        """

        path = self.output_dir / filename
        path.write_text(html, encoding="utf-8")
        return str(path)

    def export_mindmap_json(self, result: dict, filename: str = "mindmap.json") -> str:
        """
        导出思维导图为JSON

        Args:
            result: 研究结果
            filename: 文件名

        Returns:
            文件路径
        """
        mindmap = result.get("mindmap", {})

        path = self.output_dir / filename
        with open(path, "w", encoding="utf-8") as f:
            json.dump(mindmap, f, ensure_ascii=False, indent=2)
        return str(path)

    def export_all(self, result: dict) -> dict:
        """
        导出所有格式

        Args:
            result: 研究结果

        Returns:
            导出文件路径字典
        """
        paths = {}

        paths["json"] = self.export_json(result)
        paths["markdown"] = self.export_markdown(result)
        paths["csv"] = self.export_csv(result)
        paths["mindmap"] = self.export_mindmap_json(result)
        paths["flashcards"] = self.export_flashcards(result, format="json")

        return paths
