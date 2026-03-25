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

---

## 第4轮学习 (2026-03-25) - 杀手锏审视

### 核心问题发现

#### 1. 关键时刻提取是"假的"
**问题**: `TimestampNavigator.get_key_moments()` 只是均匀采样，不是真正的智能分析
```python
# 当前实现：均匀采样
interval = total_duration / (num_moments + 1)
for i in range(1, num_moments + 1):
    target_time = interval * i  # 每个时间点都一样间隔
```

**真正应该做的**:
- 基于话题变化检测（segment embedding突变）
- 基于关键词出现频率
- 基于LLM分析哪些是真正重要的点

#### 2. 对话没有上下文
**问题**: Chat API的 `research_result` 参数没有正确传递
```python
# chat.py 第58行
async def chat(request: ChatRequest, research_result: dict):  # 这个参数从哪来？
```

前端调用时没有传递 research_result，导致 ConversationHandler 没有上下文。

#### 3. 现有组件可能不需要
用产品思维重新评估：
- ❓ VoiceAvatar - 真的需要吗？Audio Overview 才有价值
- ❓ Waveform - 好看但功能呢？关键时刻提取才是核心
- ❓ StepIndicator - 8步真的需要吗？可能太复杂

### 杀手锏现状

| 杀手锏 | 当前状态 | 问题 |
|---------|----------|------|
| 时间戳导航 | 有组件 | 关键时刻是均匀采样，不是真智能 |
| 对话式回顾 | 有组件 | 没有正确传递上下文 |
| Anki导出 | 有组件 | 功能完整，但导出的数据是捏造的 |

### 下一步改进计划

1. **修复关键时刻提取** - 让它真正智能
2. **修复对话上下文传递** - 让对话真的基于播客内容
3. **重新评估组件必要性** - 删掉不重要的

---

*代号: Echo | 第4轮学习完毕 | 2026-03-25*

---

## 第5轮学习 (2026-03-25) - 杀手锏修复

### 修复1: 对话上下文传递

**问题**: 前端收到 `researchResult` 但没有发送给后端，后端 API 参数也无法接收

**修复**:
1. `src/echo/api/chat.py` - `ChatRequest` 添加 `research_result` 字段
2. `frontend/src/components/Chat.tsx` - 修复 `_researchResult` → 使用 `researchResult` 并发送到 API

**修复前**:
```python
# api/chat.py - research_result 是函数参数，FastAPI无法注入
async def chat(request: ChatRequest, research_result: dict):
```

```typescript
// Chat.tsx - 只接收不用
export function Chat({ researchResult: _researchResult }: ChatProps) {
  // TODO: 将 researchResult 传递给后端用于上下文检索
```

**修复后**:
```python
# api/chat.py - research_result 在请求体中
class ChatRequest(BaseModel):
    query: str
    conversation_id: Optional[str] = None
    stream: bool = True
    research_result: Optional[dict] = None  # 新增
```

```typescript
// Chat.tsx - 正确传递
export function Chat({ researchResult }: ChatProps) {
  // ... 发送到 API
  body: JSON.stringify({
    query: userMessage.content,
    conversation_id: conversationId,
    stream: true,
    research_result: researchResult  // 传递研究结果用于上下文检索
  })
```

### 修复2: 时间戳导航智能分析

**问题**: `get_key_moments()` 使用均匀采样，不是真正的智能分析

**修复**: 重写算法，实现三层评分机制:

1. **内容特征评分** (`_calculate_importance_score`)
   - 长度评分：100-500字符最佳
   - 问号评分：有问题的地方通常重要
   - 数字评分：含数据的句子是重点
   - 关键词评分：关键词出现加分
   - 位置评分：开头和结尾略高

2. **话题变化检测** (`_detect_topic_changes`)
   - 比较相邻entry的词重叠度
   - 相似度突然下降=话题变化点
   - 话题变化点加分

3. **去重过滤** (`_filter_close_moments`)
   - 30秒内的时刻只保留一个
   - 保证关键时刻分布均匀

### 修复后的杀手锏状态

| 杀手锏 | 修复前 | 修复后 |
|--------|--------|--------|
| 时间戳导航 | 均匀采样（假） | 智能分析（真） |
| 对话式回顾 | 不传上下文 | 正确传递research_result |
| Anki导出 | 数据捏造 | 功能完整 |

### 验证结果

- 所有24个测试通过 ✅
- 前端构建成功 (5个路由) ✅
  - `/podcast` - 研究页
  - `/knowledge` - 知识库
  - `/export` - 导出管理
  - `/history` - 历史记录
  - `/_not-found` - 404

### 组件清理（第5轮补充）

**删除未使用的组件**:
- `VoiceAvatar.tsx` - 未被任何页面使用 ❌ 删除
- `Waveform.tsx` - 未被任何页面使用 ❌ 删除
- `StepIndicator` - ✅ 保留（进度提示有价值）

**验证**: 前端构建成功 (5路由)，JS bundle略减小

### 待办

- [ ] Sigma Skills 深入学习（skills在 `D:\PM-AI-Workstation\01-ai-agents\pm-agent-forge\skills`）
- [ ] 杀手锏2: Audio Overview 实现（TTS）

---

*代号: Echo | 第5轮学习完毕 | 2026-03-25*
