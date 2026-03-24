"""知识卡片导出器 - 支持引用和时间戳

参考 khoj 的知识卡片导出实现，
将播客研究结果中的知识卡片导出为多种格式。
"""

import json
from dataclasses import dataclass, field, asdict
from typing import Optional
from pathlib import Path


@dataclass
class Citation:
    """引用信息"""
    entry_id: str
    timestamp: float
    formatted_time: str
    content: str
    score: float = 0.0


@dataclass
class KnowledgeCardExport:
    """导出的知识卡片"""
    keypoint: str
    importance: str
    citations: list[Citation] = field(default_factory=list)
    related_items: list[dict] = field(default_factory=list)
    confidence: float = 0.0
    summary: str = ""


@dataclass
class KnowledgeCardExporter:
    """知识卡片导出器

    将研究结果中的知识卡片导出为多种格式，
    包含引用和时间戳信息。
    """

    def __init__(self, output_dir: str = "./output"):
        """初始化导出器

        Args:
            output_dir: 输出目录
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def export_json(
        self,
        cards: list[KnowledgeCardExport],
        filename: str = "knowledge_cards.json"
    ) -> str:
        """导出为JSON格式

        Args:
            cards: 知识卡片列表
            filename: 文件名

        Returns:
            文件路径
        """
        path = self.output_dir / filename
        data = [asdict(card) for card in cards]
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return str(path)

    def export_markdown(
        self,
        cards: list[KnowledgeCardExport],
        filename: str = "knowledge_cards.md"
    ) -> str:
        """导出为Markdown格式

        Args:
            cards: 知识卡片列表
            filename: 文件名

        Returns:
            文件路径
        """
        lines = [
            "# 知识卡片",
            "",
            f"共 {len(cards)} 张卡片",
            "",
        ]

        for i, card in enumerate(cards, 1):
            # 卡片标题
            lines.append(f"## {i}. {card.keypoint[:60]}{'...' if len(card.keypoint) > 60 else ''}")
            lines.append("")

            # 重要性
            importance_badge = {
                "high": "🔴 高",
                "medium": "🟡 中",
                "low": "🟢 低",
            }.get(card.importance.lower(), card.importance)
            lines.append(f"**重要性**: {importance_badge}")
            lines.append("")

            # 置信度
            if card.confidence > 0:
                lines.append(f"**置信度**: {card.confidence:.0%}")
                lines.append("")

            # 摘要
            if card.summary:
                lines.append(f"**摘要**: {card.summary}")
                lines.append("")

            # 引用来源
            if card.citations:
                lines.append("**引用来源**:")
                for cit in card.citations:
                    lines.append(f"- [{cit.formatted_time}] {cit.content[:80]}{'...' if len(cit.content) > 80 else ''}")
                lines.append("")

            # 相关链接
            if card.related_items:
                lines.append("**相关链接**:")
                for item in card.related_items:
                    title = item.get("title", "链接")
                    url = item.get("url", "#")
                    lines.append(f"- [{title}]({url})")
                lines.append("")

            lines.append("---")
            lines.append("")

        path = self.output_dir / filename
        path.write_text("\n".join(lines), encoding="utf-8")
        return str(path)

    def export_html(
        self,
        cards: list[KnowledgeCardExport],
        title: str = "知识卡片",
        filename: str = "knowledge_cards.html"
    ) -> str:
        """导出为HTML格式

        Args:
            cards: 知识卡片列表
            title: 页面标题
            filename: 文件名

        Returns:
            文件路径
        """
        cards_html = []
        for i, card in enumerate(cards, 1):
            # 引用列表HTML
            citations_html = ""
            if card.citations:
                cit_list = []
                for cit in card.citations:
                    cit_list.append(f"""
                    <div class="citation">
                        <span class="timestamp">{cit.formatted_time}</span>
                        <span class="content">{cit.content[:100]}{'...' if len(cit.content) > 100 else ''}</span>
                    </div>
                    """)
                citations_html = f"""
                <div class="citations">
                    <h4>引用来源</h4>
                    {"".join(cit_list)}
                </div>
                """

            # 相关链接HTML
            related_html = ""
            if card.related_items:
                links = []
                for item in card.related_items:
                    links.append(f'<a href="{item.get("url", "#")}" target="_blank">{item.get("title", "链接")}</a>')
                related_html = f"""
                <div class="related">
                    <h4>相关链接</h4>
                    <ul>{"".join(f"<li>{l}</li>" for l in links)}</ul>
                </div>
                """

            # 重要性颜色
            importance_color = {
                "high": "#E74C3C",
                "medium": "#F39C12",
                "low": "#27AE60",
            }.get(card.importance.lower(), "#95A5A6")

            card_html = f"""
            <div class="card" style="border-left: 4px solid {importance_color};">
                <h3>{i}. {self._escape_html(card.keypoint)}</h3>
                <div class="meta">
                    <span class="importance" style="background: {importance_color};">{card.importance.upper()}</span>
                    {"<span class='confidence'>置信度: " + f"{card.confidence:.0%}" + "</span>" if card.confidence > 0 else ""}
                </div>
                {"<p class='summary'>" + self._escape_html(card.summary) + "</p>" if card.summary else ""}
                {citations_html}
                {related_html}
            </div>
            """
            cards_html.append(card_html)

        html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{self._escape_html(title)} - Echo</title>
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            background: #fafafa;
        }}
        h1 {{
            color: #2C3E50;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 3px solid #3498DB;
        }}
        .card {{
            background: white;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }}
        .card h3 {{
            color: #2C3E50;
            margin-bottom: 10px;
        }}
        .meta {{
            display: flex;
            gap: 10px;
            margin-bottom: 10px;
        }}
        .importance {{
            color: white;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 0.75em;
            font-weight: bold;
        }}
        .confidence {{
            color: #7F8C8D;
            font-size: 0.85em;
        }}
        .summary {{
            color: #555;
            margin: 10px 0;
            padding: 10px;
            background: #f8f9fa;
            border-radius: 4px;
        }}
        .citations, .related {{
            margin-top: 15px;
        }}
        .citations h4, .related h4 {{
            color: #2C3E50;
            font-size: 0.9em;
            margin-bottom: 8px;
        }}
        .citation {{
            display: flex;
            gap: 10px;
            padding: 8px;
            background: #f8f9fa;
            border-radius: 4px;
            margin-bottom: 5px;
            font-size: 0.9em;
        }}
        .timestamp {{
            color: #E67E22;
            font-weight: bold;
            flex-shrink: 0;
        }}
        .content {{
            color: #555;
        }}
        .related ul {{
            list-style: none;
            padding: 0;
        }}
        .related li {{
            padding: 5px 0;
        }}
        .related a {{
            color: #3498DB;
            text-decoration: none;
        }}
        .related a:hover {{
            text-decoration: underline;
        }}
        .footer {{
            text-align: center;
            color: #888;
            font-size: 0.85em;
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #e0e0e0;
        }}
    </style>
</head>
<body>
    <h1>{self._escape_html(title)}</h1>
    <p class="info">共 {len(cards)} 张知识卡片</p>
    {"".join(cards_html)}
    <div class="footer">
        由 Echo 播客研究Agent生成
    </div>
</body>
</html>
        """

        path = self.output_dir / filename
        path.write_text(html, encoding="utf-8")
        return str(path)

    def export_anki(
        self,
        cards: list[KnowledgeCardExport],
        filename: str = "knowledge_cards.tsv"
    ) -> str:
        """导出为Anki格式 (TSV)

        Anki格式: 前缀\t后缀\t标签

        Args:
            cards: 知识卡片列表
            filename: 文件名

        Returns:
            文件路径
        """
        lines = []
        for card in cards:
            # 前缀包含关键点
            front = f"{card.keypoint}"
            if card.summary:
                front += f"\n{card.summary}"

            # 后缀包含引用
            back_parts = []
            for cit in card.citations[:3]:
                back_parts.append(f"[{cit.formatted_time}] {cit.content[:50]}")
            back = "\n".join(back_parts) if back_parts else "无引用"

            # 标签
            tags = f"echo::{card.importance}"

            lines.append(f"{front}\t{back}\t{tags}")

        path = self.output_dir / filename
        path.write_text("\n".join(lines), encoding="utf-8")
        return str(path)

    def build_cards_from_result(
        self,
        result: dict,
        entries: Optional[list] = None
    ) -> list[KnowledgeCardExport]:
        """从研究结果构建导出的知识卡片

        Args:
            result: 研究结果字典
            entries: 可选的Entry列表 (用于引用)

        Returns:
            知识卡片列表
        """
        cards = []
        knowledge_cards = result.get("knowledge_cards", [])
        keypoints = result.get("keypoints", [])

        # 创建entry_id到citation的映射
        entry_citations = {}
        if entries:
            for entry in entries:
                entry_citations[entry.get("id", entry.get("entry_id", ""))] = Citation(
                    entry_id=entry.get("id", ""),
                    timestamp=entry.get("start_time", 0.0),
                    formatted_time=self._format_timestamp(entry.get("start_time", 0.0)),
                    content=entry.get("compiled", entry.get("raw", "")),
                    score=0.0,
                )

        for i, card_data in enumerate(knowledge_cards):
            keypoint = card_data.get("keypoint", "")

            # 找到对应的关键点
            importance = "medium"
            for kp in keypoints:
                if kp.get("content", "") == keypoint or keypoint in kp.get("content", ""):
                    importance = kp.get("importance", "medium")
                    break

            # 构建引用
            citations = []
            for cit_data in card_data.get("citations", []):
                entry_id = cit_data.get("entry_id", "")
                if entry_id in entry_citations:
                    citations.append(entry_citations[entry_id])

            # 如果没有引用，尝试从keypoint关联
            if not citations and entries:
                # 简单匹配：找包含keypoint内容的entry
                for entry in entries:
                    entry_text = entry.get("compiled", entry.get("raw", ""))
                    if keypoint[:30] in entry_text:
                        citations.append(Citation(
                            entry_id=entry.get("id", ""),
                            timestamp=entry.get("start_time", 0.0),
                            formatted_time=self._format_timestamp(entry.get("start_time", 0.0)),
                            content=entry_text[:200],
                            score=0.5,
                        ))
                        break

            cards.append(KnowledgeCardExport(
                keypoint=keypoint,
                importance=importance,
                citations=citations[:5],  # 最多5个引用
                related_items=card_data.get("related", [])[:5],  # 最多5个相关链接
                confidence=card_data.get("confidence", 0.0),
                summary="",
            ))

        return cards

    def export_all_formats(
        self,
        result: dict,
        entries: Optional[list] = None,
        base_filename: str = "knowledge_cards"
    ) -> dict:
        """导出所有格式

        Args:
            result: 研究结果
            entries: Entry列表
            base_filename: 基础文件名

        Returns:
            各格式的文件路径字典
        """
        cards = self.build_cards_from_result(result, entries)
        paths = {}

        paths["json"] = self.export_json(cards, f"{base_filename}.json")
        paths["markdown"] = self.export_markdown(cards, f"{base_filename}.md")
        paths["html"] = self.export_html(cards, title=result.get("summary", {}).get("title", "知识卡片"), filename=f"{base_filename}.html")
        paths["anki"] = self.export_anki(cards, f"{base_filename}.tsv")

        return paths

    @staticmethod
    def _format_timestamp(seconds: float) -> str:
        """格式化时间戳"""
        if seconds < 0:
            return "00:00"
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        if hours > 0:
            return f"{hours:02d}:{minutes:02d}:{secs:02d}"
        return f"{minutes:02d}:{secs:02d}"

    @staticmethod
    def _escape_html(text: str) -> str:
        """转义HTML特殊字符"""
        return (
            text.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&#39;")
        )
