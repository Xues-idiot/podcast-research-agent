# Echo 学习记录

## 第1轮学习 (2026-03-24)

### GitHub 新发现

#### notebooklm-py 参考项目
- ** Stars**: 7.2k | **架构**: Python + CLI + API
- **核心类**: `NotebookLMClient` - 异步上下文管理器模式
- **API命名空间**: notebooks, sources, artifacts, chat, research, notes, settings, sharing
- **认证**: 使用Google cookies (SID, HSID等) + CSRF token (SNlM0e)
- **RPC协议**: Google batchexecute，内部方法ID随时可能变更
- **可用功能**:
  - 播客/视频生成 (generate_audio, generate_video)
  - 思维导图 (generate_mind_map)
  - 测验/闪卡 (generate_quiz, generate_flashcards)
  - 报告 (generate_report)
  - 聊天问答 (chat.ask)

#### 播客/视频研究相关GitHub项目关键词
```
podcast transcription AI
video summarization LLM
audio transcription whisper
bilibili youtube download
knowledge management agent
RAG knowledge graph
LangGraph transcription
multi-agent research
notebooklm alternative
```

### Sigma Skills 新应用

#### critical-thinking (批判性思维)
- **应用场景**: 评估播客内容可信度、识别论证逻辑漏洞
- **模板格式**: 论证结构 → 隐含假设 → 逻辑分析 → 证据评估 → 谬误识别
- **可借鉴**: 要点重要性评分和排序逻辑

#### data-processing (数据处理)
- **应用场景**: 转录文本后处理、标准化
- **流程模式**: 理解 → 清洗 → 转换 → 特征工程 → 验证 → 输出
- **可借鉴**: 处理流程模板化思维

### 代码架构设计决策

#### Echo vs notebooklm-py 差异点
| 方面 | notebooklm-py | Echo |
|------|----------------|------|
| 依赖 | Google NotebookLM (闭源) | 开源可部署 |
| 模型 | Google Gemini | MiniMax-M2.7 |
| 搜索 | - | Tavily API |
| 转录 | NotebookLM内置 | Whisper本地 |
| 下载 | YouTube/B站API | yt-dlp |

#### Echo 核心模块设计
```
backend/
├── agents/           # AI Agent (MiniMax)
│   ├── transcriber.py   # Whisper转录
│   ├── summarizer.py    # 摘要生成
│   ├── keypoint.py      # 要点提取
│   ├── linker.py        # 知识关联
│   └── exporter.py      # 导出
├── tools/            # 工具
│   ├── whisper.py       # Whisper封装
│   ├── bilibili.py      # B站下载
│   ├── youtube.py       # YouTube下载
│   └── podcast.py       # RSS解析
├── graph/            # LangGraph编排
│   └── research_graph.py
└── api/              # API接口
    └── research.py
```

### 关键技术点

#### 1. 异步客户端模式
```python
# notebooklm-py 风格
async with await NotebookLMClient.from_storage() as client:
    result = await client.chat.ask(nb_id, question)
```
→ Echo也应采用类似async上下文管理器模式

#### 2. MiniMax API集成
- BASE_URL: `https://api.minimaxi.com/anthropic`
- Model: `MiniMax-M2.7`
- 需要封装一个统一的LLM调用层

#### 3. Tavily搜索集成
- 用于深度研究模式的web搜索
- API: `tvly-dev-...`

#### 4. Whisper本地转录
- 不依赖云服务
- 使用 `openai/whisper` 本地模型

#### 5. yt-dlp 下载
- 支持B站、YouTube
- 需要处理认证和格式转换

---

## 第2轮学习 (2026-03-25)

### Sigma Skills 新应用

#### education/learning-assessment (学习评估)
- **应用场景**: 改进Echo的问答生成质量
- **核心概念**: Bloom's Taxonomy认知层次
  - L1 记忆：识别、回忆
  - L2 理解：解释、总结
  - L3 应用：使用、计算
  - L4 分析：分析、比较
  - L5 评价：评价、判断
  - L6 创造：设计、构建
- **应用**: 增强QA生成，添加level、level_name、knowledge_point、estimated_time、scoring_hint字段

#### education/course-design (课程设计)
- **应用场景**: 知识结构化组织
- **可借鉴**: 学习路径设计、评估标准

### 代码优化

#### QA生成增强
- 添加Bloom's taxonomy认知层次
- 添加知识点标注
- 添加预计时间和评分提示
- 前端添加颜色编码的难度标签

### GitHub 趋势观察
- Tavily CLI遇到Unicode编码问题 (GBK codec)
- 需要设置UTF-8环境变量处理emoji

---

## 第3轮学习 (2026-03-25)

### Sigma Skills 新应用

#### common/documentation (文档写作)
- **应用场景**: 改进Echo项目的文档质量
- **核心概念**: 文档结构、语言风格、格式化技巧
- **文档类型**: 产品文档、技术文档、业务文档
- **文档质量标准**: 完整性、准确性、时效性、可读性、可维护性
- **应用**: 更新README、SKILL、ARCHITECTURE文档

#### common/knowledge-management (知识管理)
- **应用场景**: 知识库建设和沉淀
- **核心概念**: 知识分类、知识获取、知识共享
- **可借鉴**: 知识关联和知识卡片设计

### 文档改进

#### README.md 增强
- 添加frontmatter (name, description)
- 添加前端安装和启动说明
- 添加SSE流式API文档
- 更新输出示例包含完整字段

#### SKILL.md 更新
- 添加qa_pairs到输出结构
- 添加Bloom's taxonomy认知层次
- 更新处理时间表

#### ARCHITECTURE.md 更新
- 添加完整项目结构(含frontend)
- 添加qa-generator模块文档
- 添加flashcard-exporter模块文档
- 添加8节点LangGraph流程说明

### 项目文档完成状态
- README.md - 用户手册、使用说明
- SKILL.md - Agent技能文档
- ARCHITECTURE.md - 架构文档
- WORKFLOW.md - 自主工作流
- PROGRESS.md - 进度记录
- _LEARNING.md - 学习记录
- docs/examples.md - 使用示例

---

*代号: Echo | 第3轮学习完毕 | 2026-03-25*
