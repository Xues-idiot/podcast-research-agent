"""批量导出器 - 支持一次性导出多种格式"""

import json
from pathlib import Path
from typing import Optional


class BatchExporter:
    """批量导出器"""

    def __init__(self, output_dir: str = "./exports"):
        """初始化导出器

        Args:
            output_dir: 输出目录
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def export_all_formats(
        self,
        data: dict,
        base_name: str,
        include_formats: list = None,
    ) -> dict:
        """导出所有格式

        Args:
            data: 要导出的数据
            base_name: 基础文件名
            include_formats: 要包含的格式列表

        Returns:
            导出的文件路径字典
        """
        if include_formats is None:
            include_formats = ["json", "markdown", "csv", "txt"]

        paths = {}

        if "json" in include_formats:
            paths["json"] = self._export_json(data, base_name)

        if "markdown" in include_formats:
            paths["markdown"] = self._export_markdown(data, base_name)

        if "csv" in include_formats:
            paths["csv"] = self._export_csv(data, base_name)

        if "txt" in include_formats:
            paths["txt"] = self._export_txt(data, base_name)

        return paths

    def _export_json(self, data: dict, base_name: str) -> str:
        """导出JSON"""
        path = self.output_dir / f"{base_name}.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return str(path)

    def _export_markdown(self, data: dict, base_name: str) -> str:
        """导出Markdown"""
        lines = [f"# {data.get('title', base_name)}", ""]

        # 摘要
        if data.get("summary"):
            lines.append("## 摘要")
            summary = data["summary"]
            if isinstance(summary, dict):
                lines.append(summary.get("content", ""))
            else:
                lines.append(str(summary))
            lines.append("")

        # 要点
        if data.get("keypoints"):
            lines.append("## 关键要点")
            for i, kp in enumerate(data["keypoints"], 1):
                content = kp.get("content", kp) if isinstance(kp, dict) else kp
                lines.append(f"{i}. {content}")
            lines.append("")

        # 知识卡片
        if data.get("knowledge_cards"):
            lines.append("## 知识卡片")
            for card in data["knowledge_cards"]:
                if isinstance(card, dict):
                    lines.append(f"- **{card.get('keypoint', '')}**")
            lines.append("")

        path = self.output_dir / f"{base_name}.md"
        path.write_text("\n".join(lines), encoding="utf-8")
        return str(path)

    def _export_csv(self, data: dict, base_name: str) -> str:
        """导出CSV"""
        import csv

        rows = []

        # 要点作为CSV行
        if data.get("keypoints"):
            for kp in data["keypoints"]:
                if isinstance(kp, dict):
                    rows.append([
                        kp.get("content", ""),
                        kp.get("importance", ""),
                        kp.get("timestamp", ""),
                    ])
                else:
                    rows.append([str(kp), "", ""])

        path = self.output_dir / f"{base_name}.csv"
        with open(path, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Content", "Importance", "Timestamp"])
            writer.writerows(rows)
        return str(path)

    def _export_txt(self, data: dict, base_name: str) -> str:
        """导出纯文本"""
        lines = [data.get("title", base_name), "", "=" * 50, ""]

        if data.get("summary"):
            summary = data["summary"]
            if isinstance(summary, dict):
                lines.append(summary.get("content", ""))
            else:
                lines.append(str(summary))
            lines.append("")

        if data.get("keypoints"):
            lines.append("关键要点:")
            for i, kp in enumerate(data["keypoints"], 1):
                content = kp.get("content", kp) if isinstance(kp, dict) else kp
                lines.append(f"{i}. {content}")

        path = self.output_dir / f"{base_name}.txt"
        path.write_text("\n".join(lines), encoding="utf-8")
        return str(path)


# 全局实例
_batch_exporter: Optional[BatchExporter] = None


def get_batch_exporter() -> BatchExporter:
    """获取全局批量导出器"""
    global _batch_exporter
    if _batch_exporter is None:
        _batch_exporter = BatchExporter()
    return _batch_exporter
