"""工具元数据注册表"""

from typing import Dict, Optional

TOOL_REGISTRY: Dict[str, Dict] = {
    # ========== 播客研究工具 ==========
    "transcriber": {
        "id": "transcriber",
        "name": "音频转录",
        "name_en": "Audio Transcription",
        "description": "使用 Whisper 将音频转换为文字",
        "category": "podcast_research",
        "subcategory": "transcriber",
        "api_endpoint": "/api/research/transcribe",
        "method": "POST",
        "params": [
            {"name": "audio_url", "type": "string", "required": True, "description": "音频文件URL"}
        ],
        "icon": "mic"
    },
    "summarizer": {
        "id": "summarizer",
        "name": "智能摘要",
        "name_en": "Smart Summary",
        "description": "使用 LLM 生成播客内容摘要",
        "category": "podcast_research",
        "subcategory": "summarizer",
        "api_endpoint": "/api/research/summarize",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "要摘要的文本"}
        ],
        "icon": "file-text"
    },
    "keypoint": {
        "id": "keypoint",
        "name": "要点提取",
        "name_en": "Key Points Extraction",
        "description": "从播客内容中提取关键要点",
        "category": "podcast_research",
        "subcategory": "keypoint",
        "api_endpoint": "/api/research/keypoints",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "原始文本"}
        ],
        "icon": "list"
    },
    "mindmap": {
        "id": "mindmap",
        "name": "思维导图",
        "name_en": "Mind Map Generation",
        "description": "根据内容生成思维导图",
        "category": "podcast_research",
        "subcategory": "mindmap",
        "api_endpoint": "/api/research/mindmap",
        "method": "POST",
        "params": [
            {"name": "topic", "type": "string", "required": True, "description": "主题"}
        ],
        "icon": "share-2"
    },
    "qa_generator": {
        "id": "qa_generator",
        "name": "问答对生成",
        "name_en": "Q&A Pair Generation",
        "description": "基于 Bloom 认知层次生成问答对",
        "category": "podcast_research",
        "subcategory": "qa",
        "api_endpoint": "/api/research/qa",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "原始文本"}
        ],
        "icon": "help-circle"
    },

    # ========== 文本处理工具 ==========
    "text_splitter": {
        "id": "text_splitter",
        "name": "文本分割器",
        "name_en": "Text Splitter",
        "description": "按字符、单词或句子分割文本",
        "category": "text_processing",
        "subcategory": "format",
        "api_endpoint": "/api/text-splitter/split",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "待分割文本"},
            {"name": "delimiter", "type": "string", "required": False, "description": "分隔符"}
        ],
        "icon": "scissors"
    },
    "text_joiner": {
        "id": "text_joiner",
        "name": "文本连接器",
        "name_en": "Text Joiner",
        "description": "将多个文本片段连接成一个",
        "category": "text_processing",
        "subcategory": "format",
        "api_endpoint": "/api/text-joiner/join",
        "method": "POST",
        "params": [
            {"name": "texts", "type": "array", "required": True, "description": "文本数组"},
            {"name": "separator", "type": "string", "required": False, "description": "连接符"}
        ],
        "icon": "link"
    },
    "word_counter": {
        "id": "word_counter",
        "name": "字数统计",
        "name_en": "Word Counter",
        "description": "统计文本的字数、词数、句数",
        "category": "text_processing",
        "subcategory": "statistics",
        "api_endpoint": "/api/word-counter/count",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "待统计文本"}
        ],
        "icon": "hash"
    },
    "keyword_extractor": {
        "id": "keyword_extractor",
        "name": "关键词提取",
        "name_en": "Keyword Extraction",
        "description": "从文本中提取关键词",
        "category": "text_processing",
        "subcategory": "extract",
        "api_endpoint": "/api/keyword-extractor/extract",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "原始文本"},
            {"name": "top_n", "type": "number", "required": False, "description": "提取数量"}
        ],
        "icon": "tag"
    },
    "text_cleaner": {
        "id": "text_cleaner",
        "name": "文本清理器",
        "name_en": "Text Cleaner",
        "description": "清理文本中的空白、特殊字符",
        "category": "text_processing",
        "subcategory": "cleaner",
        "api_endpoint": "/api/text-cleaner/clean",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "待清理文本"}
        ],
        "icon": "eraser"
    },

    # ========== 数学计算工具 ==========
    "calculator": {
        "id": "calculator",
        "name": "计算器",
        "name_en": "Calculator",
        "description": "基础数学运算",
        "category": "math",
        "subcategory": "basic",
        "api_endpoint": "/api/math-utils/calculate",
        "method": "POST",
        "params": [
            {"name": "expression", "type": "string", "required": True, "description": "数学表达式"}
        ],
        "icon": "calculator"
    },
    "statistics": {
        "id": "statistics",
        "name": "统计分析",
        "name_en": "Statistics",
        "description": "计算均值、中位数、方差等",
        "category": "math",
        "subcategory": "statistical",
        "api_endpoint": "/api/math-utils/statistics",
        "method": "POST",
        "params": [
            {"name": "values", "type": "array", "required": True, "description": "数值数组"}
        ],
        "icon": "bar-chart"
    },
    "percentage": {
        "id": "percentage",
        "name": "百分比计算",
        "name_en": "Percentage Calculator",
        "description": "计算百分比、增长率等",
        "category": "math",
        "subcategory": "basic",
        "api_endpoint": "/api/percentage/calculate",
        "method": "POST",
        "params": [
            {"name": "value", "type": "number", "required": True, "description": "数值"},
            {"name": "total", "type": "number", "required": True, "description": "总数"}
        ],
        "icon": "percent"
    },
    "prime_check": {
        "id": "prime_check",
        "name": "质数检查",
        "name_en": "Prime Number Check",
        "description": "检查一个数是否为质数",
        "category": "math",
        "subcategory": "basic",
        "api_endpoint": "/api/prime-numbers/check",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "待检查的数"}
        ],
        "icon": "check"
    },

    # ========== 数据结构工具 ==========
    "list_tools": {
        "id": "list_tools",
        "name": "列表工具",
        "name_en": "List Utilities",
        "description": "列表去重、排序、分块等操作",
        "category": "data_structures",
        "subcategory": "list",
        "api_endpoint": "/api/list-utils",
        "method": "POST",
        "params": [
            {"name": "operation", "type": "string", "required": True, "description": "操作类型"}
        ],
        "icon": "list"
    },
    "dict_tools": {
        "id": "dict_tools",
        "name": "字典工具",
        "name_en": "Dictionary Utilities",
        "description": "字典合并、过滤、映射等操作",
        "category": "data_structures",
        "subcategory": "dict",
        "api_endpoint": "/api/dict-utils",
        "method": "POST",
        "params": [
            {"name": "operation", "type": "string", "required": True, "description": "操作类型"}
        ],
        "icon": "book"
    },
    "set_ops": {
        "id": "set_ops",
        "name": "集合运算",
        "name_en": "Set Operations",
        "description": "交集、并集、差集等集合运算",
        "category": "data_structures",
        "subcategory": "set",
        "api_endpoint": "/api/set-ops",
        "method": "POST",
        "params": [
            {"name": "operation", "type": "string", "required": True, "description": "运算类型"}
        ],
        "icon": "circle"
    },
    "list_intersect": {
        "id": "list_intersect",
        "name": "列表交集",
        "name_en": "List Intersection",
        "description": "计算多个列表的交集元素",
        "category": "data_structures",
        "subcategory": "list",
        "api_endpoint": "/api/list-intersect",
        "method": "POST",
        "params": [
            {"name": "lists", "type": "array", "required": True, "description": "列表数组"},
            {"name": "use_key", "type": "boolean", "required": False, "description": "是否按键比较"},
            {"name": "key", "type": "string", "required": False, "description": "字典键名"}
        ],
        "icon": "circle"
    },
    "list_union": {
        "id": "list_union",
        "name": "列表并集",
        "name_en": "List Union",
        "description": "计算多个列表的并集元素（去重）",
        "category": "data_structures",
        "subcategory": "list",
        "api_endpoint": "/api/list-union",
        "method": "POST",
        "params": [
            {"name": "lists", "type": "array", "required": True, "description": "列表数组"},
            {"name": "use_key", "type": "boolean", "required": False, "description": "是否按键比较"},
            {"name": "key", "type": "string", "required": False, "description": "字典键名"}
        ],
        "icon": "circle"
    },
    "list_diff": {
        "id": "list_diff",
        "name": "列表差集",
        "name_en": "List Difference",
        "description": "计算列表的差集或对称差集",
        "category": "data_structures",
        "subcategory": "list",
        "api_endpoint": "/api/list-diff",
        "method": "POST",
        "params": [
            {"name": "lists", "type": "array", "required": True, "description": "列表数组"},
            {"name": "symmetric", "type": "boolean", "required": False, "description": "是否对称差集"}
        ],
        "icon": "circle"
    },
    "list_slice": {
        "id": "list_slice",
        "name": "列表切片",
        "name_en": "List Slice",
        "description": "获取列表的切片、前n个或后n个元素",
        "category": "data_structures",
        "subcategory": "list",
        "api_endpoint": "/api/list-slice",
        "method": "POST",
        "params": [
            {"name": "list", "type": "array", "required": True, "description": "源列表"},
            {"name": "start", "type": "number", "required": False, "description": "起始索引"},
            {"name": "end", "type": "number", "required": False, "description": "结束索引"},
            {"name": "step", "type": "number", "required": False, "description": "步长"}
        ],
        "icon": "list"
    },
    "list_enumerate": {
        "id": "list_enumerate",
        "name": "列表枚举",
        "name_en": "List Enumerate",
        "description": "为列表元素添加索引，支持起始索引和步长",
        "category": "data_structures",
        "subcategory": "list",
        "api_endpoint": "/api/list-enumerate",
        "method": "POST",
        "params": [
            {"name": "list", "type": "array", "required": True, "description": "源列表"},
            {"name": "start", "type": "number", "required": False, "description": "起始索引"},
            {"name": "step", "type": "number", "required": False, "description": "索引步长"}
        ],
        "icon": "hash"
    },

    "list_flatten": {
        "id": "list_flatten",
        "name": "列表扁平化",
        "name_en": "List Flatten",
        "description": "将嵌套列表展开，支持深度控制、分块和滑动窗口",
        "category": "data_structures",
        "subcategory": "list",
        "api_endpoint": "/api/list-flatten",
        "method": "POST",
        "params": [
            {"name": "list", "type": "array", "required": True, "description": "源列表"},
            {"name": "depth", "type": "number", "required": False, "description": "展开深度，-1全部"}
        ],
        "icon": "list"
    },

    "list_sort": {
        "id": "list_sort",
        "name": "列表排序",
        "name_en": "List Sort",
        "description": "对列表进行排序、反转、打乱",
        "category": "data_structures",
        "subcategory": "list",
        "api_endpoint": "/api/list-sort",
        "method": "POST",
        "params": [
            {"name": "list", "type": "array", "required": True, "description": "源列表"},
            {"name": "reverse", "type": "boolean", "required": False, "description": "降序"}
        ],
        "icon": "list"
    },
    "list_find": {
        "id": "list_find",
        "name": "列表查找",
        "name_en": "List Find",
        "description": "在列表中查找元素及其索引",
        "category": "data_structures",
        "subcategory": "list",
        "api_endpoint": "/api/list-find",
        "method": "POST",
        "params": [
            {"name": "list", "type": "array", "required": True, "description": "源列表"},
            {"name": "value", "type": "any", "required": False, "description": "要查找的值"}
        ],
        "icon": "search"
    },
    "list_batch": {
        "id": "list_batch",
        "name": "列表批处理",
        "name_en": "List Batch",
        "description": "对列表元素进行批量映射和过滤操作",
        "category": "data_structures",
        "subcategory": "list",
        "api_endpoint": "/api/list-batch",
        "method": "POST",
        "params": [
            {"name": "list", "type": "array", "required": True, "description": "源列表"}
        ],
        "icon": "list"
    },
    "list_sample": {
        "id": "list_sample",
        "name": "列表采样",
        "name_en": "List Sample",
        "description": "从列表中随机抽取样本",
        "category": "data_structures",
        "subcategory": "list",
        "api_endpoint": "/api/list-sample",
        "method": "POST",
        "params": [
            {"name": "list", "type": "array", "required": True, "description": "源列表"},
            {"name": "n", "type": "number", "required": False, "description": "抽取数量"},
            {"name": "replace", "type": "boolean", "required": False, "description": "放回抽样"}
        ],
        "icon": "shuffle"
    },
    "list_stats": {
        "id": "list_stats",
        "name": "列表统计",
        "name_en": "List Stats",
        "description": "计算列表的统计信息：计数、和、平均值、最大最小值",
        "category": "data_structures",
        "subcategory": "list",
        "api_endpoint": "/api/list-stats",
        "method": "POST",
        "params": [
            {"name": "list", "type": "array", "required": True, "description": "源列表"}
        ],
        "icon": "bar-chart"
    },
    "list_zip": {
        "id": "list_zip",
        "name": "列表合并",
        "name_en": "List Zip",
        "description": "合并、连接、交错多个列表",
        "category": "data_structures",
        "subcategory": "list",
        "api_endpoint": "/api/list-zip",
        "method": "POST",
        "params": [
            {"name": "lists", "type": "array", "required": True, "description": "要合并的列表数组"}
        ],
        "icon": "list"
    },
    "list_unique": {
        "id": "list_unique",
        "name": "列表去重",
        "name_en": "List Unique",
        "description": "去除列表中的重复元素，找出重复项",
        "category": "data_structures",
        "subcategory": "list",
        "api_endpoint": "/api/list-unique",
        "method": "POST",
        "params": [
            {"name": "list", "type": "array", "required": True, "description": "源列表"},
            {"name": "preserve_order", "type": "boolean", "required": False, "description": "是否保持顺序"}
        ],
        "icon": "check"
    },

    # ========== 编码转换工具 ==========
    "base64_tool": {
        "id": "base64_tool",
        "name": "Base64 编解码",
        "name_en": "Base64 Encoder/Decoder",
        "description": "Base64 编码和解码",
        "category": "encoding",
        "subcategory": "base64",
        "api_endpoint": "/api/base64-tool/encode",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "待编码文本"}
        ],
        "icon": "lock"
    },
    "url_tool": {
        "id": "url_tool",
        "name": "URL 编解码",
        "name_en": "URL Encoder/Decoder",
        "description": "URL 编码和解码",
        "category": "encoding",
        "subcategory": "url",
        "api_endpoint": "/api/url-tool/encode",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "待编码文本"}
        ],
        "icon": "link"
    },
    "html_tool": {
        "id": "html_tool",
        "name": "HTML 编解码",
        "name_en": "HTML Encoder/Decoder",
        "description": "HTML 实体编码和解码",
        "category": "encoding",
        "subcategory": "html",
        "api_endpoint": "/api/html-parser/encode",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "待编码文本"}
        ],
        "icon": "code"
    },
    "uuid_gen": {
        "id": "uuid_gen",
        "name": "UUID 生成",
        "name_en": "UUID Generator",
        "description": "生成唯一标识符",
        "category": "encoding",
        "subcategory": "uuid",
        "api_endpoint": "/api/id-generator/generate",
        "method": "POST",
        "params": [
            {"name": "count", "type": "number", "required": False, "description": "生成数量"}
        ],
        "icon": "hash"
    },

    # ========== 验证工具 ==========
    "email_validator": {
        "id": "email_validator",
        "name": "邮箱验证",
        "name_en": "Email Validator",
        "description": "验证邮箱格式是否正确",
        "category": "validation",
        "subcategory": "email",
        "api_endpoint": "/api/validator-utils/validate-email",
        "method": "POST",
        "params": [
            {"name": "email", "type": "string", "required": True, "description": "邮箱地址"}
        ],
        "icon": "mail"
    },
    "phone_formatter": {
        "id": "phone_formatter",
        "name": "电话号码工具",
        "name_en": "Phone Number Tool",
        "description": "格式化和建议电话号码",
        "category": "validation",
        "subcategory": "phone",
        "api_endpoint": "/api/phone-formatter/format",
        "method": "POST",
        "params": [
            {"name": "phone", "type": "string", "required": True, "description": "电话号码"}
        ],
        "icon": "phone"
    },
    "json_validator": {
        "id": "json_validator",
        "name": "JSON 验证",
        "name_en": "JSON Validator",
        "description": "验证 JSON 格式是否正确",
        "category": "validation",
        "subcategory": "json",
        "api_endpoint": "/api/json-formatter/validate",
        "method": "POST",
        "params": [
            {"name": "json_str", "type": "string", "required": True, "description": "JSON 字符串"}
        ],
        "icon": "file"
    },
    "credit_card": {
        "id": "credit_card",
        "name": "信用卡工具",
        "name_en": "Credit Card Tool",
        "description": "验证和格式化信用卡号",
        "category": "validation",
        "subcategory": "credit_card",
        "api_endpoint": "/api/credit-card/validate",
        "method": "POST",
        "params": [
            {"name": "card_number", "type": "string", "required": True, "description": "卡号"}
        ],
        "icon": "credit-card"
    },

    # ========== 日期时间工具 ==========
    "date_formatter": {
        "id": "date_formatter",
        "name": "日期格式化",
        "name_en": "Date Formatter",
        "description": "日期格式转换",
        "category": "datetime",
        "subcategory": "format",
        "api_endpoint": "/api/date-formatter/format",
        "method": "POST",
        "params": [
            {"name": "date", "type": "string", "required": True, "description": "日期"},
            {"name": "format", "type": "string", "required": False, "description": "目标格式"}
        ],
        "icon": "calendar"
    },
    "time_converter": {
        "id": "time_converter",
        "name": "时间转换器",
        "name_en": "Time Converter",
        "description": "不同时区的时间转换",
        "category": "datetime",
        "subcategory": "timezone",
        "api_endpoint": "/api/time-converter/convert",
        "method": "POST",
        "params": [
            {"name": "time", "type": "string", "required": True, "description": "时间"},
            {"name": "from_tz", "type": "string", "required": True, "description": "源时区"},
            {"name": "to_tz", "type": "string", "required": True, "description": "目标时区"}
        ],
        "icon": "globe"
    },
    "timestamp_tool": {
        "id": "timestamp_tool",
        "name": "时间戳工具",
        "name_en": "Timestamp Tool",
        "description": "时间戳和日期互转",
        "category": "datetime",
        "subcategory": "timestamp",
        "api_endpoint": "/api/timestamp-tool",
        "method": "POST",
        "params": [
            {"name": "value", "type": "string", "required": True, "description": "时间戳或日期"}
        ],
        "icon": "clock"
    },

    # ========== 文件处理工具 ==========
    "file_size": {
        "id": "file_size",
        "name": "文件大小格式化",
        "name_en": "File Size Formatter",
        "description": "字节转换为人类可读格式",
        "category": "file",
        "subcategory": "format",
        "api_endpoint": "/api/file-size/format",
        "method": "POST",
        "params": [
            {"name": "bytes", "type": "number", "required": True, "description": "字节数"}
        ],
        "icon": "hard-drive"
    },
    "path_utils": {
        "id": "path_utils",
        "name": "路径工具",
        "name_en": "Path Utilities",
        "description": "路径拼接、解析、规范化",
        "category": "file",
        "subcategory": "path",
        "api_endpoint": "/api/path-utils",
        "method": "POST",
        "params": [
            {"name": "operation", "type": "string", "required": True, "description": "操作类型"}
        ],
        "icon": "folder"
    },

    # ========== 开发工具 ==========
    "json_formatter": {
        "id": "json_formatter",
        "name": "JSON 格式化",
        "name_en": "JSON Formatter",
        "description": "格式化和对齐 JSON",
        "category": "developer",
        "subcategory": "format",
        "api_endpoint": "/api/json-formatter/format",
        "method": "POST",
        "params": [
            {"name": "json_str", "type": "string", "required": True, "description": "JSON 字符串"}
        ],
        "icon": "file"
    },
    "yaml_tool": {
        "id": "yaml_tool",
        "name": "YAML 工具",
        "name_en": "YAML Tool",
        "description": "YAML 和 JSON 互转",
        "category": "developer",
        "subcategory": "convert",
        "api_endpoint": "/api/yaml-tool/convert",
        "method": "POST",
        "params": [
            {"name": "content", "type": "string", "required": True, "description": "内容"}
        ],
        "icon": "file-text"
    },
    "regex_helper": {
        "id": "regex_helper",
        "name": "正则表达式助手",
        "name_en": "Regex Helper",
        "description": "正则表达式测试和调试",
        "category": "developer",
        "subcategory": "debug",
        "api_endpoint": "/api/regex-helper/test",
        "method": "POST",
        "params": [
            {"name": "pattern", "type": "string", "required": True, "description": "正则模式"},
            {"name": "text", "type": "string", "required": True, "description": "测试文本"}
        ],
        "icon": "search"
    },

    # ========== 随机生成工具 ==========
    "random_picker": {
        "id": "random_picker",
        "name": "随机选择器",
        "name_en": "Random Picker",
        "description": "从列表中随机选择元素",
        "category": "random",
        "subcategory": "random",
        "api_endpoint": "/api/random-picker/pick",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "选项列表"},
            {"name": "count", "type": "number", "required": False, "description": "选择数量"}
        ],
        "icon": "shuffle"
    },
    "password_generator": {
        "id": "password_generator",
        "name": "密码生成器",
        "name_en": "Password Generator",
        "description": "生成安全随机密码",
        "category": "random",
        "subcategory": "password",
        "api_endpoint": "/api/password-generator/generate",
        "method": "POST",
        "params": [
            {"name": "length", "type": "number", "required": False, "description": "密码长度"}
        ],
        "icon": "lock"
    },
    "id_generator": {
        "id": "id_generator",
        "name": "ID 生成器",
        "name_en": "ID Generator",
        "description": "生成各种格式的 ID",
        "category": "random",
        "subcategory": "id",
        "api_endpoint": "/api/id-generator/generate",
        "method": "POST",
        "params": [
            {"name": "format", "type": "string", "required": False, "description": "ID 格式"}
        ],
        "icon": "hash"
    }
}


def get_tool_by_id(tool_id: str) -> Optional[Dict]:
    """根据ID获取工具"""
    return TOOL_REGISTRY.get(tool_id)


def get_tools_by_category(category_id: str) -> list:
    """获取指定分类下的所有工具"""
    return [t for t in TOOL_REGISTRY.values() if t.get("category") == category_id]


def get_tools_by_subcategory(subcategory: str) -> list:
    """获取指定子分类下的所有工具"""
    return [t for t in TOOL_REGISTRY.values() if t.get("subcategory") == subcategory]


def search_tools(query: str) -> list:
    """搜索工具"""
    query_lower = query.lower()
    return [
        t for t in TOOL_REGISTRY.values()
        if query_lower in t.get("name", "").lower()
        or query_lower in t.get("name_en", "").lower()
        or query_lower in t.get("description", "").lower()
    ]
