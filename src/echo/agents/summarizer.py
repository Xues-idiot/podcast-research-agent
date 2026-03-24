"""摘要Agent - 使用LLM生成摘要"""

from typing import Optional

from openai import AsyncOpenAI

from echo.config import MiniMaxConfig


class Summarizer:
    """
    摘要Agent - 生成播客/视频内容的摘要
    """

    SYSTEM_PROMPT = """你是一个专业的播客内容摘要专家。
你的任务是对转录文本进行分析，生成简洁、准确的摘要。

摘要要求：
1. 提取核心主题和话题
2. 识别主播/嘉宾的主要观点
3. 总结关键结论或洞见
4. 保持客观，不添加原文没有的信息

输出格式：
- 标题：简洁描述内容主题
- 摘要：2-3段话概括核心内容
- 亮点：3-5个关键点
"""

    def __init__(self, config: MiniMaxConfig):
        self.client = AsyncOpenAI(
            api_key=config.api_key,
            base_url=config.base_url,
        )
        self.model = config.model

    async def summarize(self, transcript: dict, custom_instruction: Optional[str] = None) -> dict:
        """
        生成摘要

        Args:
            transcript: 转录结果，包含 text, segments, language
            custom_instruction: 自定义指令

        Returns:
            包含 title, summary, highlights 的字典
        """
        text = transcript.get("text", "")
        language = transcript.get("language", "zh")

        user_prompt = f"""请为以下播客/视频转录内容生成摘要：

{custom_instruction or "生成标准摘要"}

---
转录内容：
{text[:8000]}  # 限制长度避免token超限
"""

        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.7,
        )

        content = response.choices[0].message.content

        # 解析LLM输出为结构化数据
        # 简单解析，实际可能需要更 robust 的解析
        return self._parse_summary(content, language)

    def _parse_summary(self, content: str, language: str) -> dict:
        """解析LLM输出为结构化格式"""
        lines = content.strip().split("\n")

        result = {
            "title": "",
            "summary": "",
            "highlights": [],
        }

        current_section = None
        buffer = []

        for line in lines:
            line = line.strip()
            if not line:
                continue

            if line.startswith("标题："):
                result["title"] = line[3:].strip()
            elif line.startswith("摘要："):
                current_section = "summary"
                result["summary"] = line[3:].strip()
            elif line.startswith("亮点："):
                current_section = "highlights"
            elif line.startswith("- ") or line.startswith("• "):
                result["highlights"].append(line[2:].strip())
            elif current_section == "summary":
                result["summary"] += "\n" + line

        return result
