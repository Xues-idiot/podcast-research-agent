"""问答生成模块 - 从转录生成问答对"""

from typing import List

from openai import AsyncOpenAI

from echo.config import MiniMaxConfig


# Bloom's Taxonomy cognitive levels
BLOOM_LEVELS = {
    "L1": {"name": "记忆", "verb": "识别、回忆、列出", "description": "测试对基本事实和概念的回忆"},
    "L2": {"name": "理解", "verb": "解释、总结、分类", "description": "测试对概念的理解和解释能力"},
    "L3": {"name": "应用", "verb": "使用、计算、演示", "description": "测试将知识应用于实际情境"},
    "L4": {"name": "分析", "verb": "分析、比较、分解", "description": "测试分解和理解结构的能力"},
    "L5": {"name": "评价", "verb": "评价、判断、批判", "description": "测试基于标准进行判断的能力"},
    "L6": {"name": "创造", "verb": "设计、构建、创作", "description": "测试综合知识创造新解决方案"},
}


class QAGenerator:
    """
    问答生成Agent - 从转录内容生成问答对

    基于Bloom's Taxonomy认知层次设计，支持：
    - L1 记忆：识别和回忆基本信息
    - L2 理解：解释和总结概念
    - L3 应用：将知识应用于新情境
    - L4 分析：分解和理解结构
    - L5 评价：基于标准进行判断
    - L6 创造：综合创造新解决方案
    """

    SYSTEM_PROMPT = """你是一个专业的播客内容分析专家，擅长基于Bloom's Taxonomy认知层次设计问题。

你的任务是从转录文本中生成有价值的问答对，每个问题都要标注认知层次。

要求：
1. 问题要有深度，能测试对内容的理解
2. 答案要准确，引用原文中的关键信息
3. 问题类型多样，覆盖不同认知层次（L1-L6）
4. 每个问答对要简洁明了
5. 包含评分提示，说明如何评判答案优劣

输出JSON格式：
{
    "qa_pairs": [
        {
            "question": "问题内容",
            "answer": "答案内容",
            "type": "fact|comprehension|application|analysis|evaluation|creation",
            "level": "L1|L2|L3|L4|L5|L6",
            "level_name": "记忆|理解|应用|分析|评价|创造",
            "knowledge_point": "知识点名称",
            "source": "原文引用（可选）",
            "estimated_time": "1-2分钟",
            "scoring_hint": "评分提示，说明如何评判答案"
        }
    ]
}

确保：
- L1问题占20%左右（基础概念）
- L2-L3问题占50%左右（理解和应用）
- L4-L6问题占30%左右（分析、评价、创造）
"""

    def __init__(self, config: MiniMaxConfig):
        self.client = AsyncOpenAI(
            api_key=config.api_key,
            base_url=config.base_url,
        )
        self.model = config.model

    async def generate(self, transcript: dict, num: int = 5) -> List[dict]:
        """
        生成问答对

        Args:
            transcript: 转录结果
            num: 生成数量

        Returns:
            问答对列表，包含Bloom's taxonomy层次信息
        """
        text = transcript.get("text", "")

        user_prompt = f"""请从以下转录文本中生成{num}个有价值的问答对：

{text[:8000]}

要求覆盖不同认知层次：
- L1 记忆：识别和回忆基本事实
- L2 理解：解释和总结概念
- L3 应用：将知识应用于新情境
- L4 分析：分解和理解结构关系
- L5 评价：基于标准进行判断
- L6 创造：综合知识提出新方案
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

        return self._parse_qa(content)

    def _parse_qa(self, content: str) -> List[dict]:
        """解析问答对"""
        import json
        import re

        # 尝试提取JSON
        json_match = re.search(r'\{[\s\S]*\}', content)
        if json_match:
            try:
                data = json.loads(json_match.group())
                qa_pairs = data.get("qa_pairs", [])
                # 确保每个QA对都有完整字段
                for qa in qa_pairs:
                    if "level" not in qa:
                        qa["level"] = "L2"
                    if "level_name" not in qa:
                        qa["level_name"] = BLOOM_LEVELS.get(qa["level"], {}).get("name", "理解")
                    if "estimated_time" not in qa:
                        qa["estimated_time"] = "1-2分钟"
                    if "scoring_hint" not in qa:
                        qa["scoring_hint"] = "答案准确且完整地回应问题即可得分"
                return qa_pairs
            except json.JSONDecodeError:
                pass

        # 降级：简单解析
        qa_pairs = []
        lines = content.strip().split("\n")

        current_q = None
        for line in lines:
            line = line.strip()
            if not line:
                continue

            if line.startswith("Q:") or line.startswith("问："):
                current_q = line[2:].strip() if line.startswith("Q:") else line[3:].strip()
            elif line.startswith("A:") or line.startswith("答："):
                if current_q:
                    answer = line[2:].strip() if line.startswith("A:") else line[3:].strip()
                    qa_pairs.append({
                        "question": current_q,
                        "answer": answer,
                        "type": "comprehension",
                        "level": "L2",
                        "level_name": "理解",
                        "estimated_time": "1-2分钟",
                        "scoring_hint": "答案准确且完整地回应问题即可得分",
                    })
                    current_q = None

        return qa_pairs

    def export_markdown(self, qa_pairs: List[dict]) -> str:
        """
        导出为Markdown格式

        Args:
            qa_pairs: 问答对列表

        Returns:
            Markdown字符串
        """
        lines = ["# 问答对", ""]

        for i, qa in enumerate(qa_pairs, 1):
            lines.append(f"## Q{i}: {qa.get('question', '')}")
            lines.append("")
            lines.append(f"**A:** {qa.get('answer', '')}")
            lines.append("")

            if qa.get("type"):
                lines.append(f"*类型: {qa['type']}*")
                lines.append("")

            if qa.get("level"):
                lines.append(f"*认知层次: {qa.get('level', '')} - {qa.get('level_name', '')}*")
                lines.append("")

            if qa.get("knowledge_point"):
                lines.append(f"*知识点: {qa['knowledge_point']}*")
                lines.append("")

            if qa.get("estimated_time"):
                lines.append(f"*预计时间: {qa['estimated_time']}*")
                lines.append("")

            if qa.get("scoring_hint"):
                lines.append(f"*评分提示: {qa['scoring_hint']}*")
                lines.append("")

            lines.append("---")
            lines.append("")

        return "\n".join(lines)
