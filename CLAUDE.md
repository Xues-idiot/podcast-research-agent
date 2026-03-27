# Echo播客研究Agent - 开发工作流

## 项目概述

- **产品**: Echo播客研究Agent
- **口号**: "让播客内容真正变成你的知识"
- **核心功能**: 时间戳导航、对话式回顾、Anki导出
- **差异化**: 中文优先、轻量、易用

## 技术栈

- **前端**: Next.js 15, React, TypeScript, Tailwind CSS, motion/react
- **后端**: Python, FastAPI, LangGraph
- **API**: MiniMax (LLM + TTS)
- **存储**: Khoj (知识库), 本地SQLite

## 循环工作流

### 自动循环流程 (每轮迭代)

```
┌─────────────────────────────────────────────────────────────┐
│                     Echo 开发循环                            │
│                                                             │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────┐ │
│  │ 1.代码审查 │ -> │ 2.Bug修复 │ -> │ 3.代码优化│ -> │4.新功能│ │
│  │  阶段     │    │  阶段     │    │   阶段    │    │阶段  │ │
│  └──────────┘    └──────────┘    └──────────┘    └──────┘ │
│       ↑                                            │        │
│       │              定期审查 (每5轮)              │        │
│       │───────────────────────────────────────────┘        │
│       │                                                       │
│       │  ┌──────────┐                                        │
│       └──│ 5.功能审查│ <- 审查功能是否真正需要、是否真正能用      │
│          │  阶段     │                                        │
│          └──────────┘                                        │
└─────────────────────────────────────────────────────────────┘
```

### 阶段详解

#### 阶段1: 代码审查 (Code Review)
- 静态分析: `py_compile` 编译检查
- 类型检查: 验证 dataclass/dict 类型兼容性
- 逻辑检查: 查找明显的逻辑错误
- 最佳实践: 检查是否遵循项目规范

#### 阶段2: Bug修复 (Bug Fix)
- 优先修复: 影响核心功能的bug
- 类型错误: dataclass传参、None值处理
- 逻辑错误: 条件判断、循环处理
- 边界情况: 空值、越界、异常处理

#### 阶段3: 代码优化 (Code Optimization)
- 性能优化: 减少不必要的计算
- 内存优化: 避免内存泄漏
- 可维护性: 简化复杂逻辑
- 冗余清理: 删除无用代码

#### 阶段4: 新功能开发 (New Features)
- 遵循产品路线图
- 优先实现高价值功能
- 确保与现有代码集成
- 完整的测试覆盖

#### 阶段5: 功能审查 (Feature Audit) - 每5轮执行
- **必要性审查**: 功能是否真正需要？
- **可用性审查**: 功能是否真正能用？
- **价值审查**: 功能是否为用户创造价值？
- **去留决定**: 保留、优化或移除

## 目录结构

```
src/echo/
├── agents/           # AI Agent实现
├── api/              # FastAPI路由
├── research/         # 研究逻辑模块
├── sources/          # 播客源解析
├── tools/            # 工具函数
├── exporters/        # 导出器
├── conversation/     # 对话管理
├── knowledge/        # 知识库
└── webhooks.py       # Webhook系统
```

## 代码规范

### Python
- 使用 `dataclass` 而非 dict 传递结构化数据
- async/await 正确配对，无 await 不使用 async
- 类型注解完整
- 异常处理得当
- 避免硬编码

### 前端 (TypeScript/React)
- 组件职责单一
- Props 类型定义完整
- 避免 any 类型
- 遵循项目命名规范

## 开发命令

```bash
# Python 编译检查
python -m py_compile src/echo/**/*.py

# 前端类型检查
cd frontend && npm run type-check

# 运行测试 (如有)
pytest tests/
```

## 持续改进指标

| 指标 | 目标 |
|------|------|
| 编译通过率 | 100% |
| Bug修复率 | 每轮至少1个 |
| 功能完整性 | 每轮至少1个新功能/优化 |
| 代码行数控制 | 合理增长，避免膨胀 |

## 自动化脚本

详见: `scripts/auto_improve.py`

执行命令:
```bash
python scripts/auto_improve.py --rounds 10 --review-every 5
```

参数:
- `--rounds`: 迭代轮数
- `--review-every`: 每N轮进行一次功能审查
- `--mode`: `bug-fix` | `feature` | `optimize` | `audit`

## 开发日志

### 第36-40轮 (2026-03-26)

**新增功能模块:**

| 轮次 | 功能 | 文件 |
|------|------|------|
| 36 | 导出预设 | `research/export_templates.py`, `api/export_templates.py` |
| 37 | Markdown格式化工具 | `research/exporters/md.py` |
| 38 | HTML格式化工具 | `research/exporters/html_exporter.py` |
| 39 | 存储使用统计 | `research/storage_stats.py`, `api/storage_stats.py` |

**编译状态:** 100% 通过 ✅

### 第41-50轮 (2026-03-26)

**新增功能模块:**

| 轮次 | 功能 | 文件 |
|------|------|------|
| 41 | URL解析器增强 | `research/url_parser.py`, `api/url_parser.py` |
| 42 | 内容格式检测器 | `research/format_detector.py`, `api/format_detector.py` |
| 43-44 | 智能分块策略 | `research/chunks.py`, `api/chunks.py` |
| 45-46 | 文本统计工具 | `research/word_counter.py`, `api/word_counter.py` |
| 47-48 | 内容去重工具 | `research/deduplicator.py`, `api/deduplicator.py` |
| 49-50 | 关键词提取 | `research/keyword_extractor.py`, `api/keyword_extractor.py` |

**编译状态:** 100% 通过 ✅

### 第51-60轮 (2026-03-26)

**新增功能模块:**

| 轮次 | 功能 | 文件 |
|------|------|------|
| 51-52 | 文本分割器 | `research/text_splitter.py`, `api/text_splitter.py` |
| 53 | 文本合并器 | `research/merger.py`, `api/merger.py` |
| 54 | 文本清理器 | `research/cleaner.py`, `api/cleaner.py` |
| 55 | 文本截断器 | `research/truncator.py`, `api/truncator.py` |
| 56 | 文本填充器 | `research/padding.py`, `api/padding.py` |
| 57 | 语言检测器 | `research/language_detector.py`, `api/language_detector.py` |
| 58 | 文本差异比较器 | `research/textdiff.py`, `api/textdiff.py` |
| 59 | 文本验证器 | `research/validator.py`, `api/validator.py` |
| 60 | 文本前缀工具 | `research/prefixer.py`, `api/prefixer.py` |

**编译状态:** 100% 通过 ✅

### 第61-100轮 (2026-03-27)

**新增功能模块:**

| 轮次 | 功能 | 文件 |
|------|------|------|
| 61 | 文本标准化工具 | `research/text_normalizer.py`, `api/text_normalizer.py` |
| 62 | 行过滤器 | `research/line_filter.py`, `api/line_filter.py` |
| 63 | 文本排序器 | `research/text_sorter.py`, `api/text_sorter.py` |
| 64 | 全文搜索引擎 | `research/search_engine.py`, `api/search_engine.py` |
| 65 | 文本替换器 | `research/text_replacer.py`, `api/text_replacer.py` |
| 66 | 行号工具 | `research/line_numberer.py`, `api/line_numberer.py` |
| 67 | 文本编码器 | `research/text_encoder.py`, `api/text_encoder.py` |
| 68 | 大小写转换器 | `research/case_converter.py`, `api/case_converter.py` |
| 69 | 文本哈希器 | `research/text_hasher.py`, `api/text_hasher.py` |
| 70 | 文本比较器 | `research/text_comparator.py`, `api/text_comparator.py` |
| 71-72 | 单词提取器 | `research/word_extractor.py`, `api/word_extractor.py` |
| 73-74 | 句子分割器 | `research/sentence_splitter.py`, `api/sentence_splitter.py` |
| 75 | 标点符号规范化器 | `research/punctuation_normalizer.py`, `api/punctuation_normalizer.py` |
| 76-77 | 文本指标计算器 | `research/text_metrics.py`, `api/text_metrics.py` |
| 78-79 | 分词工具 | `research/tokenizer.py`, `api/tokenizer.py` |
| 80-81 | 表格格式化器 | `research/textrunner.py`, `api/textrunner.py` |
| 82-83 | JSON格式化器 | `research/json_formatter.py`, `api/json_formatter.py` |
| 84-85 | XML格式化器 | `research/xml_formatter.py`, `api/xml_formatter.py` |
| 86-87 | 正则表达式助手 | `research/regex_helper.py`, `api/regex_helper.py` |
| 88-89 | 统计收集器 | `research/text_stats_collector.py`, `api/text_stats_collector.py` |
| 90-91 | 文本连接器 | `research/text_joiner.py`, `api/text_joiner.py` |
| 92-93 | 字符统计器 | `research/character_counter.py`, `api/character_counter.py` |
| 94-95 | 翻译工具 | `research/text_translator.py`, `api/text_translator.py` |

**编译状态:** 100% 通过 ✅

### 第31-35轮 (2026-03-26)

**新增功能模块:**

| 轮次 | 功能 | 文件 |
|------|------|------|
| 31 | 模板存储系统 | `research/templates_store.py`, `api/templates_store.py` |
| 32 | 键盘快捷键系统 | `research/keyboard.py`, `api/keyboard.py` |
| 33 | 自动保存草稿 | `research/watchdog.py`, `api/watchdog.py` |
| 34 | 用户反馈系统 | `research/feedback.py`, `api/feedback.py` |
| 35 | 进度追踪器 | `research/progress.py`, `api/progress_api.py` |

**编译状态:** 100% 通过 ✅
**功能审查:** 全部评估为"保留" ✅

### 第21-30轮 (2026-03-26)

**新增功能模块:**

| 轮次 | 功能 | 文件 |
|------|------|------|
| 21 | API调用统计 | `research/api_stats.py`, `api/api_stats.py` |
| 22 | 研究结果质量评分 | `research/quality.py`, `api/quality.py` |
| 23 | 自动标签系统 | `research/tags.py`, `api/tags.py` |
| 24 | 研究趋势分析 | `research/trends.py`, `api/trends.py` |
| 25 | 播客推荐系统 | `research/recommendations.py`, `api/recommendations.py` |
| 26 | 批量导出器 | `research/exporters/all_formats.py`, `api/batch_export.py` |
| 27 | 定时提醒系统 | `research/reminders.py`, `api/reminders.py` |
| 28 | 剪贴板导入器 | `research/clipboard.py`, `api/clipboard.py` |
| 29 | 快捷操作管理 | `research/shortcuts.py`, `api/shortcuts.py` |

### 第10-20轮 (更早)

**功能模块:**
- 分享功能、统计分析、收藏夹、搜索增强、播客导入器
- 通知系统、研究任务队列、书签、API速率限制
- 版本控制、多语言支持

**累计功能总数:** 58+ 模块

## Git提交要求

每次迭代后需要:
1. 运行编译检查: `python -m py_compile src/echo/**/*.py`
2. 更新本文件的开发日志
3. Git提交: `git add . && git commit -m "描述"`
4. (可选) 推送: `git push`
