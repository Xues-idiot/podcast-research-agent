# Echo (播客研究Agent) - 架构文档

## 项目结构

```
src/echo/
├── __init__.py           # 模块入口
├── client.py             # EchoClient 主客户端
├── config.py             # 配置管理
├── agents/               # AI Agent 模块
│   ├── transcriber.py    # 音频转录 (Whisper)
│   ├── summarizer.py     # 摘要生成 (LLM)
│   ├── keypoint.py       # 要点提取 (LLM)
│   ├── linker.py         # 知识关联 (Tavily)
│   └── mindmap.py        # 思维导图 (LLM)
├── conversation/         # 对话模块 (新增)
│   ├── __init__.py
│   ├── chat.py          # 对话处理器
│   ├── history.py       # 对话历史存储
│   └── prompts.py       # 提示词模板
├── knowledge/           # 知识库模块 (新增)
│   ├── __init__.py
│   ├── entry.py        # Entry模型和EntryStore
│   ├── splitter.py     # TextSplitter分割器
│   ├── bi_encoder.py   # Bi-encoder向量编码
│   └── retriever.py    # 知识检索器
├── navigation/          # 时间戳导航模块 (新增)
│   ├── __init__.py
│   └── timestamp.py     # 时间戳导航器
├── exporters/            # 导出模块 (新增)
│   ├── __init__.py
│   └── knowledge_card_exporter.py  # 知识卡片导出器
├── memory/               # 记忆模块 (新增)
│   ├── __init__.py
│   ├── memory_store.py  # 记忆存储管理
│   └── memory_updater.py # LLM驱动的记忆更新
├── tools/                # 工具模块
│   ├── downloader.py     # 统一下载接口
│   ├── bilibili.py       # B站下载
│   ├── youtube.py        # YouTube下载
│   └── podcast.py        # RSS解析
├── graph/                # LangGraph编排
│   └── research_graph.py # 研究流程图
└── api/                 # API接口
    ├── research.py       # 研究API路由
    ├── chat.py           # 对话API路由 (新增)
    ├── knowledge.py      # 知识库API路由 (新增)
    ├── sources.py        # 多源聚合API路由 (新增)
    ├── navigation.py     # 时间戳导航API路由 (新增)
    ├── export.py         # 导出API路由 (新增)
    └── memory.py         # 记忆API路由 (新增)

echo_cli/                 # CLI入口
frontend/                  # Next.js前端
├── src/
│   ├── app/             # App Router页面
│   ├── components/       # React组件 (19个, 新增Chat)
│   ├── lib/             # 工具函数
│   └── store/           # Zustand状态管理
tests/
├── unit/               # 单元测试
└── integration/         # 集成测试
scripts/                  # 脚本
├── quickstart.py
└── api_server.py       # API服务器入口
```

---

## transcript-downloader 模块

### 类型
- `URL` - 播客/视频链接
- `Transcript` - 转录文本 `{text, segments, language}`

### 函数
- `download_audio(url: URL) -> AudioFile` 下载音视频
- `transcribe(audio: AudioFile) -> Transcript` Whisper转录

### 状态
- ✅ 已实现 `tools/downloader.py`, `tools/bilibili.py`, `tools/youtube.py`
- ✅ 已实现 `agents/transcriber.py`

---

## summarizer 模块

### 类型
- `SummaryRequest` - 摘要请求
- `Summary` - 摘要结果 `{title, summary, highlights}`

### 函数
- `summarize(transcript: Transcript) -> Summary` 生成摘要
- `extract_metadata(transcript: Transcript) -> Metadata` 提取元数据

### 状态
- ✅ 已实现 `agents/summarizer.py`

---

## keypoint-generator 模块

### 类型
- `KeyPoint` - 关键要点 `{id, content, importance, applications}`
- `KeyPointList` - 要点列表

### 函数
- `generate_keypoints(transcript: Transcript, num: int) -> KeyPointList` 生成要点
- `score_keypoints(keypoints: KeyPointList) -> KeyPointList` 按重要性排序

### 状态
- ✅ 已实现 `agents/keypoint.py`

---

## knowledge-linker 模块

### 类型
- `KnowledgeCard` - 知识卡片 `{keypoint, related, confidence}`
- `RelatedItem` - 关联条目 `{title, url, content}`

### 函数
- `link_to_knowledge(keypoint: KeyPoint, knowledge_base: VectorStore) -> RelatedItem` 知识关联
- `build_knowledge_card(keypoint: KeyPoint, related: RelatedItem) -> KnowledgeCard` 构建知识卡片

### 状态
- ✅ 已实现 `agents/linker.py` (使用Tavily API)

---

## mindmap-generator 模块

### 类型
- `MindMapNode` - 思维导图节点
- `MindMap` - 思维导图 `{root, branches: [{title, children}]}`

### 函数
- `generate_mindmap(keypoints: KeyPointList) -> MindMap` 生成思维导图
- `export_json(mindmap: MindMap) -> str` 导出JSON格式

### 状态
- ✅ 已实现 `agents/mindmap.py`

---

## report-generator 模块

### 类型
- `ResearchReport` - 研究报告 `{title, content}`

### 函数
- `generate_report(summary: Summary, keypoints: KeyPointList, mindmap: MindMap) -> ResearchReport` 生成完整报告

### 状态
- ✅ 已实现 `agents/report.py`，已集成到 `graph/research_graph.py`

---

## qa-generator 模块

### 类型
- `QAPair` - 问答对 `{question, answer, type, level, level_name, knowledge_point, estimated_time, scoring_hint}`
- `BloomLevel` - Bloom's taxonomy认知层次 (L1-L6)

### 函数
- `generate_qa(transcript: Transcript, num: int) -> List[QAPair]` 生成问答对

### Bloom's Taxonomy
- L1 记忆：识别、回忆基本事实
- L2 理解：解释、总结概念
- L3 应用：将知识应用于新情境
- L4 分析：分解和理解结构关系
- L5 评价：基于标准进行判断
- L6 创造：综合知识提出新方案

### 状态
- ✅ 已实现 `agents/qa.py`，已集成到 `graph/research_graph.py`

---

## flashcard-exporter 模块

### 类型
- `FlashCard` - 闪卡 `{front, back, metadata}`

### 函数
- `export_json(result: ResearchResult, path: str)` 导出JSON格式
- `export_markdown(result: ResearchResult, path: str)` 导出Markdown格式
- `export_html(result: ResearchResult, path: str)` 导出HTML格式

### 状态
- ✅ 已实现 `agents/flashcard.py`

---

## graph/research_graph.py

### 类型
- `ResearchState` - 流程状态 `{url, audio_path, transcript, summary, keypoints, mindmap, knowledge_cards, report, qa_pairs, error}`

### 流程
```
download -> transcribe -> summarize -> keypoint -> mindmap -> link -> report -> qa -> output
```

### 状态
- ✅ 完整流程已实现，8个节点全部集成

---

## conversation 模块 (对话式问答)

> 基于播客研究结果的对话式问答功能，支持多轮对话和引用溯源

### 类型
- `ChatMessage` - 对话消息 `{role, content, timestamp, references}`
- `ChatResponse` - 聊天响应 `{answer, references, conversation_id}`

### 函数
- `ConversationHandler(research_result) -> handler` 创建对话处理器
- `handler.chat(query, stream) -> AsyncIterator[ChatResponse]` 处理对话
- `handler.get_conversation_id() -> str` 获取对话ID
- `handler.clear_history()` 清除对话历史

### ConversationHistory 类
- `add(message)` 添加消息
- `get_recent(n)` 获取最近n条消息
- `get_all()` 获取所有消息
- `export_markdown()` 导出为Markdown
- 持久化到 `~/.echo/conversations/{id}.json`

### API端点
- `POST /api/chat/chat` - 对话接口 (支持流式SSE)
- `DELETE /api/chat/conversation/{id}` - 删除对话
- `GET /api/chat/conversation/{id}/history` - 获取历史
- `POST /api/chat/conversation/{id}/export` - 导出对话

### 状态
- ✅ 基础对话处理器已实现
- ✅ 对话历史持久化已实现
- ⚠️ 向量检索待集成 (TODO)
- ⚠️ MiniMax API集成待完成 (TODO)

### 参考
- khoj 对话系统架构

---

## knowledge 模块 (知识库 Entry)

> 将播客转录分割成可检索的 Entry，支持向量检索

### 类型
- `Entry` - 最小检索单元 `{id, podcast_id, raw, compiled, start_time, end_time, metadata}`
- `EntryStore` - Entry 持久化存储管理器

### EntryStore 类
- `add_entries(podcast_id, entries)` 添加Entry
- `get_entries(podcast_id)` 获取所有Entry
- `get_entries_by_time_range(podcast_id, start, end)` 按时间范围获取
- `search(podcast_id, query, top_k)` 关键词搜索
- `delete_entries(podcast_id)` 删除Entry
- 持久化到 `~/.echo/knowledge/{podcast_id}.json`

### TextSplitter 类
- `split_transcript(podcast_id, segments, min_duration, max_duration)` 按时间窗口分割
- `split_text(text)` 递归字符分割
- `RecursiveTextSplitter` 带重叠的递归分割

### API端点
- `POST /api/knowledge/entries` - 从转录创建Entry
- `GET /api/knowledge/entries/{podcast_id}` - 获取所有Entry
- `GET /api/knowledge/entries/{podcast_id}/time-range` - 按时间范围获取
- `DELETE /api/knowledge/entries/{podcast_id}` - 删除Entry
- `POST /api/knowledge/search` - 搜索Entry
- `GET /api/knowledge/podcasts` - 列出已存储播客

### 状态
- ✅ Entry 模型已实现
- ✅ EntryStore 持久化已实现
- ✅ TextSplitter 分割器已实现
- ⚠️ 向量嵌入待集成 (Bi-encoder TODO)
- ⚠️ 向量检索待集成 (TODO)

### 参考
- khoj Entry 模型和分割策略

---

## navigation 模块 (时间戳导航)

> 基于关键内容的时间戳跳转，支持按时间戳获取附近的内容片段

### 类型
- `TimestampEntry` - 时间戳条目 `{timestamp, content, entry_id, type, relevance}`
- `JumpResult` - 跳转结果 `{target_timestamp, nearby_entries, context_before, context_after, jump_type}`

### TimestampNavigator 类
- `jump_to(timestamp, window_seconds) -> JumpResult` 跳转到指定时间戳
- `get_key_moments(num_moments) -> list[TimestampEntry]` 获取关键时刻列表
- `get_moments_by_keypoints(keypoints) -> list[TimestampEntry]` 根据关键点获取时间戳
- `get_moments_by_qa(qa_pairs) -> list[TimestampEntry]` 根据问答对获取时间戳
- `format_timestamp(seconds) -> str` 格式化时间戳 (MM:SS 或 HH:MM:SS)
- `parse_timestamp(timestamp_str) -> float` 解析时间戳字符串

### API端点
- `POST /api/navigation/register` - 注册播客时间戳数据
- `POST /api/navigation/jump` - 跳转到指定时间戳
- `GET /api/navigation/moments/{podcast_id}` - 获取关键时刻列表
- `POST /api/navigation/moments/from-keypoints` - 从关键点生成时间戳
- `POST /api/navigation/moments/from-qa` - 从问答生成时间戳高亮
- `GET /api/navigation/parse/{timestamp_str}` - 解析时间戳字符串
- `DELETE /api/navigation/{podcast_id}` - 注销播客

### 前端组件
- `TimelineNavigation` - 时间轴导航组件，支持播放控制、时间戳跳转、关键时刻列表

### 状态
- ✅ TimestampNavigator 已实现
- ✅ Navigation API 已实现
- ✅ TimelineNavigation 前端组件已实现

### 参考
- khoj trainOfThoughtVideoPlayer 时间戳导航实现

---

## exporters 模块 (知识卡片导出)

> 将知识卡片导出为多种格式，支持引用和时间戳

### 类型
- `Citation` - 引用信息 `{entry_id, timestamp, formatted_time, content, score}`
- `KnowledgeCardExport` - 导出的知识卡片 `{keypoint, importance, citations, related_items, confidence, summary}`
- `KnowledgeCardExporter` - 导出器类

### KnowledgeCardExporter 类
- `export_json(cards, filename) -> str` 导出为JSON
- `export_markdown(cards, filename) -> str` 导出为Markdown
- `export_html(cards, title, filename) -> str` 导出为HTML (完整样式)
- `export_anki(cards, filename) -> str` 导出为Anki格式 (TSV)
- `build_cards_from_result(result, entries) -> list[KnowledgeCardExport]` 从结果构建卡片
- `export_all_formats(result, entries) -> dict` 导出所有格式

### API端点
- `POST /api/export/knowledge-cards` - 导出知识卡片 (支持 json/markdown/html/pdf/anki)
- `POST /api/export/knowledge-cards/all` - 导出所有格式

### 状态
- ✅ KnowledgeCardExporter 已实现
- ✅ Export API 已实现
- ✅ 支持多种格式导出 (JSON, Markdown, HTML, PDF, Anki)

### 参考
- khoj 知识卡片导出

---

## memory 模块 (记忆系统)

> 跨会话用户偏好学习，参考 deer-flow 的记忆系统设计

### 类型
- `Fact` - 记忆事实 `{id, content, category, confidence, created_at, source}`
- `UserMemory` - 用户记忆 `{user_id, work_context, personal_context, top_of_mind, recent_months, facts}`
- `MemoryStore` - 记忆存储管理器
- `MemoryUpdater` - LLM驱动的记忆更新器

### MemoryStore 类
- `get_memory(user_id) -> UserMemory` 获取用户记忆
- `update_memory(user_id, **kwargs) -> UserMemory` 更新记忆字段
- `add_fact(user_id, content, category, confidence, source) -> Fact` 添加事实
- `get_facts(user_id, category, min_confidence) -> list[Fact]` 获取事实列表
- `get_recent_facts(user_id, top_k) -> list[Fact]` 获取重要事实
- `inject_into_context(user_id) -> str` 生成注入文本

### MemoryUpdater 类
- `learn_podcast_preference(user_id, podcast_info)` 学习播客偏好
- `learn_export_preference(user_id, format_type)` 学习导出偏好
- `learn_research_topic(user_id, topic)` 学习研究主题
- `get_personalized_context(user_id) -> str` 获取个性化上下文

### API端点
- `GET /api/memory/{user_id}` - 获取用户记忆
- `POST /api/memory/update` - 更新记忆
- `POST /api/memory/facts` - 添加事实
- `GET /api/memory/{user_id}/facts` - 获取事实列表
- `POST /api/memory/learn` - 学习偏好
- `GET /api/memory/{user_id}/context` - 获取个性化上下文
- `DELETE /api/memory/{user_id}` - 清除记忆

### 状态
- ✅ MemoryStore 记忆存储已实现
- ✅ MemoryUpdater 记忆更新已实现
- ✅ Memory API 路由已实现
- ⚠️ LLM驱动的自动记忆更新待接入 MiniMax API

### 参考
- deer-flow 记忆系统

---

## 配置

### 环境变量
```
MINIMAX_API_KEY      # MiniMax API密钥
MINIMAX_BASE_URL     # API地址 (默认: https://api.minimaxi.com/anthropic)
MINIMAX_MODEL        # 模型 (默认: MiniMax-M2.7)
TAVILY_API_KEY      # Tavily API密钥
```

---

*架构文档 | Echo | 2026-03-24 | 第1轮更新*