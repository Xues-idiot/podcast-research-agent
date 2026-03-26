"""报告生成模块 - 生成完整研究报告"""

from typing import List, Optional

from openai import AsyncOpenAI

from echo.config import MiniMaxConfig


class ReportGenerator:
    """
    报告生成Agent - 生成完整的研究报告
    """

    SYSTEM_PROMPT = """你是一个专业的研究报告撰写专家。
你的任务是将播客/视频研究结果整理成结构化的研究报告。

报告结构：
1. 标题和元信息
2. 核心摘要 (2-3段)
3. 关键要点详解
4. 应用场景
5. 延伸思考

要求：
- 语言简洁专业
- 要点突出实用
- 保持客观，不添加原内容没有的信息
"""

    def __init__(self, config: MiniMaxConfig):
        self.client = AsyncOpenAI(
            api_key=config.api_key,
            base_url=config.base_url,
        )
        self.model = config.model

    async def generate(
        self,
        summary: dict,
        keypoints: List[dict],
        mindmap: dict,
        custom_instruction: Optional[str] = None,
    ) -> dict:
        """
        生成完整报告

        Args:
            summary: 摘要结果
            keypoints: 要点列表
            mindmap: 思维导图
            custom_instruction: 自定义指令

        Returns:
            完整报告
        """
        # 构建报告内容
        kp_text = "\n".join([
            f"{i+1}. {kp.get('content', '')}"
            for i, kp in enumerate(keypoints)
        ])

        mindmap_text = self._format_mindmap(mindmap)

        user_prompt = f"""请根据以下研究结果生成完整报告：

{custom_instruction or "生成标准研究报告"}

---
摘要：
标题: {summary.get('title', '无标题')}
内容: {summary.get('summary', '')}

要点：
{kp_text}

思维导图结构：
{mindmap_text}
"""

        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.7,
        )

        content = response.choices[0].message.content or ""

        return {
            "content": content,
            "title": summary.get("title", "研究报告"),
            "summary": summary,
            "keypoints": keypoints,
            "mindmap": mindmap,
        }

    def _format_mindmap(self, mindmap: dict) -> str:
        """格式化思维导图为文本"""
        lines = [f"主题: {mindmap.get('root', '')}"]
        for branch in mindmap.get("branches", []):
            lines.append(f"  - {branch.get('title', '')}")
            for child in branch.get("children", []):
                lines.append(f"    - {child}")
        return "\n".join(lines)

    def export_markdown(self, report: dict) -> str:
        """
        导出为Markdown格式

        Args:
            report: 报告字典

        Returns:
            Markdown格式字符串
        """
        lines = [
            f"# {report.get('title', '研究报告')}",
            "",
            "## 摘要",
            report.get("summary", {}).get("summary", ""),
            "",
            "## 亮点",
        ]

        for highlight in report.get("summary", {}).get("highlights", []):
            lines.append(f"- {highlight}")

        lines.extend([
            "",
            "## 关键要点",
        ])

        for kp in report.get("keypoints", []):
            lines.append(f"### {kp.get('id', 0)}. {kp.get('content', '')}")

        lines.extend([
            "",
            "## 应用场景",
            report.get("content", ""),  # 完整报告内容
        ])

        return "\n".join(lines)
