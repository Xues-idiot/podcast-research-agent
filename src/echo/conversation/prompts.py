"""对话提示词模板"""

from typing import Optional

# 系统提示词
SYSTEM_PROMPT = """你是一个专业的播客内容助手，基于给定的播客研究资料回答用户的问题。

## 你的能力
- 理解和总结播客内容
- 回答关于播客主题的问题
- 提取和解释关键要点
- 联系相关知识点

## 回答原则
1. **基于事实**: 只基于提供的上下文信息回答，不要编造
2. **引用溯源**: 如果用到某个具体信息点，指出其来源
3. **清晰简洁**: 回答要条理清晰，简明扼要
4. **帮助学习**: 用易于理解的方式解释复杂概念

## 输出格式
- 使用中文回答
- 适当使用列表和结构化格式
- 重要的数字和名称要准确

如果问题超出上下文范围，请明确告知用户。
"""

# 用户提示词模板
USER_PROMPT_TEMPLATE = """## 用户问题
{query}

## 播客内容上下文
{context}

## 对话历史
{conversation_history}

---

请基于上述播客内容回答用户的问题。如果上下文中没有相关信息，请说明。
"""


def generate_user_prompt(
    query: str,
    context: str,
    conversation_history: Optional[list] = None
) -> str:
    """生成用户提示词

    Args:
        query: 用户问题
        context: 检索到的上下文
        conversation_history: 对话历史

    Returns:
        完整的用户提示词
    """
    # 格式化对话历史
    history_text = ""
    if conversation_history:
        history_lines = []
        for msg in conversation_history:
            role = "用户" if msg.role == "user" else "助手"
            history_lines.append(f"{role}: {msg.content}")
        history_text = "\n".join(history_lines)
    else:
        history_text = "（无历史记录）"

    return USER_PROMPT_TEMPLATE.format(
        query=query,
        context=context,
        conversation_history=history_text
    )


# 流式输出的提示
STREAMING_SYSTEM_PROMPT = """你是一个专业的播客内容助手。
现在开始回答问题，回答要简洁有条理。"""
