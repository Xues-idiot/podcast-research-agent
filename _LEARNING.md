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

*代号: Echo | 第2轮学习完毕 | 2026-03-25*
