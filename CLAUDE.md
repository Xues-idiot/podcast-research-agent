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

### 第101-140轮 (2026-03-27)

**新增功能模块:**

| 轮次 | 功能 | 文件 |
|------|------|------|
| 101-102 | CSV转换器 | `research/csv_converter.py`, `api/csv_converter.py` |
| 103-104 | HTML解析器 | `research/html_parser.py`, `api/html_parser.py` |
| 105-106 | URL工具 | `research/url_tool.py`, `api/url_tool.py` |
| 107-108 | 日期格式化器 | `research/date_formatter.py`, `api/date_formatter.py` |
| 109-110 | 颜色转换器 | `research/color_converter.py`, `api/color_converter.py` |
| 111-112 | 单位转换器 | `research/units_converter.py`, `api/units_converter.py` |
| 113-114 | Slug生成器 | `research/slug_generator.py`, `api/slug_generator.py` |
| 115-116 | 数字格式化器 | `research/number_formatter.py`, `api/number_formatter.py` |
| 117-118 | ID生成器 | `research/id_generator.py`, `api/id_generator.py` |
| 119-120 | 密码生成器 | `research/password_generator.py`, `api/password_generator.py` |
| 121-122 | 表情符号工具 | `research/emoji_tool.py`, `api/emoji_tool.py` |
| 123-124 | 随机选择器 | `research/random_picker.py`, `api/random_picker.py` |
| 125-126 | 列表工具 | `research/list_utils.py`, `api/list_utils.py` |
| 127-128 | 字典工具 | `research/dict_utils.py`, `api/dict_utils.py` |
| 129-130 | YAML工具 | `research/yaml_tool.py`, `api/yaml_tool.py` |
| 131-132 | Base64工具 | `research/base64_tool.py`, `api/base64_tool.py` |
| 133-134 | 时间转换器 | `research/time_converter.py`, `api/time_converter.py` |
| 135-136 | MIME类型工具 | `research/mime_types.py`, `api/mime_types.py` |
| 137-138 | 电话号码工具 | `research/phone_formatter.py`, `api/phone_formatter.py` |
| 139-140 | 信用卡工具 | `research/credit_card.py`, `api/credit_card.py` |

**编译状态:** 100% 通过 ✅

### 第141-170轮 (2026-03-27)

**新增功能模块:**

| 轮次 | 功能 | 文件 |
|------|------|------|
| 141-142 | 数学工具 | `research/math_utils.py`, `api/math_utils.py` |
| 143-144 | 文件大小工具 | `research/file_size.py`, `api/file_size.py` |
| 145-146 | 距离计算器 | `research/distance_calculator.py`, `api/distance_calculator.py` |
| 147-148 | 正则表达式模式库 | `research/regex_patterns.py`, `api/regex_patterns.py` |
| 149-150 | 字符串工具 | `research/string_utils.py`, `api/string_utils.py` |
| 151-152 | 路径工具 | `research/path_utils.py`, `api/path_utils.py` |
| 153-154 | 版本比较器 | `research/version_comparator.py`, `api/version_comparator.py` |
| 155-156 | 质数工具 | `research/prime_numbers.py`, `api/prime_numbers.py` |
| 157-158 | 校验和工具 | `research/checksum.py`, `api/checksum.py` |
| 159-160 | 批处理工具 | `research/batch_processor.py`, `api/batch_processor.py` |
| 161-162 | 缓存管理器 | `research/cache_manager.py`, `api/cache_manager.py` |
| 163-164 | 速率限制器 | `research/rate_limiter.py`, `api/rate_limiter.py` |
| 165-166 | 数据脱敏工具 | `research/data_sanitizer.py`, `api/data_sanitizer.py` |
| 167-168 | 数据生成器 | `research/data_generator.py`, `api/data_generator.py` |

**编译状态:** 100% 通过 ✅

### 第171-200轮 (2026-03-27)

**新增功能模块:**

| 轮次 | 功能 | 文件 |
|------|------|------|
| 171-172 | 配置加载器 | `research/config_loader.py`, `api/config_loader.py` |
| 173 | 防抖工具 | `research/debouncer.py` |
| 174 | 节流工具 | `research/throttler.py` |
| 175 | 重试工具 | `research/retry_tool.py` |
| 176 | 日志工具 | `research/logger.py` |
| 177 | 计时器 | `research/timer.py` |
| 178 | 秒表工具 | `research/stopwatch.py` |
| 179 | 事件总线 | `research/event_bus.py` |
| 180 | 观察者模式 | `research/observer.py` |
| 181 | 享元工厂 | `research/flyweight.py` |
| 182 | 对象池 | `research/object_pool.py` |
| 183-184 | 验证工具集 | `research/validator_utils.py`, `api/validator_utils.py` |
| 185-186 | 标志工具 | `research/flag_tool.py`, `api/flag_tool.py` |

**编译状态:** 100% 通过 ✅

### 第201-250轮 (2026-03-27)

**新增功能模块:**

| 轮次 | 功能 | 文件 |
|------|------|------|
| 201-220 | 计数器、百分比/平均值计算器、格式化/修剪/包裹工具、结束符/制表符转换、大小写转换、复数化器、分组/排序/分割/连接工具、前缀后缀/包含检查、空值检查/类型检测/转换、克隆等 |
| 221-230 | 字典合并/差异/过滤/映射工具、列表数学/搜索/转换/去重/zip工具 |
| 231-240 | 范围生成/分块/扁平化/窗口/配对/集合运算/采样/打乱/汇总工具 |
| 241-250 | 延迟/时间戳/秒表/超时/缓存装饰器/记忆化/LRU缓存/环形缓冲区/组合键工具 |

**编译状态:** 100% 通过 ✅

### 第251-300轮 (2026-03-27)

**新增功能模块:**

| 轮次 | 功能 | 文件 |
|------|------|------|
| 251-265 | 函数包装/偏函数/组合/柯里化/单次执行/参数翻转/恒等/空操作/调用跟踪/异常处理/切换/节流/防抖工具 |
| 266-280 | 绑定/近似/比例/插值/区间/偏移/累加器/统计/百分比/最小最大/符号/奇偶/幂/对数/角度工具 |
| 281-293 | 三角函数/随机数/选择/加权/分布/分位数/验证器/强制转换/默认值/空值工具 |
| 294-300 | 相等性/比较/逻辑/位运算/三元表达式/开关/匹配工具 |

**编译状态:** 100% 通过 ✅

### 第331-360轮 (2026-03-27)

**新增功能模块:**

| 轮次 | 功能 | 文件 |
|------|------|------|
| 331-332 | 批处理生成器 | `research/batch_gen.py`, `api/batch_gen_api.py` |
| 333-334 | 字典访问器 | `research/dict_accessor.py`, `api/dict_accessor_api.py` |
| 335-336 | 字典构建器 | `research/dict_builder.py`, `api/dict_builder_api.py` |
| 337-338 | 字典查询器 | `research/dict_query.py`, `api/dict_query_api.py` |
| 339-340 | 字典转换器 | `research/dict_transformer.py`, `api/dict_transformer_api.py` |
| 341-342 | 字典更新器 | `research/dict_updater.py`, `api/dict_updater_api.py` |
| 343-344 | 网格工具 | `research/grid.py`, `api/grid_api.py` |
| 345-346 | 键值工具 | `research/key_value_maker.py`, `api/key_value_maker_api.py` |
| 347-348 | 配对工具 | `research/pair_tool.py`, `api/pair_tool_api.py` |
| 349-350 | 范围生成工具 | `research/range_gen_tool.py`, `api/range_gen_tool_api.py` |
| 351-352 | 序列生成器 | `research/sequence_gen.py`, `api/sequence_gen_api.py` |
| 353-354 | 集合操作工具 | `research/set_ops.py`, `api/set_ops_api.py` |
| 355-356 | 三元组工具 | `research/triple.py`, `api/triple_api.py` |
| 357-358 | 元组操作工具 | `research/tuple_ops.py`, `api/tuple_ops_api.py` |
| 359-360 | 窗口工具 | `research/window_tool.py`, `api/window_tool_api.py` |

**编译状态:** 100% 通过 ✅

### 第361-400轮 (2026-03-27)

**新增功能模块:**

| 轮次 | 功能 | 文件 |
|------|------|------|
| 361 | 百分比工具 | `research/percentage.py`, `api/percentage_api.py` |
| 362 | 平均值工具 | `research/averager.py`, `api/averager_api.py` |
| 363 | 结束符工具 | `research/ender.py`, `api/ender_api.py` |
| 364 | 制表符工具 | `research/tabler.py`, `api/tabler_api.py` |
| 365 | 分组工具 | `research/group_maker.py`, `api/group_maker_api.py` |
| 366 | 包含检查工具 | `research/containser.py`, `api/containser_api.py` |
| 367 | 空值检查工具 | `research/null_checker.py`, `api/null_checker_api.py` |
| 368 | 克隆工具 | `research/cloner.py` |
| 369-370 | 时间戳/组合键/绑定工具 | timestamp_tool.py, combo_key.py, binding.py |
| 371-385 | 数学/概率/随机/分布工具 | pmath.py, log_tool.py, angle_tool.py, random_tool.py, selector_tool.py, distribution_tool.py, quantile_tool.py, validator_tool.py, caster_tool.py |
| 386-390 | 缓存/统计/超时工具 | stats_tool.py, timeout_tool.py, memoize_tool.py, cache_decorator.py |
| 391-400 | 逻辑/比较工具 | lru_cache_tool.py, circular_buffer_tool.py, comparator_tool.py, equality_tool.py, logical_tool.py, bitwise_tool.py, ternary_tool.py, switch_tool.py, match_tool.py |

**编译状态:** 100% 通过 ✅

### 第401-460轮 (2026-03-27)

**新增功能模块:**

| 轮次 | 功能 | 文件 |
|------|------|------|
| 401-410 | 时间和事件工具 | delay_tool.py, timer_tool.py, retry_tool.py, logger_tool.py, event_bus.py, observer_tool.py, flyweight_tool.py, object_pool_tool.py |
| 411-420 | 函数式编程工具 | throttle_tool.py, function_wrap.py, partial_tool.py, compose_tool.py, curry_tool.py, once_tool.py, flip_tool.py, identity_tool.py, noop_tool.py, call_tracker.py |
| 421-430 | 集合和列表工具 | exception_handler.py, switch_case.py, batch_gen_tool.py, flatten_tool.py, zip_tool.py, sample_tool.py, shuffle_tool.py |
| 431-440 | 函数式和集合工具 | unique_tool.py, enumerate_tool.py, sequence_tool.py, map_tool.py, reduce_tool.py, find_tool.py, aggregator_tool.py, collector_tool.py |
| 441-450 | 集合操作和管道工具 | reverse_tool.py, slice_tool.py, length_tool.py, empty_tool.py, defaults_tool.py, coalesce_tool.py, chunk_tool.py, batch_tool.py, pipeline_tool.py, key_selector.py |
| 451-460 | 集合和列表操作工具 | diff_tool.py, intersect_tool.py, union_tool.py, select_tool.py, merge_tool.py, append_tool.py, prepend_tool.py, update_tool.py, delete_tool.py, insert_tool.py |

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
