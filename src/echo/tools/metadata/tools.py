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
    "list_range": {
        "id": "list_range",
        "name": "列表范围",
        "name_en": "List Range",
        "description": "生成数值范围列表、重复列表、循环列表",
        "category": "data_structures",
        "subcategory": "list",
        "api_endpoint": "/api/list-range",
        "method": "POST",
        "params": [
            {"name": "start", "type": "number", "required": True, "description": "起始值"},
            {"name": "stop", "type": "number", "required": True, "description": "结束值"},
            {"name": "step", "type": "number", "required": False, "description": "步长"}
        ],
        "icon": "list"
    },
    "list_partition": {
        "id": "list_partition",
        "name": "列表分区",
        "name_en": "List Partition",
        "description": "将列表按条件分区、分组、分块",
        "category": "data_structures",
        "subcategory": "list",
        "api_endpoint": "/api/list-partition",
        "method": "POST",
        "params": [
            {"name": "list", "type": "array", "required": True, "description": "源列表"}
        ],
        "icon": "list"
    },
    "list_compare": {
        "id": "list_compare",
        "name": "列表比较",
        "name_en": "List Compare",
        "description": "比较两个列表，找出共同元素和差异",
        "category": "data_structures",
        "subcategory": "list",
        "api_endpoint": "/api/list-compare",
        "method": "POST",
        "params": [
            {"name": "list1", "type": "array", "required": True, "description": "第一个列表"},
            {"name": "list2", "type": "array", "required": True, "description": "第二个列表"}
        ],
        "icon": "check"
    },
    "list_transform": {
        "id": "list_transform",
        "name": "列表变换",
        "name_en": "List Transform",
        "description": "对列表进行累积、去重、压缩、深度扁平化等变换",
        "category": "data_structures",
        "subcategory": "list",
        "api_endpoint": "/api/list-transform",
        "method": "POST",
        "params": [
            {"name": "list", "type": "array", "required": True, "description": "源列表"}
        ],
        "icon": "list"
    },
    "string_utils": {
        "id": "string_utils",
        "name": "字符串处理",
        "name_en": "String Utils",
        "description": "字符串反转、大小写、分割、替换等操作",
        "category": "text_processing",
        "subcategory": "string",
        "api_endpoint": "/api/string",
        "method": "POST",
        "params": [
            {"name": "value", "type": "string", "required": True, "description": "字符串"}
        ],
        "icon": "code"
    },
    "math_utils": {
        "id": "math_utils",
        "name": "数学工具",
        "name_en": "Math Utils",
        "description": "基本数学运算：加减乘除、幂、开方、阶乘等",
        "category": "math",
        "subcategory": "basic",
        "api_endpoint": "/api/math",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "第一个数"},
            {"name": "b", "type": "number", "required": False, "description": "第二个数"}
        ],
        "icon": "calculator"
    },
    "dict_utils": {
        "id": "dict_utils",
        "name": "字典工具",
        "name_en": "Dict Utils",
        "description": "字典操作：获取、设置、合并、过滤、反转等",
        "category": "data_structures",
        "subcategory": "dict",
        "api_endpoint": "/api/dict",
        "method": "POST",
        "params": [
            {"name": "dict", "type": "object", "required": True, "description": "字典"}
        ],
        "icon": "book"
    },
    "datetime_utils": {
        "id": "datetime_utils",
        "name": "日期时间",
        "name_en": "DateTime Utils",
        "description": "日期时间操作：获取当前、日期加减、格式转换",
        "category": "datetime",
        "subcategory": "datetime",
        "api_endpoint": "/api/datetime",
        "method": "POST",
        "params": [],
        "icon": "calendar"
    },
    "validator_utils": {
        "id": "validator_utils",
        "name": "验证工具",
        "name_en": "Validator Utils",
        "description": "验证邮箱、URL、手机号、JSON等格式",
        "category": "validation",
        "subcategory": "validator",
        "api_endpoint": "/api/validate",
        "method": "POST",
        "params": [
            {"name": "value", "type": "string", "required": True, "description": "待验证值"}
        ],
        "icon": "check"
    },
    "encoding_utils": {
        "id": "encoding_utils",
        "name": "编码转换",
        "name_en": "Encoding Utils",
        "description": "Base64、URL、JSON、Hex编码解码",
        "category": "encoding",
        "subcategory": "encoding",
        "api_endpoint": "/api/encode",
        "method": "POST",
        "params": [
            {"name": "value", "type": "string", "required": True, "description": "待编码/解码值"}
        ],
        "icon": "lock"
    },
    "random_utils": {
        "id": "random_utils",
        "name": "随机工具",
        "name_en": "Random Utils",
        "description": "随机数、随机选择、随机字符串、UUID等",
        "category": "random",
        "subcategory": "random",
        "api_endpoint": "/api/random",
        "method": "POST",
        "params": [],
        "icon": "shuffle"
    },
    "format_utils": {
        "id": "format_utils",
        "name": "格式化工具",
        "name_en": "Format Utils",
        "description": "JSON、数字、货币、百分比、文件大小、时长等格式化",
        "category": "text_processing",
        "subcategory": "format",
        "api_endpoint": "/api/format",
        "method": "POST",
        "params": [],
        "icon": "file"
    },
    "array_utils": {
        "id": "array_utils",
        "name": "数组工具",
        "name_en": "Array Utils",
        "description": "数组操作：去重、并集、交集、差集、分块、扁平化",
        "category": "data_structures",
        "subcategory": "array",
        "api_endpoint": "/api/array",
        "method": "POST",
        "params": [],
        "icon": "list"
    },
    "color_utils": {
        "id": "color_utils",
        "name": "颜色工具",
        "name_en": "Color Utils",
        "description": "颜色格式转换：HEX、RGB、HSL，以及颜色加深变浅",
        "category": "encoding",
        "subcategory": "color",
        "api_endpoint": "/api/color",
        "method": "POST",
        "params": [],
        "icon": "circle"
    },
    "collection_utils": {
        "id": "collection_utils",
        "name": "集合工具",
        "name_en": "Collection Utils",
        "description": "集合操作：并集、交集、差集、对称差集、子集判断",
        "category": "data_structures",
        "subcategory": "collection",
        "api_endpoint": "/api/collection",
        "method": "POST",
        "params": [],
        "icon": "circle"
    },
    "regex_utils": {
        "id": "regex_utils",
        "name": "正则工具",
        "name_en": "Regex Utils",
        "description": "正则表达式匹配、搜索、替换、分割",
        "category": "developer",
        "subcategory": "regex",
        "api_endpoint": "/api/regex",
        "method": "POST",
        "params": [],
        "icon": "search"
    },
    "path_utils": {
        "id": "path_utils",
        "name": "路径工具",
        "name_en": "Path Utils",
        "description": "路径操作：拼接、分割、获取目录、文件名、扩展名",
        "category": "file",
        "subcategory": "path",
        "api_endpoint": "/api/path",
        "method": "POST",
        "params": [],
        "icon": "folder"
    },
    "time_utils": {
        "id": "time_utils",
        "name": "时间工具",
        "name_en": "Time Utils",
        "description": "时间操作：当前时间、时间戳转换、时间加减、格式化",
        "category": "datetime",
        "subcategory": "time",
        "api_endpoint": "/api/time",
        "method": "POST",
        "params": [],
        "icon": "clock"
    },
    "convert_utils": {
        "id": "convert_utils",
        "name": "转换工具",
        "name_en": "Convert Utils",
        "description": "类型转换：字符串、数字、布尔值、列表、JSON互转",
        "category": "encoding",
        "subcategory": "convert",
        "api_endpoint": "/api/convert",
        "method": "POST",
        "params": [],
        "icon": "refresh-cw"
    },
    "hash_utils": {
        "id": "hash_utils",
        "name": "哈希工具",
        "name_en": "Hash Utils",
        "description": "哈希计算：MD5、SHA1、SHA256、SHA512",
        "category": "encoding",
        "subcategory": "hash",
        "api_endpoint": "/api/hash",
        "method": "POST",
        "params": [],
        "icon": "lock"
    },
    "compare_utils": {
        "id": "compare_utils",
        "name": "比较工具",
        "name_en": "Compare Utils",
        "description": "比较操作：求最小最大值、clamp限制、范围判断",
        "category": "math",
        "subcategory": "compare",
        "api_endpoint": "/api/compare",
        "method": "POST",
        "params": [],
        "icon": "check"
    },
    "logic_utils": {
        "id": "logic_utils",
        "name": "逻辑工具",
        "name_en": "Logic Utils",
        "description": "逻辑操作：空值检查、真假判断、条件选择、管道组合",
        "category": "developer",
        "subcategory": "logic",
        "api_endpoint": "/api/logic",
        "method": "POST",
        "params": [],
        "icon": "check"
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
    },
    "generate_token": {
        "id": "generate_token",
        "name": "Token 生成器",
        "name_en": "Token Generator",
        "description": "生成随机 Token",
        "category": "crypto",
        "subcategory": "token",
        "api_endpoint": "/api/crypto/token",
        "method": "POST",
        "params": [
            {"name": "length", "type": "number", "required": False, "description": "Token 长度"}
        ],
        "icon": "key"
    },
    "generate_random_hex": {
        "id": "generate_random_hex",
        "name": "随机十六进制",
        "name_en": "Random Hex Generator",
        "description": "生成随机十六进制字符串",
        "category": "crypto",
        "subcategory": "hex",
        "api_endpoint": "/api/crypto/random-hex",
        "method": "POST",
        "params": [
            {"name": "length", "type": "number", "required": False, "description": "长度"}
        ],
        "icon": "hash"
    },
    "generate_password": {
        "id": "generate_password",
        "name": "密码生成器",
        "name_en": "Password Generator",
        "description": "生成安全随机密码",
        "category": "crypto",
        "subcategory": "password",
        "api_endpoint": "/api/crypto/password",
        "method": "POST",
        "params": [
            {"name": "length", "type": "number", "required": False, "description": "密码长度"},
            {"name": "chars", "type": "string", "required": False, "description": "字符集"}
        ],
        "icon": "lock"
    },
    "secure_random_int": {
        "id": "secure_random_int",
        "name": "安全随机整数",
        "name_en": "Secure Random Integer",
        "description": "生成安全随机整数",
        "category": "crypto",
        "subcategory": "random",
        "api_endpoint": "/api/crypto/random-int",
        "method": "POST",
        "params": [
            {"name": "min_val", "type": "number", "required": False, "description": "最小值"},
            {"name": "max_val", "type": "number", "required": False, "description": "最大值"}
        ],
        "icon": "hash"
    },
    "generate_uuid": {
        "id": "generate_uuid",
        "name": "UUID 生成器",
        "name_en": "UUID Generator",
        "description": "生成 UUID",
        "category": "crypto",
        "subcategory": "uuid",
        "api_endpoint": "/api/crypto/uuid",
        "method": "POST",
        "params": [],
        "icon": "hash"
    },
    "constant_time_compare": {
        "id": "constant_time_compare",
        "name": "恒定时间比较",
        "name_en": "Constant Time Compare",
        "description": "恒定时间比较两个字符串",
        "category": "crypto",
        "subcategory": "compare",
        "api_endpoint": "/api/crypto/compare",
        "method": "POST",
        "params": [
            {"name": "a", "type": "string", "required": True, "description": "字符串 A"},
            {"name": "b", "type": "string", "required": True, "description": "字符串 B"}
        ],
        "icon": "equals"
    },
    "salt": {
        "id": "salt",
        "name": "盐值生成器",
        "name_en": "Salt Generator",
        "description": "生成随机盐值",
        "category": "crypto",
        "subcategory": "salt",
        "api_endpoint": "/api/crypto/salt",
        "method": "POST",
        "params": [],
        "icon": "key"
    },
    "arithmetic_sequence": {
        "id": "arithmetic_sequence",
        "name": "等差数列生成",
        "name_en": "Arithmetic Sequence",
        "description": "生成等差数列",
        "category": "sequence",
        "subcategory": "arithmetic",
        "api_endpoint": "/api/sequence/arithmetic",
        "method": "POST",
        "params": [
            {"name": "start", "type": "number", "required": False, "description": "起始值"},
            {"name": "step", "type": "number", "required": False, "description": "步长"},
            {"name": "length", "type": "number", "required": False, "description": "数量"}
        ],
        "icon": "list"
    },
    "geometric_sequence": {
        "id": "geometric_sequence",
        "name": "等比数列生成",
        "name_en": "Geometric Sequence",
        "description": "生成等比数列",
        "category": "sequence",
        "subcategory": "geometric",
        "api_endpoint": "/api/sequence/geometric",
        "method": "POST",
        "params": [
            {"name": "start", "type": "number", "required": False, "description": "起始值"},
            {"name": "ratio", "type": "number", "required": False, "description": "公比"},
            {"name": "length", "type": "number", "required": False, "description": "数量"}
        ],
        "icon": "list"
    },
    "fibonacci_sequence": {
        "id": "fibonacci_sequence",
        "name": "斐波那契数列",
        "name_en": "Fibonacci Sequence",
        "description": "生成斐波那契数列",
        "category": "sequence",
        "subcategory": "fibonacci",
        "api_endpoint": "/api/sequence/fibonacci",
        "method": "POST",
        "params": [
            {"name": "length", "type": "number", "required": False, "description": "数量"}
        ],
        "icon": "list"
    },
    "prime_sequence": {
        "id": "prime_sequence",
        "name": "素数序列",
        "name_en": "Prime Sequence",
        "description": "生成素数序列",
        "category": "sequence",
        "subcategory": "prime",
        "api_endpoint": "/api/sequence/primes",
        "method": "POST",
        "params": [
            {"name": "length", "type": "number", "required": False, "description": "数量"}
        ],
        "icon": "list"
    },
    "sequence_slice": {
        "id": "sequence_slice",
        "name": "序列切片",
        "name_en": "Sequence Slice",
        "description": "对序列进行切片操作",
        "category": "sequence",
        "subcategory": "slice",
        "api_endpoint": "/api/sequence/slice",
        "method": "POST",
        "params": [
            {"name": "seq", "type": "array", "required": True, "description": "源序列"},
            {"name": "start", "type": "number", "required": False, "description": "起始索引"},
            {"name": "end", "type": "number", "required": False, "description": "结束索引"},
            {"name": "step", "type": "number", "required": False, "description": "步长"}
        ],
        "icon": "scissors"
    },
    "sequence_reverse": {
        "id": "sequence_reverse",
        "name": "序列反转",
        "name_en": "Sequence Reverse",
        "description": "反转序列顺序",
        "category": "sequence",
        "subcategory": "reverse",
        "api_endpoint": "/api/sequence/reverse",
        "method": "POST",
        "params": [
            {"name": "seq", "type": "array", "required": True, "description": "源序列"}
        ],
        "icon": "rotate-ccw"
    },
    "bitwise_and": {
        "id": "bitwise_and",
        "name": "位与运算",
        "name_en": "Bitwise AND",
        "description": "执行位与运算",
        "category": "bitwise",
        "subcategory": "and",
        "api_endpoint": "/api/bitwise/and",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "操作数A"},
            {"name": "b", "type": "number", "required": True, "description": "操作数B"}
        ],
        "icon": "check-square"
    },
    "bitwise_or": {
        "id": "bitwise_or",
        "name": "位或运算",
        "name_en": "Bitwise OR",
        "description": "执行位或运算",
        "category": "bitwise",
        "subcategory": "or",
        "api_endpoint": "/api/bitwise/or",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "操作数A"},
            {"name": "b", "type": "number", "required": True, "description": "操作数B"}
        ],
        "icon": "check-square"
    },
    "bitwise_xor": {
        "id": "bitwise_xor",
        "name": "位异或运算",
        "name_en": "Bitwise XOR",
        "description": "执行位异或运算",
        "category": "bitwise",
        "subcategory": "xor",
        "api_endpoint": "/api/bitwise/xor",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "操作数A"},
            {"name": "b", "type": "number", "required": True, "description": "操作数B"}
        ],
        "icon": "check-square"
    },
    "bitwise_not": {
        "id": "bitwise_not",
        "name": "位非运算",
        "name_en": "Bitwise NOT",
        "description": "执行位非运算",
        "category": "bitwise",
        "subcategory": "not",
        "api_endpoint": "/api/bitwise/not",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "操作数"}
        ],
        "icon": "check-square"
    },
    "left_shift": {
        "id": "left_shift",
        "name": "左移运算",
        "name_en": "Left Shift",
        "description": "执行左移运算",
        "category": "bitwise",
        "subcategory": "shift",
        "api_endpoint": "/api/bitwise/left-shift",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "操作数"},
            {"name": "b", "type": "number", "required": True, "description": "移位位数"}
        ],
        "icon": "arrow-right"
    },
    "right_shift": {
        "id": "right_shift",
        "name": "右移运算",
        "name_en": "Right Shift",
        "description": "执行右移运算",
        "category": "bitwise",
        "subcategory": "shift",
        "api_endpoint": "/api/bitwise/right-shift",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "操作数"},
            {"name": "b", "type": "number", "required": True, "description": "移位位数"}
        ],
        "icon": "arrow-left"
    },
    "count_set_bits": {
        "id": "count_set_bits",
        "name": "计数1的个数",
        "name_en": "Count Set Bits",
        "description": "统计整数中1的个数",
        "category": "bitwise",
        "subcategory": "count",
        "api_endpoint": "/api/bitwise/count-bits",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "整数"}
        ],
        "icon": "hash"
    },
    "is_power_of_two": {
        "id": "is_power_of_two",
        "name": "2的幂检查",
        "name_en": "Is Power of Two",
        "description": "判断整数是否为2的幂",
        "category": "bitwise",
        "subcategory": "check",
        "api_endpoint": "/api/bitwise/is-power-of-two",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "整数"}
        ],
        "icon": "check-circle"
    },
    "validate_email": {
        "id": "validate_email",
        "name": "邮箱验证",
        "name_en": "Email Validator",
        "description": "验证邮箱格式",
        "category": "validate",
        "subcategory": "email",
        "api_endpoint": "/api/validate/email",
        "method": "POST",
        "params": [
            {"name": "value", "type": "string", "required": True, "description": "邮箱地址"}
        ],
        "icon": "mail"
    },
    "validate_url": {
        "id": "validate_url",
        "name": "URL验证",
        "name_en": "URL Validator",
        "description": "验证URL格式",
        "category": "validate",
        "subcategory": "url",
        "api_endpoint": "/api/validate/url",
        "method": "POST",
        "params": [
            {"name": "value", "type": "string", "required": True, "description": "URL地址"}
        ],
        "icon": "link"
    },
    "validate_phone": {
        "id": "validate_phone",
        "name": "电话验证",
        "name_en": "Phone Validator",
        "description": "验证电话号码格式",
        "category": "validate",
        "subcategory": "phone",
        "api_endpoint": "/api/validate/phone",
        "method": "POST",
        "params": [
            {"name": "phone", "type": "string", "required": True, "description": "电话号码"},
            {"name": "country", "type": "string", "required": False, "description": "国家代码"}
        ],
        "icon": "phone"
    },
    "validate_ip": {
        "id": "validate_ip",
        "name": "IP地址验证",
        "name_en": "IP Validator",
        "description": "验证IP地址格式",
        "category": "validate",
        "subcategory": "ip",
        "api_endpoint": "/api/validate/ip",
        "method": "POST",
        "params": [
            {"name": "ip", "type": "string", "required": True, "description": "IP地址"},
            {"name": "version", "type": "number", "required": False, "description": "IP版本"}
        ],
        "icon": "globe"
    },
    "validate_credit_card": {
        "id": "validate_credit_card",
        "name": "信用卡验证",
        "name_en": "Credit Card Validator",
        "description": "验证信用卡号(Luhn算法)",
        "category": "validate",
        "subcategory": "card",
        "api_endpoint": "/api/validate/credit-card",
        "method": "POST",
        "params": [
            {"name": "card", "type": "string", "required": True, "description": "卡号"}
        ],
        "icon": "credit-card"
    },
    "validate_uuid": {
        "id": "validate_uuid",
        "name": "UUID验证",
        "name_en": "UUID Validator",
        "description": "验证UUID格式",
        "category": "validate",
        "subcategory": "uuid",
        "api_endpoint": "/api/validate/uuid",
        "method": "POST",
        "params": [
            {"name": "uuid", "type": "string", "required": True, "description": "UUID字符串"}
        ],
        "icon": "hash"
    },
    "validate_json": {
        "id": "validate_json",
        "name": "JSON验证",
        "name_en": "JSON Validator",
        "description": "验证JSON格式",
        "category": "validate",
        "subcategory": "json",
        "api_endpoint": "/api/validate/json",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "JSON文本"}
        ],
        "icon": "code"
    },
    "validate_range": {
        "id": "validate_range",
        "name": "范围验证",
        "name_en": "Range Validator",
        "description": "验证值是否在指定范围内",
        "category": "validate",
        "subcategory": "range",
        "api_endpoint": "/api/validate/range",
        "method": "POST",
        "params": [
            {"name": "value", "type": "number", "required": True, "description": "值"},
            {"name": "min_val", "type": "number", "required": True, "description": "最小值"},
            {"name": "max_val", "type": "number", "required": True, "description": "最大值"}
        ],
        "icon": "sliders"
    },
    "dt_now": {
        "id": "dt_now",
        "name": "当前时间",
        "name_en": "Current DateTime",
        "description": "获取当前日期时间",
        "category": "datetime",
        "subcategory": "now",
        "api_endpoint": "/api/datetime/now",
        "method": "POST",
        "params": [
            {"name": "format", "type": "string", "required": False, "description": "日期格式"}
        ],
        "icon": "clock"
    },
    "dt_today": {
        "id": "dt_today",
        "name": "今日日期",
        "name_en": "Today",
        "description": "获取今天的日期",
        "category": "datetime",
        "subcategory": "today",
        "api_endpoint": "/api/datetime/today",
        "method": "POST",
        "params": [
            {"name": "format", "type": "string", "required": False, "description": "日期格式"}
        ],
        "icon": "calendar"
    },
    "dt_add": {
        "id": "dt_add",
        "name": "日期加减",
        "name_en": "Date Add/Subtract",
        "description": "日期时间加减计算",
        "category": "datetime",
        "subcategory": "add",
        "api_endpoint": "/api/datetime/add",
        "method": "POST",
        "params": [
            {"name": "dt_str", "type": "string", "required": True, "description": "日期时间"},
            {"name": "days", "type": "number", "required": False, "description": "天数"},
            {"name": "hours", "type": "number", "required": False, "description": "小时"},
            {"name": "minutes", "type": "number", "required": False, "description": "分钟"},
            {"name": "format", "type": "string", "required": False, "description": "格式"}
        ],
        "icon": "plus-circle"
    },
    "dt_diff": {
        "id": "dt_diff",
        "name": "日期差计算",
        "name_en": "Date Difference",
        "description": "计算两个日期之间的差值",
        "category": "datetime",
        "subcategory": "diff",
        "api_endpoint": "/api/datetime/diff",
        "method": "POST",
        "params": [
            {"name": "dt1_str", "type": "string", "required": True, "description": "日期时间1"},
            {"name": "dt2_str", "type": "string", "required": True, "description": "日期时间2"},
            {"name": "format", "type": "string", "required": False, "description": "格式"}
        ],
        "icon": "minus-circle"
    },
    "dt_format": {
        "id": "dt_format",
        "name": "日期格式转换",
        "name_en": "Date Format",
        "description": "日期格式转换",
        "category": "datetime",
        "subcategory": "format",
        "api_endpoint": "/api/datetime/format",
        "method": "POST",
        "params": [
            {"name": "dt_str", "type": "string", "required": True, "description": "日期时间"},
            {"name": "from_format", "type": "string", "required": True, "description": "源格式"},
            {"name": "to_format", "type": "string", "required": True, "description": "目标格式"}
        ],
        "icon": "refresh-cw"
    },
    "dt_timestamp": {
        "id": "dt_timestamp",
        "name": "转时间戳",
        "name_en": "To Timestamp",
        "description": "日期时间转时间戳",
        "category": "datetime",
        "subcategory": "timestamp",
        "api_endpoint": "/api/datetime/timestamp",
        "method": "POST",
        "params": [
            {"name": "dt_str", "type": "string", "required": True, "description": "日期时间"},
            {"name": "format", "type": "string", "required": False, "description": "格式"}
        ],
        "icon": "hash"
    },
    "dt_from_timestamp": {
        "id": "dt_from_timestamp",
        "name": "从时间戳转日期",
        "name_en": "From Timestamp",
        "description": "时间戳转日期时间",
        "category": "datetime",
        "subcategory": "timestamp",
        "api_endpoint": "/api/datetime/from-timestamp",
        "method": "POST",
        "params": [
            {"name": "timestamp", "type": "number", "required": True, "description": "时间戳"}
        ],
        "icon": "hash"
    },
    "absolute_value": {
        "id": "absolute_value",
        "name": "绝对值",
        "name_en": "Absolute Value",
        "description": "计算绝对值",
        "category": "math",
        "subcategory": "basic",
        "api_endpoint": "/api/absolute-value",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "数值"}
        ],
        "icon": "hash"
    },
    "round_number": {
        "id": "round_number",
        "name": "四舍五入",
        "name_en": "Round Number",
        "description": "对数字四舍五入",
        "category": "math",
        "subcategory": "basic",
        "api_endpoint": "/api/round",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "数值"},
            {"name": "decimals", "type": "number", "required": False, "description": "小数位数"}
        ],
        "icon": "hash"
    },
    "clamp": {
        "id": "clamp",
        "name": "区间限制",
        "name_en": "Clamp",
        "description": "将值限制在指定范围内",
        "category": "math",
        "subcategory": "basic",
        "api_endpoint": "/api/clamp",
        "method": "POST",
        "params": [
            {"name": "value", "type": "number", "required": True, "description": "值"},
            {"name": "min_val", "type": "number", "required": True, "description": "最小值"},
            {"name": "max_val", "type": "number", "required": True, "description": "最大值"}
        ],
        "icon": "sliders"
    },
    "min_value": {
        "id": "min_value",
        "name": "最小值",
        "name_en": "Minimum",
        "description": "获取最小值",
        "category": "math",
        "subcategory": "aggregate",
        "api_endpoint": "/api/min",
        "method": "POST",
        "params": [
            {"name": "values", "type": "array", "required": True, "description": "数值列表"}
        ],
        "icon": "arrow-down"
    },
    "max_value": {
        "id": "max_value",
        "name": "最大值",
        "name_en": "Maximum",
        "description": "获取最大值",
        "category": "math",
        "subcategory": "aggregate",
        "api_endpoint": "/api/max",
        "method": "POST",
        "params": [
            {"name": "values", "type": "array", "required": True, "description": "数值列表"}
        ],
        "icon": "arrow-up"
    },
    "sum_values": {
        "id": "sum_values",
        "name": "求和",
        "name_en": "Sum",
        "description": "计算总和",
        "category": "math",
        "subcategory": "aggregate",
        "api_endpoint": "/api/sum",
        "method": "POST",
        "params": [
            {"name": "values", "type": "array", "required": True, "description": "数值列表"}
        ],
        "icon": "plus"
    },
    "avg_value": {
        "id": "avg_value",
        "name": "平均值",
        "name_en": "Average",
        "description": "计算平均值",
        "category": "math",
        "subcategory": "aggregate",
        "api_endpoint": "/api/avg",
        "method": "POST",
        "params": [
            {"name": "values", "type": "array", "required": True, "description": "数值列表"}
        ],
        "icon": "divide"
    },
    "uppercase": {
        "id": "uppercase",
        "name": "转大写",
        "name_en": "To Uppercase",
        "description": "将字符串转换为大写",
        "category": "text",
        "subcategory": "case",
        "api_endpoint": "/api/uppercase",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "type"
    },
    "lowercase": {
        "id": "lowercase",
        "name": "转小写",
        "name_en": "To Lowercase",
        "description": "将字符串转换为小写",
        "category": "text",
        "subcategory": "case",
        "api_endpoint": "/api/lowercase",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "type"
    },
    "capitalize": {
        "id": "capitalize",
        "name": "首字母大写",
        "name_en": "Capitalize",
        "description": "首字母大写",
        "category": "text",
        "subcategory": "case",
        "api_endpoint": "/api/capitalize",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "type"
    },
    "reverse_text": {
        "id": "reverse_text",
        "name": "反转文本",
        "name_en": "Reverse Text",
        "description": "反转字符串",
        "category": "text",
        "subcategory": "transform",
        "api_endpoint": "/api/reverse",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "rotate-cw"
    },
    "trim": {
        "id": "trim",
        "name": "去空白",
        "name_en": "Trim",
        "description": "去除首尾空白",
        "category": "text",
        "subcategory": "format",
        "api_endpoint": "/api/trim",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "minus"
    },
    "split_text": {
        "id": "split_text",
        "name": "分割文本",
        "name_en": "Split Text",
        "description": "按分隔符分割文本",
        "category": "text",
        "subcategory": "split",
        "api_endpoint": "/api/split",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "delimiter", "type": "string", "required": False, "description": "分隔符"}
        ],
        "icon": "scissors"
    },
    "join_text": {
        "id": "join_text",
        "name": "连接文本",
        "name_en": "Join Text",
        "description": "用分隔符连接文本列表",
        "category": "text",
        "subcategory": "join",
        "api_endpoint": "/api/join",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "文本列表"},
            {"name": "separator", "type": "string", "required": False, "description": "分隔符"}
        ],
        "icon": "plus"
    },
    "length": {
        "id": "length",
        "name": "长度",
        "name_en": "Length",
        "description": "获取列表或字符串长度",
        "category": "list",
        "subcategory": "property",
        "api_endpoint": "/api/length",
        "method": "POST",
        "params": [
            {"name": "item", "type": "array", "required": True, "description": "列表或字符串"}
        ],
        "icon": "hash"
    },
    "first_item": {
        "id": "first_item",
        "name": "首个元素",
        "name_en": "First Item",
        "description": "获取列表第一个元素",
        "category": "list",
        "subcategory": "access",
        "api_endpoint": "/api/first",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "列表"}
        ],
        "icon": "arrow-right"
    },
    "last_item": {
        "id": "last_item",
        "name": "末尾元素",
        "name_en": "Last Item",
        "description": "获取列表最后一个元素",
        "category": "list",
        "subcategory": "access",
        "api_endpoint": "/api/last",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "列表"}
        ],
        "icon": "arrow-left"
    },
    "nth_item": {
        "id": "nth_item",
        "name": "第N个元素",
        "name_en": "Nth Item",
        "description": "获取列表第N个元素",
        "category": "list",
        "subcategory": "access",
        "api_endpoint": "/api/nth",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "列表"},
            {"name": "index", "type": "number", "required": True, "description": "索引"}
        ],
        "icon": "list"
    },
    "contains": {
        "id": "contains",
        "name": "包含检查",
        "name_en": "Contains",
        "description": "检查列表是否包含元素",
        "category": "list",
        "subcategory": "check",
        "api_endpoint": "/api/contains",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "列表"},
            {"name": "value", "type": "string", "required": True, "description": "值"}
        ],
        "icon": "search"
    },
    "unique": {
        "id": "unique",
        "name": "去重",
        "name_en": "Unique",
        "description": "去除重复元素",
        "category": "list",
        "subcategory": "transform",
        "api_endpoint": "/api/unique",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "列表"}
        ],
        "icon": "filter"
    },
    "sort_list": {
        "id": "sort_list",
        "name": "排序",
        "name_en": "Sort List",
        "description": "对列表排序",
        "category": "list",
        "subcategory": "transform",
        "api_endpoint": "/api/sort",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "列表"},
            {"name": "reverse", "type": "boolean", "required": False, "description": "降序"}
        ],
        "icon": "arrow-up-down"
    },
    "encode_base64": {
        "id": "encode_base64",
        "name": "Base64编码",
        "name_en": "Base64 Encode",
        "description": "字符串Base64编码",
        "category": "encoding",
        "subcategory": "base64",
        "api_endpoint": "/api/base64/encode",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "lock"
    },
    "decode_base64": {
        "id": "decode_base64",
        "name": "Base64解码",
        "name_en": "Base64 Decode",
        "description": "Base64字符串解码",
        "category": "encoding",
        "subcategory": "base64",
        "api_endpoint": "/api/base64/decode",
        "method": "POST",
        "params": [
            {"name": "encoded", "type": "string", "required": True, "description": "编码字符串"}
        ],
        "icon": "unlock"
    },
    "url_encode": {
        "id": "url_encode",
        "name": "URL编码",
        "name_en": "URL Encode",
        "description": "URL编码",
        "category": "encoding",
        "subcategory": "url",
        "api_endpoint": "/api/url/encode",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "link"
    },
    "url_decode": {
        "id": "url_decode",
        "name": "URL解码",
        "name_en": "URL Decode",
        "description": "URL解码",
        "category": "encoding",
        "subcategory": "url",
        "api_endpoint": "/api/url/decode",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "URL编码字符串"}
        ],
        "icon": "link"
    },
    "hex_encode": {
        "id": "hex_encode",
        "name": "十六进制编码",
        "name_en": "Hex Encode",
        "description": "字符串转十六进制",
        "category": "encoding",
        "subcategory": "hex",
        "api_endpoint": "/api/hex/encode",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "hash"
    },
    "hex_decode": {
        "id": "hex_decode",
        "name": "十六进制解码",
        "name_en": "Hex Decode",
        "description": "十六进制转字符串",
        "category": "encoding",
        "subcategory": "hex",
        "api_endpoint": "/api/hex/decode",
        "method": "POST",
        "params": [
            {"name": "hex", "type": "string", "required": True, "description": "十六进制字符串"}
        ],
        "icon": "hash"
    },
    "json_encode": {
        "id": "json_encode",
        "name": "JSON编码",
        "name_en": "JSON Encode",
        "description": "对象转JSON字符串",
        "category": "encoding",
        "subcategory": "json",
        "api_endpoint": "/api/json/encode",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "对象"}
        ],
        "icon": "code"
    },
    "json_decode": {
        "id": "json_decode",
        "name": "JSON解码",
        "name_en": "JSON Decode",
        "description": "JSON字符串转对象",
        "category": "encoding",
        "subcategory": "json",
        "api_endpoint": "/api/json/decode",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "JSON字符串"}
        ],
        "icon": "code"
    },
    "random_int": {
        "id": "random_int",
        "name": "随机整数",
        "name_en": "Random Integer",
        "description": "生成随机整数",
        "category": "random",
        "subcategory": "int",
        "api_endpoint": "/api/random/int",
        "method": "POST",
        "params": [
            {"name": "min_val", "type": "number", "required": False, "description": "最小值"},
            {"name": "max_val", "type": "number", "required": False, "description": "最大值"}
        ],
        "icon": "hash"
    },
    "random_float": {
        "id": "random_float",
        "name": "随机小数",
        "name_en": "Random Float",
        "description": "生成随机小数",
        "category": "random",
        "subcategory": "float",
        "api_endpoint": "/api/random/float",
        "method": "POST",
        "params": [],
        "icon": "hash"
    },
    "random_choice": {
        "id": "random_choice",
        "name": "随机选择",
        "name_en": "Random Choice",
        "description": "从列表中随机选择",
        "category": "random",
        "subcategory": "choice",
        "api_endpoint": "/api/random/choice",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "列表"}
        ],
        "icon": "shuffle"
    },
    "random_sample": {
        "id": "random_sample",
        "name": "随机抽样",
        "name_en": "Random Sample",
        "description": "从列表中随机抽取多个",
        "category": "random",
        "subcategory": "sample",
        "api_endpoint": "/api/random/sample",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "列表"},
            {"name": "count", "type": "number", "required": True, "description": "抽取数量"}
        ],
        "icon": "shuffle"
    },
    "shuffle": {
        "id": "shuffle",
        "name": "随机打乱",
        "name_en": "Shuffle",
        "description": "随机打乱列表顺序",
        "category": "random",
        "subcategory": "shuffle",
        "api_endpoint": "/api/random/shuffle",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "列表"}
        ],
        "icon": "shuffle"
    },
    "uuid_generate": {
        "id": "uuid_generate",
        "name": "UUID生成",
        "name_en": "UUID Generate",
        "description": "生成UUID",
        "category": "random",
        "subcategory": "uuid",
        "api_endpoint": "/api/uuid/generate",
        "method": "POST",
        "params": [],
        "icon": "hash"
    },
    "slug_generate": {
        "id": "slug_generate",
        "name": "Slug生成",
        "name_en": "Slug Generate",
        "description": "生成URL友好的slug",
        "category": "random",
        "subcategory": "slug",
        "api_endpoint": "/api/slug/generate",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "link"
    },
    "chunk": {
        "id": "chunk",
        "name": "分块",
        "name_en": "Chunk",
        "description": "将列表分成指定大小的块",
        "category": "list",
        "subcategory": "transform",
        "api_endpoint": "/api/chunk",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "列表"},
            {"name": "size", "type": "number", "required": True, "description": "块大小"}
        ],
        "icon": "grid"
    },
    "flatten": {
        "id": "flatten",
        "name": "扁平化",
        "name_en": "Flatten",
        "description": "将嵌套列表扁平化",
        "category": "list",
        "subcategory": "transform",
        "api_endpoint": "/api/flatten",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "嵌套列表"},
            {"name": "depth", "type": "number", "required": False, "description": "深度,-1表示全部"}
        ],
        "icon": "minimize-2"
    },
    "zip_lists": {
        "id": "zip_lists",
        "name": "合并列表",
        "name_en": "Zip Lists",
        "description": "将多个列表配对合并",
        "category": "list",
        "subcategory": "transform",
        "api_endpoint": "/api/zip",
        "method": "POST",
        "params": [
            {"name": "lists", "type": "array", "required": True, "description": "列表数组"}
        ],
        "icon": "columns"
    },
    "enumerate_list": {
        "id": "enumerate_list",
        "name": "枚举列表",
        "name_en": "Enumerate List",
        "description": "为列表添加索引",
        "category": "list",
        "subcategory": "transform",
        "api_endpoint": "/api/enumerate",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "列表"},
            {"name": "start", "type": "number", "required": False, "description": "起始索引"}
        ],
        "icon": "list"
    },
    "window": {
        "id": "window",
        "name": "滑动窗口",
        "name_en": "Window",
        "description": "创建滑动窗口",
        "category": "list",
        "subcategory": "transform",
        "api_endpoint": "/api/window",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "列表"},
            {"name": "size", "type": "number", "required": True, "description": "窗口大小"},
            {"name": "step", "type": "number", "required": False, "description": "步长"}
        ],
        "icon": "square"
    },
    "count_by": {
        "id": "count_by",
        "name": "分组计数",
        "name_en": "Count By",
        "description": "按条件分组计数",
        "category": "list",
        "subcategory": "aggregate",
        "api_endpoint": "/api/count-by",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "列表"}
        ],
        "icon": "bar-chart"
    },
    "group_by": {
        "id": "group_by",
        "name": "分组",
        "name_en": "Group By",
        "description": "按条件分组",
        "category": "list",
        "subcategory": "transform",
        "api_endpoint": "/api/group-by",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "列表"}
        ],
        "icon": "folder"
    },
    "dict_get": {
        "id": "dict_get",
        "name": "获取值",
        "name_en": "Dict Get",
        "description": "获取字典中的值",
        "category": "dict",
        "subcategory": "access",
        "api_endpoint": "/api/dict/get",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "字典"},
            {"name": "key", "type": "string", "required": True, "description": "键"},
            {"name": "default", "type": "string", "required": False, "description": "默认值"}
        ],
        "icon": "key"
    },
    "dict_keys": {
        "id": "dict_keys",
        "name": "获取键列表",
        "name_en": "Dict Keys",
        "description": "获取字典的所有键",
        "category": "dict",
        "subcategory": "property",
        "api_endpoint": "/api/dict/keys",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "字典"}
        ],
        "icon": "list"
    },
    "dict_values": {
        "id": "dict_values",
        "name": "获取值列表",
        "name_en": "Dict Values",
        "description": "获取字典的所有值",
        "category": "dict",
        "subcategory": "property",
        "api_endpoint": "/api/dict/values",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "字典"}
        ],
        "icon": "list"
    },
    "dict_merge": {
        "id": "dict_merge",
        "name": "合并字典",
        "name_en": "Merge Dict",
        "description": "合并多个字典",
        "category": "dict",
        "subcategory": "transform",
        "api_endpoint": "/api/dict/merge",
        "method": "POST",
        "params": [
            {"name": "dicts", "type": "array", "required": True, "description": "字典数组"}
        ],
        "icon": "plus"
    },
    "dict_filter": {
        "id": "dict_filter",
        "name": "过滤字典",
        "name_en": "Filter Dict",
        "description": "按键过滤字典",
        "category": "dict",
        "subcategory": "transform",
        "api_endpoint": "/api/dict/filter",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "字典"},
            {"name": "keys", "type": "array", "required": True, "description": "要保留的键"}
        ],
        "icon": "filter"
    },
    "dict_update": {
        "id": "dict_update",
        "name": "更新字典",
        "name_en": "Update Dict",
        "description": "更新字典内容",
        "category": "dict",
        "subcategory": "transform",
        "api_endpoint": "/api/dict/update",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "字典"},
            {"name": "updates", "type": "object", "required": True, "description": "更新内容"}
        ],
        "icon": "refresh-cw"
    },
    "pad_left": {
        "id": "pad_left",
        "name": "左侧填充",
        "name_en": "Pad Left",
        "description": "在字符串左侧填充字符",
        "category": "text",
        "subcategory": "format",
        "api_endpoint": "/api/pad-left",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "length", "type": "number", "required": True, "description": "目标长度"},
            {"name": "char", "type": "string", "required": False, "description": "填充字符"}
        ],
        "icon": "align-left"
    },
    "pad_right": {
        "id": "pad_right",
        "name": "右侧填充",
        "name_en": "Pad Right",
        "description": "在字符串右侧填充字符",
        "category": "text",
        "subcategory": "format",
        "api_endpoint": "/api/pad-right",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "length", "type": "number", "required": True, "description": "目标长度"},
            {"name": "char", "type": "string", "required": False, "description": "填充字符"}
        ],
        "icon": "align-right"
    },
    "truncate": {
        "id": "truncate",
        "name": "截断文本",
        "name_en": "Truncate",
        "description": "截断字符串到指定长度",
        "category": "text",
        "subcategory": "format",
        "api_endpoint": "/api/truncate",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "length", "type": "number", "required": True, "description": "最大长度"},
            {"name": "suffix", "type": "string", "required": False, "description": "后缀"}
        ],
        "icon": "maximize-2"
    },
    "word_count": {
        "id": "word_count",
        "name": "字数统计",
        "name_en": "Word Count",
        "description": "统计文本字数",
        "category": "text",
        "subcategory": "stats",
        "api_endpoint": "/api/word-count",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "hash"
    },
    "char_count": {
        "id": "char_count",
        "name": "字符统计",
        "name_en": "Char Count",
        "description": "统计字符数",
        "category": "text",
        "subcategory": "stats",
        "api_endpoint": "/api/char-count",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "hash"
    },
    "line_count": {
        "id": "line_count",
        "name": "行数统计",
        "name_en": "Line Count",
        "description": "统计行数",
        "category": "text",
        "subcategory": "stats",
        "api_endpoint": "/api/line-count",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "hash"
    },
    "contains_any": {
        "id": "contains_any",
        "name": "包含任一",
        "name_en": "Contains Any",
        "description": "检查是否包含任一关键词",
        "category": "text",
        "subcategory": "check",
        "api_endpoint": "/api/contains-any",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "keywords", "type": "array", "required": True, "description": "关键词列表"}
        ],
        "icon": "search"
    },
    "power": {
        "id": "power",
        "name": "幂运算",
        "name_en": "Power",
        "description": "计算幂",
        "category": "math",
        "subcategory": "advanced",
        "api_endpoint": "/api/power",
        "method": "POST",
        "params": [
            {"name": "base", "type": "number", "required": True, "description": "底数"},
            {"name": "exponent", "type": "number", "required": True, "description": "指数"}
        ],
        "icon": "superscript"
    },
    "sqrt": {
        "id": "sqrt",
        "name": "平方根",
        "name_en": "Square Root",
        "description": "计算平方根",
        "category": "math",
        "subcategory": "advanced",
        "api_endpoint": "/api/sqrt",
        "method": "POST",
        "params": [
            {"name": "value", "type": "number", "required": True, "description": "数值"}
        ],
        "icon": "superscript"
    },
    "log": {
        "id": "log",
        "name": "对数",
        "name_en": "Logarithm",
        "description": "计算对数",
        "category": "math",
        "subcategory": "advanced",
        "api_endpoint": "/api/log",
        "method": "POST",
        "params": [
            {"name": "value", "type": "number", "required": True, "description": "数值"},
            {"name": "base", "type": "number", "required": False, "description": "底数"}
        ],
        "icon": "superscript"
    },
    "factorial": {
        "id": "factorial",
        "name": "阶乘",
        "name_en": "Factorial",
        "description": "计算阶乘",
        "category": "math",
        "subcategory": "advanced",
        "api_endpoint": "/api/factorial",
        "method": "POST",
        "params": [
            {"name": "value", "type": "number", "required": True, "description": "数值"}
        ],
        "icon": "hash"
    },
    "gcd": {
        "id": "gcd",
        "name": "最大公约数",
        "name_en": "GCD",
        "description": "计算最大公约数",
        "category": "math",
        "subcategory": "advanced",
        "api_endpoint": "/api/gcd",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "数值A"},
            {"name": "b", "type": "number", "required": True, "description": "数值B"}
        ],
        "icon": "divide"
    },
    "lcm": {
        "id": "lcm",
        "name": "最小公倍数",
        "name_en": "LCM",
        "description": "计算最小公倍数",
        "category": "math",
        "subcategory": "advanced",
        "api_endpoint": "/api/lcm",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "数值A"},
            {"name": "b", "type": "number", "required": True, "description": "数值B"}
        ],
        "icon": "divide"
    },
    "median": {
        "id": "median",
        "name": "中位数",
        "name_en": "Median",
        "description": "计算中位数",
        "category": "math",
        "subcategory": "stats",
        "api_endpoint": "/api/median",
        "method": "POST",
        "params": [
            {"name": "values", "type": "array", "required": True, "description": "数值列表"}
        ],
        "icon": "bar-chart"
    },
    "variance": {
        "id": "variance",
        "name": "方差",
        "name_en": "Variance",
        "description": "计算方差",
        "category": "math",
        "subcategory": "stats",
        "api_endpoint": "/api/variance",
        "method": "POST",
        "params": [
            {"name": "values", "type": "array", "required": True, "description": "数值列表"}
        ],
        "icon": "bar-chart"
    },
    "std_dev": {
        "id": "std_dev",
        "name": "标准差",
        "name_en": "Standard Deviation",
        "description": "计算标准差",
        "category": "math",
        "subcategory": "stats",
        "api_endpoint": "/api/std-dev",
        "method": "POST",
        "params": [
            {"name": "values", "type": "array", "required": True, "description": "数值列表"}
        ],
        "icon": "bar-chart"
    },
    "mode": {
        "id": "mode",
        "name": "众数",
        "name_en": "Mode",
        "description": "计算众数",
        "category": "math",
        "subcategory": "stats",
        "api_endpoint": "/api/mode",
        "method": "POST",
        "params": [
            {"name": "values", "type": "array", "required": True, "description": "数值列表"}
        ],
        "icon": "bar-chart"
    },
    "percentile": {
        "id": "percentile",
        "name": "百分位数",
        "name_en": "Percentile",
        "description": "计算百分位数",
        "category": "math",
        "subcategory": "stats",
        "api_endpoint": "/api/percentile",
        "method": "POST",
        "params": [
            {"name": "values", "type": "array", "required": True, "description": "数值列表"},
            {"name": "p", "type": "number", "required": True, "description": "百分比(0-100)"}
        ],
        "icon": "bar-chart"
    },
    "product": {
        "id": "product",
        "name": "连乘",
        "name_en": "Product",
        "description": "计算连乘结果",
        "category": "math",
        "subcategory": "aggregate",
        "api_endpoint": "/api/product",
        "method": "POST",
        "params": [
            {"name": "values", "type": "array", "required": True, "description": "数值列表"}
        ],
        "icon": "x"
    },
    "is_prime": {
        "id": "is_prime",
        "name": "质数检查",
        "name_en": "Is Prime",
        "description": "检查是否为质数",
        "category": "math",
        "subcategory": "check",
        "api_endpoint": "/api/is-prime",
        "method": "POST",
        "params": [
            {"name": "value", "type": "number", "required": True, "description": "数值"}
        ],
        "icon": "check-circle"
    },
    "starts_with": {
        "id": "starts_with",
        "name": "开头检查",
        "name_en": "Starts With",
        "description": "检查字符串开头",
        "category": "text",
        "subcategory": "check",
        "api_endpoint": "/api/starts-with",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "prefix", "type": "string", "required": True, "description": "前缀"}
        ],
        "icon": "arrow-right"
    },
    "ends_with": {
        "id": "ends_with",
        "name": "结尾检查",
        "name_en": "Ends With",
        "description": "检查字符串结尾",
        "category": "text",
        "subcategory": "check",
        "api_endpoint": "/api/ends-with",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "suffix", "type": "string", "required": True, "description": "后缀"}
        ],
        "icon": "arrow-left"
    },
    "replace": {
        "id": "replace",
        "name": "替换文本",
        "name_en": "Replace",
        "description": "替换文本中的字符串",
        "category": "text",
        "subcategory": "transform",
        "api_endpoint": "/api/replace",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "old", "type": "string", "required": True, "description": "原字符串"},
            {"name": "new", "type": "string", "required": True, "description": "新字符串"}
        ],
        "icon": "refresh-cw"
    },
    "regex_match": {
        "id": "regex_match",
        "name": "正则匹配",
        "name_en": "Regex Match",
        "description": "使用正则表达式匹配",
        "category": "text",
        "subcategory": "regex",
        "api_endpoint": "/api/regex/match",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "pattern", "type": "string", "required": True, "description": "正则模式"}
        ],
        "icon": "regex"
    },
    "regex_replace": {
        "id": "regex_replace",
        "name": "正则替换",
        "name_en": "Regex Replace",
        "description": "使用正则表达式替换",
        "category": "text",
        "subcategory": "regex",
        "api_endpoint": "/api/regex/replace",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "pattern", "type": "string", "required": True, "description": "正则模式"},
            {"name": "replacement", "type": "string", "required": True, "description": "替换内容"}
        ],
        "icon": "regex"
    },
    "regex_find": {
        "id": "regex_find",
        "name": "正则查找",
        "name_en": "Regex Find",
        "description": "使用正则表达式查找所有匹配",
        "category": "text",
        "subcategory": "regex",
        "api_endpoint": "/api/regex/find",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "pattern", "type": "string", "required": True, "description": "正则模式"}
        ],
        "icon": "search"
    },
    "strip_html": {
        "id": "strip_html",
        "name": "去除HTML",
        "name_en": "Strip HTML",
        "description": "去除文本中的HTML标签",
        "category": "text",
        "subcategory": "clean",
        "api_endpoint": "/api/strip-html",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "HTML文本"}
        ],
        "icon": "code"
    },
    "set_union": {
        "id": "set_union",
        "name": "集合并集",
        "name_en": "Set Union",
        "description": "计算集合并集",
        "category": "set",
        "subcategory": "operation",
        "api_endpoint": "/api/set/union",
        "method": "POST",
        "params": [
            {"name": "a", "type": "array", "required": True, "description": "集合A"},
            {"name": "b", "type": "array", "required": True, "description": "集合B"}
        ],
        "icon": "union"
    },
    "set_intersection": {
        "id": "set_intersection",
        "name": "集合交集",
        "name_en": "Set Intersection",
        "description": "计算集合交集",
        "category": "set",
        "subcategory": "operation",
        "api_endpoint": "/api/set/intersection",
        "method": "POST",
        "params": [
            {"name": "a", "type": "array", "required": True, "description": "集合A"},
            {"name": "b", "type": "array", "required": True, "description": "集合B"}
        ],
        "icon": "intersection"
    },
    "set_diff": {
        "id": "set_diff",
        "name": "集合差集",
        "name_en": "Set Difference",
        "description": "计算集合差集",
        "category": "set",
        "subcategory": "operation",
        "api_endpoint": "/api/set/diff",
        "method": "POST",
        "params": [
            {"name": "a", "type": "array", "required": True, "description": "集合A"},
            {"name": "b", "type": "array", "required": True, "description": "集合B"}
        ],
        "icon": "minus"
    },
    "set_sym_diff": {
        "id": "set_sym_diff",
        "name": "集合对称差",
        "name_en": "Symmetric Difference",
        "description": "计算集合对称差集",
        "category": "set",
        "subcategory": "operation",
        "api_endpoint": "/api/set/sym-diff",
        "method": "POST",
        "params": [
            {"name": "a", "type": "array", "required": True, "description": "集合A"},
            {"name": "b", "type": "array", "required": True, "description": "集合B"}
        ],
        "icon": "x"
    },
    "set_subset": {
        "id": "set_subset",
        "name": "子集检查",
        "name_en": "Is Subset",
        "description": "检查是否为子集",
        "category": "set",
        "subcategory": "check",
        "api_endpoint": "/api/set/subset",
        "method": "POST",
        "params": [
            {"name": "a", "type": "array", "required": True, "description": "集合A"},
            {"name": "b", "type": "array", "required": True, "description": "集合B"}
        ],
        "icon": "check-circle"
    },
    "range_gen": {
        "id": "range_gen",
        "name": "范围生成",
        "name_en": "Range Generate",
        "description": "生成数字范围",
        "category": "list",
        "subcategory": "generate",
        "api_endpoint": "/api/range",
        "method": "POST",
        "params": [
            {"name": "start", "type": "number", "required": True, "description": "起始值"},
            {"name": "end", "type": "number", "required": True, "description": "结束值"},
            {"name": "step", "type": "number", "required": False, "description": "步长"}
        ],
        "icon": "list"
    },
    "repeat": {
        "id": "repeat",
        "name": "重复元素",
        "name_en": "Repeat",
        "description": "重复生成元素",
        "category": "list",
        "subcategory": "generate",
        "api_endpoint": "/api/repeat",
        "method": "POST",
        "params": [
            {"name": "item", "type": "string", "required": True, "description": "元素"},
            {"name": "count", "type": "number", "required": True, "description": "重复次数"}
        ],
        "icon": "copy"
    },
    "cycle": {
        "id": "cycle",
        "name": "循环生成",
        "name_en": "Cycle",
        "description": "循环生成列表元素",
        "category": "list",
        "subcategory": "generate",
        "api_endpoint": "/api/cycle",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "元素列表"},
            {"name": "count", "type": "number", "required": True, "description": "总数量"}
        ],
        "icon": "repeat"
    },
    "dedupe": {
        "id": "dedupe",
        "name": "去重",
        "name_en": "Deduplicate",
        "description": "去除相邻重复项",
        "category": "list",
        "subcategory": "transform",
        "api_endpoint": "/api/dedupe",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "列表"}
        ],
        "icon": "filter"
    },
    "partition": {
        "id": "partition",
        "name": "分区",
        "name_en": "Partition",
        "description": "将列表按条件分区",
        "category": "list",
        "subcategory": "transform",
        "api_endpoint": "/api/partition",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "列表"}
        ],
        "icon": "columns"
    },
    "zip_longest": {
        "id": "zip_longest",
        "name": "最长合并",
        "name_en": "Zip Longest",
        "description": "将多个列表最长合并",
        "category": "list",
        "subcategory": "transform",
        "api_endpoint": "/api/zip-longest",
        "method": "POST",
        "params": [
            {"name": "lists", "type": "array", "required": True, "description": "列表数组"},
            {"name": "fill", "type": "string", "required": False, "description": "填充值"}
        ],
        "icon": "columns"
    },
    "take": {
        "id": "take",
        "name": "获取前N个",
        "name_en": "Take",
        "description": "获取列表前N个元素",
        "category": "list",
        "subcategory": "access",
        "api_endpoint": "/api/take",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "列表"},
            {"name": "count", "type": "number", "required": True, "description": "数量"}
        ],
        "icon": "arrow-right"
    },
    "skip": {
        "id": "skip",
        "name": "跳过前N个",
        "name_en": "Skip",
        "description": "跳过列表前N个元素",
        "category": "list",
        "subcategory": "transform",
        "api_endpoint": "/api/skip",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "列表"},
            {"name": "count", "type": "number", "required": True, "description": "数量"}
        ],
        "icon": "arrow-right"
    },
    "compact": {
        "id": "compact",
        "name": "去除空值",
        "name_en": "Compact",
        "description": "去除列表中的空值",
        "category": "list",
        "subcategory": "clean",
        "api_endpoint": "/api/compact",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "列表"}
        ],
        "icon": "filter"
    },
    "equal": {
        "id": "equal",
        "name": "相等",
        "name_en": "Equal",
        "description": "检查两个值是否相等",
        "category": "logic",
        "subcategory": "compare",
        "api_endpoint": "/api/equal",
        "method": "POST",
        "params": [
            {"name": "a", "type": "string", "required": True, "description": "值A"},
            {"name": "b", "type": "string", "required": True, "description": "值B"}
        ],
        "icon": "equals"
    },
    "greater_than": {
        "id": "greater_than",
        "name": "大于",
        "name_en": "Greater Than",
        "description": "检查是否大于",
        "category": "logic",
        "subcategory": "compare",
        "api_endpoint": "/api/greater-than",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "值A"},
            {"name": "b", "type": "number", "required": True, "description": "值B"}
        ],
        "icon": "chevron-right"
    },
    "less_than": {
        "id": "less_than",
        "name": "小于",
        "name_en": "Less Than",
        "description": "检查是否小于",
        "category": "logic",
        "subcategory": "compare",
        "api_endpoint": "/api/less-than",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "值A"},
            {"name": "b", "type": "number", "required": True, "description": "值B"}
        ],
        "icon": "chevron-left"
    },
    "and_op": {
        "id": "and_op",
        "name": "逻辑与",
        "name_en": "Logical AND",
        "description": "逻辑与运算",
        "category": "logic",
        "subcategory": "boolean",
        "api_endpoint": "/api/and",
        "method": "POST",
        "params": [
            {"name": "a", "type": "boolean", "required": True, "description": "值A"},
            {"name": "b", "type": "boolean", "required": True, "description": "值B"}
        ],
        "icon": "and"
    },
    "or_op": {
        "id": "or_op",
        "name": "逻辑或",
        "name_en": "Logical OR",
        "description": "逻辑或运算",
        "category": "logic",
        "subcategory": "boolean",
        "api_endpoint": "/api/or",
        "method": "POST",
        "params": [
            {"name": "a", "type": "boolean", "required": True, "description": "值A"},
            {"name": "b", "type": "boolean", "required": True, "description": "值B"}
        ],
        "icon": "or"
    },
    "not_op": {
        "id": "not_op",
        "name": "逻辑非",
        "name_en": "Logical NOT",
        "description": "逻辑非运算",
        "category": "logic",
        "subcategory": "boolean",
        "api_endpoint": "/api/not",
        "method": "POST",
        "params": [
            {"name": "a", "type": "boolean", "required": True, "description": "值"}
        ],
        "icon": "not"
    },
    "if_then": {
        "id": "if_then",
        "name": "条件执行",
        "name_en": "If Then",
        "description": "条件执行",
        "category": "logic",
        "subcategory": "conditional",
        "api_endpoint": "/api/if-then",
        "method": "POST",
        "params": [
            {"name": "condition", "type": "boolean", "required": True, "description": "条件"},
            {"name": "then_val", "type": "string", "required": True, "description": "真值"},
            {"name": "else_val", "type": "string", "required": False, "description": "假值"}
        ],
        "icon": "toggle-right"
    },
    "coalesce": {
        "id": "coalesce",
        "name": "空值合并",
        "name_en": "Coalesce",
        "description": "返回第一个非空值",
        "category": "utility",
        "subcategory": "null",
        "api_endpoint": "/api/coalesce",
        "method": "POST",
        "params": [
            {"name": "values", "type": "array", "required": True, "description": "值列表"}
        ],
        "icon": "git_merge"
    },
    "default": {
        "id": "default",
        "name": "默认值",
        "name_en": "Default",
        "description": "如果值为空则返回默认值",
        "category": "utility",
        "subcategory": "null",
        "api_endpoint": "/api/default",
        "method": "POST",
        "params": [
            {"name": "value", "type": "string", "required": True, "description": "值"},
            {"name": "default_val", "type": "string", "required": True, "description": "默认值"}
        ],
        "icon": "corner-down-left"
    },
    "type_of": {
        "id": "type_of",
        "name": "类型检查",
        "name_en": "Type Of",
        "description": "返回值的类型",
        "category": "utility",
        "subcategory": "type",
        "api_endpoint": "/api/type-of",
        "method": "POST",
        "params": [
            {"name": "value", "type": "string", "required": True, "description": "值"}
        ],
        "icon": "tag"
    },
    "is_empty": {
        "id": "is_empty",
        "name": "空值检查",
        "name_en": "Is Empty",
        "description": "检查是否为空",
        "category": "utility",
        "subcategory": "check",
        "api_endpoint": "/api/is-empty",
        "method": "POST",
        "params": [
            {"name": "value", "type": "string", "required": True, "description": "值"}
        ],
        "icon": "check-circle"
    },
    "is_null": {
        "id": "is_null",
        "name": "空检查",
        "name_en": "Is Null",
        "description": "检查是否为null",
        "category": "utility",
        "subcategory": "check",
        "api_endpoint": "/api/is-null",
        "method": "POST",
        "params": [
            {"name": "value", "type": "string", "required": True, "description": "值"}
        ],
        "icon": "check-circle"
    },
    "noop": {
        "id": "noop",
        "name": "空操作",
        "name_en": "No Operation",
        "description": "不执行任何操作",
        "category": "utility",
        "subcategory": "flow",
        "api_endpoint": "/api/noop",
        "method": "POST",
        "params": [],
        "icon": "slash"
    },
    "identity": {
        "id": "identity",
        "name": "恒等函数",
        "name_en": "Identity",
        "description": "返回输入值本身",
        "category": "utility",
        "subcategory": "flow",
        "api_endpoint": "/api/identity",
        "method": "POST",
        "params": [
            {"name": "value", "type": "string", "required": True, "description": "值"}
        ],
        "icon": "corner-down-right"
    },
    "compose": {
        "id": "compose",
        "name": "函数组合",
        "name_en": "Compose",
        "description": "组合多个函数",
        "category": "function",
        "subcategory": "compose",
        "api_endpoint": "/api/compose",
        "method": "POST",
        "params": [
            {"name": "fns", "type": "array", "required": True, "description": "函数列表"}
        ],
        "icon": "git_merge"
    },
    "curry": {
        "id": "curry",
        "name": "柯里化",
        "name_en": "Curry",
        "description": "函数柯里化",
        "category": "function",
        "subcategory": "transform",
        "api_endpoint": "/api/curry",
        "method": "POST",
        "params": [
            {"name": "fn", "type": "string", "required": True, "description": "函数"}
        ],
        "icon": "git_branch"
    },
    "partial": {
        "id": "partial",
        "name": "偏函数",
        "name_en": "Partial",
        "description": "创建偏函数",
        "category": "function",
        "subcategory": "transform",
        "api_endpoint": "/api/partial",
        "method": "POST",
        "params": [
            {"name": "fn", "type": "string", "required": True, "description": "函数"},
            {"name": "args", "type": "array", "required": True, "description": "预设参数"}
        ],
        "icon": "git_branch"
    },
    "throttle": {
        "id": "throttle",
        "name": "节流",
        "name_en": "Throttle",
        "description": "函数节流",
        "category": "function",
        "subcategory": "timing",
        "api_endpoint": "/api/throttle",
        "method": "POST",
        "params": [
            {"name": "fn", "type": "string", "required": True, "description": "函数"},
            {"name": "wait", "type": "number", "required": True, "description": "等待时间(毫秒)"}
        ],
        "icon": "clock"
    },
    "debounce": {
        "id": "debounce",
        "name": "防抖",
        "name_en": "Debounce",
        "description": "函数防抖",
        "category": "function",
        "subcategory": "timing",
        "api_endpoint": "/api/debounce",
        "method": "POST",
        "params": [
            {"name": "fn", "type": "string", "required": True, "description": "函数"},
            {"name": "wait", "type": "number", "required": True, "description": "等待时间(毫秒)"}
        ],
        "icon": "clock"
    },
    "memoize": {
        "id": "memoize",
        "name": "记忆化",
        "name_en": "Memoize",
        "description": "函数记忆化",
        "category": "function",
        "subcategory": "cache",
        "api_endpoint": "/api/memoize",
        "method": "POST",
        "params": [
            {"name": "fn", "type": "string", "required": True, "description": "函数"}
        ],
        "icon": "database"
    },
    "once": {
        "id": "once",
        "name": "单次执行",
        "name_en": "Once",
        "description": "函数只执行一次",
        "category": "function",
        "subcategory": "timing",
        "api_endpoint": "/api/once",
        "method": "POST",
        "params": [
            {"name": "fn", "type": "string", "required": True, "description": "函数"}
        ],
        "icon": "play"
    },
    "hex_to_rgb": {
        "id": "hex_to_rgb",
        "name": "HEX转RGB",
        "name_en": "HEX to RGB",
        "description": "HEX颜色转RGB",
        "category": "color",
        "subcategory": "convert",
        "api_endpoint": "/api/color/hex-to-rgb",
        "method": "POST",
        "params": [
            {"name": "hex", "type": "string", "required": True, "description": "HEX颜色值"}
        ],
        "icon": "palette"
    },
    "rgb_to_hex": {
        "id": "rgb_to_hex",
        "name": "RGB转HEX",
        "name_en": "RGB to HEX",
        "description": "RGB转HEX颜色",
        "category": "color",
        "subcategory": "convert",
        "api_endpoint": "/api/color/rgb-to-hex",
        "method": "POST",
        "params": [
            {"name": "r", "type": "number", "required": True, "description": "红色"},
            {"name": "g", "type": "number", "required": True, "description": "绿色"},
            {"name": "b", "type": "number", "required": True, "description": "蓝色"}
        ],
        "icon": "palette"
    },
    "lighten": {
        "id": "lighten",
        "name": "提亮颜色",
        "name_en": "Lighten Color",
        "description": "使颜色变亮",
        "category": "color",
        "subcategory": "adjust",
        "api_endpoint": "/api/color/lighten",
        "method": "POST",
        "params": [
            {"name": "hex", "type": "string", "required": True, "description": "HEX颜色值"},
            {"name": "amount", "type": "number", "required": False, "description": "提亮量"}
        ],
        "icon": "sun"
    },
    "darken": {
        "id": "darken",
        "name": "加深颜色",
        "name_en": "Darken Color",
        "description": "使颜色变深",
        "category": "color",
        "subcategory": "adjust",
        "api_endpoint": "/api/color/darken",
        "method": "POST",
        "params": [
            {"name": "hex", "type": "string", "required": True, "description": "HEX颜色值"},
            {"name": "amount", "type": "number", "required": False, "description": "加深量"}
        ],
        "icon": "moon"
    },
    "string_to_int": {
        "id": "string_to_int",
        "name": "字符串转整数",
        "name_en": "String to Int",
        "description": "将字符串转换为整数",
        "category": "convert",
        "subcategory": "type",
        "api_endpoint": "/api/convert/string-to-int",
        "method": "POST",
        "params": [
            {"name": "value", "type": "string", "required": True, "description": "字符串"}
        ],
        "icon": "type"
    },
    "int_to_string": {
        "id": "int_to_string",
        "name": "整数转字符串",
        "name_en": "Int to String",
        "description": "将整数转换为字符串",
        "category": "convert",
        "subcategory": "type",
        "api_endpoint": "/api/convert/int-to-string",
        "method": "POST",
        "params": [
            {"name": "value", "type": "number", "required": True, "description": "整数"}
        ],
        "icon": "type"
    },
    "to_number": {
        "id": "to_number",
        "name": "转数字",
        "name_en": "To Number",
        "description": "将字符串转换为数字",
        "category": "convert",
        "subcategory": "type",
        "api_endpoint": "/api/convert/to-number",
        "method": "POST",
        "params": [
            {"name": "value", "type": "string", "required": True, "description": "值"}
        ],
        "icon": "hash"
    },
    "batch": {
        "id": "batch",
        "name": "批量处理",
        "name_en": "Batch Process",
        "description": "批量处理元素",
        "category": "utility",
        "subcategory": "batch",
        "api_endpoint": "/api/batch",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "元素列表"},
            {"name": "fn", "type": "string", "required": True, "description": "处理函数"}
        ],
        "icon": "layers"
    },
    "chunk_batch": {
        "id": "chunk_batch",
        "name": "分块批处理",
        "name_en": "Chunk Batch",
        "description": "分块批量处理",
        "category": "utility",
        "subcategory": "batch",
        "api_endpoint": "/api/chunk-batch",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "元素列表"},
            {"name": "size", "type": "number", "required": True, "description": "块大小"}
        ],
        "icon": "grid"
    },
    "retry": {
        "id": "retry",
        "name": "重试",
        "name_en": "Retry",
        "description": "失败自动重试",
        "category": "utility",
        "subcategory": "retry",
        "api_endpoint": "/api/retry",
        "method": "POST",
        "params": [
            {"name": "fn", "type": "string", "required": True, "description": "函数"},
            {"name": "attempts", "type": "number", "required": False, "description": "重试次数"}
        ],
        "icon": "rotate-cw"
    },
    "sleep": {
        "id": "sleep",
        "name": "延迟",
        "name_en": "Sleep",
        "description": "延迟执行",
        "category": "utility",
        "subcategory": "timing",
        "api_endpoint": "/api/sleep",
        "method": "POST",
        "params": [
            {"name": "seconds", "type": "number", "required": True, "description": "秒数"}
        ],
        "icon": "clock"
    },
    "now": {
        "id": "now",
        "name": "当前时刻",
        "name_en": "Now",
        "description": "获取当前时刻",
        "category": "datetime",
        "subcategory": "now",
        "api_endpoint": "/api/now",
        "method": "POST",
        "params": [],
        "icon": "clock"
    },
    "today": {
        "id": "today",
        "name": "今日日期",
        "name_en": "Today",
        "description": "获取今天的日期",
        "category": "datetime",
        "subcategory": "date",
        "api_endpoint": "/api/today",
        "method": "POST",
        "params": [],
        "icon": "calendar"
    },
    "timestamp": {
        "id": "timestamp",
        "name": "时间戳",
        "name_en": "Timestamp",
        "description": "获取当前时间戳",
        "category": "datetime",
        "subcategory": "timestamp",
        "api_endpoint": "/api/timestamp",
        "method": "POST",
        "params": [],
        "icon": "hash"
    },
    "count_substring": {
        "id": "count_substring",
        "name": "子串计数",
        "name_en": "Count Substring",
        "description": "统计子串出现次数",
        "category": "text",
        "subcategory": "stats",
        "api_endpoint": "/api/count-substring",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "substr", "type": "string", "required": True, "description": "子串"}
        ],
        "icon": "hash"
    },
    "index_of": {
        "id": "index_of",
        "name": "查找位置",
        "name_en": "Index Of",
        "description": "查找子串位置",
        "category": "text",
        "subcategory": "search",
        "api_endpoint": "/api/index-of",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "substr", "type": "string", "required": True, "description": "子串"}
        ],
        "icon": "search"
    },
    "last_index_of": {
        "id": "last_index_of",
        "name": "最后位置",
        "name_en": "Last Index Of",
        "description": "查找子串最后位置",
        "category": "text",
        "subcategory": "search",
        "api_endpoint": "/api/last-index-of",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "substr", "type": "string", "required": True, "description": "子串"}
        ],
        "icon": "search"
    },
    "substring": {
        "id": "substring",
        "name": "子串提取",
        "name_en": "Substring",
        "description": "提取子串",
        "category": "text",
        "subcategory": "extract",
        "api_endpoint": "/api/substring",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "start", "type": "number", "required": True, "description": "起始位置"},
            {"name": "end", "type": "number", "required": False, "description": "结束位置"}
        ],
        "icon": "scissors"
    },
    "strip": {
        "id": "strip",
        "name": "去首尾空白",
        "name_en": "Strip",
        "description": "去除首尾空白",
        "category": "text",
        "subcategory": "format",
        "api_endpoint": "/api/strip",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "minus"
    },
    "lstrip": {
        "id": "lstrip",
        "name": "去左侧空白",
        "name_en": "LStrip",
        "description": "去除左侧空白",
        "category": "text",
        "subcategory": "format",
        "api_endpoint": "/api/lstrip",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "minus"
    },
    "rstrip": {
        "id": "rstrip",
        "name": "去右侧空白",
        "name_en": "RStrip",
        "description": "去除右侧空白",
        "category": "text",
        "subcategory": "format",
        "api_endpoint": "/api/rstrip",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "minus"
    },
    "any": {
        "id": "any",
        "name": "任意为真",
        "name_en": "Any",
        "description": "检查是否有任意元素为真",
        "category": "list",
        "subcategory": "check",
        "api_endpoint": "/api/any",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "列表"}
        ],
        "icon": "check-square"
    },
    "all": {
        "id": "all",
        "name": "全部为真",
        "name_en": "All",
        "description": "检查是否所有元素都为真",
        "category": "list",
        "subcategory": "check",
        "api_endpoint": "/api/all",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "列表"}
        ],
        "icon": "check-square"
    },
    "none": {
        "id": "none",
        "name": "全为假",
        "name_en": "None",
        "description": "检查是否所有元素都为假",
        "category": "list",
        "subcategory": "check",
        "api_endpoint": "/api/none",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "列表"}
        ],
        "icon": "check-square"
    },
    "find": {
        "id": "find",
        "name": "查找元素",
        "name_en": "Find",
        "description": "查找满足条件的第一个元素",
        "category": "list",
        "subcategory": "search",
        "api_endpoint": "/api/find",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "列表"}
        ],
        "icon": "search"
    },
    "filter_list": {
        "id": "filter_list",
        "name": "过滤列表",
        "name_en": "Filter List",
        "description": "过滤列表元素",
        "category": "list",
        "subcategory": "transform",
        "api_endpoint": "/api/filter",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "列表"}
        ],
        "icon": "filter"
    },
    "map_list": {
        "id": "map_list",
        "name": "映射列表",
        "name_en": "Map List",
        "description": "对列表每个元素应用函数",
        "category": "list",
        "subcategory": "transform",
        "api_endpoint": "/api/map",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "列表"},
            {"name": "fn", "type": "string", "required": True, "description": "函数"}
        ],
        "icon": "map"
    },
    "reduce": {
        "id": "reduce",
        "name": "聚合",
        "name_en": "Reduce",
        "description": "将列表归约为单个值",
        "category": "list",
        "subcategory": "aggregate",
        "api_endpoint": "/api/reduce",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "列表"},
            {"name": "fn", "type": "string", "required": True, "description": "聚合函数"}
        ],
        "icon": "git_merge"
    },
    "intersect": {
        "id": "intersect",
        "name": "交集",
        "name_en": "Intersect",
        "description": "获取两个列表的交集",
        "category": "list",
        "subcategory": "set",
        "api_endpoint": "/api/intersect",
        "method": "POST",
        "params": [
            {"name": "a", "type": "array", "required": True, "description": "列表A"},
            {"name": "b", "type": "array", "required": True, "description": "列表B"}
        ],
        "icon": "git_intersection"
    },
    "union": {
        "id": "union",
        "name": "并集",
        "name_en": "Union",
        "description": "获取两个列表的并集",
        "category": "list",
        "subcategory": "set",
        "api_endpoint": "/api/union",
        "method": "POST",
        "params": [
            {"name": "a", "type": "array", "required": True, "description": "列表A"},
            {"name": "b", "type": "array", "required": True, "description": "列表B"}
        ],
        "icon": "git_merge"
    },
    "diff": {
        "id": "diff",
        "name": "差集",
        "name_en": "Difference",
        "description": "获取两个列表的差集",
        "category": "list",
        "subcategory": "set",
        "api_endpoint": "/api/diff",
        "method": "POST",
        "params": [
            {"name": "a", "type": "array", "required": True, "description": "列表A"},
            {"name": "b", "type": "array", "required": True, "description": "列表B"}
        ],
        "icon": "minus"
    },
    "append": {
        "id": "append",
        "name": "追加",
        "name_en": "Append",
        "description": "追加元素到列表",
        "category": "list",
        "subcategory": "modify",
        "api_endpoint": "/api/append",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "列表"},
            {"name": "item", "type": "string", "required": True, "description": "元素"}
        ],
        "icon": "plus"
    },
    "prepend": {
        "id": "prepend",
        "name": "前置",
        "name_en": "Prepend",
        "description": "前置元素到列表",
        "category": "list",
        "subcategory": "modify",
        "api_endpoint": "/api/prepend",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "列表"},
            {"name": "item", "type": "string", "required": True, "description": "元素"}
        ],
        "icon": "plus"
    },
    "insert": {
        "id": "insert",
        "name": "插入",
        "name_en": "Insert",
        "description": "在指定位置插入元素",
        "category": "list",
        "subcategory": "modify",
        "api_endpoint": "/api/insert",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "列表"},
            {"name": "index", "type": "number", "required": True, "description": "位置"},
            {"name": "item", "type": "string", "required": True, "description": "元素"}
        ],
        "icon": "plus"
    },
    "update_item": {
        "id": "update_item",
        "name": "更新元素",
        "name_en": "Update Item",
        "description": "更新列表中的元素",
        "category": "list",
        "subcategory": "modify",
        "api_endpoint": "/api/update",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "列表"},
            {"name": "index", "type": "number", "required": True, "description": "位置"},
            {"name": "item", "type": "string", "required": True, "description": "新元素"}
        ],
        "icon": "edit"
    },
    "delete": {
        "id": "delete",
        "name": "删除",
        "name_en": "Delete",
        "description": "删除列表中指定位置的元素",
        "category": "list",
        "subcategory": "modify",
        "api_endpoint": "/api/delete",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "列表"},
            {"name": "index", "type": "number", "required": True, "description": "位置"}
        ],
        "icon": "trash-2"
    },
    "slice": {
        "id": "slice",
        "name": "切片",
        "name_en": "Slice",
        "description": "获取列表切片",
        "category": "list",
        "subcategory": "access",
        "api_endpoint": "/api/slice",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "列表"},
            {"name": "start", "type": "number", "required": False, "description": "起始位置"},
            {"name": "end", "type": "number", "required": False, "description": "结束位置"},
            {"name": "step", "type": "number", "required": False, "description": "步长"}
        ],
        "icon": "scissors"
    },
    "reverse_list": {
        "id": "reverse_list",
        "name": "反转列表",
        "name_en": "Reverse List",
        "description": "反转列表顺序",
        "category": "list",
        "subcategory": "transform",
        "api_endpoint": "/api/reverse",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "列表"}
        ],
        "icon": "rotate-cw"
    },
    "concat": {
        "id": "concat",
        "name": "连接列表",
        "name_en": "Concat",
        "description": "连接多个列表",
        "category": "list",
        "subcategory": "transform",
        "api_endpoint": "/api/concat",
        "method": "POST",
        "params": [
            {"name": "lists", "type": "array", "required": True, "description": "列表数组"}
        ],
        "icon": "plus"
    },
    "head": {
        "id": "head",
        "name": "首元素",
        "name_en": "Head",
        "description": "获取列表首元素",
        "category": "list",
        "subcategory": "access",
        "api_endpoint": "/api/head",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "列表"}
        ],
        "icon": "arrow-right"
    },
    "tail": {
        "id": "tail",
        "name": "尾元素",
        "name_en": "Tail",
        "description": "获取列表尾元素",
        "category": "list",
        "subcategory": "access",
        "api_endpoint": "/api/tail",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "列表"}
        ],
        "icon": "arrow-left"
    },
    "init": {
        "id": "init",
        "name": "去尾列表",
        "name_en": "Init",
        "description": "获取列表除最后一个元素外的所有元素",
        "category": "list",
        "subcategory": "access",
        "api_endpoint": "/api/init",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "列表"}
        ],
        "icon": "list"
    },
    "negate": {
        "id": "negate",
        "name": "取反",
        "name_en": "Negate",
        "description": "数值取反",
        "category": "math",
        "subcategory": "basic",
        "api_endpoint": "/api/negate",
        "method": "POST",
        "params": [
            {"name": "value", "type": "number", "required": True, "description": "数值"}
        ],
        "icon": "minus"
    },
    "increment": {
        "id": "increment",
        "name": "加一",
        "name_en": "Increment",
        "description": "数值加1",
        "category": "math",
        "subcategory": "basic",
        "api_endpoint": "/api/increment",
        "method": "POST",
        "params": [
            {"name": "value", "type": "number", "required": True, "description": "数值"}
        ],
        "icon": "plus"
    },
    "decrement": {
        "id": "decrement",
        "name": "减一",
        "name_en": "Decrement",
        "description": "数值减1",
        "category": "math",
        "subcategory": "basic",
        "api_endpoint": "/api/decrement",
        "method": "POST",
        "params": [
            {"name": "value", "type": "number", "required": True, "description": "数值"}
        ],
        "icon": "minus"
    },
    "add": {
        "id": "add",
        "name": "加法",
        "name_en": "Add",
        "description": "两数相加",
        "category": "math",
        "subcategory": "basic",
        "api_endpoint": "/api/add",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "数值A"},
            {"name": "b", "type": "number", "required": True, "description": "数值B"}
        ],
        "icon": "plus"
    },
    "subtract": {
        "id": "subtract",
        "name": "减法",
        "name_en": "Subtract",
        "description": "两数相减",
        "category": "math",
        "subcategory": "basic",
        "api_endpoint": "/api/subtract",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "数值A"},
            {"name": "b", "type": "number", "required": True, "description": "数值B"}
        ],
        "icon": "minus"
    },
    "multiply": {
        "id": "multiply",
        "name": "乘法",
        "name_en": "Multiply",
        "description": "两数相乘",
        "category": "math",
        "subcategory": "basic",
        "api_endpoint": "/api/multiply",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "数值A"},
            {"name": "b", "type": "number", "required": True, "description": "数值B"}
        ],
        "icon": "x"
    },
    "divide": {
        "id": "divide",
        "name": "除法",
        "name_en": "Divide",
        "description": "两数相除",
        "category": "math",
        "subcategory": "basic",
        "api_endpoint": "/api/divide",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "数值A"},
            {"name": "b", "type": "number", "required": True, "description": "数值B"}
        ],
        "icon": "divide"
    },
    "modulo": {
        "id": "modulo",
        "name": "取模",
        "name_en": "Modulo",
        "description": "取模运算",
        "category": "math",
        "subcategory": "basic",
        "api_endpoint": "/api/modulo",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "数值A"},
            {"name": "b", "type": "number", "required": True, "description": "数值B"}
        ],
        "icon": "percent"
    },
    "is_even": {
        "id": "is_even",
        "name": "偶数检查",
        "name_en": "Is Even",
        "description": "检查是否为偶数",
        "category": "math",
        "subcategory": "check",
        "api_endpoint": "/api/is-even",
        "method": "POST",
        "params": [
            {"name": "value", "type": "number", "required": True, "description": "数值"}
        ],
        "icon": "check-circle"
    },
    "is_odd": {
        "id": "is_odd",
        "name": "奇数检查",
        "name_en": "Is Odd",
        "description": "检查是否为奇数",
        "category": "math",
        "subcategory": "check",
        "api_endpoint": "/api/is-odd",
        "method": "POST",
        "params": [
            {"name": "value", "type": "number", "required": True, "description": "数值"}
        ],
        "icon": "check-circle"
    },
    "is_positive": {
        "id": "is_positive",
        "name": "正数检查",
        "name_en": "Is Positive",
        "description": "检查是否为正数",
        "category": "math",
        "subcategory": "check",
        "api_endpoint": "/api/is-positive",
        "method": "POST",
        "params": [
            {"name": "value", "type": "number", "required": True, "description": "数值"}
        ],
        "icon": "check-circle"
    },
    "is_negative": {
        "id": "is_negative",
        "name": "负数检查",
        "name_en": "Is Negative",
        "description": "检查是否为负数",
        "category": "math",
        "subcategory": "check",
        "api_endpoint": "/api/is-negative",
        "method": "POST",
        "params": [
            {"name": "value", "type": "number", "required": True, "description": "数值"}
        ],
        "icon": "check-circle"
    },
    "is_zero": {
        "id": "is_zero",
        "name": "零检查",
        "name_en": "Is Zero",
        "description": "检查是否为零",
        "category": "math",
        "subcategory": "check",
        "api_endpoint": "/api/is-zero",
        "method": "POST",
        "params": [
            {"name": "value", "type": "number", "required": True, "description": "数值"}
        ],
        "icon": "check-circle"
    },
    "between": {
        "id": "between",
        "name": "范围检查",
        "name_en": "Between",
        "description": "检查值是否在范围内",
        "category": "math",
        "subcategory": "check",
        "api_endpoint": "/api/between",
        "method": "POST",
        "params": [
            {"name": "value", "type": "number", "required": True, "description": "数值"},
            {"name": "min", "type": "number", "required": True, "description": "最小值"},
            {"name": "max", "type": "number", "required": True, "description": "最大值"}
        ],
        "icon": "check-circle"
    },
    "abs_diff": {
        "id": "abs_diff",
        "name": "绝对差",
        "name_en": "Absolute Difference",
        "description": "计算两个数的绝对差",
        "category": "math",
        "subcategory": "advanced",
        "api_endpoint": "/api/abs-diff",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "数值A"},
            {"name": "b", "type": "number", "required": True, "description": "数值B"}
        ],
        "icon": "minus"
    },
    "is_blank": {
        "id": "is_blank",
        "name": "空白检查",
        "name_en": "Is Blank",
        "description": "检查字符串是否空白",
        "category": "text",
        "subcategory": "check",
        "api_endpoint": "/api/is-blank",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "check-circle"
    },
    "is_alpha": {
        "id": "is_alpha",
        "name": "字母检查",
        "name_en": "Is Alpha",
        "description": "检查是否全为字母",
        "category": "text",
        "subcategory": "check",
        "api_endpoint": "/api/is-alpha",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "check-circle"
    },
    "is_digit": {
        "id": "is_digit",
        "name": "数字检查",
        "name_en": "Is Digit",
        "description": "检查是否全为数字",
        "category": "text",
        "subcategory": "check",
        "api_endpoint": "/api/is-digit",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "check-circle"
    },
    "is_alphanumeric": {
        "id": "is_alphanumeric",
        "name": "字母数字检查",
        "name_en": "Is Alphanumeric",
        "description": "检查是否全为字母或数字",
        "category": "text",
        "subcategory": "check",
        "api_endpoint": "/api/is-alphanumeric",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "check-circle"
    },
    "swap_case": {
        "id": "swap_case",
        "name": "大小写互换",
        "name_en": "Swap Case",
        "description": "大写转小写,小写转大写",
        "category": "text",
        "subcategory": "case",
        "api_endpoint": "/api/swap-case",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "refresh-cw"
    },
    "title_case": {
        "id": "title_case",
        "name": "标题大写",
        "name_en": "Title Case",
        "description": "每个单词首字母大写",
        "category": "text",
        "subcategory": "case",
        "api_endpoint": "/api/title-case",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "type"
    },
    "parse_url": {
        "id": "parse_url",
        "name": "解析URL",
        "name_en": "Parse URL",
        "description": "解析URL各部分",
        "category": "web",
        "subcategory": "url",
        "api_endpoint": "/api/parse-url",
        "method": "POST",
        "params": [
            {"name": "url", "type": "string", "required": True, "description": "URL"}
        ],
        "icon": "link"
    },
    "build_url": {
        "id": "build_url",
        "name": "构建URL",
        "name_en": "Build URL",
        "description": "构建URL",
        "category": "web",
        "subcategory": "url",
        "api_endpoint": "/api/build-url",
        "method": "POST",
        "params": [
            {"name": "scheme", "type": "string", "required": True, "description": "协议"},
            {"name": "host", "type": "string", "required": True, "description": "主机"},
            {"name": "path", "type": "string", "required": False, "description": "路径"}
        ],
        "icon": "link"
    },
    "query_param": {
        "id": "query_param",
        "name": "获取查询参数",
        "name_en": "Query Param",
        "description": "从URL获取查询参数",
        "category": "web",
        "subcategory": "url",
        "api_endpoint": "/api/query-param",
        "method": "POST",
        "params": [
            {"name": "url", "type": "string", "required": True, "description": "URL"},
            {"name": "key", "type": "string", "required": True, "description": "参数名"}
        ],
        "icon": "search"
    },
    "add_query_param": {
        "id": "add_query_param",
        "name": "添加查询参数",
        "name_en": "Add Query Param",
        "description": "向URL添加查询参数",
        "category": "web",
        "subcategory": "url",
        "api_endpoint": "/api/add-query",
        "method": "POST",
        "params": [
            {"name": "url", "type": "string", "required": True, "description": "URL"},
            {"name": "key", "type": "string", "required": True, "description": "参数名"},
            {"name": "value", "type": "string", "required": True, "description": "参数值"}
        ],
        "icon": "plus"
    },
    "strip_tags": {
        "id": "strip_tags",
        "name": "去除所有标签",
        "name_en": "Strip Tags",
        "description": "去除HTML所有标签",
        "category": "text",
        "subcategory": "clean",
        "api_endpoint": "/api/strip-tags",
        "method": "POST",
        "params": [
            {"name": "html", "type": "string", "required": True, "description": "HTML文本"}
        ],
        "icon": "code"
    },
    "escape_html": {
        "id": "escape_html",
        "name": "HTML转义",
        "name_en": "Escape HTML",
        "description": "HTML特殊字符转义",
        "category": "text",
        "subcategory": "escape",
        "api_endpoint": "/api/escape-html",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "code"
    },
    "unescape_html": {
        "id": "unescape_html",
        "name": "HTML反转义",
        "name_en": "Unescape HTML",
        "description": "HTML实体反转义",
        "category": "text",
        "subcategory": "escape",
        "api_endpoint": "/api/unescape-html",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "HTML文本"}
        ],
        "icon": "code"
    },
    "camel_to_snake": {
        "id": "camel_to_snake",
        "name": "驼峰转蛇形",
        "name_en": "Camel to Snake",
        "description": "驼峰命名转蛇形命名",
        "category": "text",
        "subcategory": "case",
        "api_endpoint": "/api/camel-to-snake",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "驼峰文本"}
        ],
        "icon": "refresh-cw"
    },
    "snake_to_camel": {
        "id": "snake_to_camel",
        "name": "蛇形转驼峰",
        "name_en": "Snake to Camel",
        "description": "蛇形命名转驼峰命名",
        "category": "text",
        "subcategory": "case",
        "api_endpoint": "/api/snake-to-camel",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "蛇形文本"}
        ],
        "icon": "refresh-cw"
    },
    "kebab_to_camel": {
        "id": "kebab_to_camel",
        "name": "串式转驼峰",
        "name_en": "Kebab to Camel",
        "description": "串式命名转驼峰命名",
        "category": "text",
        "subcategory": "case",
        "api_endpoint": "/api/kebab-to-camel",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "串式文本"}
        ],
        "icon": "refresh-cw"
    },
    "pluralize": {
        "id": "pluralize",
        "name": "复数化",
        "name_en": "Pluralize",
        "description": "单词复数化",
        "category": "text",
        "subcategory": "format",
        "api_endpoint": "/api/pluralize",
        "method": "POST",
        "params": [
            {"name": "word", "type": "string", "required": True, "description": "单词"}
        ],
        "icon": "type"
    },
    "singularize": {
        "id": "singularize",
        "name": "单数化",
        "name_en": "Singularize",
        "description": "单词单数化",
        "category": "text",
        "subcategory": "format",
        "api_endpoint": "/api/singularize",
        "method": "POST",
        "params": [
            {"name": "word", "type": "string", "required": True, "description": "单词"}
        ],
        "icon": "type"
    },
    "uuid4": {
        "id": "uuid4",
        "name": "UUID4生成",
        "name_en": "UUID4 Generate",
        "description": "生成UUID4",
        "category": "random",
        "subcategory": "uuid",
        "api_endpoint": "/api/uuid4",
        "method": "POST",
        "params": [],
        "icon": "hash"
    },
    "nanoid": {
        "id": "nanoid",
        "name": "NanoID生成",
        "name_en": "NanoID Generate",
        "description": "生成NanoID",
        "category": "random",
        "subcategory": "id",
        "api_endpoint": "/api/nanoid",
        "method": "POST",
        "params": [
            {"name": "length", "type": "number", "required": False, "description": "长度"}
        ],
        "icon": "hash"
    },
    "chunk_array": {
        "id": "chunk_array",
        "name": "数组分块",
        "name_en": "Chunk Array",
        "description": "将数组分成指定大小的块",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/chunk-array",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "size", "type": "number", "required": True, "description": "块大小"}
        ],
        "icon": "grid"
    },
    "flatten_once": {
        "id": "flatten_once",
        "name": "扁平化一层",
        "name_en": "Flatten Once",
        "description": "只扁平化一层嵌套",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/flatten-once",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "嵌套数组"}
        ],
        "icon": "minimize-2"
    },
    "deep_flatten": {
        "id": "deep_flatten",
        "name": "深度扁平化",
        "name_en": "Deep Flatten",
        "description": "完全扁平化嵌套数组",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/deep-flatten",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "嵌套数组"}
        ],
        "icon": "minimize"
    },
    "unique_by": {
        "id": "unique_by",
        "name": "按键去重",
        "name_en": "Unique By",
        "description": "按指定键去重",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/unique-by",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "key", "type": "string", "required": True, "description": "键名"}
        ],
        "icon": "filter"
    },
    "sort_by": {
        "id": "sort_by",
        "name": "按键排序",
        "name_en": "Sort By",
        "description": "按指定键排序",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/sort-by",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "key", "type": "string", "required": True, "description": "键名"}
        ],
        "icon": "arrow-up-down"
    },
    "group_by_key": {
        "id": "group_by_key",
        "name": "按键分组",
        "name_en": "Group By Key",
        "description": "按键分组数组",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/group-by-key",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "key", "type": "string", "required": True, "description": "键名"}
        ],
        "icon": "folder"
    },
    "pluck": {
        "id": "pluck",
        "name": "提取键值",
        "name_en": "Pluck",
        "description": "提取数组中每个对象的指定键值",
        "category": "array",
        "subcategory": "access",
        "api_endpoint": "/api/pluck",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "对象数组"},
            {"name": "key", "type": "string", "required": True, "description": "键名"}
        ],
        "icon": "list"
    },
    "pick": {
        "id": "pick",
        "name": "选择键",
        "name_en": "Pick",
        "description": "从对象中选择指定键",
        "category": "object",
        "subcategory": "transform",
        "api_endpoint": "/api/pick",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "对象"},
            {"name": "keys", "type": "array", "required": True, "description": "键数组"}
        ],
        "icon": "check-square"
    },
    "omit": {
        "id": "omit",
        "name": "排除键",
        "name_en": "Omit",
        "description": "排除对象中的指定键",
        "category": "object",
        "subcategory": "transform",
        "api_endpoint": "/api/omit",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "对象"},
            {"name": "keys", "type": "array", "required": True, "description": "键数组"}
        ],
        "icon": "x-square"
    },
    "has_key": {
        "id": "has_key",
        "name": "键存在检查",
        "name_en": "Has Key",
        "description": "检查对象是否有指定键",
        "category": "object",
        "subcategory": "check",
        "api_endpoint": "/api/has-key",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "对象"},
            {"name": "key", "type": "string", "required": True, "description": "键名"}
        ],
        "icon": "check-circle"
    },
    "invert": {
        "id": "invert",
        "name": "反转对象",
        "name_en": "Invert",
        "description": "反转对象的键值",
        "category": "object",
        "subcategory": "transform",
        "api_endpoint": "/api/invert",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "对象"}
        ],
        "icon": "refresh-cw"
    },
    "map_values": {
        "id": "map_values",
        "name": "映射值",
        "name_en": "Map Values",
        "description": "对对象每个值应用函数",
        "category": "object",
        "subcategory": "transform",
        "api_endpoint": "/api/map-values",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "对象"},
            {"name": "fn", "type": "string", "required": True, "description": "函数"}
        ],
        "icon": "map"
    },
    "map_keys": {
        "id": "map_keys",
        "name": "映射键",
        "name_en": "Map Keys",
        "description": "对对象每个键应用函数",
        "category": "object",
        "subcategory": "transform",
        "api_endpoint": "/api/map-keys",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "对象"},
            {"name": "fn", "type": "string", "required": True, "description": "函数"}
        ],
        "icon": "map"
    },
    "size": {
        "id": "size",
        "name": "大小",
        "name_en": "Size",
        "description": "获取对象或数组大小",
        "category": "utility",
        "subcategory": "property",
        "api_endpoint": "/api/size",
        "method": "POST",
        "params": [
            {"name": "item", "type": "string", "required": True, "description": "对象或数组"}
        ],
        "icon": "hash"
    },
    "add_days": {
        "id": "add_days",
        "name": "加天数",
        "name_en": "Add Days",
        "description": "日期加天数",
        "category": "date",
        "subcategory": "add",
        "api_endpoint": "/api/add-days",
        "method": "POST",
        "params": [
            {"name": "date", "type": "string", "required": True, "description": "日期"},
            {"name": "days", "type": "number", "required": True, "description": "天数"}
        ],
        "icon": "plus"
    },
    "sub_days": {
        "id": "sub_days",
        "name": "减天数",
        "name_en": "Sub Days",
        "description": "日期减天数",
        "category": "date",
        "subcategory": "sub",
        "api_endpoint": "/api/sub-days",
        "method": "POST",
        "params": [
            {"name": "date", "type": "string", "required": True, "description": "日期"},
            {"name": "days", "type": "number", "required": True, "description": "天数"}
        ],
        "icon": "minus"
    },
    "days_diff": {
        "id": "days_diff",
        "name": "天数差",
        "name_en": "Days Difference",
        "description": "计算两个日期的天数差",
        "category": "date",
        "subcategory": "diff",
        "api_endpoint": "/api/days-diff",
        "method": "POST",
        "params": [
            {"name": "date1", "type": "string", "required": True, "description": "日期1"},
            {"name": "date2", "type": "string", "required": True, "description": "日期2"}
        ],
        "icon": "minus"
    },
    "start_of_day": {
        "id": "start_of_day",
        "name": "日开始",
        "name_en": "Start of Day",
        "description": "获取日期开始时刻",
        "category": "date",
        "subcategory": "boundary",
        "api_endpoint": "/api/start-of-day",
        "method": "POST",
        "params": [
            {"name": "date", "type": "string", "required": True, "description": "日期"}
        ],
        "icon": "sunrise"
    },
    "end_of_day": {
        "id": "end_of_day",
        "name": "日结束",
        "name_en": "End of Day",
        "description": "获取日期结束时刻",
        "category": "date",
        "subcategory": "boundary",
        "api_endpoint": "/api/end-of-day",
        "method": "POST",
        "params": [
            {"name": "date", "type": "string", "required": True, "description": "日期"}
        ],
        "icon": "sunset"
    },
    "start_of_week": {
        "id": "start_of_week",
        "name": "周开始",
        "name_en": "Start of Week",
        "description": "获取周开始日期",
        "category": "date",
        "subcategory": "boundary",
        "api_endpoint": "/api/start-of-week",
        "method": "POST",
        "params": [
            {"name": "date", "type": "string", "required": True, "description": "日期"}
        ],
        "icon": "calendar"
    },
    "start_of_month": {
        "id": "start_of_month",
        "name": "月开始",
        "name_en": "Start of Month",
        "description": "获取月开始日期",
        "category": "date",
        "subcategory": "boundary",
        "api_endpoint": "/api/start-of-month",
        "method": "POST",
        "params": [
            {"name": "date", "type": "string", "required": True, "description": "日期"}
        ],
        "icon": "calendar"
    },
    "end_of_month": {
        "id": "end_of_month",
        "name": "月结束",
        "name_en": "End of Month",
        "description": "获取月结束日期",
        "category": "date",
        "subcategory": "boundary",
        "api_endpoint": "/api/end-of-month",
        "method": "POST",
        "params": [
            {"name": "date", "type": "string", "required": True, "description": "日期"}
        ],
        "icon": "calendar"
    },
    "quarter": {
        "id": "quarter",
        "name": "季度",
        "name_en": "Quarter",
        "description": "获取日期所在季度",
        "category": "date",
        "subcategory": "extract",
        "api_endpoint": "/api/quarter",
        "method": "POST",
        "params": [
            {"name": "date", "type": "string", "required": True, "description": "日期"}
        ],
        "icon": "calendar"
    },
    "week_of_year": {
        "id": "week_of_year",
        "name": "年周数",
        "name_en": "Week of Year",
        "description": "获取日期所在年周数",
        "category": "date",
        "subcategory": "extract",
        "api_endpoint": "/api/week-of-year",
        "method": "POST",
        "params": [
            {"name": "date", "type": "string", "required": True, "description": "日期"}
        ],
        "icon": "calendar"
    },
    "is_weekday": {
        "id": "is_weekday",
        "name": "工作日检查",
        "name_en": "Is Weekday",
        "description": "检查是否为工作日",
        "category": "date",
        "subcategory": "check",
        "api_endpoint": "/api/is-weekday",
        "method": "POST",
        "params": [
            {"name": "date", "type": "string", "required": True, "description": "日期"}
        ],
        "icon": "check-circle"
    },
    "is_weekend": {
        "id": "is_weekend",
        "name": "周末检查",
        "name_en": "Is Weekend",
        "description": "检查是否为周末",
        "category": "date",
        "subcategory": "check",
        "api_endpoint": "/api/is-weekend",
        "method": "POST",
        "params": [
            {"name": "date", "type": "string", "required": True, "description": "日期"}
        ],
        "icon": "check-circle"
    },
    "days_in_month": {
        "id": "days_in_month",
        "name": "月天数",
        "name_en": "Days in Month",
        "description": "获取月份天数",
        "category": "date",
        "subcategory": "extract",
        "api_endpoint": "/api/days-in-month",
        "method": "POST",
        "params": [
            {"name": "year", "type": "number", "required": True, "description": "年份"},
            {"name": "month", "type": "number", "required": True, "description": "月份"}
        ],
        "icon": "calendar"
    },
    "hash_md5": {
        "id": "hash_md5",
        "name": "MD5哈希",
        "name_en": "MD5 Hash",
        "description": "生成MD5哈希",
        "category": "security",
        "subcategory": "hash",
        "api_endpoint": "/api/hash/md5",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "lock"
    },
    "hash_sha1": {
        "id": "hash_sha1",
        "name": "SHA1哈希",
        "name_en": "SHA1 Hash",
        "description": "生成SHA1哈希",
        "category": "security",
        "subcategory": "hash",
        "api_endpoint": "/api/hash/sha1",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "lock"
    },
    "hash_sha256": {
        "id": "hash_sha256",
        "name": "SHA256哈希",
        "name_en": "SHA256 Hash",
        "description": "生成SHA256哈希",
        "category": "security",
        "subcategory": "hash",
        "api_endpoint": "/api/hash/sha256",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "lock"
    },
    "bcrypt_hash": {
        "id": "bcrypt_hash",
        "name": "Bcrypt哈希",
        "name_en": "Bcrypt Hash",
        "description": "生成Bcrypt哈希",
        "category": "security",
        "subcategory": "hash",
        "api_endpoint": "/api/hash/bcrypt",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "lock"
    },
    "verify_hash": {
        "id": "verify_hash",
        "name": "验证哈希",
        "name_en": "Verify Hash",
        "description": "验证哈希是否匹配",
        "category": "security",
        "subcategory": "verify",
        "api_endpoint": "/api/verify-hash",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "hash", "type": "string", "required": True, "description": "哈希值"}
        ],
        "icon": "check-circle"
    },
    "generate_token": {
        "id": "generate_token",
        "name": "生成令牌",
        "name_en": "Generate Token",
        "description": "生成随机令牌",
        "category": "security",
        "subcategory": "token",
        "api_endpoint": "/api/generate-token",
        "method": "POST",
        "params": [
            {"name": "length", "type": "number", "required": False, "description": "长度"}
        ],
        "icon": "key"
    },
    "celsius_to_fahrenheit": {
        "id": "celsius_to_fahrenheit",
        "name": "摄氏度转华氏度",
        "name_en": "Celsius to Fahrenheit",
        "description": "温度单位转换",
        "category": "convert",
        "subcategory": "temperature",
        "api_endpoint": "/api/celsius-to-fahrenheit",
        "method": "POST",
        "params": [
            {"name": "celsius", "type": "number", "required": True, "description": "摄氏度"}
        ],
        "icon": "thermometer"
    },
    "fahrenheit_to_celsius": {
        "id": "fahrenheit_to_celsius",
        "name": "华氏度转摄氏度",
        "name_en": "Fahrenheit to Celsius",
        "description": "温度单位转换",
        "category": "convert",
        "subcategory": "temperature",
        "api_endpoint": "/api/fahrenheit-to-celsius",
        "method": "POST",
        "params": [
            {"name": "fahrenheit", "type": "number", "required": True, "description": "华氏度"}
        ],
        "icon": "thermometer"
    },
    "km_to_miles": {
        "id": "km_to_miles",
        "name": "公里转英里",
        "name_en": "Km to Miles",
        "description": "距离单位转换",
        "category": "convert",
        "subcategory": "distance",
        "api_endpoint": "/api/km-to-miles",
        "method": "POST",
        "params": [
            {"name": "km", "type": "number", "required": True, "description": "公里"}
        ],
        "icon": "map"
    },
    "miles_to_km": {
        "id": "miles_to_km",
        "name": "英里转公里",
        "name_en": "Miles to Km",
        "description": "距离单位转换",
        "category": "convert",
        "subcategory": "distance",
        "api_endpoint": "/api/miles-to-km",
        "method": "POST",
        "params": [
            {"name": "miles", "type": "number", "required": True, "description": "英里"}
        ],
        "icon": "map"
    },
    "kg_to_pounds": {
        "id": "kg_to_pounds",
        "name": "公斤转磅",
        "name_en": "Kg to Pounds",
        "description": "重量单位转换",
        "category": "convert",
        "subcategory": "weight",
        "api_endpoint": "/api/kg-to-pounds",
        "method": "POST",
        "params": [
            {"name": "kg", "type": "number", "required": True, "description": "公斤"}
        ],
        "icon": "scale"
    },
    "pounds_to_kg": {
        "id": "pounds_to_kg",
        "name": "磅转公斤",
        "name_en": "Pounds to Kg",
        "description": "重量单位转换",
        "category": "convert",
        "subcategory": "weight",
        "api_endpoint": "/api/pounds-to-kg",
        "method": "POST",
        "params": [
            {"name": "pounds", "type": "number", "required": True, "description": "磅"}
        ],
        "icon": "scale"
    },
    "bytes_to_human": {
        "id": "bytes_to_human",
        "name": "字节转人类可读",
        "name_en": "Bytes to Human",
        "description": "字节数转人类可读格式",
        "category": "convert",
        "subcategory": "bytes",
        "api_endpoint": "/api/bytes-to-human",
        "method": "POST",
        "params": [
            {"name": "bytes", "type": "number", "required": True, "description": "字节数"}
        ],
        "icon": "file"
    },
    "intersperse": {
        "id": "intersperse",
        "name": "插入分隔符",
        "name_en": "Intersperse",
        "description": "在元素间插入分隔符",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/intersperse",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "separator", "type": "string", "required": True, "description": "分隔符"}
        ],
        "icon": "plus"
    },
    "interleave": {
        "id": "interleave",
        "name": "交错合并",
        "name_en": "Interleave",
        "description": "交错合并多个数组",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/interleave",
        "method": "POST",
        "params": [
            {"name": "arrays", "type": "array", "required": True, "description": "数组数组"}
        ],
        "icon": "columns"
    },
    "zip_with_index": {
        "id": "zip_with_index",
        "name": "带索引合并",
        "name_en": "Zip with Index",
        "description": "数组元素与索引配对",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/zip-with-index",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "start", "type": "number", "required": False, "description": "起始索引"}
        ],
        "icon": "list"
    },
    "scan": {
        "id": "scan",
        "name": "扫描累加",
        "name_en": "Scan",
        "description": "扫描累加数组元素",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/scan",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "git_merge"
    },
    "iterate": {
        "id": "iterate",
        "name": "迭代生成",
        "name_en": "Iterate",
        "description": "迭代生成数组",
        "category": "array",
        "subcategory": "generate",
        "api_endpoint": "/api/iterate",
        "method": "POST",
        "params": [
            {"name": "fn", "type": "string", "required": True, "description": "函数"},
            {"name": "initial", "type": "string", "required": True, "description": "初始值"},
            {"name": "count", "type": "number", "required": True, "description": "数量"}
        ],
        "icon": "repeat"
    },
    "unzip": {
        "id": "unzip",
        "name": "解压",
        "name_en": "Unzip",
        "description": "解压配对数组",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/unzip",
        "method": "POST",
        "params": [
            {"name": "pairs", "type": "array", "required": True, "description": "配对数组"}
        ],
        "icon": "unlock"
    },
    "append_any": {
        "id": "append_any",
        "name": "批量追加",
        "name_en": "Append Any",
        "description": "批量追加元素到数组",
        "category": "array",
        "subcategory": "modify",
        "api_endpoint": "/api/append-any",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "new_items", "type": "array", "required": True, "description": "新元素"}
        ],
        "icon": "plus"
    },
    "sample": {
        "id": "sample",
        "name": "随机抽样",
        "name_en": "Sample",
        "description": "从数组中随机抽样",
        "category": "array",
        "subcategory": "random",
        "api_endpoint": "/api/sample",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "count", "type": "number", "required": True, "description": "数量"}
        ],
        "icon": "shuffle"
    },
    "shuffle_copy": {
        "id": "shuffle_copy",
        "name": "随机打乱副本",
        "name_en": "Shuffle Copy",
        "description": "返回打乱后的数组副本",
        "category": "array",
        "subcategory": "random",
        "api_endpoint": "/api/shuffle-copy",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "shuffle"
    },
    "random_ints": {
        "id": "random_ints",
        "name": "随机整数数组",
        "name_en": "Random Integers",
        "description": "生成随机整数数组",
        "category": "array",
        "subcategory": "generate",
        "api_endpoint": "/api/random-ints",
        "method": "POST",
        "params": [
            {"name": "count", "type": "number", "required": True, "description": "数量"},
            {"name": "min", "type": "number", "required": False, "description": "最小值"},
            {"name": "max", "type": "number", "required": False, "description": "最大值"}
        ],
        "icon": "hash"
    },
    "range_step": {
        "id": "range_step",
        "name": "带步长范围",
        "name_en": "Range with Step",
        "description": "生成带步长的数字范围",
        "category": "array",
        "subcategory": "generate",
        "api_endpoint": "/api/range-step",
        "method": "POST",
        "params": [
            {"name": "start", "type": "number", "required": True, "description": "起始"},
            {"name": "end", "type": "number", "required": True, "description": "结束"},
            {"name": "step", "type": "number", "required": False, "description": "步长"}
        ],
        "icon": "list"
    },
    "repeat_array": {
        "id": "repeat_array",
        "name": "重复数组",
        "name_en": "Repeat Array",
        "description": "重复数组N次",
        "category": "array",
        "subcategory": "generate",
        "api_endpoint": "/api/repeat-array",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "count", "type": "number", "required": True, "description": "重复次数"}
        ],
        "icon": "copy"
    },
    "reverse_copy": {
        "id": "reverse_copy",
        "name": "反转副本",
        "name_en": "Reverse Copy",
        "description": "返回反转后的数组副本",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/reverse-copy",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "rotate-ccw"
    },
    "sum_array": {
        "id": "sum_array",
        "name": "数组求和",
        "name_en": "Array Sum",
        "description": "数组元素求和",
        "category": "array",
        "subcategory": "aggregate",
        "api_endpoint": "/api/sum-array",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "plus"
    },
    "avg_array": {
        "id": "avg_array",
        "name": "数组平均值",
        "name_en": "Array Average",
        "description": "计算数组平均值",
        "category": "array",
        "subcategory": "aggregate",
        "api_endpoint": "/api/avg-array",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "divide"
    },
    "min_array": {
        "id": "min_array",
        "name": "数组最小值",
        "name_en": "Array Min",
        "description": "获取数组最小值",
        "category": "array",
        "subcategory": "aggregate",
        "api_endpoint": "/api/min-array",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "arrow-down"
    },
    "max_array": {
        "id": "max_array",
        "name": "数组最大值",
        "name_en": "Array Max",
        "description": "获取数组最大值",
        "category": "array",
        "subcategory": "aggregate",
        "api_endpoint": "/api/max-array",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "arrow-up"
    },
    "count_array": {
        "id": "count_array",
        "name": "数组长度",
        "name_en": "Array Count",
        "description": "获取数组长度",
        "category": "array",
        "subcategory": "property",
        "api_endpoint": "/api/count-array",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "hash"
    },
    "first_n": {
        "id": "first_n",
        "name": "前N个",
        "name_en": "First N",
        "description": "获取前N个元素",
        "category": "array",
        "subcategory": "access",
        "api_endpoint": "/api/first-n",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "n", "type": "number", "required": True, "description": "数量"}
        ],
        "icon": "arrow-right"
    },
    "last_n": {
        "id": "last_n",
        "name": "后N个",
        "name_en": "Last N",
        "description": "获取后N个元素",
        "category": "array",
        "subcategory": "access",
        "api_endpoint": "/api/last-n",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "n", "type": "number", "required": True, "description": "数量"}
        ],
        "icon": "arrow-left"
    },
    "drop_n": {
        "id": "drop_n",
        "name": "丢弃前N个",
        "name_en": "Drop First N",
        "description": "丢弃前N个元素",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/drop-n",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "n", "type": "number", "required": True, "description": "数量"}
        ],
        "icon": "arrow-right"
    },
    "product_array": {
        "id": "product_array",
        "name": "数组连乘",
        "name_en": "Array Product",
        "description": "数组元素连乘",
        "category": "array",
        "subcategory": "aggregate",
        "api_endpoint": "/api/product-array",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "x"
    },
    "variance_array": {
        "id": "variance_array",
        "name": "数组方差",
        "name_en": "Array Variance",
        "description": "计算数组方差",
        "category": "array",
        "subcategory": "aggregate",
        "api_endpoint": "/api/variance-array",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "bar-chart"
    },
    "stddev_array": {
        "id": "stddev_array",
        "name": "数组标准差",
        "name_en": "Array StdDev",
        "description": "计算数组标准差",
        "category": "array",
        "subcategory": "aggregate",
        "api_endpoint": "/api/stddev-array",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "bar-chart"
    },
    "median_array": {
        "id": "median_array",
        "name": "数组中位数",
        "name_en": "Array Median",
        "description": "计算数组中位数",
        "category": "array",
        "subcategory": "aggregate",
        "api_endpoint": "/api/median-array",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "bar-chart"
    },
    "mode_array": {
        "id": "mode_array",
        "name": "数组众数",
        "name_en": "Array Mode",
        "description": "计算数组众数",
        "category": "array",
        "subcategory": "aggregate",
        "api_endpoint": "/api/mode-array",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "bar-chart"
    },
    "percentile_array": {
        "id": "percentile_array",
        "name": "数组百分位数",
        "name_en": "Array Percentile",
        "description": "计算数组百分位数",
        "category": "array",
        "subcategory": "aggregate",
        "api_endpoint": "/api/percentile-array",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "p", "type": "number", "required": True, "description": "百分比"}
        ],
        "icon": "bar-chart"
    },
    "cumsum": {
        "id": "cumsum",
        "name": "累积和",
        "name_en": "Cumulative Sum",
        "description": "计算累积和",
        "category": "array",
        "subcategory": "aggregate",
        "api_endpoint": "/api/cumsum",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "plus"
    },
    "differences": {
        "id": "differences",
        "name": "差分",
        "name_en": "Differences",
        "description": "计算差分",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/differences",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "minus"
    },
    "shift": {
        "id": "shift",
        "name": "移位",
        "name_en": "Shift",
        "description": "数组元素移位",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/shift",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "by", "type": "number", "required": False, "description": "移位数"}
        ],
        "icon": "arrow-right"
    },
    "is_unique": {
        "id": "is_unique",
        "name": "是否唯一",
        "name_en": "Is Unique",
        "description": "检查数组是否所有元素唯一",
        "category": "array",
        "subcategory": "check",
        "api_endpoint": "/api/is-unique",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "check-circle"
    },
    "has_duplicates": {
        "id": "has_duplicates",
        "name": "是否有重复",
        "name_en": "Has Duplicates",
        "description": "检查数组是否有重复元素",
        "category": "array",
        "subcategory": "check",
        "api_endpoint": "/api/has-duplicates",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "check-circle"
    },
    "duplicates": {
        "id": "duplicates",
        "name": "查找重复",
        "name_en": "Find Duplicates",
        "description": "查找数组中的重复元素",
        "category": "array",
        "subcategory": "search",
        "api_endpoint": "/api/duplicates",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "copy"
    },
    "without": {
        "id": "without",
        "name": "排除元素",
        "name_en": "Without",
        "description": "排除数组中的指定元素",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/without",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "values", "type": "array", "required": True, "description": "要排除的值"}
        ],
        "icon": "minus"
    },
    "flatten_deep": {
        "id": "flatten_deep",
        "name": "深度扁平化",
        "name_en": "Deep Flatten",
        "description": "深度扁平化嵌套数组",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/flatten-deep",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "嵌套数组"}
        ],
        "icon": "minimize"
    },
    "chunk_overlap": {
        "id": "chunk_overlap",
        "name": "重叠分块",
        "name_en": "Chunk with Overlap",
        "description": "分块且有重叠",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/chunk-overlap",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "size", "type": "number", "required": True, "description": "块大小"},
            {"name": "overlap", "type": "number", "required": False, "description": "重叠数"}
        ],
        "icon": "grid"
    },
    "split_every": {
        "id": "split_every",
        "name": "等分切割",
        "name_en": "Split Every",
        "description": "每N个元素切割一次",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/split-every",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "n", "type": "number", "required": True, "description": "每N个"}
        ],
        "icon": "scissors"
    },
    "zip_all": {
        "id": "zip_all",
        "name": "填充合并",
        "name_en": "Zip All",
        "description": "合并多个数组，缺失填充",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/zip-all",
        "method": "POST",
        "params": [
            {"name": "arrays", "type": "array", "required": True, "description": "数组数组"},
            {"name": "fill", "type": "string", "required": False, "description": "填充值"}
        ],
        "icon": "columns"
    },
    "count_occurrences": {
        "id": "count_occurrences",
        "name": "计数出现",
        "name_en": "Count Occurrences",
        "description": "统计元素出现次数",
        "category": "array",
        "subcategory": "aggregate",
        "api_endpoint": "/api/count-occurrences",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "hash"
    },
    "frequency": {
        "id": "frequency",
        "name": "频率分布",
        "name_en": "Frequency Distribution",
        "description": "计算频率分布",
        "category": "array",
        "subcategory": "aggregate",
        "api_endpoint": "/api/frequency",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "bar-chart"
    },
    "frequencies": {
        "id": "frequencies",
        "name": "频率字典",
        "name_en": "Frequencies",
        "description": "返回频率字典",
        "category": "array",
        "subcategory": "aggregate",
        "api_endpoint": "/api/frequencies",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "list"
    },
    "most_frequent": {
        "id": "most_frequent",
        "name": "最频繁",
        "name_en": "Most Frequent",
        "description": "获取最频繁的元素",
        "category": "array",
        "subcategory": "aggregate",
        "api_endpoint": "/api/most-frequent",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "n", "type": "number", "required": False, "description": "数量"}
        ],
        "icon": "star"
    },
    "least_frequent": {
        "id": "least_frequent",
        "name": "最不频繁",
        "name_en": "Least Frequent",
        "description": "获取最不频繁的元素",
        "category": "array",
        "subcategory": "aggregate",
        "api_endpoint": "/api/least-frequent",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "n", "type": "number", "required": False, "description": "数量"}
        ],
        "icon": "star"
    },
    "sort_by_key": {
        "id": "sort_by_key",
        "name": "按键排序",
        "name_en": "Sort by Key",
        "description": "按指定键排序对象数组",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/sort-by-key",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "对象数组"},
            {"name": "key", "type": "string", "required": True, "description": "键名"},
            {"name": "reverse", "type": "boolean", "required": False, "description": "降序"}
        ],
        "icon": "arrow-up-down"
    },
    "index_where": {
        "id": "index_where",
        "name": "查找索引",
        "name_en": "Index Where",
        "description": "查找满足条件的第一个索引",
        "category": "array",
        "subcategory": "search",
        "api_endpoint": "/api/index-where",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "search"
    },
    "find_index": {
        "id": "find_index",
        "name": "查找所有索引",
        "name_en": "Find All Indexes",
        "description": "查找所有满足条件的索引",
        "category": "array",
        "subcategory": "search",
        "api_endpoint": "/api/find-index",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "value", "type": "string", "required": True, "description": "值"}
        ],
        "icon": "search"
    },
    "any_match": {
        "id": "any_match",
        "name": "任意匹配",
        "name_en": "Any Match",
        "description": "检查是否有任意元素满足条件",
        "category": "array",
        "subcategory": "check",
        "api_endpoint": "/api/any-match",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "check-square"
    },
    "all_match": {
        "id": "all_match",
        "name": "全部匹配",
        "name_en": "All Match",
        "description": "检查是否所有元素都满足条件",
        "category": "array",
        "subcategory": "check",
        "api_endpoint": "/api/all-match",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "check-square"
    },
    "none_match": {
        "id": "none_match",
        "name": "无匹配",
        "name_en": "None Match",
        "description": "检查是否没有元素满足条件",
        "category": "array",
        "subcategory": "check",
        "api_endpoint": "/api/none-match",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "check-square"
    },
    "reject": {
        "id": "reject",
        "name": "拒绝元素",
        "name_en": "Reject",
        "description": "拒绝满足条件的元素",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/reject",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "filter"
    },
    "compact_array": {
        "id": "compact_array",
        "name": "紧凑数组",
        "name_en": "Compact Array",
        "description": "去除假值",
        "category": "array",
        "subcategory": "clean",
        "api_endpoint": "/api/compact-array",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "filter"
    },
    "every_nth": {
        "id": "every_nth",
        "name": "每N个取一个",
        "name_en": "Every Nth",
        "description": "每隔N个取一个元素",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/every-nth",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "n", "type": "number", "required": True, "description": "间隔"}
        ],
        "icon": "list"
    },
    "take_while": {
        "id": "take_while",
        "name": "条件取值",
        "name_en": "Take While",
        "description": "取满足条件的连续元素",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/take-while",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "arrow-right"
    },
    "drop_while": {
        "id": "drop_while",
        "name": "条件丢弃",
        "name_en": "Drop While",
        "description": "丢弃满足条件的连续元素",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/drop-while",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "arrow-right"
    },
    "key_by": {
        "id": "key_by",
        "name": "按键索引",
        "name_en": "Key By",
        "description": "按键索引数组元素",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/key-by",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "key", "type": "string", "required": True, "description": "键名"}
        ],
        "icon": "key"
    },
    "key_of": {
        "id": "key_of",
        "name": "值找键",
        "name_en": "Key Of",
        "description": "根据值查找键",
        "category": "object",
        "subcategory": "search",
        "api_endpoint": "/api/key-of",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "对象"},
            {"name": "value", "type": "string", "required": True, "description": "值"}
        ],
        "icon": "search"
    },
    "invert_map": {
        "id": "invert_map",
        "name": "反转映射",
        "name_en": "Invert Map",
        "description": "反转键值映射",
        "category": "object",
        "subcategory": "transform",
        "api_endpoint": "/api/invert-map",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "对象"}
        ],
        "icon": "refresh-cw"
    },
    "merge_all": {
        "id": "merge_all",
        "name": "合并全部",
        "name_en": "Merge All",
        "description": "合并所有对象",
        "category": "object",
        "subcategory": "transform",
        "api_endpoint": "/api/merge-all",
        "method": "POST",
        "params": [
            {"name": "objects", "type": "array", "required": True, "description": "对象数组"}
        ],
        "icon": "git_merge"
    },
    "deep_get": {
        "id": "deep_get",
        "name": "深度获取",
        "name_en": "Deep Get",
        "description": "获取嵌套属性",
        "category": "object",
        "subcategory": "access",
        "api_endpoint": "/api/deep-get",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "对象"},
            {"name": "path", "type": "string", "required": True, "description": "路径"}
        ],
        "icon": "key"
    },
    "deep_set": {
        "id": "deep_set",
        "name": "深度设置",
        "name_en": "Deep Set",
        "description": "设置嵌套属性",
        "category": "object",
        "subcategory": "transform",
        "api_endpoint": "/api/deep-set",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "对象"},
            {"name": "path", "type": "string", "required": True, "description": "路径"},
            {"name": "value", "type": "string", "required": True, "description": "值"}
        ],
        "icon": "edit"
    },
    "object_to_entries": {
        "id": "object_to_entries",
        "name": "对象转条目",
        "name_en": "Object to Entries",
        "description": "对象转换为键值对数组",
        "category": "object",
        "subcategory": "transform",
        "api_endpoint": "/api/object-to-entries",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "对象"}
        ],
        "icon": "list"
    },
    "entries_to_object": {
        "id": "entries_to_object",
        "name": "条目转对象",
        "name_en": "Entries to Object",
        "description": "键值对数组转换为对象",
        "category": "object",
        "subcategory": "transform",
        "api_endpoint": "/api/entries-to-object",
        "method": "POST",
        "params": [
            {"name": "entries", "type": "array", "required": True, "description": "键值对数组"}
        ],
        "icon": "list"
    },
    "is_even": {
        "id": "is_even",
        "name": "偶数",
        "name_en": "Is Even",
        "description": "检查是否偶数",
        "category": "math",
        "subcategory": "check",
        "api_endpoint": "/api/is-even",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "数字"}
        ],
        "icon": "check-circle"
    },
    "is_odd": {
        "id": "is_odd",
        "name": "奇数",
        "name_en": "Is Odd",
        "description": "检查是否奇数",
        "category": "math",
        "subcategory": "check",
        "api_endpoint": "/api/is-odd",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "数字"}
        ],
        "icon": "check-circle"
    },
    "is_integer": {
        "id": "is_integer",
        "name": "整数检查",
        "name_en": "Is Integer",
        "description": "检查是否为整数",
        "category": "math",
        "subcategory": "check",
        "api_endpoint": "/api/is-integer",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "数字"}
        ],
        "icon": "check-circle"
    },
    "is_decimal": {
        "id": "is_decimal",
        "name": "小数检查",
        "name_en": "Is Decimal",
        "description": "检查是否为小数",
        "category": "math",
        "subcategory": "check",
        "api_endpoint": "/api/is-decimal",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "数字"}
        ],
        "icon": "check-circle"
    },
    "is_multiple": {
        "id": "is_multiple",
        "name": "倍数检查",
        "name_en": "Is Multiple",
        "description": "检查是否为倍数",
        "category": "math",
        "subcategory": "check",
        "api_endpoint": "/api/is-multiple",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "数字"},
            {"name": "divisor", "type": "number", "required": True, "description": "除数"}
        ],
        "icon": "check-circle"
    },
    "round_to": {
        "id": "round_to",
        "name": "四舍五入到",
        "name_en": "Round To",
        "description": "四舍五入到指定位数",
        "category": "math",
        "subcategory": "transform",
        "api_endpoint": "/api/round-to",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "数字"},
            {"name": "decimals", "type": "number", "required": False, "description": "小数位数"}
        ],
        "icon": "hash"
    },
    "floor_to": {
        "id": "floor_to",
        "name": "向下取整到",
        "name_en": "Floor To",
        "description": "向下取整到指定位数",
        "category": "math",
        "subcategory": "transform",
        "api_endpoint": "/api/floor-to",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "数字"},
            {"name": "decimals", "type": "number", "required": False, "description": "小数位数"}
        ],
        "icon": "arrow-down"
    },
    "ceil_to": {
        "id": "ceil_to",
        "name": "向上取整到",
        "name_en": "Ceil To",
        "description": "向上取整到指定位数",
        "category": "math",
        "subcategory": "transform",
        "api_endpoint": "/api/ceil-to",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "数字"},
            {"name": "decimals", "type": "number", "required": False, "description": "小数位数"}
        ],
        "icon": "arrow-up"
    },
    "clamp_to": {
        "id": "clamp_to",
        "name": "限制到范围",
        "name_en": "Clamp To",
        "description": "将数字限制在指定范围内",
        "category": "math",
        "subcategory": "transform",
        "api_endpoint": "/api/clamp-to",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "数字"},
            {"name": "min", "type": "number", "required": True, "description": "最小值"},
            {"name": "max", "type": "number", "required": True, "description": "最大值"}
        ],
        "icon": "sliders"
    },
    "in_range": {
        "id": "in_range",
        "name": "在范围内",
        "name_en": "In Range",
        "description": "检查数字是否在范围内",
        "category": "math",
        "subcategory": "check",
        "api_endpoint": "/api/in-range",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "数字"},
            {"name": "min", "type": "number", "required": True, "description": "最小值"},
            {"name": "max", "type": "number", "required": True, "description": "最大值"}
        ],
        "icon": "check-circle"
    },
    "percentage_of": {
        "id": "percentage_of",
        "name": "百分比计算",
        "name_en": "Percentage Of",
        "description": "计算某数是另数的百分之几",
        "category": "math",
        "subcategory": "calculate",
        "api_endpoint": "/api/percentage-of",
        "method": "POST",
        "params": [
            {"name": "part", "type": "number", "required": True, "description": "部分"},
            {"name": "whole", "type": "number", "required": True, "description": "整体"}
        ],
        "icon": "percent"
    },
    "percentage_change": {
        "id": "percentage_change",
        "name": "百分比变化",
        "name_en": "Percentage Change",
        "description": "计算百分比变化",
        "category": "math",
        "subcategory": "calculate",
        "api_endpoint": "/api/percentage-change",
        "method": "POST",
        "params": [
            {"name": "old", "type": "number", "required": True, "description": "旧值"},
            {"name": "new", "type": "number", "required": True, "description": "新值"}
        ],
        "icon": "percent"
    },
    "ratio": {
        "id": "ratio",
        "name": "比率",
        "name_en": "Ratio",
        "description": "计算两数的比率",
        "category": "math",
        "subcategory": "calculate",
        "api_endpoint": "/api/ratio",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "数值A"},
            {"name": "b", "type": "number", "required": True, "description": "数值B"}
        ],
        "icon": "divide"
    },
    "to_percent": {
        "id": "to_percent",
        "name": "转百分比",
        "name_en": "To Percent",
        "description": "小数转百分比",
        "category": "math",
        "subcategory": "convert",
        "api_endpoint": "/api/to-percent",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "小数"}
        ],
        "icon": "percent"
    },
    "from_percent": {
        "id": "from_percent",
        "name": "从百分比",
        "name_en": "From Percent",
        "description": "百分比转小数",
        "category": "math",
        "subcategory": "convert",
        "api_endpoint": "/api/from-percent",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "百分比"}
        ],
        "icon": "percent"
    },
    "sum_of_squares": {
        "id": "sum_of_squares",
        "name": "平方和",
        "name_en": "Sum of Squares",
        "description": "计算平方和",
        "category": "math",
        "subcategory": "calculate",
        "api_endpoint": "/api/sum-of-squares",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "x"
    },
    "mean": {
        "id": "mean",
        "name": "平均值",
        "name_en": "Mean",
        "description": "计算平均值",
        "category": "math",
        "subcategory": "stats",
        "api_endpoint": "/api/mean",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "divide"
    },
    "harmonic_mean": {
        "id": "harmonic_mean",
        "name": "调和平均",
        "name_en": "Harmonic Mean",
        "description": "计算调和平均数",
        "category": "math",
        "subcategory": "stats",
        "api_endpoint": "/api/harmonic-mean",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "divide"
    },
    "geometric_mean": {
        "id": "geometric_mean",
        "name": "几何平均",
        "name_en": "Geometric Mean",
        "description": "计算几何平均数",
        "category": "math",
        "subcategory": "stats",
        "api_endpoint": "/api/geometric-mean",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "divide"
    },
    "range_value": {
        "id": "range_value",
        "name": "范围",
        "name_en": "Range",
        "description": "计算最大值与最小值之差",
        "category": "math",
        "subcategory": "stats",
        "api_endpoint": "/api/range",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "minus"
    },
    "midrange": {
        "id": "midrange",
        "name": "中程数",
        "name_en": "Midrange",
        "description": "计算中程数",
        "category": "math",
        "subcategory": "stats",
        "api_endpoint": "/api/midrange",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "divide"
    },
    "root_mean_square": {
        "id": "root_mean_square",
        "name": "均方根",
        "name_en": "Root Mean Square",
        "description": "计算均方根",
        "category": "math",
        "subcategory": "stats",
        "api_endpoint": "/api/root-mean-square",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "x"
    },
    "is_symmetric": {
        "id": "is_symmetric",
        "name": "对称检查",
        "name_en": "Is Symmetric",
        "description": "检查数组是否对称",
        "category": "array",
        "subcategory": "check",
        "api_endpoint": "/api/is-symmetric",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "check-circle"
    },
    "reverse_pairs": {
        "id": "reverse_pairs",
        "name": "反转对",
        "name_en": "Reverse Pairs",
        "description": "查找反转对数量",
        "category": "array",
        "subcategory": "search",
        "api_endpoint": "/api/reverse-pairs",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "git_pull_request"
    },
    "palindrome": {
        "id": "palindrome",
        "name": "回文检查",
        "name_en": "Is Palindrome",
        "description": "检查是否回文",
        "category": "array",
        "subcategory": "check",
        "api_endpoint": "/api/palindrome",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "check-circle"
    },
    "rotate_left": {
        "id": "rotate_left",
        "name": "左旋转",
        "name_en": "Rotate Left",
        "description": "数组左旋转",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/rotate-left",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "n", "type": "number", "required": False, "description": "旋转数"}
        ],
        "icon": "rotate-ccw"
    },
    "rotate_right": {
        "id": "rotate_right",
        "name": "右旋转",
        "name_en": "Rotate Right",
        "description": "数组右旋转",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/rotate-right",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "n", "type": "number", "required": False, "description": "旋转数"}
        ],
        "icon": "rotate-cw"
    },
    "associate_by": {
        "id": "associate_by",
        "name": "关联映射",
        "name_en": "Associate By",
        "description": "按键关联数组元素",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/associate-by",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "key", "type": "string", "required": True, "description": "键名"}
        ],
        "icon": "link"
    },
    "associate_with": {
        "id": "associate_with",
        "name": "值关联",
        "name_en": "Associate With",
        "description": "用值关联数组元素",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/associate-with",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "value", "type": "string", "required": True, "description": "值"}
        ],
        "icon": "link"
    },
    "partition_by": {
        "id": "partition_by",
        "name": "按条件分区",
        "name_en": "Partition By",
        "description": "按条件将数组分区",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/partition-by",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "columns"
    },
    "partition_at": {
        "id": "partition_at",
        "name": "按位置分区",
        "name_en": "Partition At",
        "description": "按位置将数组分区",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/partition-at",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "index", "type": "number", "required": True, "description": "位置"}
        ],
        "icon": "columns"
    },
    "sum_map": {
        "id": "sum_map",
        "name": "求和映射",
        "name_en": "Sum Map",
        "description": "对数组元素求和后映射",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/sum-map",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "plus"
    },
    "count_by_type": {
        "id": "count_by_type",
        "name": "按类型计数",
        "name_en": "Count by Type",
        "description": "按类型统计数量",
        "category": "array",
        "subcategory": "aggregate",
        "api_endpoint": "/api/count-by-type",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "hash"
    },
    "group_by_type": {
        "id": "group_by_type",
        "name": "按类型分组",
        "name_en": "Group by Type",
        "description": "按类型分组",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/group-by-type",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "folder"
    },
    "sort_naturally": {
        "id": "sort_naturally",
        "name": "自然排序",
        "name_en": "Sort Naturally",
        "description": "自然排序字符串数组",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/sort-naturally",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "字符串数组"},
            {"name": "reverse", "type": "boolean", "required": False, "description": "降序"}
        ],
        "icon": "arrow-up-down"
    },
    "move_to": {
        "id": "move_to",
        "name": "移动元素",
        "name_en": "Move To",
        "description": "将元素移动到指定位置",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/move-to",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "from", "type": "number", "required": True, "description": "原位置"},
            {"name": "to", "type": "number", "required": True, "description": "目标位置"}
        ],
        "icon": "move"
    },
    "swap": {
        "id": "swap",
        "name": "交换元素",
        "name_en": "Swap",
        "description": "交换两个位置的元素",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/swap",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "i", "type": "number", "required": True, "description": "位置1"},
            {"name": "j", "type": "number", "required": True, "description": "位置2"}
        ],
        "icon": "repeat"
    },
    "insert_at": {
        "id": "insert_at",
        "name": "指定位置插入",
        "name_en": "Insert At",
        "description": "在指定位置插入元素",
        "category": "array",
        "subcategory": "modify",
        "api_endpoint": "/api/insert-at",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "index", "type": "number", "required": True, "description": "位置"},
            {"name": "value", "type": "string", "required": True, "description": "值"}
        ],
        "icon": "plus"
    },
    "remove_at": {
        "id": "remove_at",
        "name": "指定位置删除",
        "name_en": "Remove At",
        "description": "删除指定位置的元素",
        "category": "array",
        "subcategory": "modify",
        "api_endpoint": "/api/remove-at",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "index", "type": "number", "required": True, "description": "位置"}
        ],
        "icon": "trash-2"
    },
    "replace_at": {
        "id": "replace_at",
        "name": "指定位置替换",
        "name_en": "Replace At",
        "description": "替换指定位置的元素",
        "category": "array",
        "subcategory": "modify",
        "api_endpoint": "/api/replace-at",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "index", "type": "number", "required": True, "description": "位置"},
            {"name": "value", "type": "string", "required": True, "description": "新值"}
        ],
        "icon": "edit"
    },
    "unique_by_key": {
        "id": "unique_by_key",
        "name": "按键去重",
        "name_en": "Unique by Key",
        "description": "按键去除重复元素",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/unique-by-key",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "key", "type": "string", "required": True, "description": "键名"}
        ],
        "icon": "filter"
    },
    "starts_with_val": {
        "id": "starts_with_val",
        "name": "开头匹配",
        "name_en": "Starts With Value",
        "description": "查找以指定值开头的元素",
        "category": "array",
        "subcategory": "search",
        "api_endpoint": "/api/starts-with",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "value", "type": "string", "required": True, "description": "值"}
        ],
        "icon": "search"
    },
    "ends_with_val": {
        "id": "ends_with_val",
        "name": "结尾匹配",
        "name_en": "Ends With Value",
        "description": "查找以指定值结尾的元素",
        "category": "array",
        "subcategory": "search",
        "api_endpoint": "/api/ends-with",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "value", "type": "string", "required": True, "description": "值"}
        ],
        "icon": "search"
    },
    "contains_val": {
        "id": "contains_val",
        "name": "包含匹配",
        "name_en": "Contains Value",
        "description": "查找包含指定值的元素",
        "category": "array",
        "subcategory": "search",
        "api_endpoint": "/api/contains-val",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "value", "type": "string", "required": True, "description": "值"}
        ],
        "icon": "search"
    },
    "match_regex": {
        "id": "match_regex",
        "name": "正则匹配",
        "name_en": "Match Regex",
        "description": "匹配正则表达式的元素",
        "category": "array",
        "subcategory": "search",
        "api_endpoint": "/api/match-regex",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "pattern", "type": "string", "required": True, "description": "正则"}
        ],
        "icon": "regex"
    },
    "filter_regex": {
        "id": "filter_regex",
        "name": "正则过滤",
        "name_en": "Filter Regex",
        "description": "用正则表达式过滤数组",
        "category": "array",
        "subcategory": "filter",
        "api_endpoint": "/api/filter-regex",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "pattern", "type": "string", "required": True, "description": "正则"}
        ],
        "icon": "filter"
    },
    "flat_map": {
        "id": "flat_map",
        "name": "扁平映射",
        "name_en": "Flat Map",
        "description": "映射后扁平化",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/flat-map",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "fn", "type": "string", "required": True, "description": "函数"}
        ],
        "icon": "map"
    },
    "flatten_depth": {
        "id": "flatten_depth",
        "name": "深度扁平化",
        "name_en": "Flatten Depth",
        "description": "按指定深度扁平化",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/flatten-depth",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "嵌套数组"},
            {"name": "depth", "type": "number", "required": False, "description": "深度"}
        ],
        "icon": "minimize"
    },
    "chunk_by": {
        "id": "chunk_by",
        "name": "按条件分块",
        "name_en": "Chunk By",
        "description": "按条件函数分块数组",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/chunk-by",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "fn", "type": "string", "required": True, "description": "分块函数"}
        ],
        "icon": "grid"
    },
    "window_by": {
        "id": "window_by",
        "name": "滑动窗口",
        "name_en": "Window By",
        "description": "创建滑动窗口",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/window-by",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "size", "type": "number", "required": True, "description": "窗口大小"}
        ],
        "icon": "layers"
    },
    "group_adjacent": {
        "id": "group_adjacent",
        "name": "相邻分组",
        "name_en": "Group Adjacent",
        "description": "将相邻相同元素分组",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/group-adjacent",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "group"
    },
    "split_at": {
        "id": "split_at",
        "name": "在索引分割",
        "name_en": "Split At",
        "description": "在指定索引处分割数组",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/split-at",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "index", "type": "number", "required": True, "description": "索引"}
        ],
        "icon": "scissors"
    },
    "split_by": {
        "id": "split_by",
        "name": "按值分割",
        "name_en": "Split By",
        "description": "按分隔值分割数组",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/split-by",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "separator", "type": "any", "required": True, "description": "分隔值"}
        ],
        "icon": "divide"
    },
    "take_every": {
        "id": "take_every",
        "name": "每隔取",
        "name_en": "Take Every",
        "description": "每隔N个元素取一个",
        "category": "array",
        "subcategory": "filter",
        "api_endpoint": "/api/take-every",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "n", "type": "number", "required": True, "description": "间隔"}
        ],
        "icon": "skip-forward"
    },
    "skip_every": {
        "id": "skip_every",
        "name": "每隔跳",
        "name_en": "Skip Every",
        "description": "每隔N个元素跳过一个",
        "category": "array",
        "subcategory": "filter",
        "api_endpoint": "/api/skip-every",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "n", "type": "number", "required": True, "description": "间隔"}
        ],
        "icon": "fast-forward"
    },
    "count_occurrences": {
        "id": "count_occurrences",
        "name": "计数出现",
        "name_en": "Count Occurrences",
        "description": "统计元素出现次数",
        "category": "array",
        "subcategory": "aggregate",
        "api_endpoint": "/api/count-occurrences",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "hash"
    },
    "find_duplicates": {
        "id": "find_duplicates",
        "name": "查找重复",
        "name_en": "Find Duplicates",
        "description": "查找数组中的重复元素",
        "category": "array",
        "subcategory": "filter",
        "api_endpoint": "/api/find-duplicates",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "copy"
    },
    "remove_duplicates": {
        "id": "remove_duplicates",
        "name": "去重",
        "name_en": "Remove Duplicates",
        "description": "移除数组中的重复元素",
        "category": "array",
        "subcategory": "filter",
        "api_endpoint": "/api/remove-duplicates",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "trash-2"
    },
    "rotate_array": {
        "id": "rotate_array",
        "name": "轮转数组",
        "name_en": "Rotate Array",
        "description": "循环轮转数组元素",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/rotate-array",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "n", "type": "number", "required": True, "description": "轮转数"}
        ],
        "icon": "rotate-cw"
    },
    "shuffle": {
        "id": "shuffle",
        "name": "随机打乱",
        "name_en": "Shuffle",
        "description": "随机打乱数组顺序",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/shuffle",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "shuffle"
    },
    "sample": {
        "id": "sample",
        "name": "随机采样",
        "name_en": "Sample",
        "description": "随机取一个元素",
        "category": "array",
        "subcategory": "filter",
        "api_endpoint": "/api/sample",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "target"
    },
    "sample_multiple": {
        "id": "sample_multiple",
        "name": "随机多样采样",
        "name_en": "Sample Multiple",
        "description": "随机取多个不重复元素",
        "category": "array",
        "subcategory": "filter",
        "api_endpoint": "/api/sample-multiple",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "count", "type": "number", "required": True, "description": "采样数量"}
        ],
        "icon": "list"
    },
    "sort_natural": {
        "id": "sort_natural",
        "name": "自然排序",
        "name_en": "Natural Sort",
        "description": "按自然顺序排序",
        "category": "array",
        "subcategory": "sort",
        "api_endpoint": "/api/sort-natural",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "sort-asc"
    },
    "sort_by": {
        "id": "sort_by",
        "name": "自定义排序",
        "name_en": "Sort By",
        "description": "按函数排序",
        "category": "array",
        "subcategory": "sort",
        "api_endpoint": "/api/sort-by",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "fn", "type": "string", "required": True, "description": "排序函数"}
        ],
        "icon": "arrow-up-down"
    },
    "min_by": {
        "id": "min_by",
        "name": "最小值",
        "name_en": "Min By",
        "description": "按函数取最小",
        "category": "array",
        "subcategory": "aggregate",
        "api_endpoint": "/api/min-by",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "fn", "type": "string", "required": True, "description": "比较函数"}
        ],
        "icon": "chevron-down"
    },
    "max_by": {
        "id": "max_by",
        "name": "最大值",
        "name_en": "Max By",
        "description": "按函数取最大",
        "category": "array",
        "subcategory": "aggregate",
        "api_endpoint": "/api/max-by",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "fn", "type": "string", "required": True, "description": "比较函数"}
        ],
        "icon": "chevron-up"
    },
    "first_match": {
        "id": "first_match",
        "name": "首匹配",
        "name_en": "First Match",
        "description": "查找第一个匹配元素",
        "category": "array",
        "subcategory": "search",
        "api_endpoint": "/api/first-match",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "predicate", "type": "string", "required": True, "description": "谓词函数"}
        ],
        "icon": "search"
    },
    "last_match": {
        "id": "last_match",
        "name": "末匹配",
        "name_en": "Last Match",
        "description": "查找最后一个匹配元素",
        "category": "array",
        "subcategory": "search",
        "api_endpoint": "/api/last-match",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "predicate", "type": "string", "required": True, "description": "谓词函数"}
        ],
        "icon": "search"
    },
    "find_index": {
        "id": "find_index",
        "name": "查找索引",
        "name_en": "Find Index",
        "description": "查找元素首次出现的索引",
        "category": "array",
        "subcategory": "search",
        "api_endpoint": "/api/find-index",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "value", "type": "any", "required": True, "description": "要查找的值"}
        ],
        "icon": "hash"
    },
    "array_contains": {
        "id": "array_contains",
        "name": "包含检查",
        "name_en": "Contains",
        "description": "检查数组是否包含元素",
        "category": "array",
        "subcategory": "search",
        "api_endpoint": "/api/contains",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "value", "type": "any", "required": True, "description": "要检查的值"}
        ],
        "icon": "check-circle"
    },
    "not_contains": {
        "id": "not_contains",
        "name": "不包含检查",
        "name_en": "Not Contains",
        "description": "检查数组是否不包含元素",
        "category": "array",
        "subcategory": "search",
        "api_endpoint": "/api/not-contains",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "value", "type": "any", "required": True, "description": "要检查的值"}
        ],
        "icon": "x-circle"
    },
    "any_match": {
        "id": "any_match",
        "name": "任意匹配",
        "name_en": "Any Match",
        "description": "检查是否有任意元素匹配",
        "category": "array",
        "subcategory": "search",
        "api_endpoint": "/api/any-match",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "predicate", "type": "string", "required": True, "description": "谓词函数"}
        ],
        "icon": "check-square"
    },
    "all_match": {
        "id": "all_match",
        "name": "全部匹配",
        "name_en": "All Match",
        "description": "检查是否所有元素都匹配",
        "category": "array",
        "subcategory": "search",
        "api_endpoint": "/api/all-match",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "predicate", "type": "string", "required": True, "description": "谓词函数"}
        ],
        "icon": "check"
    },
    "none_match": {
        "id": "none_match",
        "name": "无匹配",
        "name_en": "None Match",
        "description": "检查是否没有元素匹配",
        "category": "array",
        "subcategory": "search",
        "api_endpoint": "/api/none-match",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "predicate", "type": "string", "required": True, "description": "谓词函数"}
        ],
        "icon": "minus"
    },
    "difference": {
        "id": "difference",
        "name": "差集",
        "name_en": "Difference",
        "description": "获取两个数组的差集",
        "category": "array",
        "subcategory": "set",
        "api_endpoint": "/api/difference",
        "method": "POST",
        "params": [
            {"name": "a", "type": "array", "required": True, "description": "数组A"},
            {"name": "b", "type": "array", "required": True, "description": "数组B"}
        ],
        "icon": "minus"
    },
    "intersection": {
        "id": "intersection",
        "name": "交集",
        "name_en": "Intersection",
        "description": "获取两个数组的交集",
        "category": "array",
        "subcategory": "set",
        "api_endpoint": "/api/intersection",
        "method": "POST",
        "params": [
            {"name": "a", "type": "array", "required": True, "description": "数组A"},
            {"name": "b", "type": "array", "required": True, "description": "数组B"}
        ],
        "icon": "git-intersect"
    },
    "union": {
        "id": "union",
        "name": "并集",
        "name_en": "Union",
        "description": "获取两个数组的并集",
        "category": "array",
        "subcategory": "set",
        "api_endpoint": "/api/union",
        "method": "POST",
        "params": [
            {"name": "a", "type": "array", "required": True, "description": "数组A"},
            {"name": "b", "type": "array", "required": True, "description": "数组B"}
        ],
        "icon": "git-merge"
    },

    # ========== 字典工具 ==========
    "dict_get": {
        "id": "dict_get",
        "name": "字典取值",
        "name_en": "Dict Get",
        "description": "安全获取字典值",
        "category": "dict",
        "subcategory": "access",
        "api_endpoint": "/api/dict/get",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "字典"},
            {"name": "key", "type": "string", "required": True, "description": "键名"},
            {"name": "default", "type": "any", "required": False, "description": "默认值"}
        ],
        "icon": "key"
    },
    "dict_set": {
        "id": "dict_set",
        "name": "字典设值",
        "name_en": "Dict Set",
        "description": "设置字典键值",
        "category": "dict",
        "subcategory": "mutate",
        "api_endpoint": "/api/dict/set",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "字典"},
            {"name": "key", "type": "string", "required": True, "description": "键名"},
            {"name": "value", "type": "any", "required": True, "description": "值"}
        ],
        "icon": "edit"
    },
    "dict_delete": {
        "id": "dict_delete",
        "name": "字典删除",
        "name_en": "Dict Delete",
        "description": "删除字典键",
        "category": "dict",
        "subcategory": "mutate",
        "api_endpoint": "/api/dict/delete",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "字典"},
            {"name": "key", "type": "string", "required": True, "description": "键名"}
        ],
        "icon": "trash"
    },
    "dict_keys": {
        "id": "dict_keys",
        "name": "获取键列表",
        "name_en": "Dict Keys",
        "description": "获取字典所有键",
        "category": "dict",
        "subcategory": "access",
        "api_endpoint": "/api/dict/keys",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "字典"}
        ],
        "icon": "list"
    },
    "dict_values": {
        "id": "dict_values",
        "name": "获取值列表",
        "name_en": "Dict Values",
        "description": "获取字典所有值",
        "category": "dict",
        "subcategory": "access",
        "api_endpoint": "/api/dict/values",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "字典"}
        ],
        "icon": "list"
    },
    "dict_items": {
        "id": "dict_items",
        "name": "获取键值对",
        "name_en": "Dict Items",
        "description": "获取字典所有键值对",
        "category": "dict",
        "subcategory": "access",
        "api_endpoint": "/api/dict/items",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "字典"}
        ],
        "icon": "list"
    },
    "dict_merge": {
        "id": "dict_merge",
        "name": "字典合并",
        "name_en": "Dict Merge",
        "description": "合并多个字典",
        "category": "dict",
        "subcategory": "transform",
        "api_endpoint": "/api/dict/merge",
        "method": "POST",
        "params": [
            {"name": "objects", "type": "array", "required": True, "description": "字典数组"}
        ],
        "icon": "git-merge"
    },
    "dict_flatten": {
        "id": "dict_flatten",
        "name": "字典扁平化",
        "name_en": "Dict Flatten",
        "description": "将嵌套字典展平",
        "category": "dict",
        "subcategory": "transform",
        "api_endpoint": "/api/dict/flatten",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "嵌套字典"},
            {"name": "separator", "type": "string", "required": False, "description": "键分隔符"}
        ],
        "icon": "minimize"
    },
    "dict_unflatten": {
        "id": "dict_unflatten",
        "name": "字典嵌套",
        "name_en": "Dict Unflatten",
        "description": "将扁平字典还原为嵌套",
        "category": "dict",
        "subcategory": "transform",
        "api_endpoint": "/api/dict/unflatten",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "扁平字典"},
            {"name": "separator", "type": "string", "required": False, "description": "键分隔符"}
        ],
        "icon": "maximize"
    },
    "dict_filter": {
        "id": "dict_filter",
        "name": "字典过滤",
        "name_en": "Dict Filter",
        "description": "按条件过滤字典",
        "category": "dict",
        "subcategory": "filter",
        "api_endpoint": "/api/dict/filter",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "字典"},
            {"name": "predicate", "type": "string", "required": True, "description": "过滤条件"}
        ],
        "icon": "filter"
    },
    "dict_map": {
        "id": "dict_map",
        "name": "字典映射",
        "name_en": "Dict Map",
        "description": "映射字典的值",
        "category": "dict",
        "subcategory": "transform",
        "api_endpoint": "/api/dict/map",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "字典"},
            {"name": "fn", "type": "string", "required": True, "description": "映射函数"}
        ],
        "icon": "map"
    },
    "dict_invert": {
        "id": "dict_invert",
        "name": "字典反转",
        "name_en": "Dict Invert",
        "description": "交换字典的键和值",
        "category": "dict",
        "subcategory": "transform",
        "api_endpoint": "/api/dict/invert",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "字典"}
        ],
        "icon": "repeat"
    },
    "dict_pick": {
        "id": "dict_pick",
        "name": "字典选择",
        "name_en": "Dict Pick",
        "description": "选择指定键",
        "category": "dict",
        "subcategory": "filter",
        "api_endpoint": "/api/dict/pick",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "字典"},
            {"name": "keys", "type": "array", "required": True, "description": "要选择的键"}
        ],
        "icon": "check-square"
    },
    "dict_omit": {
        "id": "dict_omit",
        "name": "字典排除",
        "name_en": "Dict Omit",
        "description": "排除指定键",
        "category": "dict",
        "subcategory": "filter",
        "api_endpoint": "/api/dict/omit",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "字典"},
            {"name": "keys", "type": "array", "required": True, "description": "要排除的键"}
        ],
        "icon": "x-square"
    },
    "dict_has_key": {
        "id": "dict_has_key",
        "name": "键存在检查",
        "name_en": "Has Key",
        "description": "检查键是否存在",
        "category": "dict",
        "subcategory": "search",
        "api_endpoint": "/api/dict/has-key",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "字典"},
            {"name": "key", "type": "string", "required": True, "description": "键名"}
        ],
        "icon": "key"
    },
    "dict_is_empty": {
        "id": "dict_is_empty",
        "name": "字典空检查",
        "name_en": "Dict Is Empty",
        "description": "检查字典是否为空",
        "category": "dict",
        "subcategory": "search",
        "api_endpoint": "/api/dict/is-empty",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "字典"}
        ],
        "icon": "minus"
    },
    "dict_size": {
        "id": "dict_size",
        "name": "字典大小",
        "name_en": "Dict Size",
        "description": "获取字典键值对数量",
        "category": "dict",
        "subcategory": "aggregate",
        "api_endpoint": "/api/dict/size",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "字典"}
        ],
        "icon": "hash"
    },

    # ========== 数字工具 ==========
    "is_even": {
        "id": "is_even",
        "name": "偶数检查",
        "name_en": "Is Even",
        "description": "检查数字是否为偶数",
        "category": "math",
        "subcategory": "predicate",
        "api_endpoint": "/api/is-even",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "数字"}
        ],
        "icon": "check"
    },
    "is_odd": {
        "id": "is_odd",
        "name": "奇数检查",
        "name_en": "Is Odd",
        "description": "检查数字是否为奇数",
        "category": "math",
        "subcategory": "predicate",
        "api_endpoint": "/api/is-odd",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "数字"}
        ],
        "icon": "check"
    },
    "is_positive": {
        "id": "is_positive",
        "name": "正数检查",
        "name_en": "Is Positive",
        "description": "检查数字是否为正数",
        "category": "math",
        "subcategory": "predicate",
        "api_endpoint": "/api/is-positive",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "数字"}
        ],
        "icon": "arrow-up"
    },
    "is_negative": {
        "id": "is_negative",
        "name": "负数检查",
        "name_en": "Is Negative",
        "description": "检查数字是否为负数",
        "category": "math",
        "subcategory": "predicate",
        "api_endpoint": "/api/is-negative",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "数字"}
        ],
        "icon": "arrow-down"
    },
    "is_zero": {
        "id": "is_zero",
        "name": "零检查",
        "name_en": "Is Zero",
        "description": "检查数字是否为零",
        "category": "math",
        "subcategory": "predicate",
        "api_endpoint": "/api/is-zero",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "数字"}
        ],
        "icon": "minus"
    },
    "is_integer": {
        "id": "is_integer",
        "name": "整数检查",
        "name_en": "Is Integer",
        "description": "检查数字是否为整数",
        "category": "math",
        "subcategory": "predicate",
        "api_endpoint": "/api/is-integer",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "数字"}
        ],
        "icon": "hash"
    },
    "is_prime": {
        "id": "is_prime",
        "name": "质数检查",
        "name_en": "Is Prime",
        "description": "检查数字是否为质数",
        "category": "math",
        "subcategory": "predicate",
        "api_endpoint": "/api/is-prime",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "数字"}
        ],
        "icon": "star"
    },
    "abs": {
        "id": "abs",
        "name": "绝对值",
        "name_en": "Absolute",
        "description": "获取数字绝对值",
        "category": "math",
        "subcategory": "transform",
        "api_endpoint": "/api/abs",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "数字"}
        ],
        "icon": "move"
    },
    "sign": {
        "id": "sign",
        "name": "符号",
        "name_en": "Sign",
        "description": "获取数字符号",
        "category": "math",
        "subcategory": "transform",
        "api_endpoint": "/api/sign",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "数字"}
        ],
        "icon": "plus"
    },
    "clamp": {
        "id": "clamp",
        "name": "区间限制",
        "name_en": "Clamp",
        "description": "将数字限制在范围内",
        "category": "math",
        "subcategory": "transform",
        "api_endpoint": "/api/clamp",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "数字"},
            {"name": "min", "type": "number", "required": True, "description": "最小值"},
            {"name": "max", "type": "number", "required": True, "description": "最大值"}
        ],
        "icon": "minimize-2"
    },
    "in_range": {
        "id": "in_range",
        "name": "范围内检查",
        "name_en": "In Range",
        "description": "检查数字是否在范围内",
        "category": "math",
        "subcategory": "predicate",
        "api_endpoint": "/api/in-range",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "数字"},
            {"name": "min", "type": "number", "required": True, "description": "最小值"},
            {"name": "max", "type": "number", "required": True, "description": "最大值"}
        ],
        "icon": "check-circle"
    },
    "round_to": {
        "id": "round_to",
        "name": "四舍五入",
        "name_en": "Round To",
        "description": "将数字四舍五入到指定精度",
        "category": "math",
        "subcategory": "transform",
        "api_endpoint": "/api/round-to",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "数字"},
            {"name": "precision", "type": "number", "required": False, "description": "精度"}
        ],
        "icon": "hash"
    },
    "floor": {
        "id": "floor",
        "name": "向下取整",
        "name_en": "Floor",
        "description": "向下取整",
        "category": "math",
        "subcategory": "transform",
        "api_endpoint": "/api/floor",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "数字"}
        ],
        "icon": "arrow-down"
    },
    "ceil": {
        "id": "ceil",
        "name": "向上取整",
        "name_en": "Ceil",
        "description": "向上取整",
        "category": "math",
        "subcategory": "transform",
        "api_endpoint": "/api/ceil",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "数字"}
        ],
        "icon": "arrow-up"
    },
    "sum": {
        "id": "sum",
        "name": "求和",
        "name_en": "Sum",
        "description": "计算数组总和",
        "category": "math",
        "subcategory": "aggregate",
        "api_endpoint": "/api/sum",
        "method": "POST",
        "params": [
            {"name": "numbers", "type": "array", "required": True, "description": "数字数组"}
        ],
        "icon": "plus"
    },
    "product": {
        "id": "product",
        "name": "求积",
        "name_en": "Product",
        "description": "计算数组乘积",
        "category": "math",
        "subcategory": "aggregate",
        "api_endpoint": "/api/product",
        "method": "POST",
        "params": [
            {"name": "numbers", "type": "array", "required": True, "description": "数字数组"}
        ],
        "icon": "x"
    },
    "average": {
        "id": "average",
        "name": "平均值",
        "name_en": "Average",
        "description": "计算数组平均值",
        "category": "math",
        "subcategory": "aggregate",
        "api_endpoint": "/api/average",
        "method": "POST",
        "params": [
            {"name": "numbers", "type": "array", "required": True, "description": "数字数组"}
        ],
        "icon": "divide"
    },
    "median": {
        "id": "median",
        "name": "中位数",
        "name_en": "Median",
        "description": "计算数组中位数",
        "category": "math",
        "subcategory": "aggregate",
        "api_endpoint": "/api/median",
        "method": "POST",
        "params": [
            {"name": "numbers", "type": "array", "required": True, "description": "数字数组"}
        ],
        "icon": "bar-chart-2"
    },
    "mode": {
        "id": "mode",
        "name": "众数",
        "name_en": "Mode",
        "description": "计算数组众数",
        "category": "math",
        "subcategory": "aggregate",
        "api_endpoint": "/api/mode",
        "method": "POST",
        "params": [
            {"name": "numbers", "type": "array", "required": True, "description": "数字数组"}
        ],
        "icon": "bar-chart"
    },
    "variance": {
        "id": "variance",
        "name": "方差",
        "name_en": "Variance",
        "description": "计算数组方差",
        "category": "math",
        "subcategory": "aggregate",
        "api_endpoint": "/api/variance",
        "method": "POST",
        "params": [
            {"name": "numbers", "type": "array", "required": True, "description": "数字数组"}
        ],
        "icon": "trending-up"
    },
    "std_dev": {
        "id": "std_dev",
        "name": "标准差",
        "name_en": "Standard Deviation",
        "description": "计算数组标准差",
        "category": "math",
        "subcategory": "aggregate",
        "api_endpoint": "/api/std-dev",
        "method": "POST",
        "params": [
            {"name": "numbers", "type": "array", "required": True, "description": "数字数组"}
        ],
        "icon": "trending-nesc"
    },
    "gcd": {
        "id": "gcd",
        "name": "最大公约数",
        "name_en": "GCD",
        "description": "计算最大公约数",
        "category": "math",
        "subcategory": "calculate",
        "api_endpoint": "/api/gcd",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "数字A"},
            {"name": "b", "type": "number", "required": True, "description": "数字B"}
        ],
        "icon": "divide"
    },
    "lcm": {
        "id": "lcm",
        "name": "最小公倍数",
        "name_en": "LCM",
        "description": "计算最小公倍数",
        "category": "math",
        "subcategory": "calculate",
        "api_endpoint": "/api/lcm",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "数字A"},
            {"name": "b", "type": "number", "required": True, "description": "数字B"}
        ],
        "icon": "multiply"
    },
    "factorial": {
        "id": "factorial",
        "name": "阶乘",
        "name_en": "Factorial",
        "description": "计算阶乘",
        "category": "math",
        "subcategory": "calculate",
        "api_endpoint": "/api/factorial",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "非负整数"}
        ],
        "icon": "hash"
    },
    "fibonacci": {
        "id": "fibonacci",
        "name": "斐波那契",
        "name_en": "Fibonacci",
        "description": "生成斐波那契数列",
        "category": "math",
        "subcategory": "generate",
        "api_endpoint": "/api/fibonacci",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "数量"}
        ],
        "icon": "list"
    },
    "prime_factors": {
        "id": "prime_factors",
        "name": "质因数分解",
        "name_en": "Prime Factors",
        "description": "分解质因数",
        "category": "math",
        "subcategory": "calculate",
        "api_endpoint": "/api/prime-factors",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "数字"}
        ],
        "icon": "grid"
    },

    # ========== 字符串工具 ==========
    "capitalize": {
        "id": "capitalize",
        "name": "首字母大写",
        "name_en": "Capitalize",
        "description": "首字母大写其余小写",
        "category": "string",
        "subcategory": "transform",
        "api_endpoint": "/api/capitalize",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "type"
    },
    "title_case": {
        "id": "title_case",
        "name": "标题大写",
        "name_en": "Title Case",
        "description": "每个单词首字母大写",
        "category": "string",
        "subcategory": "transform",
        "api_endpoint": "/api/title-case",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "text"
    },
    "snake_case": {
        "id": "snake_case",
        "name": "蛇形命名",
        "name_en": "Snake Case",
        "description": "转换为蛇形命名",
        "category": "string",
        "subcategory": "transform",
        "api_endpoint": "/api/snake-case",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "minus"
    },
    "camel_case": {
        "id": "camel_case",
        "name": "驼峰命名",
        "name_en": "Camel Case",
        "description": "转换为驼峰命名",
        "category": "string",
        "subcategory": "transform",
        "api_endpoint": "/api/camel-case",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "arrow-up"
    },
    "pascal_case": {
        "id": "pascal_case",
        "name": "帕斯卡命名",
        "name_en": "Pascal Case",
        "description": "转换为帕斯卡命名",
        "category": "string",
        "subcategory": "transform",
        "api_endpoint": "/api/pascal-case",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "arrow-up-circle"
    },
    "kebab_case": {
        "id": "kebab_case",
        "name": "串形命名",
        "name_en": "Kebab Case",
        "description": "转换为串形命名",
        "category": "string",
        "subcategory": "transform",
        "api_endpoint": "/api/kebab-case",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "minus"
    },
    "slugify": {
        "id": "slugify",
        "name": "Slug化",
        "name_en": "Slugify",
        "description": "转换为URL友好格式",
        "category": "string",
        "subcategory": "transform",
        "api_endpoint": "/api/slugify",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "link"
    },
    "unescape": {
        "id": "unescape",
        "name": "反转义",
        "name_en": "Unescape",
        "description": "反转义字符串",
        "category": "string",
        "subcategory": "transform",
        "api_endpoint": "/api/unescape",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "code"
    },
    "word_count": {
        "id": "word_count",
        "name": "单词计数",
        "name_en": "Word Count",
        "description": "统计单词数量",
        "category": "string",
        "subcategory": "analyze",
        "api_endpoint": "/api/word-count",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "hash"
    },
    "char_count": {
        "id": "char_count",
        "name": "字符计数",
        "name_en": "Char Count",
        "description": "统计字符数量",
        "category": "string",
        "subcategory": "analyze",
        "api_endpoint": "/api/char-count",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "type"
    },
    "line_count": {
        "id": "line_count",
        "name": "行数统计",
        "name_en": "Line Count",
        "description": "统计行数",
        "category": "string",
        "subcategory": "analyze",
        "api_endpoint": "/api/line-count",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "list"
    },
    "trim": {
        "id": "trim",
        "name": "去除空白",
        "name_en": "Trim",
        "description": "去除首尾空白",
        "category": "string",
        "subcategory": "transform",
        "api_endpoint": "/api/trim",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "minus"
    },
    "trim_start": {
        "id": "trim_start",
        "name": "去除开头空白",
        "name_en": "Trim Start",
        "description": "去除开头空白",
        "category": "string",
        "subcategory": "transform",
        "api_endpoint": "/api/trim-start",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "arrow-left"
    },
    "trim_end": {
        "id": "trim_end",
        "name": "去除结尾空白",
        "name_en": "Trim End",
        "description": "去除结尾空白",
        "category": "string",
        "subcategory": "transform",
        "api_endpoint": "/api/trim-end",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "arrow-right"
    },
    "pad_start": {
        "id": "pad_start",
        "name": "头部填充",
        "name_en": "Pad Start",
        "description": "在开头填充字符",
        "category": "string",
        "subcategory": "transform",
        "api_endpoint": "/api/pad-start",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "length", "type": "number", "required": True, "description": "目标长度"},
            {"name": "char", "type": "string", "required": False, "description": "填充字符"}
        ],
        "icon": "arrow-left"
    },
    "pad_end": {
        "id": "pad_end",
        "name": "尾部填充",
        "name_en": "Pad End",
        "description": "在结尾填充字符",
        "category": "string",
        "subcategory": "transform",
        "api_endpoint": "/api/pad-end",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "length", "type": "number", "required": True, "description": "目标长度"},
            {"name": "char", "type": "string", "required": False, "description": "填充字符"}
        ],
        "icon": "arrow-right"
    },
    "repeat": {
        "id": "repeat",
        "name": "重复字符串",
        "name_en": "Repeat",
        "description": "重复字符串N次",
        "category": "string",
        "subcategory": "transform",
        "api_endpoint": "/api/repeat",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "count", "type": "number", "required": True, "description": "重复次数"}
        ],
        "icon": "copy"
    },
    "reverse": {
        "id": "reverse",
        "name": "反转字符串",
        "name_en": "Reverse String",
        "description": "反转字符串",
        "category": "string",
        "subcategory": "transform",
        "api_endpoint": "/api/reverse",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "rotate-ccw"
    },
    "truncate": {
        "id": "truncate",
        "name": "截断字符串",
        "name_en": "Truncate",
        "description": "截断字符串到指定长度",
        "category": "string",
        "subcategory": "transform",
        "api_endpoint": "/api/truncate",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "length", "type": "number", "required": True, "description": "长度"},
            {"name": "suffix", "type": "string", "required": False, "description": "后缀"}
        ],
        "icon": "scissors"
    },
    "wrap": {
        "id": "wrap",
        "name": "包裹字符串",
        "name_en": "Wrap",
        "description": "用字符包裹字符串",
        "category": "string",
        "subcategory": "transform",
        "api_endpoint": "/api/wrap",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "wrapper", "type": "string", "required": True, "description": "包裹字符"}
        ],
        "icon": "square"
    },
    "prefix": {
        "id": "prefix",
        "name": "添加前缀",
        "name_en": "Add Prefix",
        "description": "添加字符串前缀",
        "category": "string",
        "subcategory": "transform",
        "api_endpoint": "/api/prefix",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "prefix", "type": "string", "required": True, "description": "前缀"}
        ],
        "icon": "plus"
    },
    "suffix": {
        "id": "suffix",
        "name": "添加后缀",
        "name_en": "Add Suffix",
        "description": "添加字符串后缀",
        "category": "string",
        "subcategory": "transform",
        "api_endpoint": "/api/suffix",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "suffix", "type": "string", "required": True, "description": "后缀"}
        ],
        "icon": "plus"
    },
    "split": {
        "id": "split",
        "name": "分割字符串",
        "name_en": "Split",
        "description": "按分隔符分割字符串",
        "category": "string",
        "subcategory": "transform",
        "api_endpoint": "/api/split",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "delimiter", "type": "string", "required": True, "description": "分隔符"}
        ],
        "icon": "divide"
    },
    "join": {
        "id": "join",
        "name": "连接字符串",
        "name_en": "Join",
        "description": "用分隔符连接字符串数组",
        "category": "string",
        "subcategory": "transform",
        "api_endpoint": "/api/join",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "字符串数组"},
            {"name": "delimiter", "type": "string", "required": True, "description": "分隔符"}
        ],
        "icon": "link"
    },
    "replace": {
        "id": "replace",
        "name": "替换字符串",
        "name_en": "Replace",
        "description": "替换字符串中的文本",
        "category": "string",
        "subcategory": "transform",
        "api_endpoint": "/api/replace",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "search", "type": "string", "required": True, "description": "搜索文本"},
            {"name": "replacement", "type": "string", "required": True, "description": "替换文本"}
        ],
        "icon": "edit"
    },
    "replace_all": {
        "id": "replace_all",
        "name": "全部替换",
        "name_en": "Replace All",
        "description": "替换所有匹配的文本",
        "category": "string",
        "subcategory": "transform",
        "api_endpoint": "/api/replace-all",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "search", "type": "string", "required": True, "description": "搜索文本"},
            {"name": "replacement", "type": "string", "required": True, "description": "替换文本"}
        ],
        "icon": "edit-2"
    },
    "includes": {
        "id": "includes",
        "name": "包含检查",
        "name_en": "Includes",
        "description": "检查是否包含子串",
        "category": "string",
        "subcategory": "search",
        "api_endpoint": "/api/includes",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "search", "type": "string", "required": True, "description": "搜索文本"}
        ],
        "icon": "search"
    },
    "starts_with": {
        "id": "starts_with",
        "name": "开头检查",
        "name_en": "Starts With",
        "description": "检查是否以指定文本开头",
        "category": "string",
        "subcategory": "search",
        "api_endpoint": "/api/starts-with",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "prefix", "type": "string", "required": True, "description": "前缀"}
        ],
        "icon": "arrow-right"
    },
    "ends_with": {
        "id": "ends_with",
        "name": "结尾检查",
        "name_en": "Ends With",
        "description": "检查是否以指定文本结尾",
        "category": "string",
        "subcategory": "search",
        "api_endpoint": "/api/ends-with",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "suffix", "type": "string", "required": True, "description": "后缀"}
        ],
        "icon": "arrow-left"
    },
    "is_empty": {
        "id": "is_empty",
        "name": "空字符串检查",
        "name_en": "Is Empty",
        "description": "检查字符串是否为空",
        "category": "string",
        "subcategory": "predicate",
        "api_endpoint": "/api/is-empty",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "minus"
    },
    "is_blank": {
        "id": "is_blank",
        "name": "空白字符串检查",
        "name_en": "Is Blank",
        "description": "检查字符串是否仅为空白",
        "category": "string",
        "subcategory": "predicate",
        "api_endpoint": "/api/is-blank",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "minus"
    },
    "count_substring": {
        "id": "count_substring",
        "name": "子串计数",
        "name_en": "Count Substring",
        "description": "统计子串出现次数",
        "category": "string",
        "subcategory": "analyze",
        "api_endpoint": "/api/count-substring",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "search", "type": "string", "required": True, "description": "搜索文本"}
        ],
        "icon": "hash"
    },
    "index_of": {
        "id": "index_of",
        "name": "查找索引",
        "name_en": "Index Of",
        "description": "查找子串首次出现位置",
        "category": "string",
        "subcategory": "search",
        "api_endpoint": "/api/index-of",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "search", "type": "string", "required": True, "description": "搜索文本"}
        ],
        "icon": "search"
    },
    "last_index_of": {
        "id": "last_index_of",
        "name": "最后索引",
        "name_en": "Last Index Of",
        "description": "查找子串最后出现位置",
        "category": "string",
        "subcategory": "search",
        "api_endpoint": "/api/last-index-of",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "search", "type": "string", "required": True, "description": "搜索文本"}
        ],
        "icon": "search"
    },
    "extract": {
        "id": "extract",
        "name": "提取文本",
        "name_en": "Extract",
        "description": "按正则提取文本",
        "category": "string",
        "subcategory": "extract",
        "api_endpoint": "/api/extract",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "pattern", "type": "string", "required": True, "description": "正则模式"}
        ],
        "icon": "search"
    },
    "match": {
        "id": "match",
        "name": "匹配检查",
        "name_en": "Match",
        "description": "检查是否匹配正则",
        "category": "string",
        "subcategory": "search",
        "api_endpoint": "/api/match",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "pattern", "type": "string", "required": True, "description": "正则模式"}
        ],
        "icon": "check"
    },

    # ========== 函数式工具 ==========
    "memoize": {
        "id": "memoize",
        "name": "记忆化",
        "name_en": "Memoize",
        "description": "缓存函数结果",
        "category": "function",
        "subcategory": "utility",
        "api_endpoint": "/api/memoize",
        "method": "POST",
        "params": [
            {"name": "fn", "type": "string", "required": True, "description": "函数名"},
            {"name": "args", "type": "array", "required": True, "description": "参数"}
        ],
        "icon": "database"
    },
    "compose": {
        "id": "compose",
        "name": "组合函数",
        "name_en": "Compose",
        "description": "组合多个函数",
        "category": "function",
        "subcategory": "transform",
        "api_endpoint": "/api/compose",
        "method": "POST",
        "params": [
            {"name": "fns", "type": "array", "required": True, "description": "函数数组"}
        ],
        "icon": "link"
    },
    "pipe": {
        "id": "pipe",
        "name": "管道函数",
        "name_en": "Pipe",
        "description": "将值通过管道传递给函数",
        "category": "function",
        "subcategory": "transform",
        "api_endpoint": "/api/pipe",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "初始值"},
            {"name": "fns", "type": "array", "required": True, "description": "函数数组"}
        ],
        "icon": "arrow-right"
    },
    "curry": {
        "id": "curry",
        "name": "柯里化",
        "name_en": "Curry",
        "description": "将多参数函数 curry 化",
        "category": "function",
        "subcategory": "transform",
        "api_endpoint": "/api/curry",
        "method": "POST",
        "params": [
            {"name": "fn", "type": "string", "required": True, "description": "函数"},
            {"name": "arity", "type": "number", "required": True, "description": "参数数量"}
        ],
        "icon": "corner-down-right"
    },
    "partial": {
        "id": "partial",
        "name": "偏函数",
        "name_en": "Partial",
        "description": "创建一个部分应用的函数",
        "category": "function",
        "subcategory": "transform",
        "api_endpoint": "/api/partial",
        "method": "POST",
        "params": [
            {"name": "fn", "type": "string", "required": True, "description": "函数"},
            {"name": "args", "type": "array", "required": True, "description": "预设参数"}
        ],
        "icon": "git-branch"
    },
    "flip": {
        "id": "flip",
        "name": "翻转参数",
        "name_en": "Flip",
        "description": "翻转函数参数顺序",
        "category": "function",
        "subcategory": "transform",
        "api_endpoint": "/api/flip",
        "method": "POST",
        "params": [
            {"name": "fn", "type": "string", "required": True, "description": "函数"}
        ],
        "icon": "repeat"
    },
    "once": {
        "id": "once",
        "name": "单次执行",
        "name_en": "Once",
        "description": "确保函数只执行一次",
        "category": "function",
        "subcategory": "utility",
        "api_endpoint": "/api/once",
        "method": "POST",
        "params": [
            {"name": "fn", "type": "string", "required": True, "description": "函数"}
        ],
        "icon": "lock"
    },
    "identity": {
        "id": "identity",
        "name": "恒等函数",
        "name_en": "Identity",
        "description": "返回输入值本身",
        "category": "function",
        "subcategory": "utility",
        "api_endpoint": "/api/identity",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "任意值"}
        ],
        "icon": "equal"
    },
    "noop": {
        "id": "noop",
        "name": "空操作",
        "name_en": "Noop",
        "description": "不执行任何操作",
        "category": "function",
        "subcategory": "utility",
        "api_endpoint": "/api/noop",
        "method": "POST",
        "params": [],
        "icon": "slash"
    },
    "throttle": {
        "id": "throttle",
        "name": "节流",
        "name_en": "Throttle",
        "description": "限制函数调用频率",
        "category": "function",
        "subcategory": "utility",
        "api_endpoint": "/api/throttle",
        "method": "POST",
        "params": [
            {"name": "fn", "type": "string", "required": True, "description": "函数"},
            {"name": "delay", "type": "number", "required": True, "description": "延迟毫秒"}
        ],
        "icon": "clock"
    },
    "debounce": {
        "id": "debounce",
        "name": "防抖",
        "name_en": "Debounce",
        "description": "防抖函数调用",
        "category": "function",
        "subcategory": "utility",
        "api_endpoint": "/api/debounce",
        "method": "POST",
        "params": [
            {"name": "fn", "type": "string", "required": True, "description": "函数"},
            {"name": "delay", "type": "number", "required": True, "description": "延迟毫秒"}
        ],
        "icon": "clock"
    },
    "retry": {
        "id": "retry",
        "name": "重试",
        "name_en": "Retry",
        "description": "重试失败的操作",
        "category": "function",
        "subcategory": "utility",
        "api_endpoint": "/api/retry",
        "method": "POST",
        "params": [
            {"name": "fn", "type": "string", "required": True, "description": "函数"},
            {"name": "attempts", "type": "number", "required": False, "description": "尝试次数"}
        ],
        "icon": "refresh-cw"
    },
    "timeout": {
        "id": "timeout",
        "name": "超时控制",
        "name_en": "Timeout",
        "description": "设置函数超时",
        "category": "function",
        "subcategory": "utility",
        "api_endpoint": "/api/timeout",
        "method": "POST",
        "params": [
            {"name": "fn", "type": "string", "required": True, "description": "函数"},
            {"name": "ms", "type": "number", "required": True, "description": "超时毫秒"}
        ],
        "icon": "clock"
    },

    # ========== 类型工具 ==========
    "is_string": {
        "id": "is_string",
        "name": "字符串检查",
        "name_en": "Is String",
        "description": "检查是否为字符串",
        "category": "type",
        "subcategory": "predicate",
        "api_endpoint": "/api/is-string",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "任意值"}
        ],
        "icon": "type"
    },
    "is_number": {
        "id": "is_number",
        "name": "数字检查",
        "name_en": "Is Number",
        "description": "检查是否为数字",
        "category": "type",
        "subcategory": "predicate",
        "api_endpoint": "/api/is-number",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "任意值"}
        ],
        "icon": "hash"
    },
    "is_boolean": {
        "id": "is_boolean",
        "name": "布尔检查",
        "name_en": "Is Boolean",
        "description": "检查是否为布尔值",
        "category": "type",
        "subcategory": "predicate",
        "api_endpoint": "/api/is-boolean",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "任意值"}
        ],
        "icon": "check-square"
    },
    "is_array": {
        "id": "is_array",
        "name": "数组检查",
        "name_en": "Is Array",
        "description": "检查是否为数组",
        "category": "type",
        "subcategory": "predicate",
        "api_endpoint": "/api/is-array",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "任意值"}
        ],
        "icon": "list"
    },
    "is_object": {
        "id": "is_object",
        "name": "对象检查",
        "name_en": "Is Object",
        "description": "检查是否为对象",
        "category": "type",
        "subcategory": "predicate",
        "api_endpoint": "/api/is-object",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "任意值"}
        ],
        "icon": "square"
    },
    "is_null": {
        "id": "is_null",
        "name": "空值检查",
        "name_en": "Is Null",
        "description": "检查是否为 null",
        "category": "type",
        "subcategory": "predicate",
        "api_endpoint": "/api/is-null",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "任意值"}
        ],
        "icon": "minus"
    },
    "is_undefined": {
        "id": "is_undefined",
        "name": "未定义检查",
        "name_en": "Is Undefined",
        "description": "检查是否为 undefined",
        "category": "type",
        "subcategory": "predicate",
        "api_endpoint": "/api/is-undefined",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "任意值"}
        ],
        "icon": "help-circle"
    },
    "is_function": {
        "id": "is_function",
        "name": "函数检查",
        "name_en": "Is Function",
        "description": "检查是否为函数",
        "category": "type",
        "subcategory": "predicate",
        "api_endpoint": "/api/is-function",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "任意值"}
        ],
        "icon": "code"
    },
    "is_date": {
        "id": "is_date",
        "name": "日期检查",
        "name_en": "Is Date",
        "description": "检查是否为日期",
        "category": "type",
        "subcategory": "predicate",
        "api_endpoint": "/api/is-date",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "任意值"}
        ],
        "icon": "calendar"
    },
    "is_email": {
        "id": "is_email",
        "name": "邮箱检查",
        "name_en": "Is Email",
        "description": "检查是否为邮箱地址",
        "category": "type",
        "subcategory": "predicate",
        "api_endpoint": "/api/is-email",
        "method": "POST",
        "params": [
            {"name": "value", "type": "string", "required": True, "description": "字符串"}
        ],
        "icon": "mail"
    },
    "is_url": {
        "id": "is_url",
        "name": "URL检查",
        "name_en": "Is URL",
        "description": "检查是否为URL",
        "category": "type",
        "subcategory": "predicate",
        "api_endpoint": "/api/is-url",
        "method": "POST",
        "params": [
            {"name": "value", "type": "string", "required": True, "description": "字符串"}
        ],
        "icon": "link"
    },
    "to_string": {
        "id": "to_string",
        "name": "转字符串",
        "name_en": "To String",
        "description": "转换为字符串",
        "category": "type",
        "subcategory": "convert",
        "api_endpoint": "/api/to-string",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "任意值"}
        ],
        "icon": "type"
    },
    "to_number": {
        "id": "to_number",
        "name": "转数字",
        "name_en": "To Number",
        "description": "转换为数字",
        "category": "type",
        "subcategory": "convert",
        "api_endpoint": "/api/to-number",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "任意值"}
        ],
        "icon": "hash"
    },
    "to_boolean": {
        "id": "to_boolean",
        "name": "转布尔",
        "name_en": "To Boolean",
        "description": "转换为布尔值",
        "category": "type",
        "subcategory": "convert",
        "api_endpoint": "/api/to-boolean",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "任意值"}
        ],
        "icon": "check-square"
    },
    "to_array": {
        "id": "to_array",
        "name": "转数组",
        "name_en": "To Array",
        "description": "转换为数组",
        "category": "type",
        "subcategory": "convert",
        "api_endpoint": "/api/to-array",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "任意值"}
        ],
        "icon": "list"
    },
    "to_object": {
        "id": "to_object",
        "name": "转对象",
        "name_en": "To Object",
        "description": "转换为对象",
        "category": "type",
        "subcategory": "convert",
        "api_endpoint": "/api/to-object",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "任意值"}
        ],
        "icon": "square"
    },
    "coalesce": {
        "id": "coalesce",
        "name": "空值合并",
        "name_en": "Coalesce",
        "description": "返回第一个非空值",
        "category": "type",
        "subcategory": "utility",
        "api_endpoint": "/api/coalesce",
        "method": "POST",
        "params": [
            {"name": "values", "type": "array", "required": True, "description": "值数组"}
        ],
        "icon": "git-merge"
    },
    "default_to": {
        "id": "default_to",
        "name": "默认值",
        "name_en": "Default To",
        "description": "为空值设置默认值",
        "category": "type",
        "subcategory": "utility",
        "api_endpoint": "/api/default-to",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "值"},
            {"name": "default", "type": "any", "required": True, "description": "默认值"}
        ],
        "icon": "plus"
    },
    "is_empty": {
        "id": "is_empty",
        "name": "空值检查",
        "name_en": "Is Empty",
        "description": "检查是否为空",
        "category": "type",
        "subcategory": "predicate",
        "api_endpoint": "/api/is-empty",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "任意值"}
        ],
        "icon": "minus"
    },

    # ========== 日期时间工具 ==========
    "parse_date": {
        "id": "parse_date",
        "name": "解析日期",
        "name_en": "Parse Date",
        "description": "解析日期字符串",
        "category": "datetime",
        "subcategory": "parse",
        "api_endpoint": "/api/parse-date",
        "method": "POST",
        "params": [
            {"name": "date_str", "type": "string", "required": True, "description": "日期字符串"},
            {"name": "format", "type": "string", "required": False, "description": "格式"}
        ],
        "icon": "calendar"
    },
    "format_date": {
        "id": "format_date",
        "name": "格式化日期",
        "name_en": "Format Date",
        "description": "格式化日期",
        "category": "datetime",
        "subcategory": "format",
        "api_endpoint": "/api/format-date",
        "method": "POST",
        "params": [
            {"name": "date_str", "type": "string", "required": True, "description": "日期字符串"},
            {"name": "format", "type": "string", "required": True, "description": "目标格式"}
        ],
        "icon": "calendar"
    },
    "add_days": {
        "id": "add_days",
        "name": "加天数",
        "name_en": "Add Days",
        "description": "日期加天数",
        "category": "datetime",
        "subcategory": "arithmetic",
        "api_endpoint": "/api/add-days",
        "method": "POST",
        "params": [
            {"name": "date_str", "type": "string", "required": True, "description": "日期字符串"},
            {"name": "days", "type": "number", "required": True, "description": "天数"}
        ],
        "icon": "plus"
    },
    "subtract_days": {
        "id": "subtract_days",
        "name": "减天数",
        "name_en": "Subtract Days",
        "description": "日期减天数",
        "category": "datetime",
        "subcategory": "arithmetic",
        "api_endpoint": "/api/subtract-days",
        "method": "POST",
        "params": [
            {"name": "date_str", "type": "string", "required": True, "description": "日期字符串"},
            {"name": "days", "type": "number", "required": True, "description": "天数"}
        ],
        "icon": "minus"
    },
    "days_between": {
        "id": "days_between",
        "name": "天数差",
        "name_en": "Days Between",
        "description": "计算两个日期天数差",
        "category": "datetime",
        "subcategory": "arithmetic",
        "api_endpoint": "/api/days-between",
        "method": "POST",
        "params": [
            {"name": "date1", "type": "string", "required": True, "description": "日期1"},
            {"name": "date2", "type": "string", "required": True, "description": "日期2"}
        ],
        "icon": "calendar"
    },
    "is_weekend": {
        "id": "is_weekend",
        "name": "周末检查",
        "name_en": "Is Weekend",
        "description": "检查是否为周末",
        "category": "datetime",
        "subcategory": "predicate",
        "api_endpoint": "/api/is-weekend",
        "method": "POST",
        "params": [
            {"name": "date_str", "type": "string", "required": True, "description": "日期字符串"}
        ],
        "icon": "check"
    },
    "is_weekday": {
        "id": "is_weekday",
        "name": "工作日检查",
        "name_en": "Is Weekday",
        "description": "检查是否为工作日",
        "category": "datetime",
        "subcategory": "predicate",
        "api_endpoint": "/api/is-weekday",
        "method": "POST",
        "params": [
            {"name": "date_str", "type": "string", "required": True, "description": "日期字符串"}
        ],
        "icon": "check"
    },
    "get_weekday": {
        "id": "get_weekday",
        "name": "获取星期",
        "name_en": "Get Weekday",
        "description": "获取星期几",
        "category": "datetime",
        "subcategory": "access",
        "api_endpoint": "/api/get-weekday",
        "method": "POST",
        "params": [
            {"name": "date_str", "type": "string", "required": True, "description": "日期字符串"}
        ],
        "icon": "calendar"
    },
    "start_of_day": {
        "id": "start_of_day",
        "name": "一天开始",
        "name_en": "Start Of Day",
        "description": "获取一天开始时间",
        "category": "datetime",
        "subcategory": "truncate",
        "api_endpoint": "/api/start-of-day",
        "method": "POST",
        "params": [
            {"name": "date_str", "type": "string", "required": True, "description": "日期字符串"}
        ],
        "icon": "sunrise"
    },
    "end_of_day": {
        "id": "end_of_day",
        "name": "一天结束",
        "name_en": "End Of Day",
        "description": "获取一天结束时间",
        "category": "datetime",
        "subcategory": "truncate",
        "api_endpoint": "/api/end-of-day",
        "method": "POST",
        "params": [
            {"name": "date_str", "type": "string", "required": True, "description": "日期字符串"}
        ],
        "icon": "sunset"
    },
    "start_of_week": {
        "id": "start_of_week",
        "name": "一周开始",
        "name_en": "Start Of Week",
        "description": "获取一周开始日期",
        "category": "datetime",
        "subcategory": "truncate",
        "api_endpoint": "/api/start-of-week",
        "method": "POST",
        "params": [
            {"name": "date_str", "type": "string", "required": True, "description": "日期字符串"}
        ],
        "icon": "calendar"
    },
    "start_of_month": {
        "id": "start_of_month",
        "name": "一月开始",
        "name_en": "Start Of Month",
        "description": "获取一月开始日期",
        "category": "datetime",
        "subcategory": "truncate",
        "api_endpoint": "/api/start-of-month",
        "method": "POST",
        "params": [
            {"name": "date_str", "type": "string", "required": True, "description": "日期字符串"}
        ],
        "icon": "calendar"
    },
    "end_of_month": {
        "id": "end_of_month",
        "name": "一月结束",
        "name_en": "End Of Month",
        "description": "获取一月结束日期",
        "category": "datetime",
        "subcategory": "truncate",
        "api_endpoint": "/api/end-of-month",
        "method": "POST",
        "params": [
            {"name": "date_str", "type": "string", "required": True, "description": "日期字符串"}
        ],
        "icon": "calendar"
    },
    "diff_hours": {
        "id": "diff_hours",
        "name": "小时差",
        "name_en": "Diff Hours",
        "description": "计算小时差",
        "category": "datetime",
        "subcategory": "arithmetic",
        "api_endpoint": "/api/diff-hours",
        "method": "POST",
        "params": [
            {"name": "date1", "type": "string", "required": True, "description": "日期1"},
            {"name": "date2", "type": "string", "required": True, "description": "日期2"}
        ],
        "icon": "clock"
    },
    "diff_minutes": {
        "id": "diff_minutes",
        "name": "分钟差",
        "name_en": "Diff Minutes",
        "description": "计算分钟差",
        "category": "datetime",
        "subcategory": "arithmetic",
        "api_endpoint": "/api/diff-minutes",
        "method": "POST",
        "params": [
            {"name": "date1", "type": "string", "required": True, "description": "日期1"},
            {"name": "date2", "type": "string", "required": True, "description": "日期2"}
        ],
        "icon": "clock"
    },
    "unix_timestamp": {
        "id": "unix_timestamp",
        "name": "Unix时间戳",
        "name_en": "Unix Timestamp",
        "description": "获取Unix时间戳",
        "category": "datetime",
        "subcategory": "convert",
        "api_endpoint": "/api/unix-timestamp",
        "method": "POST",
        "params": [
            {"name": "date_str", "type": "string", "required": True, "description": "日期字符串"}
        ],
        "icon": "hash"
    },
    "from_timestamp": {
        "id": "from_timestamp",
        "name": "从时间戳",
        "name_en": "From Timestamp",
        "description": "从时间戳获取日期",
        "category": "datetime",
        "subcategory": "convert",
        "api_endpoint": "/api/from-timestamp",
        "method": "POST",
        "params": [
            {"name": "timestamp", "type": "number", "required": True, "description": "时间戳"}
        ],
        "icon": "calendar"
    },
    "is_valid_date": {
        "id": "is_valid_date",
        "name": "日期有效性",
        "name_en": "Is Valid Date",
        "description": "检查日期是否有效",
        "category": "datetime",
        "subcategory": "predicate",
        "api_endpoint": "/api/is-valid-date",
        "method": "POST",
        "params": [
            {"name": "date_str", "type": "string", "required": True, "description": "日期字符串"},
            {"name": "format", "type": "string", "required": False, "description": "格式"}
        ],
        "icon": "check"
    },

    # ========== 加密工具 ==========
    "hash_md5": {
        "id": "hash_md5",
        "name": "MD5哈希",
        "name_en": "MD5 Hash",
        "description": "计算MD5哈希",
        "category": "crypto",
        "subcategory": "hash",
        "api_endpoint": "/api/hash-md5",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "lock"
    },
    "hash_sha1": {
        "id": "hash_sha1",
        "name": "SHA1哈希",
        "name_en": "SHA1 Hash",
        "description": "计算SHA1哈希",
        "category": "crypto",
        "subcategory": "hash",
        "api_endpoint": "/api/hash-sha1",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "lock"
    },
    "hash_sha256": {
        "id": "hash_sha256",
        "name": "SHA256哈希",
        "name_en": "SHA256 Hash",
        "description": "计算SHA256哈希",
        "category": "crypto",
        "subcategory": "hash",
        "api_endpoint": "/api/hash-sha256",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "lock"
    },
    "hash_sha512": {
        "id": "hash_sha512",
        "name": "SHA512哈希",
        "name_en": "SHA512 Hash",
        "description": "计算SHA512哈希",
        "category": "crypto",
        "subcategory": "hash",
        "api_endpoint": "/api/hash-sha512",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "lock"
    },
    "bcrypt_hash": {
        "id": "bcrypt_hash",
        "name": "Bcrypt哈希",
        "name_en": "Bcrypt Hash",
        "description": "Bcrypt加密",
        "category": "crypto",
        "subcategory": "hash",
        "api_endpoint": "/api/bcrypt-hash",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "rounds", "type": "number", "required": False, "description": "轮数"}
        ],
        "icon": "lock"
    },
    "bcrypt_verify": {
        "id": "bcrypt_verify",
        "name": "Bcrypt验证",
        "name_en": "Bcrypt Verify",
        "description": "验证Bcrypt哈希",
        "category": "crypto",
        "subcategory": "verify",
        "api_endpoint": "/api/bcrypt-verify",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "hash", "type": "string", "required": True, "description": "哈希值"}
        ],
        "icon": "check-circle"
    },
    "aes_encrypt": {
        "id": "aes_encrypt",
        "name": "AES加密",
        "name_en": "AES Encrypt",
        "description": "AES对称加密",
        "category": "crypto",
        "subcategory": "encrypt",
        "api_endpoint": "/api/aes-encrypt",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "key", "type": "string", "required": True, "description": "密钥"}
        ],
        "icon": "lock"
    },
    "aes_decrypt": {
        "id": "aes_decrypt",
        "name": "AES解密",
        "name_en": "AES Decrypt",
        "description": "AES对称解密",
        "category": "crypto",
        "subcategory": "decrypt",
        "api_endpoint": "/api/aes-decrypt",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "密文"},
            {"name": "key", "type": "string", "required": True, "description": "密钥"}
        ],
        "icon": "unlock"
    },
    "rsa_generate": {
        "id": "rsa_generate",
        "name": "RSA生成",
        "name_en": "RSA Generate",
        "description": "生成RSA密钥对",
        "category": "crypto",
        "subcategory": "key",
        "api_endpoint": "/api/rsa-generate",
        "method": "POST",
        "params": [
            {"name": "bits", "type": "number", "required": False, "description": "密钥位数"}
        ],
        "icon": "key"
    },
    "rsa_encrypt": {
        "id": "rsa_encrypt",
        "name": "RSA加密",
        "name_en": "RSA Encrypt",
        "description": "RSA公钥加密",
        "category": "crypto",
        "subcategory": "encrypt",
        "api_endpoint": "/api/rsa-encrypt",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "public_key", "type": "string", "required": True, "description": "公钥"}
        ],
        "icon": "lock"
    },
    "rsa_decrypt": {
        "id": "rsa_decrypt",
        "name": "RSA解密",
        "name_en": "RSA Decrypt",
        "description": "RSA私钥解密",
        "category": "crypto",
        "subcategory": "decrypt",
        "api_endpoint": "/api/rsa-decrypt",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "密文"},
            {"name": "private_key", "type": "string", "required": True, "description": "私钥"}
        ],
        "icon": "unlock"
    },
    "hmac_sha256": {
        "id": "hmac_sha256",
        "name": "HMAC-SHA256",
        "name_en": "HMAC SHA256",
        "description": "计算HMAC-SHA256",
        "category": "crypto",
        "subcategory": "hash",
        "api_endpoint": "/api/hmac-sha256",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "key", "type": "string", "required": True, "description": "密钥"}
        ],
        "icon": "key"
    },
    "generate_uuid": {
        "id": "generate_uuid",
        "name": "生成UUID",
        "name_en": "Generate UUID",
        "description": "生成UUID",
        "category": "crypto",
        "subcategory": "generate",
        "api_endpoint": "/api/generate-uuid",
        "method": "POST",
        "params": [],
        "icon": "hash"
    },
    "generate_random": {
        "id": "generate_random",
        "name": "生成随机数",
        "name_en": "Generate Random",
        "description": "生成随机数",
        "category": "crypto",
        "subcategory": "generate",
        "api_endpoint": "/api/generate-random",
        "method": "POST",
        "params": [
            {"name": "min", "type": "number", "required": False, "description": "最小值"},
            {"name": "max", "type": "number", "required": False, "description": "最大值"}
        ],
        "icon": "hash"
    },

    # ========== 颜色工具 ==========
    "hex_to_rgb": {
        "id": "hex_to_rgb",
        "name": "HEX转RGB",
        "name_en": "HEX to RGB",
        "description": "HEX颜色转RGB",
        "category": "color",
        "subcategory": "convert",
        "api_endpoint": "/api/hex-to-rgb",
        "method": "POST",
        "params": [
            {"name": "hex", "type": "string", "required": True, "description": "HEX颜色"}
        ],
        "icon": "palette"
    },
    "rgb_to_hex": {
        "id": "rgb_to_hex",
        "name": "RGB转HEX",
        "name_en": "RGB to HEX",
        "description": "RGB转HEX颜色",
        "category": "color",
        "subcategory": "convert",
        "api_endpoint": "/api/rgb-to-hex",
        "method": "POST",
        "params": [
            {"name": "r", "type": "number", "required": True, "description": "红色"},
            {"name": "g", "type": "number", "required": True, "description": "绿色"},
            {"name": "b", "type": "number", "required": True, "description": "蓝色"}
        ],
        "icon": "palette"
    },
    "rgb_to_hsl": {
        "id": "rgb_to_hsl",
        "name": "RGB转HSL",
        "name_en": "RGB to HSL",
        "description": "RGB转HSL颜色",
        "category": "color",
        "subcategory": "convert",
        "api_endpoint": "/api/rgb-to-hsl",
        "method": "POST",
        "params": [
            {"name": "r", "type": "number", "required": True, "description": "红色"},
            {"name": "g", "type": "number", "required": True, "description": "绿色"},
            {"name": "b", "type": "number", "required": True, "description": "蓝色"}
        ],
        "icon": "palette"
    },
    "hsl_to_rgb": {
        "id": "hsl_to_rgb",
        "name": "HSL转RGB",
        "name_en": "HSL to RGB",
        "description": "HSL转RGB颜色",
        "category": "color",
        "subcategory": "convert",
        "api_endpoint": "/api/hsl-to-rgb",
        "method": "POST",
        "params": [
            {"name": "h", "type": "number", "required": True, "description": "色调"},
            {"name": "s", "type": "number", "required": True, "description": "饱和度"},
            {"name": "l", "type": "number", "required": True, "description": "亮度"}
        ],
        "icon": "palette"
    },
    "lighten": {
        "id": "lighten",
        "name": "提亮颜色",
        "name_en": "Lighten",
        "description": "提亮颜色",
        "category": "color",
        "subcategory": "transform",
        "api_endpoint": "/api/lighten",
        "method": "POST",
        "params": [
            {"name": "hex", "type": "string", "required": True, "description": "HEX颜色"},
            {"name": "amount", "type": "number", "required": False, "description": "提亮量"}
        ],
        "icon": "sun"
    },
    "darken": {
        "id": "darken",
        "name": "暗化颜色",
        "name_en": "Darken",
        "description": "暗化颜色",
        "category": "color",
        "subcategory": "transform",
        "api_endpoint": "/api/darken",
        "method": "POST",
        "params": [
            {"name": "hex", "type": "string", "required": True, "description": "HEX颜色"},
            {"name": "amount", "type": "number", "required": False, "description": "暗化量"}
        ],
        "icon": "moon"
    },
    "is_valid_color": {
        "id": "is_valid_color",
        "name": "颜色有效性",
        "name_en": "Is Valid Color",
        "description": "检查颜色是否有效",
        "category": "color",
        "subcategory": "predicate",
        "api_endpoint": "/api/is-valid-color",
        "method": "POST",
        "params": [
            {"name": "color", "type": "string", "required": True, "description": "颜色值"}
        ],
        "icon": "check"
    },

    # ========== URL工具 ==========
    "parse_url": {
        "id": "parse_url",
        "name": "解析URL",
        "name_en": "Parse URL",
        "description": "解析URL各部分",
        "category": "url",
        "subcategory": "parse",
        "api_endpoint": "/api/parse-url",
        "method": "POST",
        "params": [
            {"name": "url", "type": "string", "required": True, "description": "URL"}
        ],
        "icon": "link"
    },
    "build_url": {
        "id": "build_url",
        "name": "构建URL",
        "name_en": "Build URL",
        "description": "构建完整URL",
        "category": "url",
        "subcategory": "build",
        "api_endpoint": "/api/build-url",
        "method": "POST",
        "params": [
            {"name": "scheme", "type": "string", "required": True, "description": "协议"},
            {"name": "host", "type": "string", "required": True, "description": "主机"},
            {"name": "path", "type": "string", "required": False, "description": "路径"},
            {"name": "query", "type": "object", "required": False, "description": "查询参数"}
        ],
        "icon": "link"
    },
    "get_query_params": {
        "id": "get_query_params",
        "name": "获取查询参数",
        "name_en": "Get Query Params",
        "description": "从URL获取查询参数",
        "category": "url",
        "subcategory": "access",
        "api_endpoint": "/api/get-query-params",
        "method": "POST",
        "params": [
            {"name": "url", "type": "string", "required": True, "description": "URL"}
        ],
        "icon": "search"
    },
    "add_query_param": {
        "id": "add_query_param",
        "name": "添加查询参数",
        "name_en": "Add Query Param",
        "description": "给URL添加查询参数",
        "category": "url",
        "subcategory": "mutate",
        "api_endpoint": "/api/add-query-param",
        "method": "POST",
        "params": [
            {"name": "url", "type": "string", "required": True, "description": "URL"},
            {"name": "key", "type": "string", "required": True, "description": "参数名"},
            {"name": "value", "type": "string", "required": True, "description": "参数值"}
        ],
        "icon": "plus"
    },
    "remove_query_param": {
        "id": "remove_query_param",
        "name": "删除查询参数",
        "name_en": "Remove Query Param",
        "description": "从URL删除查询参数",
        "category": "url",
        "subcategory": "mutate",
        "api_endpoint": "/api/remove-query-param",
        "method": "POST",
        "params": [
            {"name": "url", "type": "string", "required": True, "description": "URL"},
            {"name": "key", "type": "string", "required": True, "description": "参数名"}
        ],
        "icon": "minus"
    },
    "is_valid_url": {
        "id": "is_valid_url",
        "name": "URL有效性",
        "name_en": "Is Valid URL",
        "description": "检查URL是否有效",
        "category": "url",
        "subcategory": "predicate",
        "api_endpoint": "/api/is-valid-url",
        "method": "POST",
        "params": [
            {"name": "url", "type": "string", "required": True, "description": "URL"}
        ],
        "icon": "check"
    },
    "encode_uri": {
        "id": "encode_uri",
        "name": "URI编码",
        "name_en": "Encode URI",
        "description": "URI编码",
        "category": "url",
        "subcategory": "encode",
        "api_endpoint": "/api/encode-uri",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "lock"
    },
    "decode_uri": {
        "id": "decode_uri",
        "name": "URI解码",
        "name_en": "Decode URI",
        "description": "URI解码",
        "category": "url",
        "subcategory": "decode",
        "api_endpoint": "/api/decode-uri",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "unlock"
    },

    # ========== 文件工具 ==========
    "get_extension": {
        "id": "get_extension",
        "name": "获取扩展名",
        "name_en": "Get Extension",
        "description": "获取文件扩展名",
        "category": "file",
        "subcategory": "access",
        "api_endpoint": "/api/get-extension",
        "method": "POST",
        "params": [
            {"name": "filename", "type": "string", "required": True, "description": "文件名"}
        ],
        "icon": "file"
    },
    "remove_extension": {
        "id": "remove_extension",
        "name": "去除扩展名",
        "name_en": "Remove Extension",
        "description": "去除文件扩展名",
        "category": "file",
        "subcategory": "transform",
        "api_endpoint": "/api/remove-extension",
        "method": "POST",
        "params": [
            {"name": "filename", "type": "string", "required": True, "description": "文件名"}
        ],
        "icon": "file"
    },
    "add_extension": {
        "id": "add_extension",
        "name": "添加扩展名",
        "name_en": "Add Extension",
        "description": "添加文件扩展名",
        "category": "file",
        "subcategory": "transform",
        "api_endpoint": "/api/add-extension",
        "method": "POST",
        "params": [
            {"name": "filename", "type": "string", "required": True, "description": "文件名"},
            {"name": "ext", "type": "string", "required": True, "description": "扩展名"}
        ],
        "icon": "file-plus"
    },
    "change_extension": {
        "id": "change_extension",
        "name": "更改扩展名",
        "name_en": "Change Extension",
        "description": "更改文件扩展名",
        "category": "file",
        "subcategory": "transform",
        "api_endpoint": "/api/change-extension",
        "method": "POST",
        "params": [
            {"name": "filename", "type": "string", "required": True, "description": "文件名"},
            {"name": "new_ext", "type": "string", "required": True, "description": "新扩展名"}
        ],
        "icon": "file"
    },
    "get_basename": {
        "id": "get_basename",
        "name": "获取基名",
        "name_en": "Get Basename",
        "description": "获取文件名基名",
        "category": "file",
        "subcategory": "access",
        "api_endpoint": "/api/get-basename",
        "method": "POST",
        "params": [
            {"name": "path", "type": "string", "required": True, "description": "路径"}
        ],
        "icon": "file"
    },
    "get_dirname": {
        "id": "get_dirname",
        "name": "获取目录名",
        "name_en": "Get Dirname",
        "description": "获取目录路径",
        "category": "file",
        "subcategory": "access",
        "api_endpoint": "/api/get-dirname",
        "method": "POST",
        "params": [
            {"name": "path", "type": "string", "required": True, "description": "路径"}
        ],
        "icon": "folder"
    },
    "join_path": {
        "id": "join_path",
        "name": "连接路径",
        "name_en": "Join Path",
        "description": "连接路径片段",
        "category": "file",
        "subcategory": "transform",
        "api_endpoint": "/api/join-path",
        "method": "POST",
        "params": [
            {"name": "parts", "type": "array", "required": True, "description": "路径片段"}
        ],
        "icon": "link"
    },
    "normalize_path": {
        "id": "normalize_path",
        "name": "规范化路径",
        "name_en": "Normalize Path",
        "description": "规范化文件路径",
        "category": "file",
        "subcategory": "transform",
        "api_endpoint": "/api/normalize-path",
        "method": "POST",
        "params": [
            {"name": "path", "type": "string", "required": True, "description": "路径"}
        ],
        "icon": "file"
    },
    "is_absolute": {
        "id": "is_absolute",
        "name": "绝对路径检查",
        "name_en": "Is Absolute",
        "description": "检查是否为绝对路径",
        "category": "file",
        "subcategory": "predicate",
        "api_endpoint": "/api/is-absolute",
        "method": "POST",
        "params": [
            {"name": "path", "type": "string", "required": True, "description": "路径"}
        ],
        "icon": "check"
    },
    "file_size": {
        "id": "file_size",
        "name": "文件大小",
        "name_en": "File Size",
        "description": "格式化文件大小",
        "category": "file",
        "subcategory": "analyze",
        "api_endpoint": "/api/file-size",
        "method": "POST",
        "params": [
            {"name": "bytes", "type": "number", "required": True, "description": "字节数"}
        ],
        "icon": "hard-drive"
    },

    # ========== 格式化工具 ==========
    "format_bytes": {
        "id": "format_bytes",
        "name": "格式化字节",
        "name_en": "Format Bytes",
        "description": "格式化字节数",
        "category": "format",
        "subcategory": "number",
        "api_endpoint": "/api/format-bytes",
        "method": "POST",
        "params": [
            {"name": "bytes", "type": "number", "required": True, "description": "字节数"}
        ],
        "icon": "hard-drive"
    },
    "format_number": {
        "id": "format_number",
        "name": "格式化数字",
        "name_en": "Format Number",
        "description": "格式化数字",
        "category": "format",
        "subcategory": "number",
        "api_endpoint": "/api/format-number",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "数字"},
            {"name": "decimals", "type": "number", "required": False, "description": "小数位"}
        ],
        "icon": "hash"
    },
    "format_currency": {
        "id": "format_currency",
        "name": "格式化货币",
        "name_en": "Format Currency",
        "description": "格式化货币",
        "category": "format",
        "subcategory": "number",
        "api_endpoint": "/api/format-currency",
        "method": "POST",
        "params": [
            {"name": "amount", "type": "number", "required": True, "description": "金额"},
            {"name": "currency", "type": "string", "required": False, "description": "货币代码"}
        ],
        "icon": "dollar-sign"
    },
    "format_percentage": {
        "id": "format_percentage",
        "name": "格式化百分比",
        "name_en": "Format Percentage",
        "description": "格式化百分比",
        "category": "format",
        "subcategory": "number",
        "api_endpoint": "/api/format-percentage",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "数字"},
            {"name": "decimals", "type": "number", "required": False, "description": "小数位"}
        ],
        "icon": "percent"
    },
    "pluralize": {
        "id": "pluralize",
        "name": "复数化",
        "name_en": "Pluralize",
        "description": "单词复数化",
        "category": "format",
        "subcategory": "string",
        "api_endpoint": "/api/pluralize",
        "method": "POST",
        "params": [
            {"name": "word", "type": "string", "required": True, "description": "单词"},
            {"name": "count", "type": "number", "required": True, "description": "数量"}
        ],
        "icon": "text"
    },
    "camel_to_snake": {
        "id": "camel_to_snake",
        "name": "驼峰转蛇形",
        "name_en": "Camel to Snake",
        "description": "驼峰命名转蛇形",
        "category": "format",
        "subcategory": "string",
        "api_endpoint": "/api/camel-to-snake",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "arrow-down"
    },
    "snake_to_camel": {
        "id": "snake_to_camel",
        "name": "蛇形转驼峰",
        "name_en": "Snake to Camel",
        "description": "蛇形命名转驼峰",
        "category": "format",
        "subcategory": "string",
        "api_endpoint": "/api/snake-to-camel",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "arrow-up"
    },
    "strip_tags": {
        "id": "strip_tags",
        "name": "去除HTML标签",
        "name_en": "Strip Tags",
        "description": "去除HTML标签",
        "category": "format",
        "subcategory": "string",
        "api_endpoint": "/api/strip-tags",
        "method": "POST",
        "params": [
            {"name": "html", "type": "string", "required": True, "description": "HTML文本"}
        ],
        "icon": "code"
    },
    "escape_html": {
        "id": "escape_html",
        "name": "HTML转义",
        "name_en": "Escape HTML",
        "description": "HTML特殊字符转义",
        "category": "format",
        "subcategory": "string",
        "api_endpoint": "/api/escape-html",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "code"
    },
    "unescape_html": {
        "id": "unescape_html",
        "name": "HTML反转义",
        "name_en": "Unescape HTML",
        "description": "HTML反转义",
        "category": "format",
        "subcategory": "string",
        "api_endpoint": "/api/unescape-html",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "code"
    },

    # ========== 验证工具 ==========
    "is_valid_email": {
        "id": "is_valid_email",
        "name": "邮箱验证",
        "name_en": "Is Valid Email",
        "description": "验证邮箱格式",
        "category": "validate",
        "subcategory": "format",
        "api_endpoint": "/api/validate/email",
        "method": "POST",
        "params": [
            {"name": "email", "type": "string", "required": True, "description": "邮箱"}
        ],
        "icon": "mail"
    },
    "is_valid_phone": {
        "id": "is_valid_phone",
        "name": "手机验证",
        "name_en": "Is Valid Phone",
        "description": "验证手机号格式",
        "category": "validate",
        "subcategory": "format",
        "api_endpoint": "/api/validate/phone",
        "method": "POST",
        "params": [
            {"name": "phone", "type": "string", "required": True, "description": "手机号"},
            {"name": "country", "type": "string", "required": False, "description": "国家"}
        ],
        "icon": "phone"
    },
    "is_valid_ip": {
        "id": "is_valid_ip",
        "name": "IP地址验证",
        "name_en": "Is Valid IP",
        "description": "验证IP地址格式",
        "category": "validate",
        "subcategory": "format",
        "api_endpoint": "/api/validate/ip",
        "method": "POST",
        "params": [
            {"name": "ip", "type": "string", "required": True, "description": "IP地址"},
            {"name": "version", "type": "number", "required": False, "description": "版本"}
        ],
        "icon": "globe"
    },
    "is_valid_cidr": {
        "id": "is_valid_cidr",
        "name": "CIDR验证",
        "name_en": "Is Valid CIDR",
        "description": "验证CIDR格式",
        "category": "validate",
        "subcategory": "format",
        "api_endpoint": "/api/validate/cidr",
        "method": "POST",
        "params": [
            {"name": "cidr", "type": "string", "required": True, "description": "CIDR"}
        ],
        "icon": "globe"
    },
    "is_valid_json": {
        "id": "is_valid_json",
        "name": "JSON验证",
        "name_en": "Is Valid JSON",
        "description": "验证JSON格式",
        "category": "validate",
        "subcategory": "format",
        "api_endpoint": "/api/validate/json",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "file"
    },
    "is_valid_uuid": {
        "id": "is_valid_uuid",
        "name": "UUID验证",
        "name_en": "Is Valid UUID",
        "description": "验证UUID格式",
        "category": "validate",
        "subcategory": "format",
        "api_endpoint": "/api/validate/uuid",
        "method": "POST",
        "params": [
            {"name": "uuid", "type": "string", "required": True, "description": "UUID"}
        ],
        "icon": "hash"
    },
    "is_valid_credit_card": {
        "id": "is_valid_credit_card",
        "name": "信用卡验证",
        "name_en": "Is Valid Credit Card",
        "description": "验证信用卡号",
        "category": "validate",
        "subcategory": "format",
        "api_endpoint": "/api/validate/credit-card",
        "method": "POST",
        "params": [
            {"name": "card", "type": "string", "required": True, "description": "卡号"}
        ],
        "icon": "credit-card"
    },
    "validate_length": {
        "id": "validate_length",
        "name": "长度验证",
        "name_en": "Validate Length",
        "description": "验证字符串长度",
        "category": "validate",
        "subcategory": "range",
        "api_endpoint": "/api/validate/length",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "min", "type": "number", "required": False, "description": "最小长度"},
            {"name": "max", "type": "number", "required": False, "description": "最大长度"}
        ],
        "icon": "ruler"
    },
    "validate_range": {
        "id": "validate_range",
        "name": "范围验证",
        "name_en": "Validate Range",
        "description": "验证数字范围",
        "category": "validate",
        "subcategory": "range",
        "api_endpoint": "/api/validate/range",
        "method": "POST",
        "params": [
            {"name": "value", "type": "number", "required": True, "description": "数值"},
            {"name": "min", "type": "number", "required": True, "description": "最小值"},
            {"name": "max", "type": "number", "required": True, "description": "最大值"}
        ],
        "icon": "sliders"
    },
    "is_strong_password": {
        "id": "is_strong_password",
        "name": "强密码验证",
        "name_en": "Is Strong Password",
        "description": "验证密码强度",
        "category": "validate",
        "subcategory": "security",
        "api_endpoint": "/api/is-strong-password",
        "method": "POST",
        "params": [
            {"name": "password", "type": "string", "required": True, "description": "密码"}
        ],
        "icon": "shield"
    },
    "is_valid_hex_color": {
        "id": "is_valid_hex_color",
        "name": "十六进制颜色验证",
        "name_en": "Is Valid Hex Color",
        "description": "验证十六进制颜色",
        "category": "validate",
        "subcategory": "format",
        "api_endpoint": "/api/validate/hex-color",
        "method": "POST",
        "params": [
            {"name": "color", "type": "string", "required": True, "description": "颜色"}
        ],
        "icon": "palette"
    },

    # ========== 编码转换工具 ==========
    "encode_base64": {
        "id": "encode_base64",
        "name": "Base64编码",
        "name_en": "Base64 Encode",
        "description": "Base64编码",
        "category": "encoding",
        "subcategory": "encode",
        "api_endpoint": "/api/encode/base64",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "lock"
    },
    "decode_base64": {
        "id": "decode_base64",
        "name": "Base64解码",
        "name_en": "Base64 Decode",
        "description": "Base64解码",
        "category": "encoding",
        "subcategory": "decode",
        "api_endpoint": "/api/decode/base64",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "unlock"
    },
    "encode_url": {
        "id": "encode_url",
        "name": "URL编码",
        "name_en": "URL Encode",
        "description": "URL编码",
        "category": "encoding",
        "subcategory": "encode",
        "api_endpoint": "/api/encode/url",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "link"
    },
    "decode_url": {
        "id": "decode_url",
        "name": "URL解码",
        "name_en": "URL Decode",
        "description": "URL解码",
        "category": "encoding",
        "subcategory": "decode",
        "api_endpoint": "/api/decode/url",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "link"
    },
    "encode_hex": {
        "id": "encode_hex",
        "name": "十六进制编码",
        "name_en": "Hex Encode",
        "description": "文本转十六进制",
        "category": "encoding",
        "subcategory": "encode",
        "api_endpoint": "/api/encode/hex",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "hash"
    },
    "decode_hex": {
        "id": "decode_hex",
        "name": "十六进制解码",
        "name_en": "Hex Decode",
        "description": "十六进制转文本",
        "category": "encoding",
        "subcategory": "decode",
        "api_endpoint": "/api/decode/hex",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "十六进制文本"}
        ],
        "icon": "hash"
    },
    "encode_html": {
        "id": "encode_html",
        "name": "HTML编码",
        "name_en": "HTML Encode",
        "description": "HTML特殊字符编码",
        "category": "encoding",
        "subcategory": "encode",
        "api_endpoint": "/api/encode/html",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "code"
    },
    "decode_html": {
        "id": "decode_html",
        "name": "HTML解码",
        "name_en": "HTML Decode",
        "description": "HTML特殊字符解码",
        "category": "encoding",
        "subcategory": "decode",
        "api_endpoint": "/api/decode/html",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "code"
    },
    "encode_unicode": {
        "id": "encode_unicode",
        "name": "Unicode编码",
        "name_en": "Unicode Encode",
        "description": "Unicode转义",
        "category": "encoding",
        "subcategory": "encode",
        "api_endpoint": "/api/encode/unicode",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "type"
    },
    "decode_unicode": {
        "id": "decode_unicode",
        "name": "Unicode解码",
        "name_en": "Unicode Decode",
        "description": "Unicode转义还原",
        "category": "encoding",
        "subcategory": "decode",
        "api_endpoint": "/api/decode/unicode",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "type"
    },

    # ========== 数值转换工具 ==========
    "to_binary": {
        "id": "to_binary",
        "name": "转二进制",
        "name_en": "To Binary",
        "description": "数字转二进制",
        "category": "convert",
        "subcategory": "number",
        "api_endpoint": "/api/to-binary",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "数字"}
        ],
        "icon": "hash"
    },
    "from_binary": {
        "id": "from_binary",
        "name": "从二进制",
        "name_en": "From Binary",
        "description": "二进制转数字",
        "category": "convert",
        "subcategory": "number",
        "api_endpoint": "/api/from-binary",
        "method": "POST",
        "params": [
            {"name": "binary", "type": "string", "required": True, "description": "二进制字符串"}
        ],
        "icon": "hash"
    },
    "to_octal": {
        "id": "to_octal",
        "name": "转八进制",
        "name_en": "To Octal",
        "description": "数字转八进制",
        "category": "convert",
        "subcategory": "number",
        "api_endpoint": "/api/to-octal",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "数字"}
        ],
        "icon": "hash"
    },
    "from_octal": {
        "id": "from_octal",
        "name": "从八进制",
        "name_en": "From Octal",
        "description": "八进制转数字",
        "category": "convert",
        "subcategory": "number",
        "api_endpoint": "/api/from-octal",
        "method": "POST",
        "params": [
            {"name": "octal", "type": "string", "required": True, "description": "八进制字符串"}
        ],
        "icon": "hash"
    },
    "to_hex": {
        "id": "to_hex",
        "name": "转十六进制",
        "name_en": "To Hex",
        "description": "数字转十六进制",
        "category": "convert",
        "subcategory": "number",
        "api_endpoint": "/api/to-hex",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "数字"}
        ],
        "icon": "hash"
    },
    "from_hex": {
        "id": "from_hex",
        "name": "从十六进制",
        "name_en": "From Hex",
        "description": "十六进制转数字",
        "category": "convert",
        "subcategory": "number",
        "api_endpoint": "/api/from-hex",
        "method": "POST",
        "params": [
            {"name": "hex", "type": "string", "required": True, "description": "十六进制字符串"}
        ],
        "icon": "hash"
    },
    "to_words": {
        "id": "to_words",
        "name": "数字转文字",
        "name_en": "To Words",
        "description": "数字转中文文字",
        "category": "convert",
        "subcategory": "number",
        "api_endpoint": "/api/to-words",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "数字"}
        ],
        "icon": "type"
    },
    "to_ordinal": {
        "id": "to_ordinal",
        "name": "转序数词",
        "name_en": "To Ordinal",
        "description": "数字转序数词",
        "category": "convert",
        "subcategory": "number",
        "api_endpoint": "/api/to-ordinal",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "数字"}
        ],
        "icon": "hash"
    },

    # ========== 杂项工具 ==========
    "sleep": {
        "id": "sleep",
        "name": "延迟",
        "name_en": "Sleep",
        "description": "延迟执行",
        "category": "utility",
        "subcategory": "async",
        "api_endpoint": "/api/sleep",
        "method": "POST",
        "params": [
            {"name": "ms", "type": "number", "required": True, "description": "毫秒"}
        ],
        "icon": "clock"
    },
    "noop": {
        "id": "noop",
        "name": "空操作",
        "name_en": "Noop",
        "description": "什么都不做",
        "category": "utility",
        "subcategory": "basic",
        "api_endpoint": "/api/noop",
        "method": "POST",
        "params": [],
        "icon": "minus"
    },
    "always": {
        "id": "always",
        "name": "返回真",
        "name_en": "Always",
        "description": "总是返回true",
        "category": "utility",
        "subcategory": "function",
        "api_endpoint": "/api/always",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "返回值"}
        ],
        "icon": "check"
    },
    "never": {
        "id": "never",
        "name": "返回假",
        "name_en": "Never",
        "description": "总是返回false",
        "category": "utility",
        "subcategory": "function",
        "api_endpoint": "/api/never",
        "method": "POST",
        "params": [],
        "icon": "x"
    },
    "tap": {
        "id": "tap",
        "name": "点击",
        "name_en": "Tap",
        "description": "执行并返回值",
        "category": "utility",
        "subcategory": "function",
        "api_endpoint": "/api/tap",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "值"},
            {"name": "fn", "type": "string", "required": True, "description": "函数"}
        ],
        "icon": "pointer"
    },
    "juxt": {
        "id": "juxt",
        "name": "并列函数",
        "name_en": "Juxtapose",
        "description": "应用多个函数返回数组",
        "category": "utility",
        "subcategory": "function",
        "api_endpoint": "/api/juxt",
        "method": "POST",
        "params": [
            {"name": "fns", "type": "array", "required": True, "description": "函数数组"},
            {"name": "value", "type": "any", "required": True, "description": "值"}
        ],
        "icon": "columns"
    },
    "converge": {
        "id": "converge",
        "name": "收敛函数",
        "name_en": "Converge",
        "description": "收敛函数结果",
        "category": "utility",
        "subcategory": "function",
        "api_endpoint": "/api/converge",
        "method": "POST",
        "params": [
            {"name": "fns", "type": "array", "required": True, "description": "函数数组"},
            {"name": "fn", "type": "string", "required": True, "description": "最终函数"}
        ],
        "icon": "git-merge"
    },

    # ========== 逻辑工具 ==========
    "and": {
        "id": "and",
        "name": "逻辑与",
        "name_en": "Logical And",
        "description": "逻辑与运算",
        "category": "logic",
        "subcategory": "boolean",
        "api_endpoint": "/api/and",
        "method": "POST",
        "params": [
            {"name": "a", "type": "boolean", "required": True, "description": "值A"},
            {"name": "b", "type": "boolean", "required": True, "description": "值B"}
        ],
        "icon": "check-square"
    },
    "or": {
        "id": "or",
        "name": "逻辑或",
        "name_en": "Logical Or",
        "description": "逻辑或运算",
        "category": "logic",
        "subcategory": "boolean",
        "api_endpoint": "/api/or",
        "method": "POST",
        "params": [
            {"name": "a", "type": "boolean", "required": True, "description": "值A"},
            {"name": "b", "type": "boolean", "required": True, "description": "值B"}
        ],
        "icon": "check-square"
    },
    "not": {
        "id": "not",
        "name": "逻辑非",
        "name_en": "Logical Not",
        "description": "逻辑非运算",
        "category": "logic",
        "subcategory": "boolean",
        "api_endpoint": "/api/not",
        "method": "POST",
        "params": [
            {"name": "value", "type": "boolean", "required": True, "description": "值"}
        ],
        "icon": "x-square"
    },
    "xor": {
        "id": "xor",
        "name": "异或",
        "name_en": "XOR",
        "description": "异或运算",
        "category": "logic",
        "subcategory": "boolean",
        "api_endpoint": "/api/xor",
        "method": "POST",
        "params": [
            {"name": "a", "type": "boolean", "required": True, "description": "值A"},
            {"name": "b", "type": "boolean", "required": True, "description": "值B"}
        ],
        "icon": "git-branch"
    },
    "nand": {
        "id": "nand",
        "name": "与非",
        "name_en": "NAND",
        "description": "与非运算",
        "category": "logic",
        "subcategory": "boolean",
        "api_endpoint": "/api/nand",
        "method": "POST",
        "params": [
            {"name": "a", "type": "boolean", "required": True, "description": "值A"},
            {"name": "b", "type": "boolean", "required": True, "description": "值B"}
        ],
        "icon": "git-branch"
    },
    "nor": {
        "id": "nor",
        "name": "或非",
        "name_en": "NOR",
        "description": "或非运算",
        "category": "logic",
        "subcategory": "boolean",
        "api_endpoint": "/api/nor",
        "method": "POST",
        "params": [
            {"name": "a", "type": "boolean", "required": True, "description": "值A"},
            {"name": "b", "type": "boolean", "required": True, "description": "值B"}
        ],
        "icon": "git-branch"
    },

    # ========== 位运算工具 ==========
    "bit_and": {
        "id": "bit_and",
        "name": "按位与",
        "name_en": "Bitwise AND",
        "description": "按位与运算",
        "category": "bitwise",
        "subcategory": "operator",
        "api_endpoint": "/api/bit-and",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "值A"},
            {"name": "b", "type": "number", "required": True, "description": "值B"}
        ],
        "icon": "git-branch"
    },
    "bit_or": {
        "id": "bit_or",
        "name": "按位或",
        "name_en": "Bitwise OR",
        "description": "按位或运算",
        "category": "bitwise",
        "subcategory": "operator",
        "api_endpoint": "/api/bit-or",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "值A"},
            {"name": "b", "type": "number", "required": True, "description": "值B"}
        ],
        "icon": "git-branch"
    },
    "bit_xor": {
        "id": "bit_xor",
        "name": "按位异或",
        "name_en": "Bitwise XOR",
        "description": "按位异或运算",
        "category": "bitwise",
        "subcategory": "operator",
        "api_endpoint": "/api/bit-xor",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "值A"},
            {"name": "b", "type": "number", "required": True, "description": "值B"}
        ],
        "icon": "git-branch"
    },
    "bit_not": {
        "id": "bit_not",
        "name": "按位非",
        "name_en": "Bitwise NOT",
        "description": "按位非运算",
        "category": "bitwise",
        "subcategory": "operator",
        "api_endpoint": "/api/bit-not",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "值"}
        ],
        "icon": "git-branch"
    },
    "left_shift": {
        "id": "left_shift",
        "name": "左移",
        "name_en": "Left Shift",
        "description": "左移位运算",
        "category": "bitwise",
        "subcategory": "operator",
        "api_endpoint": "/api/left-shift",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "值"},
            {"name": "bits", "type": "number", "required": True, "description": "移位数"}
        ],
        "icon": "arrow-left"
    },
    "right_shift": {
        "id": "right_shift",
        "name": "右移",
        "name_en": "Right Shift",
        "description": "右移位运算",
        "category": "bitwise",
        "subcategory": "operator",
        "api_endpoint": "/api/right-shift",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "值"},
            {"name": "bits", "type": "number", "required": True, "description": "移位数"}
        ],
        "icon": "arrow-right"
    },

    # ========== 比较工具 ==========
    "eq": {
        "id": "eq",
        "name": "等于",
        "name_en": "Equal",
        "description": "严格相等",
        "category": "compare",
        "subcategory": "operator",
        "api_endpoint": "/api/eq",
        "method": "POST",
        "params": [
            {"name": "a", "type": "any", "required": True, "description": "值A"},
            {"name": "b", "type": "any", "required": True, "description": "值B"}
        ],
        "icon": "equal"
    },
    "neq": {
        "id": "neq",
        "name": "不等于",
        "name_en": "Not Equal",
        "description": "不等于",
        "category": "compare",
        "subcategory": "operator",
        "api_endpoint": "/api/neq",
        "method": "POST",
        "params": [
            {"name": "a", "type": "any", "required": True, "description": "值A"},
            {"name": "b", "type": "any", "required": True, "description": "值B"}
        ],
        "icon": "not-equal"
    },
    "gt": {
        "id": "gt",
        "name": "大于",
        "name_en": "Greater Than",
        "description": "大于",
        "category": "compare",
        "subcategory": "operator",
        "api_endpoint": "/api/gt",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "值A"},
            {"name": "b", "type": "number", "required": True, "description": "值B"}
        ],
        "icon": "chevron-right"
    },
    "gte": {
        "id": "gte",
        "name": "大于等于",
        "name_en": "Greater Than or Equal",
        "description": "大于等于",
        "category": "compare",
        "subcategory": "operator",
        "api_endpoint": "/api/gte",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "值A"},
            {"name": "b", "type": "number", "required": True, "description": "值B"}
        ],
        "icon": "chevrons-right"
    },
    "lt": {
        "id": "lt",
        "name": "小于",
        "name_en": "Less Than",
        "description": "小于",
        "category": "compare",
        "subcategory": "operator",
        "api_endpoint": "/api/lt",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "值A"},
            {"name": "b", "type": "number", "required": True, "description": "值B"}
        ],
        "icon": "chevron-left"
    },
    "lte": {
        "id": "lte",
        "name": "小于等于",
        "name_en": "Less Than or Equal",
        "description": "小于等于",
        "category": "compare",
        "subcategory": "operator",
        "api_endpoint": "/api/lte",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "值A"},
            {"name": "b", "type": "number", "required": True, "description": "值B"}
        ],
        "icon": "chevrons-left"
    },
    "between": {
        "id": "between",
        "name": "范围内",
        "name_en": "Between",
        "description": "值是否在范围内",
        "category": "compare",
        "subcategory": "operator",
        "api_endpoint": "/api/between",
        "method": "POST",
        "params": [
            {"name": "value", "type": "number", "required": True, "description": "值"},
            {"name": "min", "type": "number", "required": True, "description": "最小值"},
            {"name": "max", "type": "number", "required": True, "description": "最大值"}
        ],
        "icon": "check-circle"
    },
    "compare": {
        "id": "compare",
        "name": "比较",
        "name_en": "Compare",
        "description": "比较两个值返回-1/0/1",
        "category": "compare",
        "subcategory": "operator",
        "api_endpoint": "/api/compare",
        "method": "POST",
        "params": [
            {"name": "a", "type": "any", "required": True, "description": "值A"},
            {"name": "b", "type": "any", "required": True, "description": "值B"}
        ],
        "icon": "arrow-left-right"
    },

    # ========== 条件工具 ==========
    "if_then": {
        "id": "if_then",
        "name": "条件执行",
        "name_en": "If Then",
        "description": "条件为真则执行",
        "category": "conditional",
        "subcategory": "operator",
        "api_endpoint": "/api/if-then",
        "method": "POST",
        "params": [
            {"name": "condition", "type": "boolean", "required": True, "description": "条件"},
            {"name": "then", "type": "any", "required": True, "description": "真时返回值"},
            {"name": "else", "type": "any", "required": False, "description": "假时返回值"}
        ],
        "icon": "git-branch"
    },
    "switch": {
        "id": "switch",
        "name": "分支选择",
        "name_en": "Switch",
        "description": "根据值选择分支",
        "category": "conditional",
        "subcategory": "operator",
        "api_endpoint": "/api/switch",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "值"},
            {"name": "cases", "type": "object", "required": True, "description": "case映射"}
        ],
        "icon": "git-branch"
    },
    "match": {
        "id": "match",
        "name": "模式匹配",
        "name_en": "Match",
        "description": "模式匹配",
        "category": "conditional",
        "subcategory": "operator",
        "api_endpoint": "/api/match",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "值"},
            {"name": "patterns", "type": "array", "required": True, "description": "模式数组"}
        ],
        "icon": "git-branch"
    },

    # ========== 三元运算符 ==========
    "ternary": {
        "id": "ternary",
        "name": "三元运算",
        "name_en": "Ternary",
        "description": "三元表达式",
        "category": "conditional",
        "subcategory": "operator",
        "api_endpoint": "/api/ternary",
        "method": "POST",
        "params": [
            {"name": "condition", "type": "boolean", "required": True, "description": "条件"},
            {"name": "true_val", "type": "any", "required": True, "description": "真值"},
            {"name": "false_val", "type": "any", "required": True, "description": "假值"}
        ],
        "icon": "git-branch"
    },

    # ========== 集合工具 ==========
    "union": {
        "id": "union",
        "name": "集合并集",
        "name_en": "Set Union",
        "description": "集合并集",
        "category": "set",
        "subcategory": "operator",
        "api_endpoint": "/api/set/union",
        "method": "POST",
        "params": [
            {"name": "a", "type": "array", "required": True, "description": "集合A"},
            {"name": "b", "type": "array", "required": True, "description": "集合B"}
        ],
        "icon": "git-merge"
    },
    "intersection": {
        "id": "intersection",
        "name": "集合交集",
        "name_en": "Set Intersection",
        "description": "集合交集",
        "category": "set",
        "subcategory": "operator",
        "api_endpoint": "/api/set/intersection",
        "method": "POST",
        "params": [
            {"name": "a", "type": "array", "required": True, "description": "集合A"},
            {"name": "b", "type": "array", "required": True, "description": "集合B"}
        ],
        "icon": "git-intersect"
    },
    "difference": {
        "id": "difference",
        "name": "集合差集",
        "name_en": "Set Difference",
        "description": "集合差集",
        "category": "set",
        "subcategory": "operator",
        "api_endpoint": "/api/set/difference",
        "method": "POST",
        "params": [
            {"name": "a", "type": "array", "required": True, "description": "集合A"},
            {"name": "b", "type": "array", "required": True, "description": "集合B"}
        ],
        "icon": "git-merge"
    },
    "symmetric_diff": {
        "id": "symmetric_diff",
        "name": "对称差集",
        "name_en": "Symmetric Difference",
        "description": "集合对称差集",
        "category": "set",
        "subcategory": "operator",
        "api_endpoint": "/api/set/symmetric-diff",
        "method": "POST",
        "params": [
            {"name": "a", "type": "array", "required": True, "description": "集合A"},
            {"name": "b", "type": "array", "required": True, "description": "集合B"}
        ],
        "icon": "git-merge"
    },
    "is_subset": {
        "id": "is_subset",
        "name": "子集检查",
        "name_en": "Is Subset",
        "description": "检查是否为子集",
        "category": "set",
        "subcategory": "predicate",
        "api_endpoint": "/api/set/is-subset",
        "method": "POST",
        "params": [
            {"name": "a", "type": "array", "required": True, "description": "子集"},
            {"name": "b", "type": "array", "required": True, "description": "父集"}
        ],
        "icon": "check"
    },
    "is_superset": {
        "id": "is_superset",
        "name": "父集检查",
        "name_en": "Is Superset",
        "description": "检查是否为父集",
        "category": "set",
        "subcategory": "predicate",
        "api_endpoint": "/api/set/is-superset",
        "method": "POST",
        "params": [
            {"name": "a", "type": "array", "required": True, "description": "父集"},
            {"name": "b", "type": "array", "required": True, "description": "子集"}
        ],
        "icon": "check"
    },
    "cartesian_product": {
        "id": "cartesian_product",
        "name": "笛卡尔积",
        "name_en": "Cartesian Product",
        "description": "计算笛卡尔积",
        "category": "set",
        "subcategory": "operator",
        "api_endpoint": "/api/set/cartesian-product",
        "method": "POST",
        "params": [
            {"name": "a", "type": "array", "required": True, "description": "集合A"},
            {"name": "b", "type": "array", "required": True, "description": "集合B"}
        ],
        "icon": "grid"
    },

    # ========== 迭代器工具 ==========
    "range": {
        "id": "range",
        "name": "范围生成",
        "name_en": "Range",
        "description": "生成数字范围",
        "category": "iterator",
        "subcategory": "generate",
        "api_endpoint": "/api/range",
        "method": "POST",
        "params": [
            {"name": "start", "type": "number", "required": True, "description": "起始"},
            {"name": "end", "type": "number", "required": True, "description": "结束"},
            {"name": "step", "type": "number", "required": False, "description": "步长"}
        ],
        "icon": "list"
    },
    "enumerate": {
        "id": "enumerate",
        "name": "枚举",
        "name_en": "Enumerate",
        "description": "枚举数组元素",
        "category": "iterator",
        "subcategory": "transform",
        "api_endpoint": "/api/enumerate",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "list"
    },
    "zip": {
        "id": "zip",
        "name": "压缩",
        "name_en": "Zip",
        "description": "压缩多个数组",
        "category": "iterator",
        "subcategory": "transform",
        "api_endpoint": "/api/zip",
        "method": "POST",
        "params": [
            {"name": "arrays", "type": "array", "required": True, "description": "数组数组"}
        ],
        "icon": "columns"
    },
    "unzip": {
        "id": "unzip",
        "name": "解压",
        "name_en": "Unzip",
        "description": "解压数组",
        "category": "iterator",
        "subcategory": "transform",
        "api_endpoint": "/api/unzip",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "columns"
    },
    "cycle": {
        "id": "cycle",
        "name": "循环",
        "name_en": "Cycle",
        "description": "无限循环数组",
        "category": "iterator",
        "subcategory": "generate",
        "api_endpoint": "/api/cycle",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "count", "type": "number", "required": True, "description": "次数"}
        ],
        "icon": "repeat"
    },
    "repeat": {
        "id": "repeat",
        "name": "重复",
        "name_en": "Repeat",
        "description": "重复元素",
        "category": "iterator",
        "subcategory": "generate",
        "api_endpoint": "/api/repeat",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "值"},
            {"name": "count", "type": "number", "required": True, "description": "次数"}
        ],
        "icon": "copy"
    },

    # ========== 序列工具 ==========
    "head": {
        "id": "head",
        "name": "首元素",
        "name_en": "Head",
        "description": "获取数组首元素",
        "category": "sequence",
        "subcategory": "access",
        "api_endpoint": "/api/head",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "arrow-left"
    },
    "tail": {
        "id": "tail",
        "name": "尾元素",
        "name_en": "Tail",
        "description": "获取数组尾元素",
        "category": "sequence",
        "subcategory": "access",
        "api_endpoint": "/api/tail",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "arrow-right"
    },
    "last": {
        "id": "last",
        "name": "最后一个",
        "name_en": "Last",
        "description": "获取数组最后一个",
        "category": "sequence",
        "subcategory": "access",
        "api_endpoint": "/api/last",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "arrow-right"
    },
    "init": {
        "id": "init",
        "name": "初始元素",
        "name_en": "Init",
        "description": "获取除最后一个外的所有元素",
        "category": "sequence",
        "subcategory": "access",
        "api_endpoint": "/api/init",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "arrow-left"
    },
    "take": {
        "id": "take",
        "name": "取前N个",
        "name_en": "Take",
        "description": "取数组前N个元素",
        "category": "sequence",
        "subcategory": "access",
        "api_endpoint": "/api/take",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "n", "type": "number", "required": True, "description": "数量"}
        ],
        "icon": "arrow-left"
    },
    "drop": {
        "id": "drop",
        "name": "丢弃前N个",
        "name_en": "Drop",
        "description": "丢弃数组前N个元素",
        "category": "sequence",
        "subcategory": "access",
        "api_endpoint": "/api/drop",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "n", "type": "number", "required": True, "description": "数量"}
        ],
        "icon": "arrow-right"
    },
    "nth": {
        "id": "nth",
        "name": "第N个元素",
        "name_en": "Nth",
        "description": "获取第N个元素",
        "category": "sequence",
        "subcategory": "access",
        "api_endpoint": "/api/nth",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "n", "type": "number", "required": True, "description": "索引"}
        ],
        "icon": "list"
    },
    "slice": {
        "id": "slice",
        "name": "切片",
        "name_en": "Slice",
        "description": "数组切片",
        "category": "sequence",
        "subcategory": "access",
        "api_endpoint": "/api/slice",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "start", "type": "number", "required": True, "description": "起始"},
            {"name": "end", "type": "number", "required": False, "description": "结束"}
        ],
        "icon": "scissors"
    },

    # ========== 对象工具 ==========
    "has_property": {
        "id": "has_property",
        "name": "属性存在",
        "name_en": "Has Property",
        "description": "检查对象是否有属性",
        "category": "object",
        "subcategory": "predicate",
        "api_endpoint": "/api/has-property",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "对象"},
            {"name": "prop", "type": "string", "required": True, "description": "属性名"}
        ],
        "icon": "key"
    },
    "get_property": {
        "id": "get_property",
        "name": "获取属性",
        "name_en": "Get Property",
        "description": "获取对象属性值",
        "category": "object",
        "subcategory": "access",
        "api_endpoint": "/api/get-property",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "对象"},
            {"name": "prop", "type": "string", "required": True, "description": "属性名"}
        ],
        "icon": "key"
    },
    "set_property": {
        "id": "set_property",
        "name": "设置属性",
        "name_en": "Set Property",
        "description": "设置对象属性值",
        "category": "object",
        "subcategory": "mutate",
        "api_endpoint": "/api/set-property",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "对象"},
            {"name": "prop", "type": "string", "required": True, "description": "属性名"},
            {"name": "value", "type": "any", "required": True, "description": "值"}
        ],
        "icon": "edit"
    },
    "delete_property": {
        "id": "delete_property",
        "name": "删除属性",
        "name_en": "Delete Property",
        "description": "删除对象属性",
        "category": "object",
        "subcategory": "mutate",
        "api_endpoint": "/api/delete-property",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "对象"},
            {"name": "prop", "type": "string", "required": True, "description": "属性名"}
        ],
        "icon": "trash"
    },
    "keys": {
        "id": "keys",
        "name": "获取键",
        "name_en": "Keys",
        "description": "获取对象所有键",
        "category": "object",
        "subcategory": "access",
        "api_endpoint": "/api/keys",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "对象"}
        ],
        "icon": "list"
    },
    "values": {
        "id": "values",
        "name": "获取值",
        "name_en": "Values",
        "description": "获取对象所有值",
        "category": "object",
        "subcategory": "access",
        "api_endpoint": "/api/values",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "对象"}
        ],
        "icon": "list"
    },
    "entries": {
        "id": "entries",
        "name": "获取条目",
        "name_en": "Entries",
        "description": "获取对象所有键值对",
        "category": "object",
        "subcategory": "access",
        "api_endpoint": "/api/entries",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "对象"}
        ],
        "icon": "list"
    },
    "clone": {
        "id": "clone",
        "name": "克隆",
        "name_en": "Clone",
        "description": "浅克隆对象",
        "category": "object",
        "subcategory": "transform",
        "api_endpoint": "/api/clone",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "对象"}
        ],
        "icon": "copy"
    },
    "deep_clone": {
        "id": "deep_clone",
        "name": "深克隆",
        "name_en": "Deep Clone",
        "description": "深克隆对象",
        "category": "object",
        "subcategory": "transform",
        "api_endpoint": "/api/deep-clone",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "对象"}
        ],
        "icon": "copy"
    },

    # ========== 数组变换工具 ==========
    "map": {
        "id": "map",
        "name": "映射",
        "name_en": "Map",
        "description": "映射数组元素",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/map",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "fn", "type": "string", "required": True, "description": "映射函数"}
        ],
        "icon": "map"
    },
    "filter": {
        "id": "filter",
        "name": "过滤",
        "name_en": "Filter",
        "description": "过滤数组元素",
        "category": "array",
        "subcategory": "filter",
        "api_endpoint": "/api/filter",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "fn", "type": "string", "required": True, "description": "过滤函数"}
        ],
        "icon": "filter"
    },
    "reduce": {
        "id": "reduce",
        "name": "归约",
        "name_en": "Reduce",
        "description": "归约数组元素",
        "category": "array",
        "subcategory": "aggregate",
        "api_endpoint": "/api/reduce",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "fn", "type": "string", "required": True, "description": "归约函数"},
            {"name": "initial", "type": "any", "required": False, "description": "初始值"}
        ],
        "icon": "git-merge"
    },
    "find": {
        "id": "find",
        "name": "查找",
        "name_en": "Find",
        "description": "查找满足条件的元素",
        "category": "array",
        "subcategory": "search",
        "api_endpoint": "/api/find",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "fn", "type": "string", "required": True, "description": "查找函数"}
        ],
        "icon": "search"
    },
    "find_index": {
        "id": "find_index",
        "name": "查找索引",
        "name_en": "Find Index",
        "description": "查找满足条件的元素索引",
        "category": "array",
        "subcategory": "search",
        "api_endpoint": "/api/find-index",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "fn", "type": "string", "required": True, "description": "查找函数"}
        ],
        "icon": "search"
    },
    "some": {
        "id": "some",
        "name": "存在匹配",
        "name_en": "Some",
        "description": "是否存在匹配元素",
        "category": "array",
        "subcategory": "search",
        "api_endpoint": "/api/some",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "fn", "type": "string", "required": True, "description": "匹配函数"}
        ],
        "icon": "check-square"
    },
    "every": {
        "id": "every",
        "name": "全部匹配",
        "name_en": "Every",
        "description": "是否全部元素都匹配",
        "category": "array",
        "subcategory": "search",
        "api_endpoint": "/api/every",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "fn", "type": "string", "required": True, "description": "匹配函数"}
        ],
        "icon": "check"
    },
    "none": {
        "id": "none",
        "name": "无匹配",
        "name_en": "None",
        "description": "是否没有匹配元素",
        "category": "array",
        "subcategory": "search",
        "api_endpoint": "/api/none",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "fn", "type": "string", "required": True, "description": "匹配函数"}
        ],
        "icon": "x"
    },
    "sort": {
        "id": "sort",
        "name": "排序",
        "name_en": "Sort",
        "description": "排序数组",
        "category": "array",
        "subcategory": "sort",
        "api_endpoint": "/api/sort",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "fn", "type": "string", "required": False, "description": "排序函数"}
        ],
        "icon": "sort-asc"
    },
    "reverse": {
        "id": "reverse",
        "name": "反转",
        "name_en": "Reverse",
        "description": "反转数组",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/reverse",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "rotate-ccw"
    },
    "concat": {
        "id": "concat",
        "name": "连接",
        "name_en": "Concat",
        "description": "连接多个数组",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/concat",
        "method": "POST",
        "params": [
            {"name": "arrays", "type": "array", "required": True, "description": "数组数组"}
        ],
        "icon": "link"
    },
    "flatten": {
        "id": "flatten",
        "name": "扁平化",
        "name_en": "Flatten",
        "description": "扁平化数组",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/flatten",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "嵌套数组"}
        ],
        "icon": "minimize"
    },
    "compact": {
        "id": "compact",
        "name": "压缩",
        "name_en": "Compact",
        "description": "移除假值",
        "category": "array",
        "subcategory": "filter",
        "api_endpoint": "/api/compact",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "compress"
    },
    "unique": {
        "id": "unique",
        "name": "去重",
        "name_en": "Unique",
        "description": "数组去重",
        "category": "array",
        "subcategory": "filter",
        "api_endpoint": "/api/unique",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "trash-2"
    },

    # ========== 数学进阶工具 ==========
    "pow": {
        "id": "pow",
        "name": "幂运算",
        "name_en": "Power",
        "description": "计算幂次方",
        "category": "math",
        "subcategory": "operator",
        "api_endpoint": "/api/pow",
        "method": "POST",
        "params": [
            {"name": "base", "type": "number", "required": True, "description": "底数"},
            {"name": "exp", "type": "number", "required": True, "description": "指数"}
        ],
        "icon": "zap"
    },
    "sqrt": {
        "id": "sqrt",
        "name": "平方根",
        "name_en": "Square Root",
        "description": "计算平方根",
        "category": "math",
        "subcategory": "operator",
        "api_endpoint": "/api/sqrt",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "数字"}
        ],
        "icon": "zap"
    },
    "log": {
        "id": "log",
        "name": "对数",
        "name_en": "Logarithm",
        "description": "计算对数",
        "category": "math",
        "subcategory": "operator",
        "api_endpoint": "/api/log",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "数字"},
            {"name": "base", "type": "number", "required": False, "description": "底数"}
        ],
        "icon": "zap"
    },
    "ln": {
        "id": "ln",
        "name": "自然对数",
        "name_en": "Natural Log",
        "description": "计算自然对数",
        "category": "math",
        "subcategory": "operator",
        "api_endpoint": "/api/ln",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "数字"}
        ],
        "icon": "zap"
    },
    "sin": {
        "id": "sin",
        "name": "正弦",
        "name_en": "Sine",
        "description": "计算正弦值",
        "category": "math",
        "subcategory": "trigonometry",
        "api_endpoint": "/api/sin",
        "method": "POST",
        "params": [
            {"name": "angle", "type": "number", "required": True, "description": "角度"}
        ],
        "icon": "triangle"
    },
    "cos": {
        "id": "cos",
        "name": "余弦",
        "name_en": "Cosine",
        "description": "计算余弦值",
        "category": "math",
        "subcategory": "trigonometry",
        "api_endpoint": "/api/cos",
        "method": "POST",
        "params": [
            {"name": "angle", "type": "number", "required": True, "description": "角度"}
        ],
        "icon": "triangle"
    },
    "tan": {
        "id": "tan",
        "name": "正切",
        "name_en": "Tangent",
        "description": "计算正切值",
        "category": "math",
        "subcategory": "trigonometry",
        "api_endpoint": "/api/tan",
        "method": "POST",
        "params": [
            {"name": "angle", "type": "number", "required": True, "description": "角度"}
        ],
        "icon": "triangle"
    },
    "degrees_to_radians": {
        "id": "degrees_to_radians",
        "name": "角度转弧度",
        "name_en": "Degrees to Radians",
        "description": "角度转弧度",
        "category": "math",
        "subcategory": "convert",
        "api_endpoint": "/api/degrees-to-radians",
        "method": "POST",
        "params": [
            {"name": "degrees", "type": "number", "required": True, "description": "角度"}
        ],
        "icon": "rotate-cw"
    },
    "radians_to_degrees": {
        "id": "radians_to_degrees",
        "name": "弧度转角度",
        "name_en": "Radians to Degrees",
        "description": "弧度转角度",
        "category": "math",
        "subcategory": "convert",
        "api_endpoint": "/api/radians-to-degrees",
        "method": "POST",
        "params": [
            {"name": "radians", "type": "number", "required": True, "description": "弧度"}
        ],
        "icon": "rotate-ccw"
    },
    "percent_of": {
        "id": "percent_of",
        "name": "百分比",
        "name_en": "Percent Of",
        "description": "计算A占B的百分比",
        "category": "math",
        "subcategory": "operator",
        "api_endpoint": "/api/percent-of",
        "method": "POST",
        "params": [
            {"name": "part", "type": "number", "required": True, "description": "部分"},
            {"name": "whole", "type": "number", "required": True, "description": "整体"}
        ],
        "icon": "percent"
    },
    "percentage_change": {
        "id": "percentage_change",
        "name": "百分比变化",
        "name_en": "Percentage Change",
        "description": "计算百分比变化",
        "category": "math",
        "subcategory": "operator",
        "api_endpoint": "/api/percentage-change",
        "method": "POST",
        "params": [
            {"name": "old", "type": "number", "required": True, "description": "旧值"},
            {"name": "new", "type": "number", "required": True, "description": "新值"}
        ],
        "icon": "trending-up"
    },
    "mean": {
        "id": "mean",
        "name": "平均值",
        "name_en": "Mean",
        "description": "计算平均值",
        "category": "math",
        "subcategory": "statistics",
        "api_endpoint": "/api/mean",
        "method": "POST",
        "params": [
            {"name": "numbers", "type": "array", "required": True, "description": "数字数组"}
        ],
        "icon": "bar-chart"
    },
    "harmonic_mean": {
        "id": "harmonic_mean",
        "name": "调和平均",
        "name_en": "Harmonic Mean",
        "description": "计算调和平均",
        "category": "math",
        "subcategory": "statistics",
        "api_endpoint": "/api/harmonic-mean",
        "method": "POST",
        "params": [
            {"name": "numbers", "type": "array", "required": True, "description": "数字数组"}
        ],
        "icon": "bar-chart"
    },
    "geometric_mean": {
        "id": "geometric_mean",
        "name": "几何平均",
        "name_en": "Geometric Mean",
        "description": "计算几何平均",
        "category": "math",
        "subcategory": "statistics",
        "api_endpoint": "/api/geometric-mean",
        "method": "POST",
        "params": [
            {"name": "numbers", "type": "array", "required": True, "description": "数字数组"}
        ],
        "icon": "bar-chart"
    },
    "root_mean_square": {
        "id": "root_mean_square",
        "name": "均方根",
        "name_en": "Root Mean Square",
        "description": "计算均方根",
        "category": "math",
        "subcategory": "statistics",
        "api_endpoint": "/api/root-mean-square",
        "method": "POST",
        "params": [
            {"name": "numbers", "type": "array", "required": True, "description": "数字数组"}
        ],
        "icon": "bar-chart"
    },
    "percentile": {
        "id": "percentile",
        "name": "百分位数",
        "name_en": "Percentile",
        "description": "计算百分位数",
        "category": "math",
        "subcategory": "statistics",
        "api_endpoint": "/api/percentile",
        "method": "POST",
        "params": [
            {"name": "numbers", "type": "array", "required": True, "description": "数字数组"},
            {"name": "p", "type": "number", "required": True, "description": "百分位"}
        ],
        "icon": "bar-chart"
    },
    "covariance": {
        "id": "covariance",
        "name": "协方差",
        "name_en": "Covariance",
        "description": "计算协方差",
        "category": "math",
        "subcategory": "statistics",
        "api_endpoint": "/api/covariance",
        "method": "POST",
        "params": [
            {"name": "x", "type": "array", "required": True, "description": "X数组"},
            {"name": "y", "type": "array", "required": True, "description": "Y数组"}
        ],
        "icon": "trending-up"
    },
    "combination": {
        "id": "combination",
        "name": "组合数",
        "name_en": "Combination",
        "description": "计算组合数",
        "category": "math",
        "subcategory": "combinatorics",
        "api_endpoint": "/api/combination",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "总数"},
            {"name": "r", "type": "number", "required": True, "description": "选取数"}
        ],
        "icon": "grid"
    },
    "permutation": {
        "id": "permutation",
        "name": "排列数",
        "name_en": "Permutation",
        "description": "计算排列数",
        "category": "math",
        "subcategory": "combinatorics",
        "api_endpoint": "/api/permutation",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "总数"},
            {"name": "r", "type": "number", "required": True, "description": "选取数"}
        ],
        "icon": "grid"
    },
    "is_perfect_square": {
        "id": "is_perfect_square",
        "name": "完全平方数检查",
        "name_en": "Is Perfect Square",
        "description": "检查是否为完全平方数",
        "category": "math",
        "subcategory": "predicate",
        "api_endpoint": "/api/is-perfect-square",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "数字"}
        ],
        "icon": "check"
    },
    "is_perfect_number": {
        "id": "is_perfect_number",
        "name": "完全数检查",
        "name_en": "Is Perfect Number",
        "description": "检查是否为完全数",
        "category": "math",
        "subcategory": "predicate",
        "api_endpoint": "/api/is-perfect-number",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "数字"}
        ],
        "icon": "check"
    },
    "quadrant": {
        "id": "quadrant",
        "name": "象限",
        "name_en": "Quadrant",
        "description": "获取坐标所在象限",
        "category": "math",
        "subcategory": "geometry",
        "api_endpoint": "/api/quadrant",
        "method": "POST",
        "params": [
            {"name": "x", "type": "number", "required": True, "description": "X坐标"},
            {"name": "y", "type": "number", "required": True, "description": "Y坐标"}
        ],
        "icon": "grid"
    },
    "distance": {
        "id": "distance",
        "name": "距离",
        "name_en": "Distance",
        "description": "计算两点距离",
        "category": "math",
        "subcategory": "geometry",
        "api_endpoint": "/api/distance",
        "method": "POST",
        "params": [
            {"name": "x1", "type": "number", "required": True, "description": "X1"},
            {"name": "y1", "type": "number", "required": True, "description": "Y1"},
            {"name": "x2", "type": "number", "required": True, "description": "X2"},
            {"name": "y2", "type": "number", "required": True, "description": "Y2"}
        ],
        "icon": "move"
    },
    "midpoint": {
        "id": "midpoint",
        "name": "中点",
        "name_en": "Midpoint",
        "description": "计算线段中点",
        "category": "math",
        "subcategory": "geometry",
        "api_endpoint": "/api/midpoint",
        "method": "POST",
        "params": [
            {"name": "x1", "type": "number", "required": True, "description": "X1"},
            {"name": "y1", "type": "number", "required": True, "description": "Y1"},
            {"name": "x2", "type": "number", "required": True, "description": "X2"},
            {"name": "y2", "type": "number", "required": True, "description": "Y2"}
        ],
        "icon": "crosshair"
    },
    "slope": {
        "id": "slope",
        "name": "斜率",
        "name_en": "Slope",
        "description": "计算直线斜率",
        "category": "math",
        "subcategory": "geometry",
        "api_endpoint": "/api/slope",
        "method": "POST",
        "params": [
            {"name": "x1", "type": "number", "required": True, "description": "X1"},
            {"name": "y1", "type": "number", "required": True, "description": "Y1"},
            {"name": "x2", "type": "number", "required": True, "description": "X2"},
            {"name": "y2", "type": "number", "required": True, "description": "Y2"}
        ],
        "icon": "trending-up"
    },

    # ========== 时间工具 ==========
    "now": {
        "id": "now",
        "name": "当前时间",
        "name_en": "Now",
        "description": "获取当前时间",
        "category": "time",
        "subcategory": "access",
        "api_endpoint": "/api/now",
        "method": "POST",
        "params": [],
        "icon": "clock"
    },
    "today": {
        "id": "today",
        "name": "今天",
        "name_en": "Today",
        "description": "获取今天的日期",
        "category": "time",
        "subcategory": "access",
        "api_endpoint": "/api/today",
        "method": "POST",
        "params": [],
        "icon": "calendar"
    },
    "timestamp": {
        "id": "timestamp",
        "name": "时间戳",
        "name_en": "Timestamp",
        "description": "获取当前时间戳",
        "category": "time",
        "subcategory": "convert",
        "api_endpoint": "/api/timestamp",
        "method": "POST",
        "params": [],
        "icon": "hash"
    },
    "format_time": {
        "id": "format_time",
        "name": "格式化时间",
        "name_en": "Format Time",
        "description": "格式化时间字符串",
        "category": "time",
        "subcategory": "format",
        "api_endpoint": "/api/format-time",
        "method": "POST",
        "params": [
            {"name": "time", "type": "string", "required": True, "description": "时间"},
            {"name": "format", "type": "string", "required": True, "description": "格式"}
        ],
        "icon": "clock"
    },
    "add_hours": {
        "id": "add_hours",
        "name": "加小时",
        "name_en": "Add Hours",
        "description": "时间加小时",
        "category": "time",
        "subcategory": "arithmetic",
        "api_endpoint": "/api/add-hours",
        "method": "POST",
        "params": [
            {"name": "time", "type": "string", "required": True, "description": "时间"},
            {"name": "hours", "type": "number", "required": True, "description": "小时数"}
        ],
        "icon": "plus"
    },
    "add_minutes": {
        "id": "add_minutes",
        "name": "加分钟",
        "name_en": "Add Minutes",
        "description": "时间加分钟",
        "category": "time",
        "subcategory": "arithmetic",
        "api_endpoint": "/api/add-minutes",
        "method": "POST",
        "params": [
            {"name": "time", "type": "string", "required": True, "description": "时间"},
            {"name": "minutes", "type": "number", "required": True, "description": "分钟数"}
        ],
        "icon": "plus"
    },
    "time_diff": {
        "id": "time_diff",
        "name": "时间差",
        "name_en": "Time Diff",
        "description": "计算时间差（秒）",
        "category": "time",
        "subcategory": "arithmetic",
        "api_endpoint": "/api/time-diff",
        "method": "POST",
        "params": [
            {"name": "time1", "type": "string", "required": True, "description": "时间1"},
            {"name": "time2", "type": "string", "required": True, "description": "时间2"}
        ],
        "icon": "clock"
    },
    "is_valid_time": {
        "id": "is_valid_time",
        "name": "时间有效性",
        "name_en": "Is Valid Time",
        "description": "检查时间是否有效",
        "category": "time",
        "subcategory": "predicate",
        "api_endpoint": "/api/is-valid-time",
        "method": "POST",
        "params": [
            {"name": "time", "type": "string", "required": True, "description": "时间"},
            {"name": "format", "type": "string", "required": False, "description": "格式"}
        ],
        "icon": "check"
    },

    # ========== UUID工具 ==========
    "uuid_v1": {
        "id": "uuid_v1",
        "name": "UUIDv1",
        "name_en": "UUID v1",
        "description": "生成UUID v1",
        "category": "uuid",
        "subcategory": "generate",
        "api_endpoint": "/api/uuid-v1",
        "method": "POST",
        "params": [],
        "icon": "hash"
    },
    "uuid_v4": {
        "id": "uuid_v4",
        "name": "UUIDv4",
        "name_en": "UUID v4",
        "description": "生成UUID v4",
        "category": "uuid",
        "subcategory": "generate",
        "api_endpoint": "/api/uuid-v4",
        "method": "POST",
        "params": [],
        "icon": "hash"
    },
    "uuid_validate": {
        "id": "uuid_validate",
        "name": "UUID验证",
        "name_en": "Validate UUID",
        "description": "验证UUID格式",
        "category": "uuid",
        "subcategory": "validate",
        "api_endpoint": "/api/uuid-validate",
        "method": "POST",
        "params": [
            {"name": "uuid", "type": "string", "required": True, "description": "UUID"}
        ],
        "icon": "check"
    },
    "uuid_to_hex": {
        "id": "uuid_to_hex",
        "name": "UUID转HEX",
        "name_en": "UUID to HEX",
        "description": "UUID转换为HEX",
        "category": "uuid",
        "subcategory": "convert",
        "api_endpoint": "/api/uuid-to-hex",
        "method": "POST",
        "params": [
            {"name": "uuid", "type": "string", "required": True, "description": "UUID"}
        ],
        "icon": "hash"
    },

    # ========== 随机工具 ==========
    "random_int": {
        "id": "random_int",
        "name": "随机整数",
        "name_en": "Random Int",
        "description": "生成随机整数",
        "category": "random",
        "subcategory": "generate",
        "api_endpoint": "/api/random-int",
        "method": "POST",
        "params": [
            {"name": "min", "type": "number", "required": False, "description": "最小值"},
            {"name": "max", "type": "number", "required": False, "description": "最大值"}
        ],
        "icon": "hash"
    },
    "random_float": {
        "id": "random_float",
        "name": "随机小数",
        "name_en": "Random Float",
        "description": "生成随机小数",
        "category": "random",
        "subcategory": "generate",
        "api_endpoint": "/api/random-float",
        "method": "POST",
        "params": [
            {"name": "min", "type": "number", "required": False, "description": "最小值"},
            {"name": "max", "type": "number", "required": False, "description": "最大值"}
        ],
        "icon": "hash"
    },
    "random_choice": {
        "id": "random_choice",
        "name": "随机选择",
        "name_en": "Random Choice",
        "description": "从数组随机选择一个",
        "category": "random",
        "subcategory": "generate",
        "api_endpoint": "/api/random-choice",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "shuffle"
    },
    "random_sample": {
        "id": "random_sample",
        "name": "随机抽样",
        "name_en": "Random Sample",
        "description": "随机抽取不重复元素",
        "category": "random",
        "subcategory": "generate",
        "api_endpoint": "/api/random-sample",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "count", "type": "number", "required": True, "description": "数量"}
        ],
        "icon": "list"
    },
    "random_uuid": {
        "id": "random_uuid",
        "name": "随机UUID",
        "name_en": "Random UUID",
        "description": "生成随机UUID",
        "category": "random",
        "subcategory": "generate",
        "api_endpoint": "/api/random-uuid",
        "method": "POST",
        "params": [],
        "icon": "hash"
    },
    "random_string": {
        "id": "random_string",
        "name": "随机字符串",
        "name_en": "Random String",
        "description": "生成随机字符串",
        "category": "random",
        "subcategory": "generate",
        "api_endpoint": "/api/random-string",
        "method": "POST",
        "params": [
            {"name": "length", "type": "number", "required": True, "description": "长度"},
            {"name": "charset", "type": "string", "required": False, "description": "字符集"}
        ],
        "icon": "type"
    },
    "random_color": {
        "id": "random_color",
        "name": "随机颜色",
        "name_en": "Random Color",
        "description": "生成随机颜色",
        "category": "random",
        "subcategory": "generate",
        "api_endpoint": "/api/random-color",
        "method": "POST",
        "params": [],
        "icon": "palette"
    },
    "shuffle_array": {
        "id": "shuffle_array",
        "name": "打乱数组",
        "name_en": "Shuffle Array",
        "description": "随机打乱数组",
        "category": "random",
        "subcategory": "transform",
        "api_endpoint": "/api/shuffle-array",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "shuffle"
    },

    # ========== 序列生成工具 ==========
    "arithmetic_sequence": {
        "id": "arithmetic_sequence",
        "name": "等差数列",
        "name_en": "Arithmetic Sequence",
        "description": "生成等差数列",
        "category": "sequence",
        "subcategory": "generate",
        "api_endpoint": "/api/arithmetic-sequence",
        "method": "POST",
        "params": [
            {"name": "start", "type": "number", "required": True, "description": "起始"},
            {"name": "diff", "type": "number", "required": True, "description": "公差"},
            {"name": "count", "type": "number", "required": True, "description": "数量"}
        ],
        "icon": "list"
    },
    "geometric_sequence": {
        "id": "geometric_sequence",
        "name": "等比数列",
        "name_en": "Geometric Sequence",
        "description": "生成等比数列",
        "category": "sequence",
        "subcategory": "generate",
        "api_endpoint": "/api/geometric-sequence",
        "method": "POST",
        "params": [
            {"name": "start", "type": "number", "required": True, "description": "起始"},
            {"name": "ratio", "type": "number", "required": True, "description": "公比"},
            {"name": "count", "type": "number", "required": True, "description": "数量"}
        ],
        "icon": "list"
    },
    "fibonacci_sequence": {
        "id": "fibonacci_sequence",
        "name": "斐波那契数列",
        "name_en": "Fibonacci Sequence",
        "description": "生成斐波那契数列",
        "category": "sequence",
        "subcategory": "generate",
        "api_endpoint": "/api/fibonacci-sequence",
        "method": "POST",
        "params": [
            {"name": "count", "type": "number", "required": True, "description": "数量"}
        ],
        "icon": "list"
    },
    "prime_sequence": {
        "id": "prime_sequence",
        "name": "素数序列",
        "name_en": "Prime Sequence",
        "description": "生成素数序列",
        "category": "sequence",
        "subcategory": "generate",
        "api_endpoint": "/api/prime-sequence",
        "method": "POST",
        "params": [
            {"name": "count", "type": "number", "required": True, "description": "数量"}
        ],
        "icon": "list"
    },
    "sequence_slice": {
        "id": "sequence_slice",
        "name": "序列切片",
        "name_en": "Sequence Slice",
        "description": "序列切片",
        "category": "sequence",
        "subcategory": "transform",
        "api_endpoint": "/api/sequence-slice",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "序列"},
            {"name": "start", "type": "number", "required": False, "description": "起始"},
            {"name": "end", "type": "number", "required": False, "description": "结束"}
        ],
        "icon": "scissors"
    },
    "sequence_reverse": {
        "id": "sequence_reverse",
        "name": "序列反转",
        "name_en": "Sequence Reverse",
        "description": "反转序列",
        "category": "sequence",
        "subcategory": "transform",
        "api_endpoint": "/api/sequence-reverse",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "序列"}
        ],
        "icon": "rotate-ccw"
    },

    # ========== JSON工具 ==========
    "parse_json": {
        "id": "parse_json",
        "name": "解析JSON",
        "name_en": "Parse JSON",
        "description": "解析JSON字符串",
        "category": "json",
        "subcategory": "parse",
        "api_endpoint": "/api/parse-json",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "JSON字符串"}
        ],
        "icon": "file"
    },
    "to_json": {
        "id": "to_json",
        "name": "转JSON",
        "name_en": "To JSON",
        "description": "对象转JSON字符串",
        "category": "json",
        "subcategory": "convert",
        "api_endpoint": "/api/to-json",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "any", "required": True, "description": "对象"}
        ],
        "icon": "file"
    },
    "json_get": {
        "id": "json_get",
        "name": "JSON取值",
        "name_en": "JSON Get",
        "description": "安全获取JSON值",
        "category": "json",
        "subcategory": "access",
        "api_endpoint": "/api/json-get",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "any", "required": True, "description": "对象"},
            {"name": "path", "type": "string", "required": True, "description": "JSON路径"}
        ],
        "icon": "key"
    },
    "json_set": {
        "id": "json_set",
        "name": "JSON设值",
        "name_en": "JSON Set",
        "description": "设置JSON值",
        "category": "json",
        "subcategory": "mutate",
        "api_endpoint": "/api/json-set",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "any", "required": True, "description": "对象"},
            {"name": "path", "type": "string", "required": True, "description": "JSON路径"},
            {"name": "value", "type": "any", "required": True, "description": "值"}
        ],
        "icon": "edit"
    },
    "json_keys": {
        "id": "json_keys",
        "name": "JSON键",
        "name_en": "JSON Keys",
        "description": "获取JSON所有键",
        "category": "json",
        "subcategory": "access",
        "api_endpoint": "/api/json-keys",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "any", "required": True, "description": "对象"}
        ],
        "icon": "list"
    },
    "json_values": {
        "id": "json_values",
        "name": "JSON值",
        "name_en": "JSON Values",
        "description": "获取JSON所有值",
        "category": "json",
        "subcategory": "access",
        "api_endpoint": "/api/json-values",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "any", "required": True, "description": "对象"}
        ],
        "icon": "list"
    },
    "json_merge": {
        "id": "json_merge",
        "name": "JSON合并",
        "name_en": "JSON Merge",
        "description": "合并多个JSON",
        "category": "json",
        "subcategory": "transform",
        "api_endpoint": "/api/json-merge",
        "method": "POST",
        "params": [
            {"name": "objects", "type": "array", "required": True, "description": "对象数组"}
        ],
        "icon": "git-merge"
    },
    "is_valid_json": {
        "id": "is_valid_json",
        "name": "JSON有效性",
        "name_en": "Is Valid JSON",
        "description": "检查是否为有效JSON",
        "category": "json",
        "subcategory": "validate",
        "api_endpoint": "/api/is-valid-json",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "字符串"}
        ],
        "icon": "check"
    },

    # ========== YAML工具 ==========
    "parse_yaml": {
        "id": "parse_yaml",
        "name": "解析YAML",
        "name_en": "Parse YAML",
        "description": "解析YAML字符串",
        "category": "yaml",
        "subcategory": "parse",
        "api_endpoint": "/api/parse-yaml",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "YAML字符串"}
        ],
        "icon": "file"
    },
    "to_yaml": {
        "id": "to_yaml",
        "name": "转YAML",
        "name_en": "To YAML",
        "description": "对象转YAML",
        "category": "yaml",
        "subcategory": "convert",
        "api_endpoint": "/api/to-yaml",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "any", "required": True, "description": "对象"}
        ],
        "icon": "file"
    },

    # ========== CSV工具 ==========
    "parse_csv": {
        "id": "parse_csv",
        "name": "解析CSV",
        "name_en": "Parse CSV",
        "description": "解析CSV字符串",
        "category": "csv",
        "subcategory": "parse",
        "api_endpoint": "/api/parse-csv",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "CSV字符串"},
            {"name": "delimiter", "type": "string", "required": False, "description": "分隔符"}
        ],
        "icon": "file"
    },
    "to_csv": {
        "id": "to_csv",
        "name": "转CSV",
        "name_en": "To CSV",
        "description": "数组转CSV",
        "category": "csv",
        "subcategory": "convert",
        "api_endpoint": "/api/to-csv",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "delimiter", "type": "string", "required": False, "description": "分隔符"}
        ],
        "icon": "file"
    },

    # ========== XML工具 ==========
    "parse_xml": {
        "id": "parse_xml",
        "name": "解析XML",
        "name_en": "Parse XML",
        "description": "解析XML字符串",
        "category": "xml",
        "subcategory": "parse",
        "api_endpoint": "/api/parse-xml",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "XML字符串"}
        ],
        "icon": "file"
    },
    "to_xml": {
        "id": "to_xml",
        "name": "转XML",
        "name_en": "To XML",
        "description": "对象转XML",
        "category": "xml",
        "subcategory": "convert",
        "api_endpoint": "/api/to-xml",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "any", "required": True, "description": "对象"},
            {"name": "root", "type": "string", "required": False, "description": "根节点"}
        ],
        "icon": "file"
    },

    # ========== HTML工具 ==========
    "parse_html": {
        "id": "parse_html",
        "name": "解析HTML",
        "name_en": "Parse HTML",
        "description": "解析HTML字符串",
        "category": "html",
        "subcategory": "parse",
        "api_endpoint": "/api/parse-html",
        "method": "POST",
        "params": [
            {"name": "html", "type": "string", "required": True, "description": "HTML字符串"}
        ],
        "icon": "code"
    },
    "to_html": {
        "id": "to_html",
        "name": "转HTML",
        "name_en": "To HTML",
        "description": "文本转HTML",
        "category": "html",
        "subcategory": "convert",
        "api_endpoint": "/api/to-html",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "code"
    },
    "strip_html": {
        "id": "strip_html",
        "name": "去除HTML",
        "name_en": "Strip HTML",
        "description": "去除HTML标签",
        "category": "html",
        "subcategory": "transform",
        "api_endpoint": "/api/strip-html",
        "method": "POST",
        "params": [
            {"name": "html", "type": "string", "required": True, "description": "HTML"}
        ],
        "icon": "code"
    },
    "escape_html": {
        "id": "escape_html",
        "name": "HTML转义",
        "name_en": "Escape HTML",
        "description": "HTML特殊字符转义",
        "category": "html",
        "subcategory": "transform",
        "api_endpoint": "/api/escape-html",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "lock"
    },
    "unescape_html": {
        "id": "unescape_html",
        "name": "HTML反转义",
        "name_en": "Unescape HTML",
        "description": "HTML反转义",
        "category": "html",
        "subcategory": "transform",
        "api_endpoint": "/api/unescape-html",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "unlock"
    },

    # ========== URL工具 ==========
    "parse_url": {
        "id": "parse_url",
        "name": "解析URL",
        "name_en": "Parse URL",
        "description": "解析URL各部分",
        "category": "url",
        "subcategory": "parse",
        "api_endpoint": "/api/parse-url",
        "method": "POST",
        "params": [
            {"name": "url", "type": "string", "required": True, "description": "URL"}
        ],
        "icon": "link"
    },
    "build_url": {
        "id": "build_url",
        "name": "构建URL",
        "name_en": "Build URL",
        "description": "构建完整URL",
        "category": "url",
        "subcategory": "build",
        "api_endpoint": "/api/build-url",
        "method": "POST",
        "params": [
            {"name": "scheme", "type": "string", "required": True, "description": "协议"},
            {"name": "host", "type": "string", "required": True, "description": "主机"},
            {"name": "path", "type": "string", "required": False, "description": "路径"}
        ],
        "icon": "link"
    },
    "encode_url": {
        "id": "encode_url",
        "name": "URL编码",
        "name_en": "URL Encode",
        "description": "URL编码",
        "category": "url",
        "subcategory": "encode",
        "api_endpoint": "/api/encode-url",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "lock"
    },
    "decode_url": {
        "id": "decode_url",
        "name": "URL解码",
        "name_en": "URL Decode",
        "description": "URL解码",
        "category": "url",
        "subcategory": "decode",
        "api_endpoint": "/api/decode-url",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "unlock"
    },

    # ========== IP工具 ==========
    "is_valid_ip": {
        "id": "is_valid_ip",
        "name": "IP有效性",
        "name_en": "Is Valid IP",
        "description": "检查IP是否有效",
        "category": "ip",
        "subcategory": "validate",
        "api_endpoint": "/api/is-valid-ip",
        "method": "POST",
        "params": [
            {"name": "ip", "type": "string", "required": True, "description": "IP地址"}
        ],
        "icon": "globe"
    },
    "ip_to_int": {
        "id": "ip_to_int",
        "name": "IP转整数",
        "name_en": "IP to Int",
        "description": "IP地址转整数",
        "category": "ip",
        "subcategory": "convert",
        "api_endpoint": "/api/ip-to-int",
        "method": "POST",
        "params": [
            {"name": "ip", "type": "string", "required": True, "description": "IP地址"}
        ],
        "icon": "hash"
    },
    "int_to_ip": {
        "id": "int_to_ip",
        "name": "整数转IP",
        "name_en": "Int to IP",
        "description": "整数转IP地址",
        "category": "ip",
        "subcategory": "convert",
        "api_endpoint": "/api/int-to-ip",
        "method": "POST",
        "params": [
            {"name": "num", "type": "number", "required": True, "description": "整数"}
        ],
        "icon": "globe"
    },
    "is_ipv4": {
        "id": "is_ipv4",
        "name": "IPv4检查",
        "name_en": "Is IPv4",
        "description": "检查是否为IPv4",
        "category": "ip",
        "subcategory": "predicate",
        "api_endpoint": "/api/is-ipv4",
        "method": "POST",
        "params": [
            {"name": "ip", "type": "string", "required": True, "description": "IP地址"}
        ],
        "icon": "check"
    },
    "is_ipv6": {
        "id": "is_ipv6",
        "name": "IPv6检查",
        "name_en": "Is IPv6",
        "description": "检查是否为IPv6",
        "category": "ip",
        "subcategory": "predicate",
        "api_endpoint": "/api/is-ipv6",
        "method": "POST",
        "params": [
            {"name": "ip", "type": "string", "required": True, "description": "IP地址"}
        ],
        "icon": "check"
    },

    # ========== 哈希工具 ==========
    "hash_md5": {
        "id": "hash_md5",
        "name": "MD5哈希",
        "name_en": "MD5 Hash",
        "description": "计算MD5哈希",
        "category": "hash",
        "subcategory": "hash",
        "api_endpoint": "/api/hash-md5",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "lock"
    },
    "hash_sha1": {
        "id": "hash_sha1",
        "name": "SHA1哈希",
        "name_en": "SHA1 Hash",
        "description": "计算SHA1哈希",
        "category": "hash",
        "subcategory": "hash",
        "api_endpoint": "/api/hash-sha1",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "lock"
    },
    "hash_sha256": {
        "id": "hash_sha256",
        "name": "SHA256哈希",
        "name_en": "SHA256 Hash",
        "description": "计算SHA256哈希",
        "category": "hash",
        "subcategory": "hash",
        "api_endpoint": "/api/hash-sha256",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "lock"
    },
    "hash_sha512": {
        "id": "hash_sha512",
        "name": "SHA512哈希",
        "name_en": "SHA512 Hash",
        "description": "计算SHA512哈希",
        "category": "hash",
        "subcategory": "hash",
        "api_endpoint": "/api/hash-sha512",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "lock"
    },
    "hash_ripemd160": {
        "id": "hash_ripemd160",
        "name": "RIPEMD160哈希",
        "name_en": "RIPEMD160 Hash",
        "description": "计算RIPEMD160哈希",
        "category": "hash",
        "subcategory": "hash",
        "api_endpoint": "/api/hash-ripemd160",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "lock"
    },

    # ========== 压缩工具 ==========
    "gzip_compress": {
        "id": "gzip_compress",
        "name": "Gzip压缩",
        "name_en": "Gzip Compress",
        "description": "Gzip压缩",
        "category": "compress",
        "subcategory": "compress",
        "api_endpoint": "/api/gzip-compress",
        "method": "POST",
        "params": [
            {"name": "data", "type": "string", "required": True, "description": "数据"}
        ],
        "icon": "minimize"
    },
    "gzip_decompress": {
        "id": "gzip_decompress",
        "name": "Gzip解压",
        "name_en": "Gzip Decompress",
        "description": "Gzip解压",
        "category": "compress",
        "subcategory": "decompress",
        "api_endpoint": "/api/gzip-decompress",
        "method": "POST",
        "params": [
            {"name": "data", "type": "string", "required": True, "description": "数据"}
        ],
        "icon": "maximize"
    },
    "zlib_compress": {
        "id": "zlib_compress",
        "name": "Zlib压缩",
        "name_en": "Zlib Compress",
        "description": "Zlib压缩",
        "category": "compress",
        "subcategory": "compress",
        "api_endpoint": "/api/zlib-compress",
        "method": "POST",
        "params": [
            {"name": "data", "type": "string", "required": True, "description": "数据"}
        ],
        "icon": "minimize"
    },
    "zlib_decompress": {
        "id": "zlib_decompress",
        "name": "Zlib解压",
        "name_en": "Zlib Decompress",
        "description": "Zlib解压",
        "category": "compress",
        "subcategory": "decompress",
        "api_endpoint": "/api/zlib-decompress",
        "method": "POST",
        "params": [
            {"name": "data", "type": "string", "required": True, "description": "数据"}
        ],
        "icon": "maximize"
    },

    # ========== 国际化工具 ==========
    "slugify": {
        "id": "slugify",
        "name": "Slug化",
        "name_en": "Slugify",
        "description": "文本转URL友好格式",
        "category": "i18n",
        "subcategory": "transform",
        "api_endpoint": "/api/slugify",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "link"
    },
    "to_ascii": {
        "id": "to_ascii",
        "name": "转ASCII",
        "name_en": "To ASCII",
        "description": "转ASCII字符",
        "category": "i18n",
        "subcategory": "convert",
        "api_endpoint": "/api/to-ascii",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "type"
    },
    "to_unicode": {
        "id": "to_unicode",
        "name": "转Unicode",
        "name_en": "To Unicode",
        "description": "转Unicode字符",
        "category": "i18n",
        "subcategory": "convert",
        "api_endpoint": "/api/to-unicode",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "type"
    },
    "normalize_unicode": {
        "id": "normalize_unicode",
        "name": "Unicode标准化",
        "name_en": "Normalize Unicode",
        "description": "Unicode标准化",
        "category": "i18n",
        "subcategory": "normalize",
        "api_endpoint": "/api/normalize-unicode",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "form", "type": "string", "required": False, "description": "形式"}
        ],
        "icon": "type"
    },

    # ========== 格式化工具 ==========
    "format_phone": {
        "id": "format_phone",
        "name": "格式化电话",
        "name_en": "Format Phone",
        "description": "格式化电话号码",
        "category": "format",
        "subcategory": "phone",
        "api_endpoint": "/api/format-phone",
        "method": "POST",
        "params": [
            {"name": "phone", "type": "string", "required": True, "description": "电话"},
            {"name": "country", "type": "string", "required": False, "description": "国家"}
        ],
        "icon": "phone"
    },
    "format_credit_card": {
        "id": "format_credit_card",
        "name": "格式化信用卡",
        "name_en": "Format Credit Card",
        "description": "格式化信用卡号",
        "category": "format",
        "subcategory": "financial",
        "api_endpoint": "/api/format-credit-card",
        "method": "POST",
        "params": [
            {"name": "card", "type": "string", "required": True, "description": "卡号"}
        ],
        "icon": "credit-card"
    },
    "mask_credit_card": {
        "id": "mask_credit_card",
        "name": "遮蔽信用卡",
        "name_en": "Mask Credit Card",
        "description": "遮蔽信用卡号",
        "category": "format",
        "subcategory": "financial",
        "api_endpoint": "/api/mask-credit-card",
        "method": "POST",
        "params": [
            {"name": "card", "type": "string", "required": True, "description": "卡号"}
        ],
        "icon": "eye-off"
    },
    "mask_email": {
        "id": "mask_email",
        "name": "遮蔽邮箱",
        "name_en": "Mask Email",
        "description": "遮蔽邮箱地址",
        "category": "format",
        "subcategory": "email",
        "api_endpoint": "/api/mask-email",
        "method": "POST",
        "params": [
            {"name": "email", "type": "string", "required": True, "description": "邮箱"}
        ],
        "icon": "eye-off"
    },
    "format_date": {
        "id": "format_date",
        "name": "格式化日期",
        "name_en": "Format Date",
        "description": "格式化日期",
        "category": "format",
        "subcategory": "date",
        "api_endpoint": "/api/format-date",
        "method": "POST",
        "params": [
            {"name": "date", "type": "string", "required": True, "description": "日期"},
            {"name": "format", "type": "string", "required": True, "description": "格式"}
        ],
        "icon": "calendar"
    },
    "format_time": {
        "id": "format_time",
        "name": "格式化时间",
        "name_en": "Format Time",
        "description": "格式化时间",
        "category": "format",
        "subcategory": "time",
        "api_endpoint": "/api/format-time",
        "method": "POST",
        "params": [
            {"name": "time", "type": "string", "required": True, "description": "时间"},
            {"name": "format", "type": "string", "required": True, "description": "格式"}
        ],
        "icon": "clock"
    },

    # ========== 批处理工具 ==========
    "batch": {
        "id": "batch",
        "name": "批处理",
        "name_en": "Batch",
        "description": "分批处理数组",
        "category": "batch",
        "subcategory": "process",
        "api_endpoint": "/api/batch",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "size", "type": "number", "required": True, "description": "批次大小"}
        ],
        "icon": "layers"
    },
    "chunk": {
        "id": "chunk",
        "name": "分块",
        "name_en": "Chunk",
        "description": "将数组分块",
        "category": "batch",
        "subcategory": "process",
        "api_endpoint": "/api/chunk",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "size", "type": "number", "required": True, "description": "块大小"}
        ],
        "icon": "grid"
    },
    "partition": {
        "id": "partition",
        "name": "分区",
        "name_en": "Partition",
        "description": "将数组分区",
        "category": "batch",
        "subcategory": "process",
        "api_endpoint": "/api/partition",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "fn", "type": "string", "required": True, "description": "分区函数"}
        ],
        "icon": "columns"
    },
    "group_by": {
        "id": "group_by",
        "name": "分组",
        "name_en": "Group By",
        "description": "按键分组",
        "category": "batch",
        "subcategory": "group",
        "api_endpoint": "/api/group-by",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "key", "type": "string", "required": True, "description": "分组键"}
        ],
        "icon": "group"
    },
    "count_by": {
        "id": "count_by",
        "name": "计数",
        "name_en": "Count By",
        "description": "按函数计数",
        "category": "batch",
        "subcategory": "aggregate",
        "api_endpoint": "/api/count-by",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "fn", "type": "string", "required": True, "description": "计数函数"}
        ],
        "icon": "hash"
    },

    # ========== 管道工具 ==========
    "pipe": {
        "id": "pipe",
        "name": "管道",
        "name_en": "Pipe",
        "description": "管道处理",
        "category": "pipe",
        "subcategory": "process",
        "api_endpoint": "/api/pipe",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "初始值"},
            {"name": "fns", "type": "array", "required": True, "description": "函数数组"}
        ],
        "icon": "arrow-right"
    },
    "compose": {
        "id": "compose",
        "name": "组合",
        "name_en": "Compose",
        "description": "组合函数",
        "category": "pipe",
        "subcategory": "function",
        "api_endpoint": "/api/compose",
        "method": "POST",
        "params": [
            {"name": "fns", "type": "array", "required": True, "description": "函数数组"}
        ],
        "icon": "link"
    },
    "trace": {
        "id": "trace",
        "name": "追踪",
        "name_en": "Trace",
        "description": "追踪函数调用",
        "category": "pipe",
        "subcategory": "debug",
        "api_endpoint": "/api/trace",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "值"},
            {"name": "fn", "type": "string", "required": True, "description": "函数"}
        ],
        "icon": "activity"
    },

    # ========== 异步工具 ==========
    "delay": {
        "id": "delay",
        "name": "延迟",
        "name_en": "Delay",
        "description": "延迟执行",
        "category": "async",
        "subcategory": "timing",
        "api_endpoint": "/api/delay",
        "method": "POST",
        "params": [
            {"name": "ms", "type": "number", "required": True, "description": "毫秒"}
        ],
        "icon": "clock"
    },
    "timeout": {
        "id": "timeout",
        "name": "超时",
        "name_en": "Timeout",
        "description": "设置超时",
        "category": "async",
        "subcategory": "timing",
        "api_endpoint": "/api/timeout",
        "method": "POST",
        "params": [
            {"name": "fn", "type": "string", "required": True, "description": "函数"},
            {"name": "ms", "type": "number", "required": True, "description": "超时毫秒"}
        ],
        "icon": "clock"
    },
    "retry": {
        "id": "retry",
        "name": "重试",
        "name_en": "Retry",
        "description": "重试操作",
        "category": "async",
        "subcategory": "retry",
        "api_endpoint": "/api/retry",
        "method": "POST",
        "params": [
            {"name": "fn", "type": "string", "required": True, "description": "函数"},
            {"name": "attempts", "type": "number", "required": False, "description": "尝试次数"}
        ],
        "icon": "refresh-cw"
    },
    "debounce": {
        "id": "debounce",
        "name": "防抖",
        "name_en": "Debounce",
        "description": "防抖函数",
        "category": "async",
        "subcategory": "timing",
        "api_endpoint": "/api/debounce",
        "method": "POST",
        "params": [
            {"name": "fn", "type": "string", "required": True, "description": "函数"},
            {"name": "ms", "type": "number", "required": True, "description": "毫秒"}
        ],
        "icon": "clock"
    },
    "throttle": {
        "id": "throttle",
        "name": "节流",
        "name_en": "Throttle",
        "description": "节流函数",
        "category": "async",
        "subcategory": "timing",
        "api_endpoint": "/api/throttle",
        "method": "POST",
        "params": [
            {"name": "fn", "type": "string", "required": True, "description": "函数"},
            {"name": "ms", "type": "number", "required": True, "description": "毫秒"}
        ],
        "icon": "clock"
    },

    # ========== 缓存工具 ==========
    "memoize": {
        "id": "memoize",
        "name": "记忆化",
        "name_en": "Memoize",
        "description": "缓存函数结果",
        "category": "cache",
        "subcategory": "memoize",
        "api_endpoint": "/api/memoize",
        "method": "POST",
        "params": [
            {"name": "fn", "type": "string", "required": True, "description": "函数"},
            {"name": "args", "type": "array", "required": True, "description": "参数"}
        ],
        "icon": "database"
    },
    "cache_get": {
        "id": "cache_get",
        "name": "缓存获取",
        "name_en": "Cache Get",
        "description": "获取缓存值",
        "category": "cache",
        "subcategory": "access",
        "api_endpoint": "/api/cache-get",
        "method": "POST",
        "params": [
            {"name": "key", "type": "string", "required": True, "description": "键"}
        ],
        "icon": "database"
    },
    "cache_set": {
        "id": "cache_set",
        "name": "缓存设置",
        "name_en": "Cache Set",
        "description": "设置缓存值",
        "category": "cache",
        "subcategory": "mutate",
        "api_endpoint": "/api/cache-set",
        "method": "POST",
        "params": [
            {"name": "key", "type": "string", "required": True, "description": "键"},
            {"name": "value", "type": "any", "required": True, "description": "值"},
            {"name": "ttl", "type": "number", "required": False, "description": "过期秒数"}
        ],
        "icon": "database"
    },
    "cache_clear": {
        "id": "cache_clear",
        "name": "缓存清除",
        "name_en": "Cache Clear",
        "description": "清除所有缓存",
        "category": "cache",
        "subcategory": "mutate",
        "api_endpoint": "/api/cache-clear",
        "method": "POST",
        "params": [],
        "icon": "trash"
    },

    # ========== 事件工具 ==========
    "emit": {
        "id": "emit",
        "name": "发送事件",
        "name_en": "Emit",
        "description": "发送事件",
        "category": "event",
        "subcategory": "emit",
        "api_endpoint": "/api/emit",
        "method": "POST",
        "params": [
            {"name": "event", "type": "string", "required": True, "description": "事件名"},
            {"name": "data", "type": "any", "required": True, "description": "数据"}
        ],
        "icon": "zap"
    },
    "on": {
        "id": "on",
        "name": "监听事件",
        "name_en": "On",
        "description": "监听事件",
        "category": "event",
        "subcategory": "listen",
        "api_endpoint": "/api/on",
        "method": "POST",
        "params": [
            {"name": "event", "type": "string", "required": True, "description": "事件名"},
            {"name": "fn", "type": "string", "required": True, "description": "处理函数"}
        ],
        "icon": "eye"
    },
    "off": {
        "id": "off",
        "name": "取消监听",
        "name_en": "Off",
        "description": "取消事件监听",
        "category": "event",
        "subcategory": "listen",
        "api_endpoint": "/api/off",
        "method": "POST",
        "params": [
            {"name": "event", "type": "string", "required": True, "description": "事件名"}
        ],
        "icon": "eye-off"
    },

    # ========== 日志工具 ==========
    "log": {
        "id": "log",
        "name": "日志",
        "name_en": "Log",
        "description": "记录日志",
        "category": "log",
        "subcategory": "write",
        "api_endpoint": "/api/log",
        "method": "POST",
        "params": [
            {"name": "message", "type": "string", "required": True, "description": "消息"},
            {"name": "level", "type": "string", "required": False, "description": "级别"}
        ],
        "icon": "file-text"
    },
    "log_debug": {
        "id": "log_debug",
        "name": "调试日志",
        "name_en": "Debug Log",
        "description": "记录调试日志",
        "category": "log",
        "subcategory": "write",
        "api_endpoint": "/api/log-debug",
        "method": "POST",
        "params": [
            {"name": "message", "type": "string", "required": True, "description": "消息"}
        ],
        "icon": "bug"
    },
    "log_error": {
        "id": "log_error",
        "name": "错误日志",
        "name_en": "Error Log",
        "description": "记录错误日志",
        "category": "log",
        "subcategory": "write",
        "api_endpoint": "/api/log-error",
        "method": "POST",
        "params": [
            {"name": "message", "type": "string", "required": True, "description": "消息"}
        ],
        "icon": "alert-circle"
    },
    "log_warn": {
        "id": "log_warn",
        "name": "警告日志",
        "name_en": "Warn Log",
        "description": "记录警告日志",
        "category": "log",
        "subcategory": "write",
        "api_endpoint": "/api/log-warn",
        "method": "POST",
        "params": [
            {"name": "message", "type": "string", "required": True, "description": "消息"}
        ],
        "icon": "alert-triangle"
    },

    # ========== 反射工具 ==========
    "typeof": {
        "id": "typeof",
        "name": "类型of",
        "name_en": "Typeof",
        "description": "获取值的类型",
        "category": "reflect",
        "subcategory": "type",
        "api_endpoint": "/api/typeof",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "值"}
        ],
        "icon": "code"
    },
    "to_type": {
        "id": "to_type",
        "name": "转类型",
        "name_en": "To Type",
        "description": "强制类型转换",
        "category": "reflect",
        "subcategory": "convert",
        "api_endpoint": "/api/to-type",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "值"},
            {"name": "type", "type": "string", "required": True, "description": "目标类型"}
        ],
        "icon": "refresh-cw"
    },

    # ========== 异常处理工具 ==========
    "try_catch": {
        "id": "try_catch",
        "name": "尝试捕获",
        "name_en": "Try Catch",
        "description": "尝试执行并捕获异常",
        "category": "exception",
        "subcategory": "handle",
        "api_endpoint": "/api/try-catch",
        "method": "POST",
        "params": [
            {"name": "fn", "type": "string", "required": True, "description": "函数"},
            {"name": "catch", "type": "string", "required": False, "description": "异常处理"}
        ],
        "icon": "shield"
    },
    "throw": {
        "id": "throw",
        "name": "抛出异常",
        "name_en": "Throw",
        "description": "抛出异常",
        "category": "exception",
        "subcategory": "throw",
        "api_endpoint": "/api/throw",
        "method": "POST",
        "params": [
            {"name": "message", "type": "string", "required": True, "description": "消息"}
        ],
        "icon": "alert-circle"
    },
    "is_error": {
        "id": "is_error",
        "name": "错误检查",
        "name_en": "Is Error",
        "description": "检查是否为错误",
        "category": "exception",
        "subcategory": "predicate",
        "api_endpoint": "/api/is-error",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "值"}
        ],
        "icon": "check"
    },

    # ========== 调试工具 ==========
    "debug": {
        "id": "debug",
        "name": "调试",
        "name_en": "Debug",
        "description": "输出调试信息",
        "category": "debug",
        "subcategory": "print",
        "api_endpoint": "/api/debug",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "值"}
        ],
        "icon": "bug"
    },
    "inspect": {
        "id": "inspect",
        "name": "检查",
        "name_en": "Inspect",
        "description": "检查对象结构",
        "category": "debug",
        "subcategory": "print",
        "api_endpoint": "/api/inspect",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "值"}
        ],
        "icon": "search"
    },
    "tap": {
        "id": "tap",
        "name": "点击",
        "name_en": "Tap",
        "description": "执行并返回",
        "category": "debug",
        "subcategory": "print",
        "api_endpoint": "/api/tap",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "值"},
            {"name": "fn", "type": "string", "required": False, "description": "函数"}
        ],
        "icon": "pointer"
    },

    # ========== 断言工具 ==========
    "assert": {
        "id": "assert",
        "name": "断言",
        "name_en": "Assert",
        "description": "断言条件为真",
        "category": "assert",
        "subcategory": "check",
        "api_endpoint": "/api/assert",
        "method": "POST",
        "params": [
            {"name": "condition", "type": "boolean", "required": True, "description": "条件"},
            {"name": "message", "type": "string", "required": False, "description": "消息"}
        ],
        "icon": "check-square"
    },
    "assert_equal": {
        "id": "assert_equal",
        "name": "断言相等",
        "name_en": "Assert Equal",
        "description": "断言两个值相等",
        "category": "assert",
        "subcategory": "check",
        "api_endpoint": "/api/assert-equal",
        "method": "POST",
        "params": [
            {"name": "a", "type": "any", "required": True, "description": "值A"},
            {"name": "b", "type": "any", "required": True, "description": "值B"}
        ],
        "icon": "equal"
    },
    "assert_not_equal": {
        "id": "assert_not_equal",
        "name": "断言不等",
        "name_en": "Assert Not Equal",
        "description": "断言两个值不等",
        "category": "assert",
        "subcategory": "check",
        "api_endpoint": "/api/assert-not-equal",
        "method": "POST",
        "params": [
            {"name": "a", "type": "any", "required": True, "description": "值A"},
            {"name": "b", "type": "any", "required": True, "description": "值B"}
        ],
        "icon": "not-equal"
    },
    "assert_type": {
        "id": "assert_type",
        "name": "断言类型",
        "name_en": "Assert Type",
        "description": "断言值类型",
        "category": "assert",
        "subcategory": "check",
        "api_endpoint": "/api/assert-type",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "值"},
            {"name": "type", "type": "string", "required": True, "description": "类型"}
        ],
        "icon": "code"
    },

    # ========== 测试工具 ==========
    "test": {
        "id": "test",
        "name": "测试",
        "name_en": "Test",
        "description": "运行测试",
        "category": "test",
        "subcategory": "run",
        "api_endpoint": "/api/test",
        "method": "POST",
        "params": [
            {"name": "fn", "type": "string", "required": True, "description": "测试函数"}
        ],
        "icon": "play"
    },
    "describe": {
        "id": "describe",
        "name": "描述测试",
        "name_en": "Describe",
        "description": "描述测试用例",
        "category": "test",
        "subcategory": "structure",
        "api_endpoint": "/api/describe",
        "method": "POST",
        "params": [
            {"name": "name", "type": "string", "required": True, "description": "名称"},
            {"name": "fn", "type": "string", "required": True, "description": "函数"}
        ],
        "icon": "file-text"
    },
    "it": {
        "id": "it",
        "name": "测试项",
        "name_en": "It",
        "description": "定义测试项",
        "category": "test",
        "subcategory": "structure",
        "api_endpoint": "/api/it",
        "method": "POST",
        "params": [
            {"name": "name", "type": "string", "required": True, "description": "名称"},
            {"name": "fn", "type": "string", "required": True, "description": "函数"}
        ],
        "icon": "check-circle"
    },
    "expect": {
        "id": "expect",
        "name": "期望",
        "name_en": "Expect",
        "description": "期望值",
        "category": "test",
        "subcategory": "assert",
        "api_endpoint": "/api/expect",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "值"}
        ],
        "icon": "eye"
    },

    # ========== 树形结构工具 ==========
    "tree_create": {
        "id": "tree_create",
        "name": "创建树",
        "name_en": "Create Tree",
        "description": "创建树结构",
        "category": "tree",
        "subcategory": "create",
        "api_endpoint": "/api/tree-create",
        "method": "POST",
        "params": [
            {"name": "data", "type": "any", "required": True, "description": "数据"},
            {"name": "children", "type": "string", "required": False, "description": "子节点键"}
        ],
        "icon": "git-branch"
    },
    "tree_get": {
        "id": "tree_get",
        "name": "获取节点",
        "name_en": "Get Node",
        "description": "获取树节点",
        "category": "tree",
        "subcategory": "access",
        "api_endpoint": "/api/tree-get",
        "method": "POST",
        "params": [
            {"name": "tree", "type": "any", "required": True, "description": "树"},
            {"name": "path", "type": "string", "required": True, "description": "路径"}
        ],
        "icon": "search"
    },
    "tree_set": {
        "id": "tree_set",
        "name": "设置节点",
        "name_en": "Set Node",
        "description": "设置树节点",
        "category": "tree",
        "subcategory": "mutate",
        "api_endpoint": "/api/tree-set",
        "method": "POST",
        "params": [
            {"name": "tree", "type": "any", "required": True, "description": "树"},
            {"name": "path", "type": "string", "required": True, "description": "路径"},
            {"name": "value", "type": "any", "required": True, "description": "值"}
        ],
        "icon": "edit"
    },
    "tree_flatten": {
        "id": "tree_flatten",
        "name": "树扁平化",
        "name_en": "Flatten Tree",
        "description": "将树扁平化",
        "category": "tree",
        "subcategory": "transform",
        "api_endpoint": "/api/tree-flatten",
        "method": "POST",
        "params": [
            {"name": "tree", "type": "any", "required": True, "description": "树"}
        ],
        "icon": "minimize"
    },
    "tree_map": {
        "id": "tree_map",
        "name": "树映射",
        "name_en": "Map Tree",
        "description": "映射树节点",
        "category": "tree",
        "subcategory": "transform",
        "api_endpoint": "/api/tree-map",
        "method": "POST",
        "params": [
            {"name": "tree", "type": "any", "required": True, "description": "树"},
            {"name": "fn", "type": "string", "required": True, "description": "映射函数"}
        ],
        "icon": "map"
    },

    # ========== 图结构工具 ==========
    "graph_create": {
        "id": "graph_create",
        "name": "创建图",
        "name_en": "Create Graph",
        "description": "创建图结构",
        "category": "graph",
        "subcategory": "create",
        "api_endpoint": "/api/graph-create",
        "method": "POST",
        "params": [
            {"name": "edges", "type": "array", "required": True, "description": "边数组"},
            {"name": "directed", "type": "boolean", "required": False, "description": "有向"}
        ],
        "icon": "git-branch"
    },
    "graph_add_node": {
        "id": "graph_add_node",
        "name": "添加节点",
        "name_en": "Add Node",
        "description": "添加图节点",
        "category": "graph",
        "subcategory": "mutate",
        "api_endpoint": "/api/graph-add-node",
        "method": "POST",
        "params": [
            {"name": "graph", "type": "any", "required": True, "description": "图"},
            {"name": "node", "type": "any", "required": True, "description": "节点"}
        ],
        "icon": "plus"
    },
    "graph_add_edge": {
        "id": "graph_add_edge",
        "name": "添加边",
        "name_en": "Add Edge",
        "description": "添加图边",
        "category": "graph",
        "subcategory": "mutate",
        "api_endpoint": "/api/graph-add-edge",
        "method": "POST",
        "params": [
            {"name": "graph", "type": "any", "required": True, "description": "图"},
            {"name": "from", "type": "any", "required": True, "description": "起点"},
            {"name": "to", "type": "any", "required": True, "description": "终点"}
        ],
        "icon": "link"
    },
    "graph_bfs": {
        "id": "graph_bfs",
        "name": "广度优先",
        "name_en": "BFS",
        "description": "广度优先搜索",
        "category": "graph",
        "subcategory": "traverse",
        "api_endpoint": "/api/graph-bfs",
        "method": "POST",
        "params": [
            {"name": "graph", "type": "any", "required": True, "description": "图"},
            {"name": "start", "type": "any", "required": True, "description": "起始节点"}
        ],
        "icon": "git-branch"
    },
    "graph_dfs": {
        "id": "graph_dfs",
        "name": "深度优先",
        "name_en": "DFS",
        "description": "深度优先搜索",
        "category": "graph",
        "subcategory": "traverse",
        "api_endpoint": "/api/graph-dfs",
        "method": "POST",
        "params": [
            {"name": "graph", "type": "any", "required": True, "description": "图"},
            {"name": "start", "type": "any", "required": True, "description": "起始节点"}
        ],
        "icon": "git-branch"
    },
    "graph_shortest_path": {
        "id": "graph_shortest_path",
        "name": "最短路径",
        "name_en": "Shortest Path",
        "description": "最短路径",
        "category": "graph",
        "subcategory": "path",
        "api_endpoint": "/api/graph-shortest-path",
        "method": "POST",
        "params": [
            {"name": "graph", "type": "any", "required": True, "description": "图"},
            {"name": "from", "type": "any", "required": True, "description": "起点"},
            {"name": "to", "type": "any", "required": True, "description": "终点"}
        ],
        "icon": "route"
    },

    # ========== 队列工具 ==========
    "queue_create": {
        "id": "queue_create",
        "name": "创建队列",
        "name_en": "Create Queue",
        "description": "创建队列",
        "category": "queue",
        "subcategory": "create",
        "api_endpoint": "/api/queue-create",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": False, "description": "初始元素"}
        ],
        "icon": "list"
    },
    "queue_enqueue": {
        "id": "queue_enqueue",
        "name": "入队",
        "name_en": "Enqueue",
        "description": "元素入队",
        "category": "queue",
        "subcategory": "mutate",
        "api_endpoint": "/api/queue-enqueue",
        "method": "POST",
        "params": [
            {"name": "queue", "type": "array", "required": True, "description": "队列"},
            {"name": "item", "type": "any", "required": True, "description": "元素"}
        ],
        "icon": "plus"
    },
    "queue_dequeue": {
        "id": "queue_dequeue",
        "name": "出队",
        "name_en": "Dequeue",
        "description": "元素出队",
        "category": "queue",
        "subcategory": "mutate",
        "api_endpoint": "/api/queue-dequeue",
        "method": "POST",
        "params": [
            {"name": "queue", "type": "array", "required": True, "description": "队列"}
        ],
        "icon": "minus"
    },
    "queue_peek": {
        "id": "queue_peek",
        "name": "查看队首",
        "name_en": "Peek Queue",
        "description": "查看队首元素",
        "category": "queue",
        "subcategory": "access",
        "api_endpoint": "/api/queue-peek",
        "method": "POST",
        "params": [
            {"name": "queue", "type": "array", "required": True, "description": "队列"}
        ],
        "icon": "eye"
    },

    # ========== 栈工具 ==========
    "stack_create": {
        "id": "stack_create",
        "name": "创建栈",
        "name_en": "Create Stack",
        "description": "创建栈",
        "category": "stack",
        "subcategory": "create",
        "api_endpoint": "/api/stack-create",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": False, "description": "初始元素"}
        ],
        "icon": "list"
    },
    "stack_push": {
        "id": "stack_push",
        "name": "压栈",
        "name_en": "Push",
        "description": "元素压栈",
        "category": "stack",
        "subcategory": "mutate",
        "api_endpoint": "/api/stack-push",
        "method": "POST",
        "params": [
            {"name": "stack", "type": "array", "required": True, "description": "栈"},
            {"name": "item", "type": "any", "required": True, "description": "元素"}
        ],
        "icon": "plus"
    },
    "stack_pop": {
        "id": "stack_pop",
        "name": "弹栈",
        "name_en": "Pop",
        "description": "元素弹栈",
        "category": "stack",
        "subcategory": "mutate",
        "api_endpoint": "/api/stack-pop",
        "method": "POST",
        "params": [
            {"name": "stack", "type": "array", "required": True, "description": "栈"}
        ],
        "icon": "minus"
    },
    "stack_peek": {
        "id": "stack_peek",
        "name": "查看栈顶",
        "name_en": "Peek Stack",
        "description": "查看栈顶元素",
        "category": "stack",
        "subcategory": "access",
        "api_endpoint": "/api/stack-peek",
        "method": "POST",
        "params": [
            {"name": "stack", "type": "array", "required": True, "description": "栈"}
        ],
        "icon": "eye"
    },

    # ========== 堆工具 ==========
    "heap_create": {
        "id": "heap_create",
        "name": "创建堆",
        "name_en": "Create Heap",
        "description": "创建堆",
        "category": "heap",
        "subcategory": "create",
        "api_endpoint": "/api/heap-create",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": False, "description": "初始元素"},
            {"name": "compare", "type": "string", "required": False, "description": "比较函数"}
        ],
        "icon": "list"
    },
    "heap_push": {
        "id": "heap_push",
        "name": "堆插入",
        "name_en": "Heap Push",
        "description": "插入堆元素",
        "category": "heap",
        "subcategory": "mutate",
        "api_endpoint": "/api/heap-push",
        "method": "POST",
        "params": [
            {"name": "heap", "type": "array", "required": True, "description": "堆"},
            {"name": "item", "type": "any", "required": True, "description": "元素"}
        ],
        "icon": "plus"
    },
    "heap_pop": {
        "id": "heap_pop",
        "name": "堆弹出",
        "name_en": "Heap Pop",
        "description": "弹出堆顶",
        "category": "heap",
        "subcategory": "mutate",
        "api_endpoint": "/api/heap-pop",
        "method": "POST",
        "params": [
            {"name": "heap", "type": "array", "required": True, "description": "堆"}
        ],
        "icon": "minus"
    },
    "heap_peek": {
        "id": "heap_peek",
        "name": "查看堆顶",
        "name_en": "Peek Heap",
        "description": "查看堆顶元素",
        "category": "heap",
        "subcategory": "access",
        "api_endpoint": "/api/heap-peek",
        "method": "POST",
        "params": [
            {"name": "heap", "type": "array", "required": True, "description": "堆"}
        ],
        "icon": "eye"
    },

    # ========== 集合工具 ==========
    "set_create": {
        "id": "set_create",
        "name": "创建集合",
        "name_en": "Create Set",
        "description": "创建集合",
        "category": "set",
        "subcategory": "create",
        "api_endpoint": "/api/set-create",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": False, "description": "初始元素"}
        ],
        "icon": "hash"
    },
    "set_add": {
        "id": "set_add",
        "name": "添加元素",
        "name_en": "Set Add",
        "description": "添加集合元素",
        "category": "set",
        "subcategory": "mutate",
        "api_endpoint": "/api/set-add",
        "method": "POST",
        "params": [
            {"name": "set", "type": "array", "required": True, "description": "集合"},
            {"name": "item", "type": "any", "required": True, "description": "元素"}
        ],
        "icon": "plus"
    },
    "set_remove": {
        "id": "set_remove",
        "name": "删除元素",
        "name_en": "Set Remove",
        "description": "删除集合元素",
        "category": "set",
        "subcategory": "mutate",
        "api_endpoint": "/api/set-remove",
        "method": "POST",
        "params": [
            {"name": "set", "type": "array", "required": True, "description": "集合"},
            {"name": "item", "type": "any", "required": True, "description": "元素"}
        ],
        "icon": "minus"
    },
    "set_has": {
        "id": "set_has",
        "name": "元素存在",
        "name_en": "Set Has",
        "description": "检查元素是否存在",
        "category": "set",
        "subcategory": "search",
        "api_endpoint": "/api/set-has",
        "method": "POST",
        "params": [
            {"name": "set", "type": "array", "required": True, "description": "集合"},
            {"name": "item", "type": "any", "required": True, "description": "元素"}
        ],
        "icon": "check"
    },
    "set_union": {
        "id": "set_union",
        "name": "集合并集",
        "name_en": "Set Union",
        "description": "集合并集",
        "category": "set",
        "subcategory": "operator",
        "api_endpoint": "/api/set-union",
        "method": "POST",
        "params": [
            {"name": "a", "type": "array", "required": True, "description": "集合A"},
            {"name": "b", "type": "array", "required": True, "description": "集合B"}
        ],
        "icon": "git-merge"
    },
    "set_intersection": {
        "id": "set_intersection",
        "name": "集合交集",
        "name_en": "Set Intersection",
        "description": "集合交集",
        "category": "set",
        "subcategory": "operator",
        "api_endpoint": "/api/set-intersection",
        "method": "POST",
        "params": [
            {"name": "a", "type": "array", "required": True, "description": "集合A"},
            {"name": "b", "type": "array", "required": True, "description": "集合B"}
        ],
        "icon": "git-intersect"
    },
    "set_difference": {
        "id": "set_difference",
        "name": "集合差集",
        "name_en": "Set Difference",
        "description": "集合差集",
        "category": "set",
        "subcategory": "operator",
        "api_endpoint": "/api/set-difference",
        "method": "POST",
        "params": [
            {"name": "a", "type": "array", "required": True, "description": "集合A"},
            {"name": "b", "type": "array", "required": True, "description": "集合B"}
        ],
        "icon": "git-merge"
    },

    # ========== 链表工具 ==========
    "list_create": {
        "id": "list_create",
        "name": "创建链表",
        "name_en": "Create List",
        "description": "创建链表",
        "category": "list",
        "subcategory": "create",
        "api_endpoint": "/api/list-create",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": False, "description": "初始元素"}
        ],
        "icon": "list"
    },
    "list_append": {
        "id": "list_append",
        "name": "追加",
        "name_en": "Append",
        "description": "链表追加",
        "category": "list",
        "subcategory": "mutate",
        "api_endpoint": "/api/list-append",
        "method": "POST",
        "params": [
            {"name": "list", "type": "array", "required": True, "description": "链表"},
            {"name": "item", "type": "any", "required": True, "description": "元素"}
        ],
        "icon": "plus"
    },
    "list_prepend": {
        "id": "list_prepend",
        "name": "前置",
        "name_en": "Prepend",
        "description": "链表前置",
        "category": "list",
        "subcategory": "mutate",
        "api_endpoint": "/api/list-prepend",
        "method": "POST",
        "params": [
            {"name": "list", "type": "array", "required": True, "description": "链表"},
            {"name": "item", "type": "any", "required": True, "description": "元素"}
        ],
        "icon": "plus"
    },
    "list_insert": {
        "id": "list_insert",
        "name": "插入",
        "name_en": "Insert",
        "description": "链表插入",
        "category": "list",
        "subcategory": "mutate",
        "api_endpoint": "/api/list-insert",
        "method": "POST",
        "params": [
            {"name": "list", "type": "array", "required": True, "description": "链表"},
            {"name": "index", "type": "number", "required": True, "description": "索引"},
            {"name": "item", "type": "any", "required": True, "description": "元素"}
        ],
        "icon": "edit"
    },
    "list_delete": {
        "id": "list_delete",
        "name": "删除",
        "name_en": "Delete",
        "description": "链表删除",
        "category": "list",
        "subcategory": "mutate",
        "api_endpoint": "/api/list-delete",
        "method": "POST",
        "params": [
            {"name": "list", "type": "array", "required": True, "description": "链表"},
            {"name": "index", "type": "number", "required": True, "description": "索引"}
        ],
        "icon": "trash"
    },
    "list_get": {
        "id": "list_get",
        "name": "获取",
        "name_en": "Get",
        "description": "获取链表元素",
        "category": "list",
        "subcategory": "access",
        "api_endpoint": "/api/list-get",
        "method": "POST",
        "params": [
            {"name": "list", "type": "array", "required": True, "description": "链表"},
            {"name": "index", "type": "number", "required": True, "description": "索引"}
        ],
        "icon": "search"
    },

    # ========== 表格工具 ==========
    "table_create": {
        "id": "table_create",
        "name": "创建表格",
        "name_en": "Create Table",
        "description": "创建表格",
        "category": "table",
        "subcategory": "create",
        "api_endpoint": "/api/table-create",
        "method": "POST",
        "params": [
            {"name": "headers", "type": "array", "required": True, "description": "表头"},
            {"name": "rows", "type": "array", "required": False, "description": "行数据"}
        ],
        "icon": "grid"
    },
    "table_select": {
        "id": "table_select",
        "name": "选择列",
        "name_en": "Select Columns",
        "description": "选择表格列",
        "category": "table",
        "subcategory": "query",
        "api_endpoint": "/api/table-select",
        "method": "POST",
        "params": [
            {"name": "table", "type": "array", "required": True, "description": "表格"},
            {"name": "columns", "type": "array", "required": True, "description": "列名"}
        ],
        "icon": "check-square"
    },
    "table_filter": {
        "id": "table_filter",
        "name": "过滤行",
        "name_en": "Filter Rows",
        "description": "过滤表格行",
        "category": "table",
        "subcategory": "query",
        "api_endpoint": "/api/table-filter",
        "method": "POST",
        "params": [
            {"name": "table", "type": "array", "required": True, "description": "表格"},
            {"name": "fn", "type": "string", "required": True, "description": "过滤函数"}
        ],
        "icon": "filter"
    },
    "table_sort": {
        "id": "table_sort",
        "name": "排序",
        "name_en": "Sort Table",
        "description": "表格排序",
        "category": "table",
        "subcategory": "transform",
        "api_endpoint": "/api/table-sort",
        "method": "POST",
        "params": [
            {"name": "table", "type": "array", "required": True, "description": "表格"},
            {"name": "column", "type": "string", "required": True, "description": "排序列"},
            {"name": "desc", "type": "boolean", "required": False, "description": "降序"}
        ],
        "icon": "sort-asc"
    },
    "table_group": {
        "id": "table_group",
        "name": "分组",
        "name_en": "Group Table",
        "description": "表格分组",
        "category": "table",
        "subcategory": "transform",
        "api_endpoint": "/api/table-group",
        "method": "POST",
        "params": [
            {"name": "table", "type": "array", "required": True, "description": "表格"},
            {"name": "column", "type": "string", "required": True, "description": "分组列"}
        ],
        "icon": "group"
    },
    "table_join": {
        "id": "table_join",
        "name": "连接表",
        "name_en": "Join Tables",
        "description": "连接两个表格",
        "category": "table",
        "subcategory": "transform",
        "api_endpoint": "/api/table-join",
        "method": "POST",
        "params": [
            {"name": "a", "type": "array", "required": True, "description": "表A"},
            {"name": "b", "type": "array", "required": True, "description": "表B"},
            {"name": "on", "type": "string", "required": True, "description": "连接键"}
        ],
        "icon": "link"
    },

    # ========== 缓冲区工具 ==========
    "buffer_create": {
        "id": "buffer_create",
        "name": "创建缓冲区",
        "name_en": "Create Buffer",
        "description": "创建缓冲区",
        "category": "buffer",
        "subcategory": "create",
        "api_endpoint": "/api/buffer-create",
        "method": "POST",
        "params": [
            {"name": "size", "type": "number", "required": False, "description": "大小"}
        ],
        "icon": "box"
    },
    "buffer_write": {
        "id": "buffer_write",
        "name": "写入",
        "name_en": "Write Buffer",
        "description": "写入缓冲区",
        "category": "buffer",
        "subcategory": "mutate",
        "api_endpoint": "/api/buffer-write",
        "method": "POST",
        "params": [
            {"name": "buffer", "type": "string", "required": True, "description": "缓冲区"},
            {"name": "data", "type": "any", "required": True, "description": "数据"}
        ],
        "icon": "edit"
    },
    "buffer_read": {
        "id": "buffer_read",
        "name": "读取",
        "name_en": "Read Buffer",
        "description": "读取缓冲区",
        "category": "buffer",
        "subcategory": "access",
        "api_endpoint": "/api/buffer-read",
        "method": "POST",
        "params": [
            {"name": "buffer", "type": "string", "required": True, "description": "缓冲区"}
        ],
        "icon": "search"
    },
    "buffer_clear": {
        "id": "buffer_clear",
        "name": "清空",
        "name_en": "Clear Buffer",
        "description": "清空缓冲区",
        "category": "buffer",
        "subcategory": "mutate",
        "api_endpoint": "/api/buffer-clear",
        "method": "POST",
        "params": [
            {"name": "buffer", "type": "string", "required": True, "description": "缓冲区"}
        ],
        "icon": "trash"
    },

    # ========== 环形缓冲区工具 ==========
    "ring_create": {
        "id": "ring_create",
        "name": "创建环",
        "name_en": "Create Ring",
        "description": "创建环形缓冲区",
        "category": "ring",
        "subcategory": "create",
        "api_endpoint": "/api/ring-create",
        "method": "POST",
        "params": [
            {"name": "size", "type": "number", "required": True, "description": "大小"}
        ],
        "icon": "repeat"
    },
    "ring_push": {
        "id": "ring_push",
        "name": "环插入",
        "name_en": "Ring Push",
        "description": "环缓冲区插入",
        "category": "ring",
        "subcategory": "mutate",
        "api_endpoint": "/api/ring-push",
        "method": "POST",
        "params": [
            {"name": "ring", "type": "array", "required": True, "description": "环"},
            {"name": "item", "type": "any", "required": True, "description": "元素"}
        ],
        "icon": "plus"
    },
    "ring_pop": {
        "id": "ring_pop",
        "name": "环弹出",
        "name_en": "Ring Pop",
        "description": "环缓冲区弹出",
        "category": "ring",
        "subcategory": "mutate",
        "api_endpoint": "/api/ring-pop",
        "method": "POST",
        "params": [
            {"name": "ring", "type": "array", "required": True, "description": "环"}
        ],
        "icon": "minus"
    },

    # ========== 布隆过滤器工具 ==========
    "bloom_create": {
        "id": "bloom_create",
        "name": "创建布隆过滤器",
        "name_en": "Create Bloom Filter",
        "description": "创建布隆过滤器",
        "category": "bloom",
        "subcategory": "create",
        "api_endpoint": "/api/bloom-create",
        "method": "POST",
        "params": [
            {"name": "size", "type": "number", "required": False, "description": "大小"},
            {"name": "hashes", "type": "number", "required": False, "description": "哈希数"}
        ],
        "icon": "filter"
    },
    "bloom_add": {
        "id": "bloom_add",
        "name": "布隆添加",
        "name_en": "Bloom Add",
        "description": "布隆过滤器添加",
        "category": "bloom",
        "subcategory": "mutate",
        "api_endpoint": "/api/bloom-add",
        "method": "POST",
        "params": [
            {"name": "bloom", "type": "any", "required": True, "description": "过滤器"},
            {"name": "item", "type": "string", "required": True, "description": "元素"}
        ],
        "icon": "plus"
    },
    "bloom_has": {
        "id": "bloom_has",
        "name": "布隆检查",
        "name_en": "Bloom Has",
        "description": "检查元素是否可能存在",
        "category": "bloom",
        "subcategory": "search",
        "api_endpoint": "/api/bloom-has",
        "method": "POST",
        "params": [
            {"name": "bloom", "type": "any", "required": True, "description": "过滤器"},
            {"name": "item", "type": "string", "required": True, "description": "元素"}
        ],
        "icon": "check"
    },

    # ========== LRU缓存工具 ==========
    "lru_create": {
        "id": "lru_create",
        "name": "创建LRU",
        "name_en": "Create LRU",
        "description": "创建LRU缓存",
        "category": "lru",
        "subcategory": "create",
        "api_endpoint": "/api/lru-create",
        "method": "POST",
        "params": [
            {"name": "capacity", "type": "number", "required": True, "description": "容量"}
        ],
        "icon": "database"
    },
    "lru_get": {
        "id": "lru_get",
        "name": "LRU获取",
        "name_en": "LRU Get",
        "description": "获取LRU缓存",
        "category": "lru",
        "subcategory": "access",
        "api_endpoint": "/api/lru-get",
        "method": "POST",
        "params": [
            {"name": "lru", "type": "any", "required": True, "description": "缓存"},
            {"name": "key", "type": "string", "required": True, "description": "键"}
        ],
        "icon": "search"
    },
    "lru_set": {
        "id": "lru_set",
        "name": "LRU设置",
        "name_en": "LRU Set",
        "description": "设置LRU缓存",
        "category": "lru",
        "subcategory": "mutate",
        "api_endpoint": "/api/lru-set",
        "method": "POST",
        "params": [
            {"name": "lru", "type": "any", "required": True, "description": "缓存"},
            {"name": "key", "type": "string", "required": True, "description": "键"},
            {"name": "value", "type": "any", "required": True, "description": "值"}
        ],
        "icon": "edit"
    },

    # ========== 跳表工具 ==========
    "skip_list_create": {
        "id": "skip_list_create",
        "name": "创建跳表",
        "name_en": "Create Skip List",
        "description": "创建跳表",
        "category": "skiplist",
        "subcategory": "create",
        "api_endpoint": "/api/skip-list-create",
        "method": "POST",
        "params": [
            {"name": "levels", "type": "number", "required": False, "description": "层数"}
        ],
        "icon": "list"
    },
    "skip_list_add": {
        "id": "skip_list_add",
        "name": "跳表添加",
        "name_en": "Skip List Add",
        "description": "跳表添加元素",
        "category": "skiplist",
        "subcategory": "mutate",
        "api_endpoint": "/api/skip-list-add",
        "method": "POST",
        "params": [
            {"name": "list", "type": "any", "required": True, "description": "跳表"},
            {"name": "item", "type": "any", "required": True, "description": "元素"}
        ],
        "icon": "plus"
    },
    "skip_list_has": {
        "id": "skip_list_has",
        "name": "跳表检查",
        "name_en": "Skip List Has",
        "description": "检查元素是否存在",
        "category": "skiplist",
        "subcategory": "search",
        "api_endpoint": "/api/skip-list-has",
        "method": "POST",
        "params": [
            {"name": "list", "type": "any", "required": True, "description": "跳表"},
            {"name": "item", "type": "any", "required": True, "description": "元素"}
        ],
        "icon": "check"
    },

    # ========== 字典树工具 ==========
    "trie_create": {
        "id": "trie_create",
        "name": "创建字典树",
        "name_en": "Create Trie",
        "description": "创建字典树",
        "category": "trie",
        "subcategory": "create",
        "api_endpoint": "/api/trie-create",
        "method": "POST",
        "params": [],
        "icon": "tree"
    },
    "trie_add": {
        "id": "trie_add",
        "name": "字典树添加",
        "name_en": "Trie Add",
        "description": "字典树添加单词",
        "category": "trie",
        "subcategory": "mutate",
        "api_endpoint": "/api/trie-add",
        "method": "POST",
        "params": [
            {"name": "trie", "type": "any", "required": True, "description": "字典树"},
            {"name": "word", "type": "string", "required": True, "description": "单词"}
        ],
        "icon": "plus"
    },
    "trie_has": {
        "id": "trie_has",
        "name": "字典树检查",
        "name_en": "Trie Has",
        "description": "检查单词是否存在",
        "category": "trie",
        "subcategory": "search",
        "api_endpoint": "/api/trie-has",
        "method": "POST",
        "params": [
            {"name": "trie", "type": "any", "required": True, "description": "字典树"},
            {"name": "word", "type": "string", "required": True, "description": "单词"}
        ],
        "icon": "check"
    },
    "trie_search": {
        "id": "trie_search",
        "name": "字典树搜索",
        "name_en": "Trie Search",
        "description": "搜索前缀",
        "category": "trie",
        "subcategory": "search",
        "api_endpoint": "/api/trie-search",
        "method": "POST",
        "params": [
            {"name": "trie", "type": "any", "required": True, "description": "字典树"},
            {"name": "prefix", "type": "string", "required": True, "description": "前缀"}
        ],
        "icon": "search"
    },

    # ========== 算法工具 ==========
    "bubble_sort": {
        "id": "bubble_sort",
        "name": "冒泡排序",
        "name_en": "Bubble Sort",
        "description": "冒泡排序",
        "category": "algorithm",
        "subcategory": "sort",
        "api_endpoint": "/api/bubble-sort",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "sort-asc"
    },
    "quick_sort": {
        "id": "quick_sort",
        "name": "快速排序",
        "name_en": "Quick Sort",
        "description": "快速排序",
        "category": "algorithm",
        "subcategory": "sort",
        "api_endpoint": "/api/quick-sort",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "sort-asc"
    },
    "merge_sort": {
        "id": "merge_sort",
        "name": "归并排序",
        "name_en": "Merge Sort",
        "description": "归并排序",
        "category": "algorithm",
        "subcategory": "sort",
        "api_endpoint": "/api/merge-sort",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "sort-asc"
    },
    "binary_search": {
        "id": "binary_search",
        "name": "二分搜索",
        "name_en": "Binary Search",
        "description": "二分搜索",
        "category": "algorithm",
        "subcategory": "search",
        "api_endpoint": "/api/binary-search",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "有序数组"},
            {"name": "target", "type": "any", "required": True, "description": "目标值"}
        ],
        "icon": "search"
    },
    "linear_search": {
        "id": "linear_search",
        "name": "线性搜索",
        "name_en": "Linear Search",
        "description": "线性搜索",
        "category": "algorithm",
        "subcategory": "search",
        "api_endpoint": "/api/linear-search",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "target", "type": "any", "required": True, "description": "目标值"}
        ],
        "icon": "search"
    },
    "dijkstra": {
        "id": "dijkstra",
        "name": "Dijkstra",
        "name_en": "Dijkstra",
        "description": "Dijkstra最短路径",
        "category": "algorithm",
        "subcategory": "graph",
        "api_endpoint": "/api/dijkstra",
        "method": "POST",
        "params": [
            {"name": "graph", "type": "any", "required": True, "description": "图"},
            {"name": "start", "type": "any", "required": True, "description": "起点"}
        ],
        "icon": "route"
    },
    "bellman_ford": {
        "id": "bellman_ford",
        "name": "Bellman-Ford",
        "name_en": "Bellman-Ford",
        "description": "Bellman-Ford最短路径",
        "category": "algorithm",
        "subcategory": "graph",
        "api_endpoint": "/api/bellman-ford",
        "method": "POST",
        "params": [
            {"name": "graph", "type": "any", "required": True, "description": "图"},
            {"name": "start", "type": "any", "required": True, "description": "起点"}
        ],
        "icon": "route"
    },
    "floyd_warshall": {
        "id": "floyd_warshall",
        "name": "Floyd-Warshall",
        "name_en": "Floyd-Warshall",
        "description": "Floyd-Warshall全源最短路径",
        "category": "algorithm",
        "subcategory": "graph",
        "api_endpoint": "/api/floyd-warshall",
        "method": "POST",
        "params": [
            {"name": "graph", "type": "any", "required": True, "description": "图"}
        ],
        "icon": "route"
    },
    "kruskal": {
        "id": "kruskal",
        "name": "Kruskal",
        "name_en": "Kruskal",
        "description": "Kruskal最小生成树",
        "category": "algorithm",
        "subcategory": "graph",
        "api_endpoint": "/api/kruskal",
        "method": "POST",
        "params": [
            {"name": "graph", "type": "any", "required": True, "description": "图"}
        ],
        "icon": "git-branch"
    },
    "prim": {
        "id": "prim",
        "name": "Prim",
        "name_en": "Prim",
        "description": "Prim最小生成树",
        "category": "algorithm",
        "subcategory": "graph",
        "api_endpoint": "/api/prim",
        "method": "POST",
        "params": [
            {"name": "graph", "type": "any", "required": True, "description": "图"}
        ],
        "icon": "git-branch"
    },
    "topological_sort": {
        "id": "topological_sort",
        "name": "拓扑排序",
        "name_en": "Topological Sort",
        "description": "拓扑排序",
        "category": "algorithm",
        "subcategory": "graph",
        "api_endpoint": "/api/topological-sort",
        "method": "POST",
        "params": [
            {"name": "graph", "type": "any", "required": True, "description": "有向无环图"}
        ],
        "icon": "git-branch"
    },
    "knapsack": {
        "id": "knapsack",
        "name": "背包问题",
        "name_en": "Knapsack",
        "description": "0-1背包问题",
        "category": "algorithm",
        "subcategory": "dp",
        "api_endpoint": "/api/knapsack",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "物品数组"},
            {"name": "capacity", "type": "number", "required": True, "description": "容量"}
        ],
        "icon": "box"
    },
    "levenshtein": {
        "id": "levenshtein",
        "name": "编辑距离",
        "name_en": "Levenshtein Distance",
        "description": "计算编辑距离",
        "category": "algorithm",
        "subcategory": "string",
        "api_endpoint": "/api/levenshtein",
        "method": "POST",
        "params": [
            {"name": "a", "type": "string", "required": True, "description": "字符串A"},
            {"name": "b", "type": "string", "required": True, "description": "字符串B"}
        ],
        "icon": "edit"
    },
    "lcs": {
        "id": "lcs",
        "name": "最长公共子序列",
        "name_en": "Longest Common Subsequence",
        "description": "计算LCS",
        "category": "algorithm",
        "subcategory": "string",
        "api_endpoint": "/api/lcs",
        "method": "POST",
        "params": [
            {"name": "a", "type": "string", "required": True, "description": "字符串A"},
            {"name": "b", "type": "string", "required": True, "description": "字符串B"}
        ],
        "icon": "git-branch"
    },

    # ========== 字符串搜索工具 ==========
    "find_all": {
        "id": "find_all",
        "name": "查找所有",
        "name_en": "Find All",
        "description": "查找所有匹配项",
        "category": "string",
        "subcategory": "search",
        "api_endpoint": "/api/find-all",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "search", "type": "string", "required": True, "description": "搜索字符串"}
        ],
        "icon": "search"
    },
    "find_all_regex": {
        "id": "find_all_regex",
        "name": "正则查找所有",
        "name_en": "Find All Regex",
        "description": "正则查找所有匹配",
        "category": "string",
        "subcategory": "search",
        "api_endpoint": "/api/find-all-regex",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "pattern", "type": "string", "required": True, "description": "正则模式"}
        ],
        "icon": "search"
    },
    "replace_all": {
        "id": "replace_all",
        "name": "替换所有",
        "name_en": "Replace All",
        "description": "替换所有匹配项",
        "category": "string",
        "subcategory": "transform",
        "api_endpoint": "/api/replace-all",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "search", "type": "string", "required": True, "description": "搜索字符串"},
            {"name": "replacement", "type": "string", "required": True, "description": "替换字符串"}
        ],
        "icon": "edit"
    },
    "replace_regex": {
        "id": "replace_regex",
        "name": "正则替换",
        "name_en": "Replace Regex",
        "description": "正则表达式替换",
        "category": "string",
        "subcategory": "transform",
        "api_endpoint": "/api/replace-regex",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "pattern", "type": "string", "required": True, "description": "正则模式"},
            {"name": "replacement", "type": "string", "required": True, "description": "替换字符串"}
        ],
        "icon": "edit"
    },
    "split_lines": {
        "id": "split_lines",
        "name": "分割行",
        "name_en": "Split Lines",
        "description": "按行分割",
        "category": "string",
        "subcategory": "transform",
        "api_endpoint": "/api/split-lines",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "divide"
    },
    "join_lines": {
        "id": "join_lines",
        "name": "合并行",
        "name_en": "Join Lines",
        "description": "合并行",
        "category": "string",
        "subcategory": "transform",
        "api_endpoint": "/api/join-lines",
        "method": "POST",
        "params": [
            {"name": "lines", "type": "array", "required": True, "description": "行数组"},
            {"name": "separator", "type": "string", "required": False, "description": "分隔符"}
        ],
        "icon": "link"
    },
    "trim_lines": {
        "id": "trim_lines",
        "name": "修剪行",
        "name_en": "Trim Lines",
        "description": "修剪每行",
        "category": "string",
        "subcategory": "transform",
        "api_endpoint": "/api/trim-lines",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "minus"
    },
    "filter_lines": {
        "id": "filter_lines",
        "name": "过滤行",
        "name_en": "Filter Lines",
        "description": "过滤行",
        "category": "string",
        "subcategory": "filter",
        "api_endpoint": "/api/filter-lines",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "fn", "type": "string", "required": True, "description": "过滤函数"}
        ],
        "icon": "filter"
    },
    "map_lines": {
        "id": "map_lines",
        "name": "映射行",
        "name_en": "Map Lines",
        "description": "映射每行",
        "category": "string",
        "subcategory": "transform",
        "api_endpoint": "/api/map-lines",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "fn", "type": "string", "required": True, "description": "映射函数"}
        ],
        "icon": "map"
    },

    # ========== 文本分析工具 ==========
    "word_frequency": {
        "id": "word_frequency",
        "name": "词频统计",
        "name_en": "Word Frequency",
        "description": "统计词频",
        "category": "text",
        "subcategory": "analyze",
        "api_endpoint": "/api/word-frequency",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "hash"
    },
    "char_frequency": {
        "id": "char_frequency",
        "name": "字符频率",
        "name_en": "Char Frequency",
        "description": "统计字符频率",
        "category": "text",
        "subcategory": "analyze",
        "api_endpoint": "/api/char-frequency",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "hash"
    },
    "ngrams": {
        "id": "ngrams",
        "name": "N元语法",
        "name_en": "Ngrams",
        "description": "生成N元语法",
        "category": "text",
        "subcategory": "analyze",
        "api_endpoint": "/api/ngrams",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "n", "type": "number", "required": True, "description": "N值"}
        ],
        "icon": "list"
    },
    "sentiment": {
        "id": "sentiment",
        "name": "情感分析",
        "name_en": "Sentiment",
        "description": "简单情感分析",
        "category": "text",
        "subcategory": "analyze",
        "api_endpoint": "/api/sentiment",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "heart"
    },
    "readability": {
        "id": "readability",
        "name": "可读性",
        "name_en": "Readability",
        "description": "计算可读性分数",
        "category": "text",
        "subcategory": "analyze",
        "api_endpoint": "/api/readability",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "book-open"
    },

    # ========== 文本生成工具 ==========
    "lorem_ipsum": {
        "id": "lorem_ipsum",
        "name": "随机文本",
        "name_en": "Lorem Ipsum",
        "description": "生成随机文本",
        "category": "text",
        "subcategory": "generate",
        "api_endpoint": "/api/lorem-ipsum",
        "method": "POST",
        "params": [
            {"name": "count", "type": "number", "required": False, "description": "段落数"}
        ],
        "icon": "file-text"
    },
    "generate_sentence": {
        "id": "generate_sentence",
        "name": "生成句子",
        "name_en": "Generate Sentence",
        "description": "生成随机句子",
        "category": "text",
        "subcategory": "generate",
        "api_endpoint": "/api/generate-sentence",
        "method": "POST",
        "params": [
            {"name": "words", "type": "number", "required": False, "description": "单词数"}
        ],
        "icon": "file-text"
    },
    "generate_paragraph": {
        "id": "generate_paragraph",
        "name": "生成段落",
        "name_en": "Generate Paragraph",
        "description": "生成随机段落",
        "category": "text",
        "subcategory": "generate",
        "api_endpoint": "/api/generate-paragraph",
        "method": "POST",
        "params": [
            {"name": "sentences", "type": "number", "required": False, "description": "句子数"}
        ],
        "icon": "file-text"
    },

    # ========== 转换工具 ==========
    "to_upper": {
        "id": "to_upper",
        "name": "转大写",
        "name_en": "To Upper",
        "description": "转大写",
        "category": "convert",
        "subcategory": "case",
        "api_endpoint": "/api/to-upper",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "arrow-up"
    },
    "to_lower": {
        "id": "to_lower",
        "name": "转小写",
        "name_en": "To Lower",
        "description": "转小写",
        "category": "convert",
        "subcategory": "case",
        "api_endpoint": "/api/to-lower",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "arrow-down"
    },
    "to_title": {
        "id": "to_title",
        "name": "转标题",
        "name_en": "To Title",
        "description": "转标题大小写",
        "category": "convert",
        "subcategory": "case",
        "api_endpoint": "/api/to-title",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "type"
    },
    "to_snake": {
        "id": "to_snake",
        "name": "转蛇形",
        "name_en": "To Snake Case",
        "description": "转蛇形命名",
        "category": "convert",
        "subcategory": "case",
        "api_endpoint": "/api/to-snake",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "minus"
    },
    "to_camel": {
        "id": "to_camel",
        "name": "转驼峰",
        "name_en": "To Camel Case",
        "description": "转驼峰命名",
        "category": "convert",
        "subcategory": "case",
        "api_endpoint": "/api/to-camel",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "arrow-up"
    },
    "to_pascal": {
        "id": "to_pascal",
        "name": "转帕斯卡",
        "name_en": "To Pascal Case",
        "description": "转帕斯卡命名",
        "category": "convert",
        "subcategory": "case",
        "api_endpoint": "/api/to-pascal",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "arrow-up-circle"
    },
    "to_kebab": {
        "id": "to_kebab",
        "name": "转串形",
        "name_en": "To Kebab Case",
        "description": "转串形命名",
        "category": "convert",
        "subcategory": "case",
        "api_endpoint": "/api/to-kebab",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "minus"
    },

    # ========== 验证工具 ==========
    "is_alpha": {
        "id": "is_alpha",
        "name": "字母检查",
        "name_en": "Is Alpha",
        "description": "是否全为字母",
        "category": "validate",
        "subcategory": "string",
        "api_endpoint": "/api/is-alpha",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "type"
    },
    "is_numeric": {
        "id": "is_numeric",
        "name": "数字检查",
        "name_en": "Is Numeric",
        "description": "是否全为数字",
        "category": "validate",
        "subcategory": "string",
        "api_endpoint": "/api/is-numeric",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "hash"
    },
    "is_alphanumeric": {
        "id": "is_alphanumeric",
        "name": "字母数字检查",
        "name_en": "Is Alphanumeric",
        "description": "是否字母数字",
        "category": "validate",
        "subcategory": "string",
        "api_endpoint": "/api/is-alphanumeric",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "type"
    },
    "is_blank": {
        "id": "is_blank",
        "name": "空白检查",
        "name_en": "Is Blank",
        "description": "是否全为空白",
        "category": "validate",
        "subcategory": "string",
        "api_endpoint": "/api/is-blank",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "minus"
    },
    "is_palindrome": {
        "id": "is_palindrome",
        "name": "回文检查",
        "name_en": "Is Palindrome",
        "description": "是否为回文",
        "category": "validate",
        "subcategory": "string",
        "api_endpoint": "/api/is-palindrome",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "check"
    },

    # ========== Base64工具 ==========
    "base64_encode": {
        "id": "base64_encode",
        "name": "Base64编码",
        "name_en": "Base64 Encode",
        "description": "Base64编码",
        "category": "encoding",
        "subcategory": "base64",
        "api_endpoint": "/api/base64-encode",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "lock"
    },
    "base64_decode": {
        "id": "base64_decode",
        "name": "Base64解码",
        "name_en": "Base64 Decode",
        "description": "Base64解码",
        "category": "encoding",
        "subcategory": "base64",
        "api_endpoint": "/api/base64-decode",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "unlock"
    },

    # ========== Hex工具 ==========
    "hex_encode": {
        "id": "hex_encode",
        "name": "Hex编码",
        "name_en": "Hex Encode",
        "description": "文本转Hex",
        "category": "encoding",
        "subcategory": "hex",
        "api_endpoint": "/api/hex-encode",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "hash"
    },
    "hex_decode": {
        "id": "hex_decode",
        "name": "Hex解码",
        "name_en": "Hex Decode",
        "description": "Hex转文本",
        "category": "encoding",
        "subcategory": "hex",
        "api_endpoint": "/api/hex-decode",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "Hex文本"}
        ],
        "icon": "hash"
    },

    # ========== URL编码工具 ==========
    "url_encode": {
        "id": "url_encode",
        "name": "URL编码",
        "name_en": "URL Encode",
        "description": "URL编码",
        "category": "encoding",
        "subcategory": "url",
        "api_endpoint": "/api/url-encode",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "link"
    },
    "url_decode": {
        "id": "url_decode",
        "name": "URL解码",
        "name_en": "URL Decode",
        "description": "URL解码",
        "category": "encoding",
        "subcategory": "url",
        "api_endpoint": "/api/url-decode",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "link"
    },

    # ========== HTML工具 ==========
    "html_escape": {
        "id": "html_escape",
        "name": "HTML转义",
        "name_en": "HTML Escape",
        "description": "HTML特殊字符转义",
        "category": "encoding",
        "subcategory": "html",
        "api_endpoint": "/api/html-escape",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "code"
    },
    "html_unescape": {
        "id": "html_unescape",
        "name": "HTML反转义",
        "name_en": "HTML Unescape",
        "description": "HTML反转义",
        "category": "encoding",
        "subcategory": "html",
        "api_endpoint": "/api/html-unescape",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "code"
    },
    "strip_tags": {
        "id": "strip_tags",
        "name": "去除标签",
        "name_en": "Strip Tags",
        "description": "去除HTML标签",
        "category": "encoding",
        "subcategory": "html",
        "api_endpoint": "/api/strip-tags",
        "method": "POST",
        "params": [
            {"name": "html", "type": "string", "required": True, "description": "HTML"}
        ],
        "icon": "code"
    },

    # ========== 百分比工具 ==========
    "percent_of": {
        "id": "percent_of",
        "name": "百分比",
        "name_en": "Percent Of",
        "description": "计算百分比",
        "category": "math",
        "subcategory": "percent",
        "api_endpoint": "/api/percent-of",
        "method": "POST",
        "params": [
            {"name": "value", "type": "number", "required": True, "description": "值"},
            {"name": "total", "type": "number", "required": True, "description": "总数"}
        ],
        "icon": "percent"
    },
    "percent_change": {
        "id": "percent_change",
        "name": "百分比变化",
        "name_en": "Percent Change",
        "description": "计算百分比变化",
        "category": "math",
        "subcategory": "percent",
        "api_endpoint": "/api/percent-change",
        "method": "POST",
        "params": [
            {"name": "old", "type": "number", "required": True, "description": "旧值"},
            {"name": "new", "type": "number", "required": True, "description": "新值"}
        ],
        "icon": "trending-up"
    },
    "percent_diff": {
        "id": "percent_diff",
        "name": "百分比差异",
        "name_en": "Percent Diff",
        "description": "计算百分比差异",
        "category": "math",
        "subcategory": "percent",
        "api_endpoint": "/api/percent-diff",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "值A"},
            {"name": "b", "type": "number", "required": True, "description": "值B"}
        ],
        "icon": "percent"
    },
    "percentile": {
        "id": "percentile",
        "name": "百分位数",
        "name_en": "Percentile",
        "description": "计算百分位数",
        "category": "math",
        "subcategory": "statistics",
        "api_endpoint": "/api/percentile",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "p", "type": "number", "required": True, "description": "百分位"}
        ],
        "icon": "bar-chart"
    },

    # ========== 三角函数工具 ==========
    "sin": {
        "id": "sin",
        "name": "正弦",
        "name_en": "Sine",
        "description": "计算正弦",
        "category": "math",
        "subcategory": "trigonometry",
        "api_endpoint": "/api/sin",
        "method": "POST",
        "params": [
            {"name": "angle", "type": "number", "required": True, "description": "角度"}
        ],
        "icon": "triangle"
    },
    "cos": {
        "id": "cos",
        "name": "余弦",
        "name_en": "Cosine",
        "description": "计算余弦",
        "category": "math",
        "subcategory": "trigonometry",
        "api_endpoint": "/api/cos",
        "method": "POST",
        "params": [
            {"name": "angle", "type": "number", "required": True, "description": "角度"}
        ],
        "icon": "triangle"
    },
    "tan": {
        "id": "tan",
        "name": "正切",
        "name_en": "Tangent",
        "description": "计算正切",
        "category": "math",
        "subcategory": "trigonometry",
        "api_endpoint": "/api/tan",
        "method": "POST",
        "params": [
            {"name": "angle", "type": "number", "required": True, "description": "角度"}
        ],
        "icon": "triangle"
    },
    "asin": {
        "id": "asin",
        "name": "反正弦",
        "name_en": "Arc Sine",
        "description": "计算反正弦",
        "category": "math",
        "subcategory": "trigonometry",
        "api_endpoint": "/api/asin",
        "method": "POST",
        "params": [
            {"name": "value", "type": "number", "required": True, "description": "值"}
        ],
        "icon": "triangle"
    },
    "acos": {
        "id": "acos",
        "name": "反余弦",
        "name_en": "Arc Cosine",
        "description": "计算反余弦",
        "category": "math",
        "subcategory": "trigonometry",
        "api_endpoint": "/api/acos",
        "method": "POST",
        "params": [
            {"name": "value", "type": "number", "required": True, "description": "值"}
        ],
        "icon": "triangle"
    },
    "atan": {
        "id": "atan",
        "name": "反正切",
        "name_en": "Arc Tangent",
        "description": "计算反正切",
        "category": "math",
        "subcategory": "trigonometry",
        "api_endpoint": "/api/atan",
        "method": "POST",
        "params": [
            {"name": "value", "type": "number", "required": True, "description": "值"}
        ],
        "icon": "triangle"
    },

    # ========== 复数工具 ==========
    "complex_add": {
        "id": "complex_add",
        "name": "复数加法",
        "name_en": "Complex Add",
        "description": "复数相加",
        "category": "math",
        "subcategory": "complex",
        "api_endpoint": "/api/complex-add",
        "method": "POST",
        "params": [
            {"name": "a", "type": "string", "required": True, "description": "复数A"},
            {"name": "b", "type": "string", "required": True, "description": "复数B"}
        ],
        "icon": "plus"
    },
    "complex_sub": {
        "id": "complex_sub",
        "name": "复数减法",
        "name_en": "Complex Sub",
        "description": "复数相减",
        "category": "math",
        "subcategory": "complex",
        "api_endpoint": "/api/complex-sub",
        "method": "POST",
        "params": [
            {"name": "a", "type": "string", "required": True, "description": "复数A"},
            {"name": "b", "type": "string", "required": True, "description": "复数B"}
        ],
        "icon": "minus"
    },
    "complex_mul": {
        "id": "complex_mul",
        "name": "复数乘法",
        "name_en": "Complex Mul",
        "description": "复数相乘",
        "category": "math",
        "subcategory": "complex",
        "api_endpoint": "/api/complex-mul",
        "method": "POST",
        "params": [
            {"name": "a", "type": "string", "required": True, "description": "复数A"},
            {"name": "b", "type": "string", "required": True, "description": "复数B"}
        ],
        "icon": "x"
    },
    "complex_div": {
        "id": "complex_div",
        "name": "复数除法",
        "name_en": "Complex Div",
        "description": "复数相除",
        "category": "math",
        "subcategory": "complex",
        "api_endpoint": "/api/complex-div",
        "method": "POST",
        "params": [
            {"name": "a", "type": "string", "required": True, "description": "复数A"},
            {"name": "b", "type": "string", "required": True, "description": "复数B"}
        ],
        "icon": "divide"
    },
    "complex_abs": {
        "id": "complex_abs",
        "name": "复数模",
        "name_en": "Complex Abs",
        "description": "复数的模",
        "category": "math",
        "subcategory": "complex",
        "api_endpoint": "/api/complex-abs",
        "method": "POST",
        "params": [
            {"name": "c", "type": "string", "required": True, "description": "复数"}
        ],
        "icon": "move"
    },

    # ========== 矩阵工具 ==========
    "matrix_add": {
        "id": "matrix_add",
        "name": "矩阵加法",
        "name_en": "Matrix Add",
        "description": "矩阵相加",
        "category": "math",
        "subcategory": "matrix",
        "api_endpoint": "/api/matrix-add",
        "method": "POST",
        "params": [
            {"name": "a", "type": "array", "required": True, "description": "矩阵A"},
            {"name": "b", "type": "array", "required": True, "description": "矩阵B"}
        ],
        "icon": "plus"
    },
    "matrix_sub": {
        "id": "matrix_sub",
        "name": "矩阵减法",
        "name_en": "Matrix Sub",
        "description": "矩阵相减",
        "category": "math",
        "subcategory": "matrix",
        "api_endpoint": "/api/matrix-sub",
        "method": "POST",
        "params": [
            {"name": "a", "type": "array", "required": True, "description": "矩阵A"},
            {"name": "b", "type": "array", "required": True, "description": "矩阵B"}
        ],
        "icon": "minus"
    },
    "matrix_mul": {
        "id": "matrix_mul",
        "name": "矩阵乘法",
        "name_en": "Matrix Mul",
        "description": "矩阵相乘",
        "category": "math",
        "subcategory": "matrix",
        "api_endpoint": "/api/matrix-mul",
        "method": "POST",
        "params": [
            {"name": "a", "type": "array", "required": True, "description": "矩阵A"},
            {"name": "b", "type": "array", "required": True, "description": "矩阵B"}
        ],
        "icon": "x"
    },
    "matrix_transpose": {
        "id": "matrix_transpose",
        "name": "矩阵转置",
        "name_en": "Matrix Transpose",
        "description": "矩阵转置",
        "category": "math",
        "subcategory": "matrix",
        "api_endpoint": "/api/matrix-transpose",
        "method": "POST",
        "params": [
            {"name": "m", "type": "array", "required": True, "description": "矩阵"}
        ],
        "icon": "repeat"
    },
    "matrix_det": {
        "id": "matrix_det",
        "name": "矩阵行列式",
        "name_en": "Matrix Det",
        "description": "计算行列式",
        "category": "math",
        "subcategory": "matrix",
        "api_endpoint": "/api/matrix-det",
        "method": "POST",
        "params": [
            {"name": "m", "type": "array", "required": True, "description": "矩阵"}
        ],
        "icon": "grid"
    },
    "matrix_inverse": {
        "id": "matrix_inverse",
        "name": "矩阵逆",
        "name_en": "Matrix Inverse",
        "description": "计算逆矩阵",
        "category": "math",
        "subcategory": "matrix",
        "api_endpoint": "/api/matrix-inverse",
        "method": "POST",
        "params": [
            {"name": "m", "type": "array", "required": True, "description": "矩阵"}
        ],
        "icon": "grid"
    },

    # ========== 向量工具 ==========
    "vector_add": {
        "id": "vector_add",
        "name": "向量加法",
        "name_en": "Vector Add",
        "description": "向量相加",
        "category": "math",
        "subcategory": "vector",
        "api_endpoint": "/api/vector-add",
        "method": "POST",
        "params": [
            {"name": "a", "type": "array", "required": True, "description": "向量A"},
            {"name": "b", "type": "array", "required": True, "description": "向量B"}
        ],
        "icon": "plus"
    },
    "vector_sub": {
        "id": "vector_sub",
        "name": "向量减法",
        "name_en": "Vector Sub",
        "description": "向量相减",
        "category": "math",
        "subcategory": "vector",
        "api_endpoint": "/api/vector-sub",
        "method": "POST",
        "params": [
            {"name": "a", "type": "array", "required": True, "description": "向量A"},
            {"name": "b", "type": "array", "required": True, "description": "向量B"}
        ],
        "icon": "minus"
    },
    "vector_dot": {
        "id": "vector_dot",
        "name": "向量点积",
        "name_en": "Vector Dot",
        "description": "计算点积",
        "category": "math",
        "subcategory": "vector",
        "api_endpoint": "/api/vector-dot",
        "method": "POST",
        "params": [
            {"name": "a", "type": "array", "required": True, "description": "向量A"},
            {"name": "b", "type": "array", "required": True, "description": "向量B"}
        ],
        "icon": "dot"
    },
    "vector_cross": {
        "id": "vector_cross",
        "name": "向量叉积",
        "name_en": "Vector Cross",
        "description": "计算叉积",
        "category": "math",
        "subcategory": "vector",
        "api_endpoint": "/api/vector-cross",
        "method": "POST",
        "params": [
            {"name": "a", "type": "array", "required": True, "description": "向量A"},
            {"name": "b", "type": "array", "required": True, "description": "向量B"}
        ],
        "icon": "crosshair"
    },
    "vector_magnitude": {
        "id": "vector_magnitude",
        "name": "向量模",
        "name_en": "Vector Magnitude",
        "description": "计算向量模",
        "category": "math",
        "subcategory": "vector",
        "api_endpoint": "/api/vector-magnitude",
        "method": "POST",
        "params": [
            {"name": "v", "type": "array", "required": True, "description": "向量"}
        ],
        "icon": "move"
    },
    "vector_normalize": {
        "id": "vector_normalize",
        "name": "向量归一化",
        "name_en": "Vector Normalize",
        "description": "归一化向量",
        "category": "math",
        "subcategory": "vector",
        "api_endpoint": "/api/vector-normalize",
        "method": "POST",
        "params": [
            {"name": "v", "type": "array", "required": True, "description": "向量"}
        ],
        "icon": "maximize"
    },

    # ========== 概率分布工具 ==========
    "random_normal": {
        "id": "random_normal",
        "name": "正态分布",
        "name_en": "Normal Distribution",
        "description": "生成正态分布随机数",
        "category": "probability",
        "subcategory": "distribution",
        "api_endpoint": "/api/random-normal",
        "method": "POST",
        "params": [
            {"name": "mean", "type": "number", "required": False, "description": "均值"},
            {"name": "std", "type": "number", "required": False, "description": "标准差"}
        ],
        "icon": "activity"
    },
    "random_uniform": {
        "id": "random_uniform",
        "name": "均匀分布",
        "name_en": "Uniform Distribution",
        "description": "生成均匀分布随机数",
        "category": "probability",
        "subcategory": "distribution",
        "api_endpoint": "/api/random-uniform",
        "method": "POST",
        "params": [
            {"name": "min", "type": "number", "required": False, "description": "最小值"},
            {"name": "max", "type": "number", "required": False, "description": "最大值"}
        ],
        "icon": "shuffle"
    },
    "random_exponential": {
        "id": "random_exponential",
        "name": "指数分布",
        "name_en": "Exponential Distribution",
        "description": "生成指数分布随机数",
        "category": "probability",
        "subcategory": "distribution",
        "api_endpoint": "/api/random-exponential",
        "method": "POST",
        "params": [
            {"name": "lambda", "type": "number", "required": False, "description": "lambda"}
        ],
        "icon": "activity"
    },
    "random_poisson": {
        "id": "random_poisson",
        "name": "泊松分布",
        "name_en": "Poisson Distribution",
        "description": "生成泊松分布随机数",
        "category": "probability",
        "subcategory": "distribution",
        "api_endpoint": "/api/random-poisson",
        "method": "POST",
        "params": [
            {"name": "lambda", "type": "number", "required": True, "description": "lambda"}
        ],
        "icon": "activity"
    },
    "random_binomial": {
        "id": "random_binomial",
        "name": "二项分布",
        "name_en": "Binomial Distribution",
        "description": "生成二项分布随机数",
        "category": "probability",
        "subcategory": "distribution",
        "api_endpoint": "/api/random-binomial",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "次数"},
            {"name": "p", "type": "number", "required": True, "description": "概率"}
        ],
        "icon": "activity"
    },

    # ========== 统计工具 ==========
    "mean": {
        "id": "mean",
        "name": "平均值",
        "name_en": "Mean",
        "description": "计算平均值",
        "category": "statistics",
        "subcategory": "average",
        "api_endpoint": "/api/mean",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "bar-chart"
    },
    "median": {
        "id": "median",
        "name": "中位数",
        "name_en": "Median",
        "description": "计算中位数",
        "category": "statistics",
        "subcategory": "average",
        "api_endpoint": "/api/median",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "bar-chart"
    },
    "mode": {
        "id": "mode",
        "name": "众数",
        "name_en": "Mode",
        "description": "计算众数",
        "category": "statistics",
        "subcategory": "average",
        "api_endpoint": "/api/mode",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "bar-chart"
    },
    "variance": {
        "id": "variance",
        "name": "方差",
        "name_en": "Variance",
        "description": "计算方差",
        "category": "statistics",
        "subcategory": "dispersion",
        "api_endpoint": "/api/variance",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "trending-up"
    },
    "std_dev": {
        "id": "std_dev",
        "name": "标准差",
        "name_en": "Standard Deviation",
        "description": "计算标准差",
        "category": "statistics",
        "subcategory": "dispersion",
        "api_endpoint": "/api/std-dev",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "trending-nesc"
    },
    "skewness": {
        "id": "skewness",
        "name": "偏度",
        "name_en": "Skewness",
        "description": "计算偏度",
        "category": "statistics",
        "subcategory": "shape",
        "api_endpoint": "/api/skewness",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "trending-up"
    },
    "kurtosis": {
        "id": "kurtosis",
        "name": "峰度",
        "name_en": "Kurtosis",
        "description": "计算峰度",
        "category": "statistics",
        "subcategory": "shape",
        "api_endpoint": "/api/kurtosis",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "trending-up"
    },
    "correlation": {
        "id": "correlation",
        "name": "相关系数",
        "name_en": "Correlation",
        "description": "计算相关系数",
        "category": "statistics",
        "subcategory": "relationship",
        "api_endpoint": "/api/correlation",
        "method": "POST",
        "params": [
            {"name": "x", "type": "array", "required": True, "description": "X数组"},
            {"name": "y", "type": "array", "required": True, "description": "Y数组"}
        ],
        "icon": "trending-up"
    },
    "covariance": {
        "id": "covariance",
        "name": "协方差",
        "name_en": "Covariance",
        "description": "计算协方差",
        "category": "statistics",
        "subcategory": "relationship",
        "api_endpoint": "/api/covariance",
        "method": "POST",
        "params": [
            {"name": "x", "type": "array", "required": True, "description": "X数组"},
            {"name": "y", "type": "array", "required": True, "description": "Y数组"}
        ],
        "icon": "trending-up"
    },

    # ========== 回归工具 ==========
    "linear_regression": {
        "id": "linear_regression",
        "name": "线性回归",
        "name_en": "Linear Regression",
        "description": "线性回归分析",
        "category": "regression",
        "subcategory": "linear",
        "api_endpoint": "/api/linear-regression",
        "method": "POST",
        "params": [
            {"name": "x", "type": "array", "required": True, "description": "X数组"},
            {"name": "y", "type": "array", "required": True, "description": "Y数组"}
        ],
        "icon": "trending-up"
    },
    "polynomial_regression": {
        "id": "polynomial_regression",
        "name": "多项式回归",
        "name_en": "Polynomial Regression",
        "description": "多项式回归分析",
        "category": "regression",
        "subcategory": "polynomial",
        "api_endpoint": "/api/polynomial-regression",
        "method": "POST",
        "params": [
            {"name": "x", "type": "array", "required": True, "description": "X数组"},
            {"name": "y", "type": "array", "required": True, "description": "Y数组"},
            {"name": "degree", "type": "number", "required": False, "description": "次数"}
        ],
        "icon": "trending-up"
    },

    # ========== 插值工具 ==========
    "lerp": {
        "id": "lerp",
        "name": "线性插值",
        "name_en": "Linear Interpolation",
        "description": "线性插值",
        "category": "interpolation",
        "subcategory": "linear",
        "api_endpoint": "/api/lerp",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "起点"},
            {"name": "b", "type": "number", "required": True, "description": "终点"},
            {"name": "t", "type": "number", "required": True, "description": "参数"}
        ],
        "icon": "move"
    },
    "slerp": {
        "id": "slerp",
        "name": "球面线性插值",
        "name_en": "Spherical Linear Interpolation",
        "description": "球面线性插值",
        "category": "interpolation",
        "subcategory": "spherical",
        "api_endpoint": "/api/slerp",
        "method": "POST",
        "params": [
            {"name": "a", "type": "array", "required": True, "description": "起点向量"},
            {"name": "b", "type": "array", "required": True, "description": "终点向量"},
            {"name": "t", "type": "number", "required": True, "description": "参数"}
        ],
        "icon": "move"
    },
    "bilinear_interpolate": {
        "id": "bilinear_interpolate",
        "name": "双线性插值",
        "name_en": "Bilinear Interpolation",
        "description": "双线性插值",
        "category": "interpolation",
        "subcategory": "2d",
        "api_endpoint": "/api/bilinear-interpolate",
        "method": "POST",
        "params": [
            {"name": "q", "type": "array", "required": True, "description": "四个点"},
            {"name": "tx", "type": "number", "required": True, "description": "X参数"},
            {"name": "ty", "type": "number", "required": True, "description": "Y参数"}
        ],
        "icon": "grid"
    },

    # ========== 平滑工具 ==========
    "moving_average": {
        "id": "moving_average",
        "name": "移动平均",
        "name_en": "Moving Average",
        "description": "计算移动平均",
        "category": "smoothing",
        "subcategory": "average",
        "api_endpoint": "/api/moving-average",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "window", "type": "number", "required": True, "description": "窗口大小"}
        ],
        "icon": "trending-up"
    },
    "exponential_smooth": {
        "id": "exponential_smooth",
        "name": "指数平滑",
        "name_en": "Exponential Smoothing",
        "description": "指数平滑",
        "category": "smoothing",
        "subcategory": "exponential",
        "api_endpoint": "/api/exponential-smooth",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "alpha", "type": "number", "required": False, "description": "alpha"}
        ],
        "icon": "trending-up"
    },
    "savitzky_golay": {
        "id": "savitzky_golay",
        "name": "Savitzky-Golay滤波",
        "name_en": "Savitzky-Golay Filter",
        "description": "Savitzky-Golay平滑",
        "category": "smoothing",
        "subcategory": "filter",
        "api_endpoint": "/api/savitzky-golay",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "window", "type": "number", "required": True, "description": "窗口"},
            {"name": "order", "type": "number", "required": False, "description": "阶数"}
        ],
        "icon": "activity"
    },

    # ========== 信号处理工具 ==========
    "convolve": {
        "id": "convolve",
        "name": "卷积",
        "name_en": "Convolve",
        "description": "计算卷积",
        "category": "signal",
        "subcategory": "convolution",
        "api_endpoint": "/api/convolve",
        "method": "POST",
        "params": [
            {"name": "signal", "type": "array", "required": True, "description": "信号"},
            {"name": "kernel", "type": "array", "required": True, "description": "核"}
        ],
        "icon": "activity"
    },
    "autocorrelate": {
        "id": "autocorrelate",
        "name": "自相关",
        "name_en": "Autocorrelate",
        "description": "计算自相关",
        "category": "signal",
        "subcategory": "correlation",
        "api_endpoint": "/api/autocorrelate",
        "method": "POST",
        "params": [
            {"name": "signal", "type": "array", "required": True, "description": "信号"}
        ],
        "icon": "activity"
    },
    "crosscorrelate": {
        "id": "crosscorrelate",
        "name": "互相关",
        "name_en": "Crosscorrelate",
        "description": "计算互相关",
        "category": "signal",
        "subcategory": "correlation",
        "api_endpoint": "/api/crosscorrelate",
        "method": "POST",
        "params": [
            {"name": "a", "type": "array", "required": True, "description": "信号A"},
            {"name": "b", "type": "array", "required": True, "description": "信号B"}
        ],
        "icon": "activity"
    },
    "fft": {
        "id": "fft",
        "name": "FFT",
        "name_en": "FFT",
        "description": "快速傅里叶变换",
        "category": "signal",
        "subcategory": "transform",
        "api_endpoint": "/api/fft",
        "method": "POST",
        "params": [
            {"name": "signal", "type": "array", "required": True, "description": "信号"}
        ],
        "icon": "activity"
    },
    "ifft": {
        "id": "ifft",
        "name": "IFFT",
        "name_en": "Inverse FFT",
        "description": "逆快速傅里叶变换",
        "category": "signal",
        "subcategory": "transform",
        "api_endpoint": "/api/ifft",
        "method": "POST",
        "params": [
            {"name": "spectrum", "type": "array", "required": True, "description": "频谱"}
        ],
        "icon": "activity"
    },

    # ========== 滤波器工具 ==========
    "lowpass_filter": {
        "id": "lowpass_filter",
        "name": "低通滤波",
        "name_en": "Low Pass Filter",
        "description": "低通滤波器",
        "category": "filter",
        "subcategory": "frequency",
        "api_endpoint": "/api/lowpass-filter",
        "method": "POST",
        "params": [
            {"name": "signal", "type": "array", "required": True, "description": "信号"},
            {"name": "cutoff", "type": "number", "required": True, "description": "截止频率"}
        ],
        "icon": "filter"
    },
    "highpass_filter": {
        "id": "highpass_filter",
        "name": "高通滤波",
        "name_en": "High Pass Filter",
        "description": "高通滤波器",
        "category": "filter",
        "subcategory": "frequency",
        "api_endpoint": "/api/highpass-filter",
        "method": "POST",
        "params": [
            {"name": "signal", "type": "array", "required": True, "description": "信号"},
            {"name": "cutoff", "type": "number", "required": True, "description": "截止频率"}
        ],
        "icon": "filter"
    },
    "bandpass_filter": {
        "id": "bandpass_filter",
        "name": "带通滤波",
        "name_en": "Band Pass Filter",
        "description": "带通滤波器",
        "category": "filter",
        "subcategory": "frequency",
        "api_endpoint": "/api/bandpass-filter",
        "method": "POST",
        "params": [
            {"name": "signal", "type": "array", "required": True, "description": "信号"},
            {"name": "low", "type": "number", "required": True, "description": "低频"},
            {"name": "high", "type": "number", "required": True, "description": "高频"}
        ],
        "icon": "filter"
    },
    "median_filter": {
        "id": "median_filter",
        "name": "中值滤波",
        "name_en": "Median Filter",
        "description": "中值滤波器",
        "category": "filter",
        "subcategory": "order",
        "api_endpoint": "/api/median-filter",
        "method": "POST",
        "params": [
            {"name": "signal", "type": "array", "required": True, "description": "信号"},
            {"name": "window", "type": "number", "required": True, "description": "窗口大小"}
        ],
        "icon": "filter"
    },
    "kalman_filter": {
        "id": "kalman_filter",
        "name": "卡尔曼滤波",
        "name_en": "Kalman Filter",
        "description": "卡尔曼滤波器",
        "category": "filter",
        "subcategory": "optimal",
        "api_endpoint": "/api/kalman-filter",
        "method": "POST",
        "params": [
            {"name": "measurement", "type": "number", "required": True, "description": "测量值"},
            {"name": "estimate", "type": "number", "required": False, "description": "估计值"}
        ],
        "icon": "filter"
    },

    # ========== 检测工具 ==========
    "peak_detect": {
        "id": "peak_detect",
        "name": "峰值检测",
        "name_en": "Peak Detection",
        "description": "检测峰值",
        "category": "detect",
        "subcategory": "peak",
        "api_endpoint": "/api/peak-detect",
        "method": "POST",
        "params": [
            {"name": "signal", "type": "array", "required": True, "description": "信号"},
            {"name": "threshold", "type": "number", "required": False, "description": "阈值"}
        ],
        "icon": "activity"
    },
    "zero_crossing": {
        "id": "zero_crossing",
        "name": "过零检测",
        "name_en": "Zero Crossing",
        "description": "检测过零点",
        "category": "detect",
        "subcategory": "zero",
        "api_endpoint": "/api/zero-crossing",
        "method": "POST",
        "params": [
            {"name": "signal", "type": "array", "required": True, "description": "信号"}
        ],
        "icon": "activity"
    },
    "envelope": {
        "id": "envelope",
        "name": "包络检测",
        "name_en": "Envelope Detection",
        "description": "检测信号包络",
        "category": "detect",
        "subcategory": "envelope",
        "api_endpoint": "/api/envelope",
        "method": "POST",
        "params": [
            {"name": "signal", "type": "array", "required": True, "description": "信号"}
        ],
        "icon": "activity"
    },

    # ========== 音频工具 ==========
    "audio_envelope": {
        "id": "audio_envelope",
        "name": "音频包络",
        "name_en": "Audio Envelope",
        "description": "生成音频包络",
        "category": "audio",
        "subcategory": "envelope",
        "api_endpoint": "/api/audio-envelope",
        "method": "POST",
        "params": [
            {"name": "attack", "type": "number", "required": False, "description": "起音"},
            {"name": "decay", "type": "number", "required": False, "description": "衰减"},
            {"name": "sustain", "type": "number", "required": False, "description": "持续"},
            {"name": "release", "type": "number", "required": False, "description": "释放"}
        ],
        "icon": "activity"
    },
    "audio_compressor": {
        "id": "audio_compressor",
        "name": "音频压缩",
        "name_en": "Audio Compressor",
        "description": "音频压缩器",
        "category": "audio",
        "subcategory": "dynamics",
        "api_endpoint": "/api/audio-compressor",
        "method": "POST",
        "params": [
            {"name": "signal", "type": "array", "required": True, "description": "信号"},
            {"name": "threshold", "type": "number", "required": False, "description": "阈值"},
            {"name": "ratio", "type": "number", "required": False, "description": "比率"}
        ],
        "icon": "activity"
    },
    "audio_delay": {
        "id": "audio_delay",
        "name": "音频延迟",
        "name_en": "Audio Delay",
        "description": "音频延迟效果",
        "category": "audio",
        "subcategory": "effect",
        "api_endpoint": "/api/audio-delay",
        "method": "POST",
        "params": [
            {"name": "signal", "type": "array", "required": True, "description": "信号"},
            {"name": "delay", "type": "number", "required": True, "description": "延迟时间"},
            {"name": "feedback", "type": "number", "required": False, "description": "反馈"}
        ],
        "icon": "activity"
    },
    "audio_reverb": {
        "id": "audio_reverb",
        "name": "音频混响",
        "name_en": "Audio Reverb",
        "description": "音频混响效果",
        "category": "audio",
        "subcategory": "effect",
        "api_endpoint": "/api/audio-reverb",
        "method": "POST",
        "params": [
            {"name": "signal", "type": "array", "required": True, "description": "信号"},
            {"name": "room_size", "type": "number", "required": False, "description": "房间大小"},
            {"name": "damping", "type": "number", "required": False, "description": "阻尼"}
        ],
        "icon": "activity"
    },
    "audio_chorus": {
        "id": "audio_chorus",
        "name": "音频合唱",
        "name_en": "Audio Chorus",
        "description": "音频合唱效果",
        "category": "audio",
        "subcategory": "effect",
        "api_endpoint": "/api/audio-chorus",
        "method": "POST",
        "params": [
            {"name": "signal", "type": "array", "required": True, "description": "信号"},
            {"name": "depth", "type": "number", "required": False, "description": "深度"},
            {"name": "rate", "type": "number", "required": False, "description": "速率"}
        ],
        "icon": "activity"
    },

    # ========== 图像处理工具 ==========
    "image_rotate": {
        "id": "image_rotate",
        "name": "图像旋转",
        "name_en": "Image Rotate",
        "description": "旋转图像",
        "category": "image",
        "subcategory": "transform",
        "api_endpoint": "/api/image-rotate",
        "method": "POST",
        "params": [
            {"name": "image", "type": "string", "required": True, "description": "图像数据"},
            {"name": "angle", "type": "number", "required": True, "description": "角度"}
        ],
        "icon": "rotate-cw"
    },
    "image_flip": {
        "id": "image_flip",
        "name": "图像翻转",
        "name_en": "Image Flip",
        "description": "翻转图像",
        "category": "image",
        "subcategory": "transform",
        "api_endpoint": "/api/image-flip",
        "method": "POST",
        "params": [
            {"name": "image", "type": "string", "required": True, "description": "图像数据"},
            {"name": "horizontal", "type": "boolean", "required": False, "description": "水平翻转"}
        ],
        "icon": "arrow-up-down"
    },
    "image_resize": {
        "id": "image_resize",
        "name": "图像缩放",
        "name_en": "Image Resize",
        "description": "缩放图像",
        "category": "image",
        "subcategory": "transform",
        "api_endpoint": "/api/image-resize",
        "method": "POST",
        "params": [
            {"name": "image", "type": "string", "required": True, "description": "图像数据"},
            {"name": "width", "type": "number", "required": True, "description": "宽度"},
            {"name": "height", "type": "number", "required": True, "description": "高度"}
        ],
        "icon": "maximize"
    },
    "image_crop": {
        "id": "image_crop",
        "name": "图像裁剪",
        "name_en": "Image Crop",
        "description": "裁剪图像",
        "category": "image",
        "subcategory": "transform",
        "api_endpoint": "/api/image-crop",
        "method": "POST",
        "params": [
            {"name": "image", "type": "string", "required": True, "description": "图像数据"},
            {"name": "x", "type": "number", "required": True, "description": "X"},
            {"name": "y", "type": "number", "required": True, "description": "Y"},
            {"name": "width", "type": "number", "required": True, "description": "宽度"},
            {"name": "height", "type": "number", "required": True, "description": "高度"}
        ],
        "icon": "crop"
    },
    "image_blur": {
        "id": "image_blur",
        "name": "图像模糊",
        "name_en": "Image Blur",
        "description": "模糊图像",
        "category": "image",
        "subcategory": "filter",
        "api_endpoint": "/api/image-blur",
        "method": "POST",
        "params": [
            {"name": "image", "type": "string", "required": True, "description": "图像数据"},
            {"name": "radius", "type": "number", "required": False, "description": "半径"}
        ],
        "icon": "droplet"
    },

    # ========== 视频处理工具 ==========
    "video_rotate": {
        "id": "video_rotate",
        "name": "视频旋转",
        "name_en": "Video Rotate",
        "description": "旋转视频",
        "category": "video",
        "subcategory": "transform",
        "api_endpoint": "/api/video-rotate",
        "method": "POST",
        "params": [
            {"name": "video", "type": "string", "required": True, "description": "视频数据"},
            {"name": "angle", "type": "number", "required": True, "description": "角度"}
        ],
        "icon": "rotate-cw"
    },
    "video_flip": {
        "id": "video_flip",
        "name": "视频翻转",
        "name_en": "Video Flip",
        "description": "翻转视频",
        "category": "video",
        "subcategory": "transform",
        "api_endpoint": "/api/video-flip",
        "method": "POST",
        "params": [
            {"name": "video", "type": "string", "required": True, "description": "视频数据"},
            {"name": "horizontal", "type": "boolean", "required": False, "description": "水平翻转"}
        ],
        "icon": "arrow-up-down"
    },
    "video_scale": {
        "id": "video_scale",
        "name": "视频缩放",
        "name_en": "Video Scale",
        "description": "缩放视频",
        "category": "video",
        "subcategory": "transform",
        "api_endpoint": "/api/video-scale",
        "method": "POST",
        "params": [
            {"name": "video", "type": "string", "required": True, "description": "视频数据"},
            {"name": "width", "type": "number", "required": True, "description": "宽度"},
            {"name": "height", "type": "number", "required": True, "description": "高度"}
        ],
        "icon": "maximize"
    },
    "video_crop": {
        "id": "video_crop",
        "name": "视频裁剪",
        "name_en": "Video Crop",
        "description": "裁剪视频",
        "category": "video",
        "subcategory": "transform",
        "api_endpoint": "/api/video-crop",
        "method": "POST",
        "params": [
            {"name": "video", "type": "string", "required": True, "description": "视频数据"},
            {"name": "x", "type": "number", "required": True, "description": "X"},
            {"name": "y", "type": "number", "required": True, "description": "Y"},
            {"name": "width", "type": "number", "required": True, "description": "宽度"},
            {"name": "height", "type": "number", "required": True, "description": "高度"}
        ],
        "icon": "crop"
    },
    "video_blur": {
        "id": "video_blur",
        "name": "视频模糊",
        "name_en": "Video Blur",
        "description": "模糊视频",
        "category": "video",
        "subcategory": "filter",
        "api_endpoint": "/api/video-blur",
        "method": "POST",
        "params": [
            {"name": "video", "type": "string", "required": True, "description": "视频数据"},
            {"name": "radius", "type": "number", "required": False, "description": "半径"}
        ],
        "icon": "droplet"
    },

    # ========== 几何计算工具 ==========
    "circle_area": {
        "id": "circle_area",
        "name": "圆面积",
        "name_en": "Circle Area",
        "description": "计算圆面积",
        "category": "geometry",
        "subcategory": "2d",
        "api_endpoint": "/api/circle-area",
        "method": "POST",
        "params": [
            {"name": "radius", "type": "number", "required": True, "description": "半径"}
        ],
        "icon": "circle"
    },
    "circle_circumference": {
        "id": "circle_circumference",
        "name": "圆周长",
        "name_en": "Circle Circumference",
        "description": "计算圆周长",
        "category": "geometry",
        "subcategory": "2d",
        "api_endpoint": "/api/circle-circumference",
        "method": "POST",
        "params": [
            {"name": "radius", "type": "number", "required": True, "description": "半径"}
        ],
        "icon": "circle"
    },
    "sphere_volume": {
        "id": "sphere_volume",
        "name": "球体积",
        "name_en": "Sphere Volume",
        "description": "计算球体积",
        "category": "geometry",
        "subcategory": "3d",
        "api_endpoint": "/api/sphere-volume",
        "method": "POST",
        "params": [
            {"name": "radius", "type": "number", "required": True, "description": "半径"}
        ],
        "icon": "circle"
    },
    "sphere_surface_area": {
        "id": "sphere_surface_area",
        "name": "球表面积",
        "name_en": "Sphere Surface Area",
        "description": "计算球表面积",
        "category": "geometry",
        "subcategory": "3d",
        "api_endpoint": "/api/sphere-surface-area",
        "method": "POST",
        "params": [
            {"name": "radius", "type": "number", "required": True, "description": "半径"}
        ],
        "icon": "circle"
    },
    "polygon_area": {
        "id": "polygon_area",
        "name": "多边形面积",
        "name_en": "Polygon Area",
        "description": "计算多边形面积",
        "category": "geometry",
        "subcategory": "2d",
        "api_endpoint": "/api/polygon-area",
        "method": "POST",
        "params": [
            {"name": "vertices", "type": "array", "required": True, "description": "顶点数组"}
        ],
        "icon": "triangle"
    },
    "line_intersection": {
        "id": "line_intersection",
        "name": "直线交点",
        "name_en": "Line Intersection",
        "description": "计算两条直线交点",
        "category": "geometry",
        "subcategory": "2d",
        "api_endpoint": "/api/line-intersection",
        "method": "POST",
        "params": [
            {"name": "p1", "type": "array", "required": True, "description": "直线1起点"},
            {"name": "p2", "type": "array", "required": True, "description": "直线1终点"},
            {"name": "p3", "type": "array", "required": True, "description": "直线2起点"},
            {"name": "p4", "type": "array", "required": True, "description": "直线2终点"}
        ],
        "icon": "crosshair"
    },
    "point_in_polygon": {
        "id": "point_in_polygon",
        "name": "点在多边形内",
        "name_en": "Point In Polygon",
        "description": "检查点是否在多边形内",
        "category": "geometry",
        "subcategory": "2d",
        "api_endpoint": "/api/point-in-polygon",
        "method": "POST",
        "params": [
            {"name": "point", "type": "array", "required": True, "description": "点"},
            {"name": "vertices", "type": "array", "required": True, "description": "多边形顶点"}
        ],
        "icon": "check-circle"
    },
    "distance_2d": {
        "id": "distance_2d",
        "name": "二维距离",
        "name_en": "2D Distance",
        "description": "计算两点间距离",
        "category": "geometry",
        "subcategory": "2d",
        "api_endpoint": "/api/distance-2d",
        "method": "POST",
        "params": [
            {"name": "x1", "type": "number", "required": True, "description": "X1"},
            {"name": "y1", "type": "number", "required": True, "description": "Y1"},
            {"name": "x2", "type": "number", "required": True, "description": "X2"},
            {"name": "y2", "type": "number", "required": True, "description": "Y2"}
        ],
        "icon": "move"
    },
    "distance_3d": {
        "id": "distance_3d",
        "name": "三维距离",
        "name_en": "3D Distance",
        "description": "计算三维距离",
        "category": "geometry",
        "subcategory": "3d",
        "api_endpoint": "/api/distance-3d",
        "method": "POST",
        "params": [
            {"name": "x1", "type": "number", "required": True, "description": "X1"},
            {"name": "y1", "type": "number", "required": True, "description": "Y1"},
            {"name": "z1", "type": "number", "required": True, "description": "Z1"},
            {"name": "x2", "type": "number", "required": True, "description": "X2"},
            {"name": "y2", "type": "number", "required": True, "description": "Y2"},
            {"name": "z2", "type": "number", "required": True, "description": "Z2"}
        ],
        "icon": "move"
    },

    # ========== 单位转换工具 ==========
    "celsius_to_fahrenheit": {
        "id": "celsius_to_fahrenheit",
        "name": "摄氏转华氏",
        "name_en": "Celsius to Fahrenheit",
        "description": "摄氏温度转华氏",
        "category": "convert",
        "subcategory": "temperature",
        "api_endpoint": "/api/celsius-to-fahrenheit",
        "method": "POST",
        "params": [
            {"name": "celsius", "type": "number", "required": True, "description": "摄氏温度"}
        ],
        "icon": "thermometer"
    },
    "fahrenheit_to_celsius": {
        "id": "fahrenheit_to_celsius",
        "name": "华氏转摄氏",
        "name_en": "Fahrenheit to Celsius",
        "description": "华氏温度转摄氏",
        "category": "convert",
        "subcategory": "temperature",
        "api_endpoint": "/api/fahrenheit-to-celsius",
        "method": "POST",
        "params": [
            {"name": "fahrenheit", "type": "number", "required": True, "description": "华氏温度"}
        ],
        "icon": "thermometer"
    },
    "km_to_miles": {
        "id": "km_to_miles",
        "name": "公里转英里",
        "name_en": "Km to Miles",
        "description": "公里转英里",
        "category": "convert",
        "subcategory": "distance",
        "api_endpoint": "/api/km-to-miles",
        "method": "POST",
        "params": [
            {"name": "km", "type": "number", "required": True, "description": "公里"}
        ],
        "icon": "map"
    },
    "miles_to_km": {
        "id": "miles_to_km",
        "name": "英里转公里",
        "name_en": "Miles to Km",
        "description": "英里转公里",
        "category": "convert",
        "subcategory": "distance",
        "api_endpoint": "/api/miles-to-km",
        "method": "POST",
        "params": [
            {"name": "miles", "type": "number", "required": True, "description": "英里"}
        ],
        "icon": "map"
    },
    "kg_to_lbs": {
        "id": "kg_to_lbs",
        "name": "公斤转磅",
        "name_en": "Kg to Lbs",
        "description": "公斤转磅",
        "category": "convert",
        "subcategory": "weight",
        "api_endpoint": "/api/kg-to-lbs",
        "method": "POST",
        "params": [
            {"name": "kg", "type": "number", "required": True, "description": "公斤"}
        ],
        "icon": "scale"
    },
    "lbs_to_kg": {
        "id": "lbs_to_kg",
        "name": "磅转公斤",
        "name_en": "Lbs to Kg",
        "description": "磅转公斤",
        "category": "convert",
        "subcategory": "weight",
        "api_endpoint": "/api/lbs-to-kg",
        "method": "POST",
        "params": [
            {"name": "lbs", "type": "number", "required": True, "description": "磅"}
        ],
        "icon": "scale"
    },
    "bytes_to_human": {
        "id": "bytes_to_human",
        "name": "字节转人类可读",
        "name_en": "Bytes to Human",
        "description": "字节数转人类可读格式",
        "category": "convert",
        "subcategory": "data",
        "api_endpoint": "/api/bytes-to-human",
        "method": "POST",
        "params": [
            {"name": "bytes", "type": "number", "required": True, "description": "字节数"}
        ],
        "icon": "hard-drive"
    },

    # ========== 时间相关 ==========
    "seconds_to_minutes": {
        "id": "seconds_to_minutes",
        "name": "秒转分钟",
        "name_en": "Seconds to Minutes",
        "description": "秒转分钟",
        "category": "convert",
        "subcategory": "time",
        "api_endpoint": "/api/seconds-to-minutes",
        "method": "POST",
        "params": [
            {"name": "seconds", "type": "number", "required": True, "description": "秒"}
        ],
        "icon": "clock"
    },
    "minutes_to_hours": {
        "id": "minutes_to_hours",
        "name": "分钟转小时",
        "name_en": "Minutes to Hours",
        "description": "分钟转小时",
        "category": "convert",
        "subcategory": "time",
        "api_endpoint": "/api/minutes-to-hours",
        "method": "POST",
        "params": [
            {"name": "minutes", "type": "number", "required": True, "description": "分钟"}
        ],
        "icon": "clock"
    },
    "hours_to_days": {
        "id": "hours_to_days",
        "name": "小时转天",
        "name_en": "Hours to Days",
        "description": "小时转天",
        "category": "convert",
        "subcategory": "time",
        "api_endpoint": "/api/hours-to-days",
        "method": "POST",
        "params": [
            {"name": "hours", "type": "number", "required": True, "description": "小时"}
        ],
        "icon": "calendar"
    },

    # ========== 通用转换 ==========
    "int_to_float": {
        "id": "int_to_float",
        "name": "整数转浮点",
        "name_en": "Int to Float",
        "description": "整数转浮点数",
        "category": "convert",
        "subcategory": "type",
        "api_endpoint": "/api/int-to-float",
        "method": "POST",
        "params": [
            {"name": "value", "type": "number", "required": True, "description": "整数"}
        ],
        "icon": "hash"
    },
    "float_to_int": {
        "id": "float_to_int",
        "name": "浮点转整数",
        "name_en": "Float to Int",
        "description": "浮点数转整数",
        "category": "convert",
        "subcategory": "type",
        "api_endpoint": "/api/float-to-int",
        "method": "POST",
        "params": [
            {"name": "value", "type": "number", "required": True, "description": "浮点数"}
        ],
        "icon": "hash"
    },
    "str_to_int": {
        "id": "str_to_int",
        "name": "字符串转整数",
        "name_en": "Str to Int",
        "description": "字符串转整数",
        "category": "convert",
        "subcategory": "type",
        "api_endpoint": "/api/str-to-int",
        "method": "POST",
        "params": [
            {"name": "value", "type": "string", "required": True, "description": "字符串"}
        ],
        "icon": "type"
    },
    "str_to_float": {
        "id": "str_to_float",
        "name": "字符串转浮点",
        "name_en": "Str to Float",
        "description": "字符串转浮点数",
        "category": "convert",
        "subcategory": "type",
        "api_endpoint": "/api/str-to-float",
        "method": "POST",
        "params": [
            {"name": "value", "type": "string", "required": True, "description": "字符串"}
        ],
        "icon": "type"
    },
    "int_to_str": {
        "id": "int_to_str",
        "name": "整数转字符串",
        "name_en": "Int to Str",
        "description": "整数转字符串",
        "category": "convert",
        "subcategory": "type",
        "api_endpoint": "/api/int-to-str",
        "method": "POST",
        "params": [
            {"name": "value", "type": "number", "required": True, "description": "整数"}
        ],
        "icon": "type"
    },
    "bool_to_int": {
        "id": "bool_to_int",
        "name": "布尔转整数",
        "name_en": "Bool to Int",
        "description": "布尔转整数",
        "category": "convert",
        "subcategory": "type",
        "api_endpoint": "/api/bool-to-int",
        "method": "POST",
        "params": [
            {"name": "value", "type": "boolean", "required": True, "description": "布尔值"}
        ],
        "icon": "check-square"
    },
    "int_to_bool": {
        "id": "int_to_bool",
        "name": "整数转布尔",
        "name_en": "Int to Bool",
        "description": "整数转布尔",
        "category": "convert",
        "subcategory": "type",
        "api_endpoint": "/api/int-to-bool",
        "method": "POST",
        "params": [
            {"name": "value", "type": "number", "required": True, "description": "整数"}
        ],
        "icon": "check-square"
    },

    # ========== 对象操作工具 ==========
    "object_get": {
        "id": "object_get",
        "name": "对象取值",
        "name_en": "Object Get",
        "description": "安全获取对象属性",
        "category": "object",
        "subcategory": "access",
        "api_endpoint": "/api/object-get",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "对象"},
            {"name": "path", "type": "string", "required": True, "description": "属性路径"},
            {"name": "default", "type": "any", "required": False, "description": "默认值"}
        ],
        "icon": "key"
    },
    "object_set": {
        "id": "object_set",
        "name": "对象设值",
        "name_en": "Object Set",
        "description": "设置对象属性",
        "category": "object",
        "subcategory": "mutate",
        "api_endpoint": "/api/object-set",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "对象"},
            {"name": "path", "type": "string", "required": True, "description": "属性路径"},
            {"name": "value", "type": "any", "required": True, "description": "值"}
        ],
        "icon": "edit"
    },
    "object_delete": {
        "id": "object_delete",
        "name": "对象删除",
        "name_en": "Object Delete",
        "description": "删除对象属性",
        "category": "object",
        "subcategory": "mutate",
        "api_endpoint": "/api/object-delete",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "对象"},
            {"name": "path", "type": "string", "required": True, "description": "属性路径"}
        ],
        "icon": "trash"
    },
    "object_has": {
        "id": "object_has",
        "name": "对象属性检查",
        "name_en": "Object Has",
        "description": "检查对象是否有属性",
        "category": "object",
        "subcategory": "predicate",
        "api_endpoint": "/api/object-has",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "对象"},
            {"name": "path", "type": "string", "required": True, "description": "属性路径"}
        ],
        "icon": "key"
    },
    "object_keys": {
        "id": "object_keys",
        "name": "对象键列表",
        "name_en": "Object Keys",
        "description": "获取对象所有键",
        "category": "object",
        "subcategory": "access",
        "api_endpoint": "/api/object-keys",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "对象"}
        ],
        "icon": "list"
    },
    "object_values": {
        "id": "object_values",
        "name": "对象值列表",
        "name_en": "Object Values",
        "description": "获取对象所有值",
        "category": "object",
        "subcategory": "access",
        "api_endpoint": "/api/object-values",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "对象"}
        ],
        "icon": "list"
    },
    "object_entries": {
        "id": "object_entries",
        "name": "对象条目列表",
        "name_en": "Object Entries",
        "description": "获取对象所有键值对",
        "category": "object",
        "subcategory": "access",
        "api_endpoint": "/api/object-entries",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "对象"}
        ],
        "icon": "list"
    },
    "object_merge": {
        "id": "object_merge",
        "name": "对象合并",
        "name_en": "Object Merge",
        "description": "合并多个对象",
        "category": "object",
        "subcategory": "transform",
        "api_endpoint": "/api/object-merge",
        "method": "POST",
        "params": [
            {"name": "objects", "type": "array", "required": True, "description": "对象数组"}
        ],
        "icon": "git-merge"
    },
    "object_pick": {
        "id": "object_pick",
        "name": "对象选择",
        "name_en": "Object Pick",
        "description": "选择对象部分属性",
        "category": "object",
        "subcategory": "transform",
        "api_endpoint": "/api/object-pick",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "对象"},
            {"name": "keys", "type": "array", "required": True, "description": "要选择的键"}
        ],
        "icon": "check-square"
    },
    "object_omit": {
        "id": "object_omit",
        "name": "对象排除",
        "name_en": "Object Omit",
        "description": "排除对象部分属性",
        "category": "object",
        "subcategory": "transform",
        "api_endpoint": "/api/object-omit",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "对象"},
            {"name": "keys", "type": "array", "required": True, "description": "要排除的键"}
        ],
        "icon": "x-square"
    },
    "object_clone": {
        "id": "object_clone",
        "name": "对象克隆",
        "name_en": "Object Clone",
        "description": "克隆对象",
        "category": "object",
        "subcategory": "transform",
        "api_endpoint": "/api/object-clone",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "对象"}
        ],
        "icon": "copy"
    },

    # ========== 数组查找工具 ==========
    "array_find": {
        "id": "array_find",
        "name": "数组查找",
        "name_en": "Array Find",
        "description": "查找满足条件的元素",
        "category": "array",
        "subcategory": "search",
        "api_endpoint": "/api/array-find",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "fn", "type": "string", "required": True, "description": "查找函数"}
        ],
        "icon": "search"
    },
    "array_find_index": {
        "id": "array_find_index",
        "name": "数组查找索引",
        "name_en": "Array Find Index",
        "description": "查找满足条件的元素索引",
        "category": "array",
        "subcategory": "search",
        "api_endpoint": "/api/array-find-index",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "fn", "type": "string", "required": True, "description": "查找函数"}
        ],
        "icon": "hash"
    },
    "array_includes": {
        "id": "array_includes",
        "name": "数组包含",
        "name_en": "Array Includes",
        "description": "检查数组是否包含元素",
        "category": "array",
        "subcategory": "search",
        "api_endpoint": "/api/array-includes",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "value", "type": "any", "required": True, "description": "要检查的值"}
        ],
        "icon": "check-circle"
    },
    "array_index_of": {
        "id": "array_index_of",
        "name": "数组索引",
        "name_en": "Array Index Of",
        "description": "查找元素首次出现的索引",
        "category": "array",
        "subcategory": "search",
        "api_endpoint": "/api/array-index-of",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "value", "type": "any", "required": True, "description": "要查找的值"}
        ],
        "icon": "hash"
    },
    "array_last_index_of": {
        "id": "array_last_index_of",
        "name": "数组最后索引",
        "name_en": "Array Last Index Of",
        "description": "查找元素最后出现的位置",
        "category": "array",
        "subcategory": "search",
        "api_endpoint": "/api/array-last-index-of",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "value", "type": "any", "required": True, "description": "要查找的值"}
        ],
        "icon": "hash"
    },

    # ========== 数组变换工具 ==========
    "array_map": {
        "id": "array_map",
        "name": "数组映射",
        "name_en": "Array Map",
        "description": "映射数组元素",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/array-map",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "fn", "type": "string", "required": True, "description": "映射函数"}
        ],
        "icon": "map"
    },
    "array_filter": {
        "id": "array_filter",
        "name": "数组过滤",
        "name_en": "Array Filter",
        "description": "过滤数组元素",
        "category": "array",
        "subcategory": "filter",
        "api_endpoint": "/api/array-filter",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "fn", "type": "string", "required": True, "description": "过滤函数"}
        ],
        "icon": "filter"
    },
    "array_reduce": {
        "id": "array_reduce",
        "name": "数组归约",
        "name_en": "Array Reduce",
        "description": "归约数组元素",
        "category": "array",
        "subcategory": "aggregate",
        "api_endpoint": "/api/array-reduce",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "fn", "type": "string", "required": True, "description": "归约函数"},
            {"name": "initial", "type": "any", "required": False, "description": "初始值"}
        ],
        "icon": "git-merge"
    },
    "array_flatten": {
        "id": "array_flatten",
        "name": "数组扁平化",
        "name_en": "Array Flatten",
        "description": "扁平化数组",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/array-flatten",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "嵌套数组"}
        ],
        "icon": "minimize"
    },
    "array_unique": {
        "id": "array_unique",
        "name": "数组去重",
        "name_en": "Array Unique",
        "description": "数组去重",
        "category": "array",
        "subcategory": "filter",
        "api_endpoint": "/api/array-unique",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "trash-2"
    },
    "array_compact": {
        "id": "array_compact",
        "name": "数组压缩",
        "name_en": "Array Compact",
        "description": "移除假值",
        "category": "array",
        "subcategory": "filter",
        "api_endpoint": "/api/array-compact",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "compress"
    },
    "array_sort": {
        "id": "array_sort",
        "name": "数组排序",
        "name_en": "Array Sort",
        "description": "排序数组",
        "category": "array",
        "subcategory": "sort",
        "api_endpoint": "/api/array-sort",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "fn", "type": "string", "required": False, "description": "排序函数"}
        ],
        "icon": "sort-asc"
    },
    "array_reverse": {
        "id": "array_reverse",
        "name": "数组反转",
        "name_en": "Array Reverse",
        "description": "反转数组",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/array-reverse",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "rotate-ccw"
    },
    "array_concat": {
        "id": "array_concat",
        "name": "数组连接",
        "name_en": "Array Concat",
        "description": "连接多个数组",
        "category": "array",
        "subcategory": "transform",
        "api_endpoint": "/api/array-concat",
        "method": "POST",
        "params": [
            {"name": "arrays", "type": "array", "required": True, "description": "数组数组"}
        ],
        "icon": "link"
    },
    "array_slice": {
        "id": "array_slice",
        "name": "数组切片",
        "name_en": "Array Slice",
        "description": "切片数组",
        "category": "array",
        "subcategory": "access",
        "api_endpoint": "/api/array-slice",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "start", "type": "number", "required": True, "description": "起始"},
            {"name": "end", "type": "number", "required": False, "description": "结束"}
        ],
        "icon": "scissors"
    },

    # ========== 数组聚合工具 ==========
    "array_sum": {
        "id": "array_sum",
        "name": "数组求和",
        "name_en": "Array Sum",
        "description": "计算数组总和",
        "category": "array",
        "subcategory": "aggregate",
        "api_endpoint": "/api/array-sum",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "plus"
    },
    "array_product": {
        "id": "array_product",
        "name": "数组求积",
        "name_en": "Array Product",
        "description": "计算数组乘积",
        "category": "array",
        "subcategory": "aggregate",
        "api_endpoint": "/api/array-product",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "x"
    },
    "array_average": {
        "id": "array_average",
        "name": "数组平均值",
        "name_en": "Array Average",
        "description": "计算数组平均值",
        "category": "array",
        "subcategory": "aggregate",
        "api_endpoint": "/api/array-average",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "divide"
    },
    "array_count": {
        "id": "array_count",
        "name": "数组计数",
        "name_en": "Array Count",
        "description": "计算满足条件的元素数",
        "category": "array",
        "subcategory": "aggregate",
        "api_endpoint": "/api/array-count",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "fn", "type": "string", "required": False, "description": "计数函数"}
        ],
        "icon": "hash"
    },
    "array_every": {
        "id": "array_every",
        "name": "数组全部满足",
        "name_en": "Array Every",
        "description": "检查是否所有元素都满足条件",
        "category": "array",
        "subcategory": "search",
        "api_endpoint": "/api/array-every",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "fn", "type": "string", "required": True, "description": "检查函数"}
        ],
        "icon": "check"
    },
    "array_some": {
        "id": "array_some",
        "name": "数组部分满足",
        "name_en": "Array Some",
        "description": "检查是否有元素满足条件",
        "category": "array",
        "subcategory": "search",
        "api_endpoint": "/api/array-some",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "fn", "type": "string", "required": True, "description": "检查函数"}
        ],
        "icon": "check-square"
    },

    # ========== 数组分组工具 ==========
    "array_group_by": {
        "id": "array_group_by",
        "name": "数组分组",
        "name_en": "Array Group By",
        "description": "按键分组",
        "category": "array",
        "subcategory": "group",
        "api_endpoint": "/api/array-group-by",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "key", "type": "string", "required": True, "description": "分组键"}
        ],
        "icon": "group"
    },
    "array_partition": {
        "id": "array_partition",
        "name": "数组分区",
        "name_en": "Array Partition",
        "description": "将数组分为两部分",
        "category": "array",
        "subcategory": "group",
        "api_endpoint": "/api/array-partition",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "fn", "type": "string", "required": True, "description": "分区函数"}
        ],
        "icon": "columns"
    },
    "array_chunk": {
        "id": "array_chunk",
        "name": "数组分块",
        "name_en": "Array Chunk",
        "description": "将数组分成多个块",
        "category": "array",
        "subcategory": "group",
        "api_endpoint": "/api/array-chunk",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "size", "type": "number", "required": True, "description": "块大小"}
        ],
        "icon": "grid"
    },

    # ========== 数组操作工具 ==========
    "array_drop": {
        "id": "array_drop",
        "name": "数组丢弃",
        "name_en": "Array Drop",
        "description": "丢弃前N个元素",
        "category": "array",
        "subcategory": "access",
        "api_endpoint": "/api/array-drop",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "n", "type": "number", "required": True, "description": "丢弃数量"}
        ],
        "icon": "arrow-right"
    },
    "array_take": {
        "id": "array_take",
        "name": "数组取",
        "name_en": "Array Take",
        "description": "取前N个元素",
        "category": "array",
        "subcategory": "access",
        "api_endpoint": "/api/array-take",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "n", "type": "number", "required": True, "description": "取数量"}
        ],
        "icon": "arrow-left"
    },
    "array_head": {
        "id": "array_head",
        "name": "数组头部",
        "name_en": "Array Head",
        "description": "获取数组第一个元素",
        "category": "array",
        "subcategory": "access",
        "api_endpoint": "/api/array-head",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "arrow-left"
    },
    "array_tail": {
        "id": "array_tail",
        "name": "数组尾部",
        "name_en": "Array Tail",
        "description": "获取数组除第一个外的所有元素",
        "category": "array",
        "subcategory": "access",
        "api_endpoint": "/api/array-tail",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "arrow-right"
    },
    "array_init": {
        "id": "array_init",
        "name": "数组初始",
        "name_en": "Array Init",
        "description": "获取数组除最后一个外的所有元素",
        "category": "array",
        "subcategory": "access",
        "api_endpoint": "/api/array-init",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "arrow-left"
    },
    "array_last": {
        "id": "array_last",
        "name": "数组最后一个",
        "name_en": "Array Last",
        "description": "获取数组最后一个元素",
        "category": "array",
        "subcategory": "access",
        "api_endpoint": "/api/array-last",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "arrow-right"
    },

    # ========== 数组数学工具 ==========
    "array_min": {
        "id": "array_min",
        "name": "数组最小值",
        "name_en": "Array Min",
        "description": "获取数组最小值",
        "category": "array",
        "subcategory": "aggregate",
        "api_endpoint": "/api/array-min",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "chevron-down"
    },
    "array_max": {
        "id": "array_max",
        "name": "数组最大值",
        "name_en": "Array Max",
        "description": "获取数组最大值",
        "category": "array",
        "subcategory": "aggregate",
        "api_endpoint": "/api/array-max",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "chevron-up"
    },
    "array_min_by": {
        "id": "array_min_by",
        "name": "数组最小值by",
        "name_en": "Array Min By",
        "description": "按函数获取最小值",
        "category": "array",
        "subcategory": "aggregate",
        "api_endpoint": "/api/array-min-by",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "fn", "type": "string", "required": True, "description": "比较函数"}
        ],
        "icon": "chevron-down"
    },
    "array_max_by": {
        "id": "array_max_by",
        "name": "数组最大值by",
        "name_en": "Array Max By",
        "description": "按函数获取最大值",
        "category": "array",
        "subcategory": "aggregate",
        "api_endpoint": "/api/array-max-by",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数组"},
            {"name": "fn", "type": "string", "required": True, "description": "比较函数"}
        ],
        "icon": "chevron-up"
    },

    # ========== 数组交集并集差集 ==========
    "array_union": {
        "id": "array_union",
        "name": "数组并集",
        "name_en": "Array Union",
        "description": "获取数组并集",
        "category": "array",
        "subcategory": "set",
        "api_endpoint": "/api/array-union",
        "method": "POST",
        "params": [
            {"name": "arrays", "type": "array", "required": True, "description": "数组数组"}
        ],
        "icon": "git-merge"
    },
    "array_intersection": {
        "id": "array_intersection",
        "name": "数组交集",
        "name_en": "Array Intersection",
        "description": "获取数组交集",
        "category": "array",
        "subcategory": "set",
        "api_endpoint": "/api/array-intersection",
        "method": "POST",
        "params": [
            {"name": "a", "type": "array", "required": True, "description": "数组A"},
            {"name": "b", "type": "array", "required": True, "description": "数组B"}
        ],
        "icon": "git-intersect"
    },
    "array_difference": {
        "id": "array_difference",
        "name": "数组差集",
        "name_en": "Array Difference",
        "description": "获取数组差集",
        "category": "array",
        "subcategory": "set",
        "api_endpoint": "/api/array-difference",
        "method": "POST",
        "params": [
            {"name": "a", "type": "array", "required": True, "description": "数组A"},
            {"name": "b", "type": "array", "required": True, "description": "数组B"}
        ],
        "icon": "git-merge"
    },

    # ========== 函数式编程工具 ==========
    "compose": {
        "id": "compose",
        "name": "组合函数",
        "name_en": "Compose Functions",
        "description": "组合多个函数",
        "category": "function",
        "subcategory": "compose",
        "api_endpoint": "/api/compose",
        "method": "POST",
        "params": [
            {"name": "fns", "type": "array", "required": True, "description": "函数数组"}
        ],
        "icon": "link"
    },
    "pipe": {
        "id": "pipe",
        "name": "管道函数",
        "name_en": "Pipe Functions",
        "description": "将值通过管道传递给函数",
        "category": "function",
        "subcategory": "pipe",
        "api_endpoint": "/api/pipe",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "初始值"},
            {"name": "fns", "type": "array", "required": True, "description": "函数数组"}
        ],
        "icon": "arrow-right"
    },
    "curry": {
        "id": "curry",
        "name": "柯里化",
        "name_en": "Curry",
        "description": "函数柯里化",
        "category": "function",
        "subcategory": "transform",
        "api_endpoint": "/api/curry",
        "method": "POST",
        "params": [
            {"name": "fn", "type": "string", "required": True, "description": "函数"},
            {"name": "arity", "type": "number", "required": True, "description": "参数数量"}
        ],
        "icon": "corner-down-right"
    },
    "partial": {
        "id": "partial",
        "name": "偏函数",
        "name_en": "Partial",
        "description": "创建偏函数",
        "category": "function",
        "subcategory": "transform",
        "api_endpoint": "/api/partial",
        "method": "POST",
        "params": [
            {"name": "fn", "type": "string", "required": True, "description": "函数"},
            {"name": "args", "type": "array", "required": True, "description": "预设参数"}
        ],
        "icon": "git-branch"
    },
    "memoize": {
        "id": "memoize",
        "name": "记忆化",
        "name_en": "Memoize",
        "description": "缓存函数结果",
        "category": "function",
        "subcategory": "cache",
        "api_endpoint": "/api/memoize",
        "method": "POST",
        "params": [
            {"name": "fn", "type": "string", "required": True, "description": "函数"},
            {"name": "args", "type": "array", "required": True, "description": "参数"}
        ],
        "icon": "database"
    },
    "once": {
        "id": "once",
        "name": "单次执行",
        "name_en": "Once",
        "description": "确保函数只执行一次",
        "category": "function",
        "subcategory": "control",
        "api_endpoint": "/api/once",
        "method": "POST",
        "params": [
            {"name": "fn", "type": "string", "required": True, "description": "函数"}
        ],
        "icon": "lock"
    },
    "after": {
        "id": "after",
        "name": "之后执行",
        "name_en": "After",
        "description": "函数在N次调用后执行",
        "category": "function",
        "subcategory": "control",
        "api_endpoint": "/api/after",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "调用次数"},
            {"name": "fn", "type": "string", "required": True, "description": "函数"}
        ],
        "icon": "clock"
    },
    "before": {
        "id": "before",
        "name": "之前执行",
        "name_en": "Before",
        "description": "函数在N次调用前执行",
        "category": "function",
        "subcategory": "control",
        "api_endpoint": "/api/before",
        "method": "POST",
        "params": [
            {"name": "n", "type": "number", "required": True, "description": "调用次数"},
            {"name": "fn", "type": "string", "required": True, "description": "函数"}
        ],
        "icon": "clock"
    },
    "flip": {
        "id": "flip",
        "name": "翻转参数",
        "name_en": "Flip",
        "description": "翻转函数参数顺序",
        "category": "function",
        "subcategory": "transform",
        "api_endpoint": "/api/flip",
        "method": "POST",
        "params": [
            {"name": "fn", "type": "string", "required": True, "description": "函数"}
        ],
        "icon": "repeat"
    },
    "unary": {
        "id": "unary",
        "name": "一元化",
        "name_en": "Unary",
        "description": "将多参数函数转为一元",
        "category": "function",
        "subcategory": "transform",
        "api_endpoint": "/api/unary",
        "method": "POST",
        "params": [
            {"name": "fn", "type": "string", "required": True, "description": "函数"}
        ],
        "icon": "arrow-right"
    },
    "binary": {
        "id": "binary",
        "name": "二元化",
        "name_en": "Binary",
        "description": "将多参数函数转为二元",
        "category": "function",
        "subcategory": "transform",
        "api_endpoint": "/api/binary",
        "method": "POST",
        "params": [
            {"name": "fn", "type": "string", "required": True, "description": "函数"}
        ],
        "icon": "arrow-right"
    },
    "throttle": {
        "id": "throttle",
        "name": "节流",
        "name_en": "Throttle",
        "description": "节流函数调用",
        "category": "function",
        "subcategory": "timing",
        "api_endpoint": "/api/throttle",
        "method": "POST",
        "params": [
            {"name": "fn", "type": "string", "required": True, "description": "函数"},
            {"name": "wait", "type": "number", "required": True, "description": "等待毫秒"}
        ],
        "icon": "clock"
    },
    "debounce": {
        "id": "debounce",
        "name": "防抖",
        "name_en": "Debounce",
        "description": "防抖函数调用",
        "category": "function",
        "subcategory": "timing",
        "api_endpoint": "/api/debounce",
        "method": "POST",
        "params": [
            {"name": "fn", "type": "string", "required": True, "description": "函数"},
            {"name": "wait", "type": "number", "required": True, "description": "等待毫秒"}
        ],
        "icon": "clock"
    },
    "wrap": {
        "id": "wrap",
        "name": "包装函数",
        "name_en": "Wrap",
        "description": "包装函数",
        "category": "function",
        "subcategory": "transform",
        "api_endpoint": "/api/wrap",
        "method": "POST",
        "params": [
            {"name": "fn", "type": "string", "required": True, "description": "函数"},
            {"name": "wrapper", "type": "string", "required": True, "description": "包装函数"}
        ],
        "icon": "package"
    },
    "negate": {
        "id": "negate",
        "name": "求反",
        "name_en": "Negate",
        "description": "返回函数的否定",
        "category": "function",
        "subcategory": "transform",
        "api_endpoint": "/api/negate",
        "method": "POST",
        "params": [
            {"name": "fn", "type": "string", "required": True, "description": "函数"}
        ],
        "icon": "minus"
    },

    # ========== 条件判断工具 ==========
    "is_empty": {
        "id": "is_empty",
        "name": "为空检查",
        "name_en": "Is Empty",
        "description": "检查是否为空",
        "category": "predicate",
        "subcategory": "check",
        "api_endpoint": "/api/is-empty",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "值"}
        ],
        "icon": "minus"
    },
    "is_nil": {
        "id": "is_nil",
        "name": "nil检查",
        "name_en": "Is Nil",
        "description": "检查是否为nil",
        "category": "predicate",
        "subcategory": "check",
        "api_endpoint": "/api/is-nil",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "值"}
        ],
        "icon": "minus"
    },
    "is_undefined": {
        "id": "is_undefined",
        "name": "未定义检查",
        "name_en": "Is Undefined",
        "description": "检查是否未定义",
        "category": "predicate",
        "subcategory": "check",
        "api_endpoint": "/api/is-undefined",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "值"}
        ],
        "icon": "help-circle"
    },
    "is_null": {
        "id": "is_null",
        "name": "null检查",
        "name_en": "Is Null",
        "description": "检查是否为null",
        "category": "predicate",
        "subcategory": "check",
        "api_endpoint": "/api/is-null",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "值"}
        ],
        "icon": "minus"
    },
    "is_string": {
        "id": "is_string",
        "name": "字符串检查",
        "name_en": "Is String",
        "description": "检查是否为字符串",
        "category": "predicate",
        "subcategory": "type",
        "api_endpoint": "/api/is-string",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "值"}
        ],
        "icon": "type"
    },
    "is_number": {
        "id": "is_number",
        "name": "数字检查",
        "name_en": "Is Number",
        "description": "检查是否为数字",
        "category": "predicate",
        "subcategory": "type",
        "api_endpoint": "/api/is-number",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "值"}
        ],
        "icon": "hash"
    },
    "is_boolean": {
        "id": "is_boolean",
        "name": "布尔检查",
        "name_en": "Is Boolean",
        "description": "检查是否为布尔值",
        "category": "predicate",
        "subcategory": "type",
        "api_endpoint": "/api/is-boolean",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "值"}
        ],
        "icon": "check-square"
    },
    "is_array": {
        "id": "is_array",
        "name": "数组检查",
        "name_en": "Is Array",
        "description": "检查是否为数组",
        "category": "predicate",
        "subcategory": "type",
        "api_endpoint": "/api/is-array",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "值"}
        ],
        "icon": "list"
    },
    "is_object": {
        "id": "is_object",
        "name": "对象检查",
        "name_en": "Is Object",
        "description": "检查是否为对象",
        "category": "predicate",
        "subcategory": "type",
        "api_endpoint": "/api/is-object",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "值"}
        ],
        "icon": "square"
    },
    "is_function": {
        "id": "is_function",
        "name": "函数检查",
        "name_en": "Is Function",
        "description": "检查是否为函数",
        "category": "predicate",
        "subcategory": "type",
        "api_endpoint": "/api/is-function",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "值"}
        ],
        "icon": "code"
    },
    "is_date": {
        "id": "is_date",
        "name": "日期检查",
        "name_en": "Is Date",
        "description": "检查是否为日期",
        "category": "predicate",
        "subcategory": "type",
        "api_endpoint": "/api/is-date",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "值"}
        ],
        "icon": "calendar"
    },
    "is_symbol": {
        "id": "is_symbol",
        "name": "Symbol检查",
        "name_en": "Is Symbol",
        "description": "检查是否为Symbol",
        "category": "predicate",
        "subcategory": "type",
        "api_endpoint": "/api/is-symbol",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "值"}
        ],
        "icon": "hash"
    },
    "is_promise": {
        "id": "is_promise",
        "name": "Promise检查",
        "name_en": "Is Promise",
        "description": "检查是否为Promise",
        "category": "predicate",
        "subcategory": "type",
        "api_endpoint": "/api/is-promise",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "值"}
        ],
        "icon": "clock"
    },
    "is_iterable": {
        "id": "is_iterable",
        "name": "可迭代检查",
        "name_en": "Is Iterable",
        "description": "检查是否可迭代",
        "category": "predicate",
        "subcategory": "type",
        "api_endpoint": "/api/is-iterable",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "值"}
        ],
        "icon": "list"
    },
    "is_array_like": {
        "id": "is_array_like",
        "name": "类数组检查",
        "name_en": "Is Array Like",
        "description": "检查是否类数组",
        "category": "predicate",
        "subcategory": "type",
        "api_endpoint": "/api/is-array-like",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "值"}
        ],
        "icon": "list"
    },

    # ========== 实用工具 ==========
    "noop": {
        "id": "noop",
        "name": "空操作",
        "name_en": "Noop",
        "description": "空操作函数",
        "category": "utility",
        "subcategory": "basic",
        "api_endpoint": "/api/noop",
        "method": "POST",
        "params": [],
        "icon": "minus"
    },
    "identity": {
        "id": "identity",
        "name": "恒等函数",
        "name_en": "Identity",
        "description": "返回输入值本身",
        "category": "utility",
        "subcategory": "basic",
        "api_endpoint": "identity",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "任意值"}
        ],
        "icon": "equal"
    },
    "always": {
        "id": "always",
        "name": "总是返回",
        "name_en": "Always",
        "description": "总是返回指定值",
        "category": "utility",
        "subcategory": "function",
        "api_endpoint": "/api/always",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "返回值"}
        ],
        "icon": "check"
    },
    "never": {
        "id": "never",
        "name": "从不返回",
        "name_en": "Never",
        "description": "从不返回",
        "category": "utility",
        "subcategory": "function",
        "api_endpoint": "/api/never",
        "method": "POST",
        "params": [],
        "icon": "x"
    },
    "default_to": {
        "id": "default_to",
        "name": "默认值",
        "name_en": "Default To",
        "description": "为空值设置默认值",
        "category": "utility",
        "subcategory": "value",
        "api_endpoint": "/api/default-to",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "值"},
            {"name": "default", "type": "any", "required": True, "description": "默认值"}
        ],
        "icon": "plus"
    },
    "coalesce": {
        "id": "coalesce",
        "name": "空值合并",
        "name_en": "Coalesce",
        "description": "返回第一个非空值",
        "category": "utility",
        "subcategory": "value",
        "api_endpoint": "/api/coalesce",
        "method": "POST",
        "params": [
            {"name": "values", "type": "array", "required": True, "description": "值数组"}
        ],
        "icon": "git-merge"
    },
    "tap": {
        "id": "tap",
        "name": "点击",
        "name_en": "Tap",
        "description": "执行函数并返回值",
        "category": "utility",
        "subcategory": "function",
        "api_endpoint": "/api/tap",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "值"},
            {"name": "fn", "type": "string", "required": True, "description": "函数"}
        ],
        "icon": "pointer"
    },
    " juxt": {
        "id": "juxt",
        "name": "并列函数",
        "name_en": "Juxtapose",
        "description": "应用多个函数返回数组",
        "category": "utility",
        "subcategory": "function",
        "api_endpoint": "/api/juxt",
        "method": "POST",
        "params": [
            {"name": "fns", "type": "array", "required": True, "description": "函数数组"},
            {"name": "value", "type": "any", "required": True, "description": "值"}
        ],
        "icon": "columns"
    },
    "converge": {
        "id": "converge",
        "name": "收敛函数",
        "name_en": "Converge",
        "description": "收敛函数结果",
        "category": "utility",
        "subcategory": "function",
        "api_endpoint": "/api/converge",
        "method": "POST",
        "params": [
            {"name": "fns", "type": "array", "required": True, "description": "函数数组"},
            {"name": "fn", "type": "string", "required": True, "description": "最终函数"}
        ],
        "icon": "git-merge"
    },
    "apply": {
        "id": "apply",
        "name": "应用函数",
        "name_en": "Apply",
        "description": "将数组展开为函数参数",
        "category": "utility",
        "subcategory": "function",
        "api_endpoint": "/api/apply",
        "method": "POST",
        "params": [
            {"name": "fn", "type": "string", "required": True, "description": "函数"},
            {"name": "args", "type": "array", "required": True, "description": "参数数组"}
        ],
        "icon": "arrow-right"
    },
    "spread": {
        "id": "spread",
        "name": "展开",
        "name_en": "Spread",
        "description": "展开数组为多个参数",
        "category": "utility",
        "subcategory": "function",
        "api_endpoint": "/api/spread",
        "method": "POST",
        "params": [
            {"name": "fn", "type": "string", "required": True, "description": "函数"},
            {"name": "args", "type": "array", "required": True, "description": "参数数组"}
        ],
        "icon": "maximize"
    },
    "flip": {
        "id": "flip",
        "name": "翻转",
        "name_en": "Flip",
        "description": "翻转函数参数顺序",
        "category": "utility",
        "subcategory": "function",
        "api_endpoint": "/api/flip",
        "method": "POST",
        "params": [
            {"name": "fn", "type": "string", "required": True, "description": "函数"}
        ],
        "icon": "repeat"
    },

    # ========== 字符串工具 ==========
    "camel_case": {
        "id": "camel_case",
        "name": "驼峰命名",
        "name_en": "Camel Case",
        "description": "转驼峰命名",
        "category": "string",
        "subcategory": "case",
        "api_endpoint": "/api/camel-case",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "arrow-up"
    },
    "snake_case": {
        "id": "snake_case",
        "name": "蛇形命名",
        "name_en": "Snake Case",
        "description": "转蛇形命名",
        "category": "string",
        "subcategory": "case",
        "api_endpoint": "/api/snake-case",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "minus"
    },
    "pascal_case": {
        "id": "pascal_case",
        "name": "帕斯卡命名",
        "name_en": "Pascal Case",
        "description": "转帕斯卡命名",
        "category": "string",
        "subcategory": "case",
        "api_endpoint": "/api/pascal-case",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "arrow-up-circle"
    },
    "kebab_case": {
        "id": "kebab_case",
        "name": "串形命名",
        "name_en": "Kebab Case",
        "description": "转串形命名",
        "category": "string",
        "subcategory": "case",
        "api_endpoint": "/api/kebab-case",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "minus"
    },
    "capitalize": {
        "id": "capitalize",
        "name": "首字母大写",
        "name_en": "Capitalize",
        "description": "首字母大写",
        "category": "string",
        "subcategory": "case",
        "api_endpoint": "/api/capitalize",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "type"
    },
    "upper_first": {
        "id": "upper_first",
        "name": "首字母大写",
        "name_en": "Upper First",
        "description": "首字母大写其余小写",
        "category": "string",
        "subcategory": "case",
        "api_endpoint": "/api/upper-first",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "type"
    },
    "lower_first": {
        "id": "lower_first",
        "name": "首字母小写",
        "name_en": "Lower First",
        "description": "首字母小写",
        "category": "string",
        "subcategory": "case",
        "api_endpoint": "/api/lower-first",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "type"
    },
    "swap_case": {
        "id": "swap_case",
        "name": "大小写互换",
        "name_en": "Swap Case",
        "description": "大小写互换",
        "category": "string",
        "subcategory": "case",
        "api_endpoint": "/api/swap-case",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "arrow-up-down"
    },
    "reverse_string": {
        "id": "reverse_string",
        "name": "反转字符串",
        "name_en": "Reverse String",
        "description": "反转字符串",
        "category": "string",
        "subcategory": "transform",
        "api_endpoint": "/api/reverse-string",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "rotate-ccw"
    },
    "truncate_string": {
        "id": "truncate_string",
        "name": "截断字符串",
        "name_en": "Truncate String",
        "description": "截断字符串",
        "category": "string",
        "subcategory": "transform",
        "api_endpoint": "/api/truncate-string",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "length", "type": "number", "required": True, "description": "长度"},
            {"name": "suffix", "type": "string", "required": False, "description": "后缀"}
        ],
        "icon": "scissors"
    },
    "pad": {
        "id": "pad",
        "name": "填充",
        "name_en": "Pad",
        "description": "填充字符串",
        "category": "string",
        "subcategory": "transform",
        "api_endpoint": "/api/pad",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "length", "type": "number", "required": True, "description": "长度"},
            {"name": "char", "type": "string", "required": False, "description": "填充字符"}
        ],
        "icon": "plus"
    },
    "words": {
        "id": "words",
        "name": "分词",
        "name_en": "Words",
        "description": "将字符串拆分为单词数组",
        "category": "string",
        "subcategory": "transform",
        "api_endpoint": "/api/words",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "list"
    },
    "unwords": {
        "id": "unwords",
        "name": "合并词",
        "name_en": "Unwords",
        "description": "将单词数组合并为字符串",
        "category": "string",
        "subcategory": "transform",
        "api_endpoint": "/api/unwords",
        "method": "POST",
        "params": [
            {"name": "words", "type": "array", "required": True, "description": "单词数组"}
        ],
        "icon": "link"
    },
    "lines": {
        "id": "lines",
        "name": "分行",
        "name_en": "Lines",
        "description": "将字符串拆分为行数组",
        "category": "string",
        "subcategory": "transform",
        "api_endpoint": "/api/lines",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "list"
    },
    "unlines": {
        "id": "unlines",
        "name": "合并行",
        "name_en": "Unlines",
        "description": "将行数组合并为字符串",
        "category": "string",
        "subcategory": "transform",
        "api_endpoint": "/api/unlines",
        "method": "POST",
        "params": [
            {"name": "lines", "type": "array", "required": True, "description": "行数组"}
        ],
        "icon": "link"
    },

    # ========== 格式化工具 ==========
    "format_template": {
        "id": "format_template",
        "name": "模板格式化",
        "name_en": "Template Formatter",
        "description": "使用模板格式化字符串",
        "category": "string",
        "subcategory": "format",
        "api_endpoint": "/api/format_template",
        "method": "POST",
        "params": [
            {"name": "template", "type": "string", "required": True, "description": "模板字符串"},
            {"name": "values", "type": "object", "required": True, "description": "填充值"}
        ],
        "icon": "file-text"
    },
    "indent": {
        "id": "indent",
        "name": "缩进",
        "name_en": "Indent",
        "description": "为每行添加缩进",
        "category": "string",
        "subcategory": "format",
        "api_endpoint": "/api/indent",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "spaces", "type": "number", "required": False, "description": "缩进空格数", "default": 2}
        ],
        "icon": "align-left"
    },
    "dedent": {
        "id": "dedent",
        "name": "去除缩进",
        "name_en": "Dedent",
        "description": "去除每行的公共缩进",
        "category": "string",
        "subcategory": "format",
        "api_endpoint": "/api/dedent",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "align-left"
    },
    "wrap_text": {
        "id": "wrap_text",
        "name": "文本包裹",
        "name_en": "Wrap Text",
        "description": "将长文本按指定宽度换行",
        "category": "string",
        "subcategory": "format",
        "api_endpoint": "/api/wrap_text",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "width", "type": "number", "required": False, "description": "行宽度", "default": 80}
        ],
        "icon": "wrap-text"
    },
    "center": {
        "id": "center",
        "name": "居中对齐",
        "name_en": "Center",
        "description": "将文本居中对齐",
        "category": "string",
        "subcategory": "format",
        "api_endpoint": "/api/center",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "width", "type": "number", "required": False, "description": "总宽度", "default": 80}
        ],
        "icon": "align-center"
    },
    "ljust": {
        "id": "ljust",
        "name": "左对齐",
        "name_en": "Left Justify",
        "description": "将文本左对齐到指定宽度",
        "category": "string",
        "subcategory": "format",
        "api_endpoint": "/api/ljust",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "width", "type": "number", "required": False, "description": "总宽度", "default": 80}
        ],
        "icon": "align-left"
    },
    "rjust": {
        "id": "rjust",
        "name": "右对齐",
        "name_en": "Right Justify",
        "description": "将文本右对齐到指定宽度",
        "category": "string",
        "subcategory": "format",
        "api_endpoint": "/api/rjust",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "width", "type": "number", "required": False, "description": "总宽度", "default": 80}
        ],
        "icon": "align-right"
    },

    # ========== UUID工具 ==========
    "uuid_v1": {
        "id": "uuid_v1",
        "name": "UUID v1",
        "name_en": "UUID v1",
        "description": "生成基于时间的UUID",
        "category": "uuid",
        "subcategory": "generate",
        "api_endpoint": "/api/uuid_v1",
        "method": "POST",
        "params": [],
        "icon": "hash"
    },
    "uuid_v4": {
        "id": "uuid_v4",
        "name": "UUID v4",
        "name_en": "UUID v4",
        "description": "生成随机UUID",
        "category": "uuid",
        "subcategory": "generate",
        "api_endpoint": "/api/uuid_v4",
        "method": "POST",
        "params": [],
        "icon": "hash"
    },
    "uuid_validate": {
        "id": "uuid_validate",
        "name": "UUID验证",
        "name_en": "UUID Validate",
        "description": "验证UUID格式是否有效",
        "category": "uuid",
        "subcategory": "validate",
        "api_endpoint": "/api/uuid_validate",
        "method": "POST",
        "params": [
            {"name": "uuid", "type": "string", "required": True, "description": "UUID字符串"}
        ],
        "icon": "check"
    },
    "uuid_version": {
        "id": "uuid_version",
        "name": "UUID版本",
        "name_en": "UUID Version",
        "description": "获取UUID的版本号",
        "category": "uuid",
        "subcategory": "info",
        "api_endpoint": "/api/uuid_version",
        "method": "POST",
        "params": [
            {"name": "uuid", "type": "string", "required": True, "description": "UUID字符串"}
        ],
        "icon": "info"
    },

    # ========== NanoID工具 ==========
    "nanoid": {
        "id": "nanoid",
        "name": "NanoID生成",
        "name_en": "NanoID Generator",
        "description": "生成小型唯一的ID字符串",
        "category": "uuid",
        "subcategory": "generate",
        "api_endpoint": "/api/nanoid",
        "method": "POST",
        "params": [
            {"name": "size", "type": "number", "required": False, "description": "ID长度", "default": 21}
        ],
        "icon": "hash"
    },
    "nanoid_alphabet": {
        "id": "nanoid_alphabet",
        "name": "自定义NanoID",
        "name_en": "NanoID Custom",
        "description": "使用自定义字母表生成NanoID",
        "category": "uuid",
        "subcategory": "generate",
        "api_endpoint": "/api/nanoid_alphabet",
        "method": "POST",
        "params": [
            {"name": "alphabet", "type": "string", "required": True, "description": "字符集"},
            {"name": "size", "type": "number", "required": False, "description": "ID长度", "default": 21}
        ],
        "icon": "hash"
    },

    # ========== 哈希工具 ==========
    "hash_md5": {
        "id": "hash_md5",
        "name": "MD5哈希",
        "name_en": "MD5 Hash",
        "description": "计算字符串的MD5哈希值",
        "category": "crypto",
        "subcategory": "hash",
        "api_endpoint": "/api/hash_md5",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "lock"
    },
    "hash_sha1": {
        "id": "hash_sha1",
        "name": "SHA1哈希",
        "name_en": "SHA1 Hash",
        "description": "计算字符串的SHA1哈希值",
        "category": "crypto",
        "subcategory": "hash",
        "api_endpoint": "/api/hash_sha1",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "lock"
    },
    "hash_sha256": {
        "id": "hash_sha256",
        "name": "SHA256哈希",
        "name_en": "SHA256 Hash",
        "description": "计算字符串的SHA256哈希值",
        "category": "crypto",
        "subcategory": "hash",
        "api_endpoint": "/api/hash_sha256",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "lock"
    },
    "hash_bcrypt": {
        "id": "hash_bcrypt",
        "name": "Bcrypt哈希",
        "name_en": "Bcrypt Hash",
        "description": "使用Bcrypt算法哈希密码",
        "category": "crypto",
        "subcategory": "hash",
        "api_endpoint": "/api/hash_bcrypt",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "密码"}
        ],
        "icon": "lock"
    },
    "verify_bcrypt": {
        "id": "verify_bcrypt",
        "name": "Bcrypt验证",
        "name_en": "Bcrypt Verify",
        "description": "验证密码与Bcrypt哈希是否匹配",
        "category": "crypto",
        "subcategory": "verify",
        "api_endpoint": "/api/verify_bcrypt",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "密码"},
            {"name": "hash", "type": "string", "required": True, "description": "哈希值"}
        ],
        "icon": "check"
    },
    "generate_token": {
        "id": "generate_token",
        "name": "生成令牌",
        "name_en": "Generate Token",
        "description": "生成随机令牌",
        "category": "crypto",
        "subcategory": "generate",
        "api_endpoint": "/api/generate_token",
        "method": "POST",
        "params": [
            {"name": "length", "type": "number", "required": False, "description": "令牌长度", "default": 32}
        ],
        "icon": "key"
    },

    # ========== HMAC工具 ==========
    "hmac_md5": {
        "id": "hmac_md5",
        "name": "HMAC-MD5",
        "name_en": "HMAC-MD5",
        "description": "生成HMAC-MD5认证码",
        "category": "crypto",
        "subcategory": "hmac",
        "api_endpoint": "/api/hmac_md5",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "消息"},
            {"name": "key", "type": "string", "required": True, "description": "密钥"}
        ],
        "icon": "key"
    },
    "hmac_sha256": {
        "id": "hmac_sha256",
        "name": "HMAC-SHA256",
        "name_en": "HMAC-SHA256",
        "description": "生成HMAC-SHA256认证码",
        "category": "crypto",
        "subcategory": "hmac",
        "api_endpoint": "/api/hmac_sha256",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "消息"},
            {"name": "key", "type": "string", "required": True, "description": "密钥"}
        ],
        "icon": "key"
    },

    # ========== 加密解密工具 ==========
    "aes_encrypt": {
        "id": "aes_encrypt",
        "name": "AES加密",
        "name_en": "AES Encrypt",
        "description": "使用AES算法加密数据",
        "category": "crypto",
        "subcategory": "encrypt",
        "api_endpoint": "/api/aes_encrypt",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "明文"},
            {"name": "key", "type": "string", "required": True, "description": "密钥"}
        ],
        "icon": "lock"
    },
    "aes_decrypt": {
        "id": "aes_decrypt",
        "name": "AES解密",
        "name_en": "AES Decrypt",
        "description": "使用AES算法解密数据",
        "category": "crypto",
        "subcategory": "decrypt",
        "api_endpoint": "/api/aes_decrypt",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "密文"},
            {"name": "key", "type": "string", "required": True, "description": "密钥"}
        ],
        "icon": "unlock"
    },
    "rsa_generate": {
        "id": "rsa_generate",
        "name": "RSA密钥生成",
        "name_en": "RSA Key Generator",
        "description": "生成RSA公钥私钥对",
        "category": "crypto",
        "subcategory": "rsa",
        "api_endpoint": "/api/rsa_generate",
        "method": "POST",
        "params": [
            {"name": "bits", "type": "number", "required": False, "description": "密钥位数", "default": 2048}
        ],
        "icon": "key"
    },
    "rsa_encrypt": {
        "id": "rsa_encrypt",
        "name": "RSA加密",
        "name_en": "RSA Encrypt",
        "description": "使用RSA公钥加密数据",
        "category": "crypto",
        "subcategory": "encrypt",
        "api_endpoint": "/api/rsa_encrypt",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "明文"},
            {"name": "public_key", "type": "string", "required": True, "description": "公钥"}
        ],
        "icon": "lock"
    },
    "rsa_decrypt": {
        "id": "rsa_decrypt",
        "name": "RSA解密",
        "name_en": "RSA Decrypt",
        "description": "使用RSA私钥解密数据",
        "category": "crypto",
        "subcategory": "decrypt",
        "api_endpoint": "/api/rsa_decrypt",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "密文"},
            {"name": "private_key", "type": "string", "required": True, "description": "私钥"}
        ],
        "icon": "unlock"
    },
    "xor_encrypt": {
        "id": "xor_encrypt",
        "name": "XOR加密",
        "name_en": "XOR Encrypt",
        "description": "使用XOR算法加密数据",
        "category": "crypto",
        "subcategory": "encrypt",
        "api_endpoint": "/api/xor_encrypt",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "明文"},
            {"name": "key", "type": "string", "required": True, "description": "密钥"}
        ],
        "icon": "lock"
    },
    "xor_decrypt": {
        "id": "xor_decrypt",
        "name": "XOR解密",
        "name_en": "XOR Decrypt",
        "description": "使用XOR算法解密数据",
        "category": "crypto",
        "subcategory": "decrypt",
        "api_endpoint": "/api/xor_decrypt",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "密文"},
            {"name": "key", "type": "string", "required": True, "description": "密钥"}
        ],
        "icon": "unlock"
    },
    "rot13": {
        "id": "rot13",
        "name": "ROT13加密",
        "name_en": "ROT13 Cipher",
        "description": "使用ROT13算法加密解密",
        "category": "crypto",
        "subcategory": "cipher",
        "api_endpoint": "/api/rot13",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "lock"
    },
    "caesar_cipher": {
        "id": "caesar_cipher",
        "name": "凯撒密码",
        "name_en": "Caesar Cipher",
        "description": "使用凯撒密码加密文本",
        "category": "crypto",
        "subcategory": "cipher",
        "api_endpoint": "/api/caesar_cipher",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "shift", "type": "number", "required": False, "description": "偏移量", "default": 3}
        ],
        "icon": "lock"
    },

    # ========== 时间工具 ==========
    "now": {
        "id": "now",
        "name": "当前时刻",
        "name_en": "Now",
        "description": "获取当前日期时间",
        "category": "datetime",
        "subcategory": "current",
        "api_endpoint": "/api/now",
        "method": "POST",
        "params": [],
        "icon": "clock"
    },
    "today": {
        "id": "today",
        "name": "今日日期",
        "name_en": "Today",
        "description": "获取今天的日期",
        "category": "datetime",
        "subcategory": "current",
        "api_endpoint": "/api/today",
        "method": "POST",
        "params": [],
        "icon": "calendar"
    },
    "timestamp": {
        "id": "timestamp",
        "name": "时间戳",
        "name_en": "Timestamp",
        "description": "获取当前Unix时间戳",
        "category": "datetime",
        "subcategory": "current",
        "api_endpoint": "/api/timestamp",
        "method": "POST",
        "params": [],
        "icon": "clock"
    },
    "format_time": {
        "id": "format_time",
        "name": "格式化时间",
        "name_en": "Format Time",
        "description": "格式化时间字符串",
        "category": "datetime",
        "subcategory": "format",
        "api_endpoint": "/api/format_time",
        "method": "POST",
        "params": [
            {"name": "time", "type": "string", "required": True, "description": "时间字符串"},
            {"name": "format", "type": "string", "required": False, "description": "格式", "default": "%Y-%m-%d %H:%M:%S"}
        ],
        "icon": "clock"
    },
    "parse_date": {
        "id": "parse_date",
        "name": "解析日期",
        "name_en": "Parse Date",
        "description": "解析日期字符串为日期对象",
        "category": "datetime",
        "subcategory": "parse",
        "api_endpoint": "/api/parse_date",
        "method": "POST",
        "params": [
            {"name": "date_string", "type": "string", "required": True, "description": "日期字符串"}
        ],
        "icon": "calendar"
    },
    "add_days": {
        "id": "add_days",
        "name": "加天数",
        "name_en": "Add Days",
        "description": "给日期加指定天数",
        "category": "datetime",
        "subcategory": "arithmetic",
        "api_endpoint": "/api/add_days",
        "method": "POST",
        "params": [
            {"name": "date", "type": "string", "required": True, "description": "日期"},
            {"name": "days", "type": "number", "required": True, "description": "天数"}
        ],
        "icon": "plus"
    },
    "subtract_days": {
        "id": "subtract_days",
        "name": "减天数",
        "name_en": "Subtract Days",
        "description": "给日期减指定天数",
        "category": "datetime",
        "subcategory": "arithmetic",
        "api_endpoint": "/api/subtract_days",
        "method": "POST",
        "params": [
            {"name": "date", "type": "string", "required": True, "description": "日期"},
            {"name": "days", "type": "number", "required": True, "description": "天数"}
        ],
        "icon": "minus"
    },
    "days_between": {
        "id": "days_between",
        "name": "天数差",
        "name_en": "Days Between",
        "description": "计算两个日期之间的天数",
        "category": "datetime",
        "subcategory": "arithmetic",
        "api_endpoint": "/api/days_between",
        "method": "POST",
        "params": [
            {"name": "start_date", "type": "string", "required": True, "description": "开始日期"},
            {"name": "end_date", "type": "string", "required": True, "description": "结束日期"}
        ],
        "icon": "calendar"
    },
    "start_of_day": {
        "id": "start_of_day",
        "name": "日开始",
        "name_en": "Start of Day",
        "description": "获取一天的开始时间",
        "category": "datetime",
        "subcategory": "truncate",
        "api_endpoint": "/api/start_of_day",
        "method": "POST",
        "params": [
            {"name": "date", "type": "string", "required": True, "description": "日期"}
        ],
        "icon": "sunrise"
    },
    "end_of_day": {
        "id": "end_of_day",
        "name": "日结束",
        "name_en": "End of Day",
        "description": "获取一天的结束时间",
        "category": "datetime",
        "subcategory": "truncate",
        "api_endpoint": "/api/end_of_day",
        "method": "POST",
        "params": [
            {"name": "date", "type": "string", "required": True, "description": "日期"}
        ],
        "icon": "sunset"
    },
    "start_of_week": {
        "id": "start_of_week",
        "name": "周开始",
        "name_en": "Start of Week",
        "description": "获取一周的开始日期",
        "category": "datetime",
        "subcategory": "truncate",
        "api_endpoint": "/api/start_of_week",
        "method": "POST",
        "params": [
            {"name": "date", "type": "string", "required": True, "description": "日期"}
        ],
        "icon": "calendar"
    },
    "start_of_month": {
        "id": "start_of_month",
        "name": "月开始",
        "name_en": "Start of Month",
        "description": "获取一月的开始日期",
        "category": "datetime",
        "subcategory": "truncate",
        "api_endpoint": "/api/start_of_month",
        "method": "POST",
        "params": [
            {"name": "date", "type": "string", "required": True, "description": "日期"}
        ],
        "icon": "calendar"
    },
    "end_of_month": {
        "id": "end_of_month",
        "name": "月结束",
        "name_en": "End of Month",
        "description": "获取一月的结束日期",
        "category": "datetime",
        "subcategory": "truncate",
        "api_endpoint": "/api/end_of_month",
        "method": "POST",
        "params": [
            {"name": "date", "type": "string", "required": True, "description": "日期"}
        ],
        "icon": "calendar"
    },
    "quarter_of_year": {
        "id": "quarter_of_year",
        "name": "年度季度",
        "name_en": "Quarter of Year",
        "description": "获取日期所在的季度",
        "category": "datetime",
        "subcategory": "info",
        "api_endpoint": "/api/quarter_of_year",
        "method": "POST",
        "params": [
            {"name": "date", "type": "string", "required": True, "description": "日期"}
        ],
        "icon": "calendar"
    },
    "week_of_year": {
        "id": "week_of_year",
        "name": "年周数",
        "name_en": "Week of Year",
        "description": "获取日期所在的周数",
        "category": "datetime",
        "subcategory": "info",
        "api_endpoint": "/api/week_of_year",
        "method": "POST",
        "params": [
            {"name": "date", "type": "string", "required": True, "description": "日期"}
        ],
        "icon": "calendar"
    },
    "is_weekend": {
        "id": "is_weekend",
        "name": "是否周末",
        "name_en": "Is Weekend",
        "description": "判断是否为周末",
        "category": "datetime",
        "subcategory": "check",
        "api_endpoint": "/api/is_weekend",
        "method": "POST",
        "params": [
            {"name": "date", "type": "string", "required": True, "description": "日期"}
        ],
        "icon": "check"
    },
    "is_weekday": {
        "id": "is_weekday",
        "name": "是否工作日",
        "name_en": "Is Weekday",
        "description": "判断是否为工作日",
        "category": "datetime",
        "subcategory": "check",
        "api_endpoint": "/api/is_weekday",
        "method": "POST",
        "params": [
            {"name": "date", "type": "string", "required": True, "description": "日期"}
        ],
        "icon": "check"
    },
    "days_in_month": {
        "id": "days_in_month",
        "name": "月天数",
        "name_en": "Days in Month",
        "description": "获取某月的天数",
        "category": "datetime",
        "subcategory": "info",
        "api_endpoint": "/api/days_in_month",
        "method": "POST",
        "params": [
            {"name": "year", "type": "number", "required": True, "description": "年份"},
            {"name": "month", "type": "number", "required": True, "description": "月份"}
        ],
        "icon": "calendar"
    },

    # ========== 验证工具 ==========
    "is_valid_email": {
        "id": "is_valid_email",
        "name": "邮箱验证",
        "name_en": "Email Validator",
        "description": "验证邮箱格式是否有效",
        "category": "validate",
        "subcategory": "format",
        "api_endpoint": "/api/is_valid_email",
        "method": "POST",
        "params": [
            {"name": "email", "type": "string", "required": True, "description": "邮箱地址"}
        ],
        "icon": "check"
    },
    "is_valid_url": {
        "id": "is_valid_url",
        "name": "URL验证",
        "name_en": "URL Validator",
        "description": "验证URL格式是否有效",
        "category": "validate",
        "subcategory": "format",
        "api_endpoint": "/api/is_valid_url",
        "method": "POST",
        "params": [
            {"name": "url", "type": "string", "required": True, "description": "URL地址"}
        ],
        "icon": "check"
    },
    "is_valid_phone": {
        "id": "is_valid_phone",
        "name": "电话验证",
        "name_en": "Phone Validator",
        "description": "验证电话号码格式是否有效",
        "category": "validate",
        "subcategory": "format",
        "api_endpoint": "/api/is_valid_phone",
        "method": "POST",
        "params": [
            {"name": "phone", "type": "string", "required": True, "description": "电话号码"}
        ],
        "icon": "check"
    },
    "is_valid_ip": {
        "id": "is_valid_ip",
        "name": "IP地址验证",
        "name_en": "IP Address Validator",
        "description": "验证IP地址格式是否有效",
        "category": "validate",
        "subcategory": "format",
        "api_endpoint": "/api/is_valid_ip",
        "method": "POST",
        "params": [
            {"name": "ip", "type": "string", "required": True, "description": "IP地址"}
        ],
        "icon": "check"
    },
    "is_valid_uuid": {
        "id": "is_valid_uuid",
        "name": "UUID验证",
        "name_en": "UUID Validator",
        "description": "验证UUID格式是否有效",
        "category": "validate",
        "subcategory": "format",
        "api_endpoint": "/api/is_valid_uuid",
        "method": "POST",
        "params": [
            {"name": "uuid", "type": "string", "required": True, "description": "UUID字符串"}
        ],
        "icon": "check"
    },
    "is_valid_json": {
        "id": "is_valid_json",
        "name": "JSON验证",
        "name_en": "JSON Validator",
        "description": "验证JSON格式是否有效",
        "category": "validate",
        "subcategory": "format",
        "api_endpoint": "/api/is_valid_json",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "JSON字符串"}
        ],
        "icon": "check"
    },
    "is_valid_credit_card": {
        "id": "is_valid_credit_card",
        "name": "信用卡验证",
        "name_en": "Credit Card Validator",
        "description": "验证信用卡号是否有效",
        "category": "validate",
        "subcategory": "format",
        "api_endpoint": "/api/is_valid_credit_card",
        "method": "POST",
        "params": [
            {"name": "card_number", "type": "string", "required": True, "description": "卡号"}
        ],
        "icon": "credit-card"
    },
    "validate_range": {
        "id": "validate_range",
        "name": "范围验证",
        "name_en": "Range Validator",
        "description": "验证数值是否在指定范围内",
        "category": "validate",
        "subcategory": "range",
        "api_endpoint": "/api/validate_range",
        "method": "POST",
        "params": [
            {"name": "value", "type": "number", "required": True, "description": "数值"},
            {"name": "min", "type": "number", "required": True, "description": "最小值"},
            {"name": "max", "type": "number", "required": True, "description": "最大值"}
        ],
        "icon": "check"
    },
    "is_alpha": {
        "id": "is_alpha",
        "name": "纯字母验证",
        "name_en": "Is Alpha",
        "description": "验证是否只包含字母",
        "category": "validate",
        "subcategory": "string",
        "api_endpoint": "/api/is_alpha",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "check"
    },
    "is_numeric": {
        "id": "is_numeric",
        "name": "纯数字验证",
        "name_en": "Is Numeric",
        "description": "验证是否只包含数字",
        "category": "validate",
        "subcategory": "string",
        "api_endpoint": "/api/is_numeric",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "check"
    },
    "is_alphanumeric": {
        "id": "is_alphanumeric",
        "name": "字母数字验证",
        "name_en": "Is Alphanumeric",
        "description": "验证是否只包含字母和数字",
        "category": "validate",
        "subcategory": "string",
        "api_endpoint": "/api/is_alphanumeric",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "check"
    },
    "is_blank": {
        "id": "is_blank",
        "name": "空白验证",
        "name_en": "Is Blank",
        "description": "验证是否为空或空白",
        "category": "validate",
        "subcategory": "string",
        "api_endpoint": "/api/is_blank",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "check"
    },

    # ========== 编码解码工具 ==========
    "decode_base64": {
        "id": "decode_base64",
        "name": "Base64解码",
        "name_en": "Base64 Decode",
        "description": "将Base64字符串解码",
        "category": "encoding",
        "subcategory": "decode",
        "api_endpoint": "/api/decode_base64",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "Base64字符串"}
        ],
        "icon": "code"
    },
    "encode_hex": {
        "id": "encode_hex",
        "name": "HEX编码",
        "name_en": "HEX Encode",
        "description": "将字符串编码为HEX",
        "category": "encoding",
        "subcategory": "encode",
        "api_endpoint": "/api/encode_hex",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "code"
    },
    "decode_hex": {
        "id": "decode_hex",
        "name": "HEX解码",
        "name_en": "HEX Decode",
        "description": "将HEX字符串解码",
        "category": "encoding",
        "subcategory": "decode",
        "api_endpoint": "/api/decode_hex",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "HEX字符串"}
        ],
        "icon": "code"
    },
    "decode_url": {
        "id": "decode_url",
        "name": "URL解码",
        "name_en": "URL Decode",
        "description": "将URL编码字符串解码",
        "category": "encoding",
        "subcategory": "decode",
        "api_endpoint": "/api/decode_url",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "URL编码字符串"}
        ],
        "icon": "link"
    },
    "decode_html": {
        "id": "decode_html",
        "name": "HTML解码",
        "name_en": "HTML Decode",
        "description": "将HTML实体解码",
        "category": "encoding",
        "subcategory": "decode",
        "api_endpoint": "/api/decode_html",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "HTML实体字符串"}
        ],
        "icon": "code"
    },
    "strip_tags": {
        "id": "strip_tags",
        "name": "去除HTML标签",
        "name_en": "Strip HTML Tags",
        "description": "去除字符串中的HTML标签",
        "category": "encoding",
        "subcategory": "strip",
        "api_endpoint": "/api/strip_tags",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "HTML文本"}
        ],
        "icon": "code"
    },
    "escape_json": {
        "id": "escape_json",
        "name": "JSON转义",
        "name_en": "Escape JSON",
        "description": "转义JSON特殊字符",
        "category": "encoding",
        "subcategory": "escape",
        "api_endpoint": "/api/escape_json",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "code"
    },
    "unescape_json": {
        "id": "unescape_json",
        "name": "JSON去转义",
        "name_en": "Unescape JSON",
        "description": "反转义JSON特殊字符",
        "category": "encoding",
        "subcategory": "unescape",
        "api_endpoint": "/api/unescape_json",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "code"
    },
    "encode_csv": {
        "id": "encode_csv",
        "name": "CSV编码",
        "name_en": "CSV Encode",
        "description": "将数据编码为CSV格式",
        "category": "encoding",
        "subcategory": "encode",
        "api_endpoint": "/api/encode_csv",
        "method": "POST",
        "params": [
            {"name": "data", "type": "array", "required": True, "description": "数据数组"}
        ],
        "icon": "code"
    },
    "decode_csv": {
        "id": "decode_csv",
        "name": "CSV解码",
        "name_en": "CSV Decode",
        "description": "将CSV字符串解码",
        "category": "encoding",
        "subcategory": "decode",
        "api_endpoint": "/api/decode_csv",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "CSV字符串"}
        ],
        "icon": "code"
    },

    # ========== 随机工具 ==========
    "random_int": {
        "id": "random_int",
        "name": "随机整数",
        "name_en": "Random Integer",
        "description": "生成指定范围内的随机整数",
        "category": "random",
        "subcategory": "integer",
        "api_endpoint": "/api/random_int",
        "method": "POST",
        "params": [
            {"name": "min", "type": "number", "required": True, "description": "最小值"},
            {"name": "max", "type": "number", "required": True, "description": "最大值"}
        ],
        "icon": "hash"
    },
    "random_float": {
        "id": "random_float",
        "name": "随机小数",
        "name_en": "Random Float",
        "description": "生成0到1之间的随机小数",
        "category": "random",
        "subcategory": "float",
        "api_endpoint": "/api/random_float",
        "method": "POST",
        "params": [],
        "icon": "hash"
    },
    "random_choice": {
        "id": "random_choice",
        "name": "随机选择",
        "name_en": "Random Choice",
        "description": "从数组中随机选择一个元素",
        "category": "random",
        "subcategory": "choice",
        "api_endpoint": "/api/random_choice",
        "method": "POST",
        "params": [
            {"name": "array", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "shuffle"
    },
    "random_sample": {
        "id": "random_sample",
        "name": "随机抽样",
        "name_en": "Random Sample",
        "description": "从数组中随机抽取指定数量的元素",
        "category": "random",
        "subcategory": "sample",
        "api_endpoint": "/api/random_sample",
        "method": "POST",
        "params": [
            {"name": "array", "type": "array", "required": True, "description": "数组"},
            {"name": "n", "type": "number", "required": True, "description": "抽取数量"}
        ],
        "icon": "shuffle"
    },
    "random_shuffle": {
        "id": "random_shuffle",
        "name": "随机打乱",
        "name_en": "Random Shuffle",
        "description": "随机打乱数组顺序",
        "category": "random",
        "subcategory": "shuffle",
        "api_endpoint": "/api/random_shuffle",
        "method": "POST",
        "params": [
            {"name": "array", "type": "array", "required": True, "description": "数组"}
        ],
        "icon": "shuffle"
    },
    "random_uuid": {
        "id": "random_uuid",
        "name": "随机UUID",
        "name_en": "Random UUID",
        "description": "生成随机UUID",
        "category": "random",
        "subcategory": "uuid",
        "api_endpoint": "/api/random_uuid",
        "method": "POST",
        "params": [],
        "icon": "hash"
    },
    "random_color": {
        "id": "random_color",
        "name": "随机颜色",
        "name_en": "Random Color",
        "description": "生成随机颜色值",
        "category": "random",
        "subcategory": "color",
        "api_endpoint": "/api/random_color",
        "method": "POST",
        "params": [],
        "icon": "palette"
    },
    "random_date": {
        "id": "random_date",
        "name": "随机日期",
        "name_en": "Random Date",
        "description": "生成指定范围内的随机日期",
        "category": "random",
        "subcategory": "date",
        "api_endpoint": "/api/random_date",
        "method": "POST",
        "params": [
            {"name": "start_date", "type": "string", "required": True, "description": "开始日期"},
            {"name": "end_date", "type": "string", "required": True, "description": "结束日期"}
        ],
        "icon": "calendar"
    },
    "random_time": {
        "id": "random_time",
        "name": "随机时间",
        "name_en": "Random Time",
        "description": "生成随机时间",
        "category": "random",
        "subcategory": "time",
        "api_endpoint": "/api/random_time",
        "method": "POST",
        "params": [],
        "icon": "clock"
    },
    "random_bool": {
        "id": "random_bool",
        "name": "随机布尔",
        "name_en": "Random Boolean",
        "description": "生成随机布尔值",
        "category": "random",
        "subcategory": "bool",
        "api_endpoint": "/api/random_bool",
        "method": "POST",
        "params": [],
        "icon": "hash"
    },

    # ========== 序列工具 ==========
    "arithmetic_sequence": {
        "id": "arithmetic_sequence",
        "name": "等差数列",
        "name_en": "Arithmetic Sequence",
        "description": "生成等差数列",
        "category": "sequence",
        "subcategory": "arithmetic",
        "api_endpoint": "/api/arithmetic_sequence",
        "method": "POST",
        "params": [
            {"name": "start", "type": "number", "required": True, "description": "起始值"},
            {"name": "diff", "type": "number", "required": True, "description": "公差"},
            {"name": "count", "type": "number", "required": True, "description": "数量"}
        ],
        "icon": "list"
    },
    "geometric_sequence": {
        "id": "geometric_sequence",
        "name": "等比数列",
        "name_en": "Geometric Sequence",
        "description": "生成等比数列",
        "category": "sequence",
        "subcategory": "geometric",
        "api_endpoint": "/api/geometric_sequence",
        "method": "POST",
        "params": [
            {"name": "start", "type": "number", "required": True, "description": "起始值"},
            {"name": "ratio", "type": "number", "required": True, "description": "公比"},
            {"name": "count", "type": "number", "required": True, "description": "数量"}
        ],
        "icon": "list"
    },
    "fibonacci": {
        "id": "fibonacci",
        "name": "斐波那契数列",
        "name_en": "Fibonacci Sequence",
        "description": "生成斐波那契数列",
        "category": "sequence",
        "subcategory": "fibonacci",
        "api_endpoint": "/api/fibonacci",
        "method": "POST",
        "params": [
            {"name": "count", "type": "number", "required": True, "description": "数量"}
        ],
        "icon": "list"
    },
    "prime_sequence": {
        "id": "prime_sequence",
        "name": "质数序列",
        "name_en": "Prime Sequence",
        "description": "生成质数序列",
        "category": "sequence",
        "subcategory": "prime",
        "api_endpoint": "/api/prime_sequence",
        "method": "POST",
        "params": [
            {"name": "count", "type": "number", "required": True, "description": "数量"}
        ],
        "icon": "list"
    },
    "range_gen": {
        "id": "range_gen",
        "name": "范围生成",
        "name_en": "Range Generator",
        "description": "生成数字范围",
        "category": "sequence",
        "subcategory": "range",
        "api_endpoint": "/api/range_gen",
        "method": "POST",
        "params": [
            {"name": "start", "type": "number", "required": True, "description": "起始值"},
            {"name": "end", "type": "number", "required": True, "description": "结束值"},
            {"name": "step", "type": "number", "required": False, "description": "步长", "default": 1}
        ],
        "icon": "list"
    },
    "sequence_slice": {
        "id": "sequence_slice",
        "name": "序列切片",
        "name_en": "Sequence Slice",
        "description": "获取序列的切片",
        "category": "sequence",
        "subcategory": "slice",
        "api_endpoint": "/api/sequence_slice",
        "method": "POST",
        "params": [
            {"name": "sequence", "type": "array", "required": True, "description": "序列"},
            {"name": "start", "type": "number", "required": False, "description": "起始索引"},
            {"name": "end", "type": "number", "required": False, "description": "结束索引"}
        ],
        "icon": "scissors"
    },
    "sequence_reverse": {
        "id": "sequence_reverse",
        "name": "序列反转",
        "name_en": "Sequence Reverse",
        "description": "反转序列顺序",
        "category": "sequence",
        "subcategory": "reverse",
        "api_endpoint": "/api/sequence_reverse",
        "method": "POST",
        "params": [
            {"name": "sequence", "type": "array", "required": True, "description": "序列"}
        ],
        "icon": "shuffle"
    },

    # ========== 位运算工具 ==========
    "bit_and": {
        "id": "bit_and",
        "name": "位与",
        "name_en": "Bitwise AND",
        "description": "执行按位与运算",
        "category": "bitwise",
        "subcategory": "and",
        "api_endpoint": "/api/bit_and",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "操作数A"},
            {"name": "b", "type": "number", "required": True, "description": "操作数B"}
        ],
        "icon": "code"
    },
    "bit_or": {
        "id": "bit_or",
        "name": "位或",
        "name_en": "Bitwise OR",
        "description": "执行按位或运算",
        "category": "bitwise",
        "subcategory": "or",
        "api_endpoint": "/api/bit_or",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "操作数A"},
            {"name": "b", "type": "number", "required": True, "description": "操作数B"}
        ],
        "icon": "code"
    },
    "bit_xor": {
        "id": "bit_xor",
        "name": "位异或",
        "name_en": "Bitwise XOR",
        "description": "执行按位异或运算",
        "category": "bitwise",
        "subcategory": "xor",
        "api_endpoint": "/api/bit_xor",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "操作数A"},
            {"name": "b", "type": "number", "required": True, "description": "操作数B"}
        ],
        "icon": "code"
    },
    "bit_not": {
        "id": "bit_not",
        "name": "位非",
        "name_en": "Bitwise NOT",
        "description": "执行按位非运算",
        "category": "bitwise",
        "subcategory": "not",
        "api_endpoint": "/api/bit_not",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "操作数"}
        ],
        "icon": "code"
    },
    "bit_left_shift": {
        "id": "bit_left_shift",
        "name": "左移",
        "name_en": "Left Shift",
        "description": "执行左移运算",
        "category": "bitwise",
        "subcategory": "shift",
        "api_endpoint": "/api/bit_left_shift",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "操作数"},
            {"name": "bits", "type": "number", "required": True, "description": "移位数"}
        ],
        "icon": "code"
    },
    "bit_right_shift": {
        "id": "bit_right_shift",
        "name": "右移",
        "name_en": "Right Shift",
        "description": "执行右移运算",
        "category": "bitwise",
        "subcategory": "shift",
        "api_endpoint": "/api/bit_right_shift",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "操作数"},
            {"name": "bits", "type": "number", "required": True, "description": "移位数"}
        ],
        "icon": "code"
    },
    "bit_count_ones": {
        "id": "bit_count_ones",
        "name": "计数1的个数",
        "name_en": "Count Ones",
        "description": "计算二进制中1的个数",
        "category": "bitwise",
        "subcategory": "count",
        "api_endpoint": "/api/bit_count_ones",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "操作数"}
        ],
        "icon": "hash"
    },
    "is_power_of_two": {
        "id": "is_power_of_two",
        "name": "2的幂检查",
        "name_en": "Is Power of Two",
        "description": "检查是否为2的幂",
        "category": "bitwise",
        "subcategory": "check",
        "api_endpoint": "/api/is_power_of_two",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "操作数"}
        ],
        "icon": "check"
    },

    # ========== JSON工具 ==========
    "parse_json": {
        "id": "parse_json",
        "name": "JSON解析",
        "name_en": "Parse JSON",
        "description": "将JSON字符串解析为对象",
        "category": "json",
        "subcategory": "parse",
        "api_endpoint": "/api/parse_json",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "JSON字符串"}
        ],
        "icon": "code"
    },
    "to_json": {
        "id": "to_json",
        "name": "JSON序列化",
        "name_en": "To JSON",
        "description": "将对象序列化为JSON字符串",
        "category": "json",
        "subcategory": "serialize",
        "api_endpoint": "/api/to_json",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "对象"}
        ],
        "icon": "code"
    },
    "json_get": {
        "id": "json_get",
        "name": "JSON获取",
        "name_en": "JSON Get",
        "description": "获取JSON对象中的指定路径的值",
        "category": "json",
        "subcategory": "get",
        "api_endpoint": "/api/json_get",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "JSON对象"},
            {"name": "path", "type": "string", "required": True, "description": "路径"}
        ],
        "icon": "search"
    },
    "json_set": {
        "id": "json_set",
        "name": "JSON设置",
        "name_en": "JSON Set",
        "description": "设置JSON对象中指定路径的值",
        "category": "json",
        "subcategory": "set",
        "api_endpoint": "/api/json_set",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "JSON对象"},
            {"name": "path", "type": "string", "required": True, "description": "路径"},
            {"name": "value", "type": "object", "required": True, "description": "值"}
        ],
        "icon": "edit"
    },
    "json_merge": {
        "id": "json_merge",
        "name": "JSON合并",
        "name_en": "JSON Merge",
        "description": "合并多个JSON对象",
        "category": "json",
        "subcategory": "merge",
        "api_endpoint": "/api/json_merge",
        "method": "POST",
        "params": [
            {"name": "objects", "type": "array", "required": True, "description": "JSON对象数组"}
        ],
        "icon": "git-merge"
    },
    "json_keys": {
        "id": "json_keys",
        "name": "JSON键列表",
        "name_en": "JSON Keys",
        "description": "获取JSON对象的所有键",
        "category": "json",
        "subcategory": "keys",
        "api_endpoint": "/api/json_keys",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "JSON对象"}
        ],
        "icon": "list"
    },
    "json_values": {
        "id": "json_values",
        "name": "JSON值列表",
        "name_en": "JSON Values",
        "description": "获取JSON对象的所有值",
        "category": "json",
        "subcategory": "values",
        "api_endpoint": "/api/json_values",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "JSON对象"}
        ],
        "icon": "list"
    },
    "json_flatten": {
        "id": "json_flatten",
        "name": "JSON扁平化",
        "name_en": "JSON Flatten",
        "description": "将嵌套JSON对象扁平化",
        "category": "json",
        "subcategory": "flatten",
        "api_endpoint": "/api/json_flatten",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "JSON对象"}
        ],
        "icon": "compress"
    },
    "json_unflatten": {
        "id": "json_unflatten",
        "name": "JSON反扁平化",
        "name_en": "JSON Unflatten",
        "description": "将扁平化JSON对象恢复为嵌套结构",
        "category": "json",
        "subcategory": "unflatten",
        "api_endpoint": "/api/json_unflatten",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "扁平化对象"}
        ],
        "icon": "expand"
    },

    # ========== YAML工具 ==========
    "parse_yaml": {
        "id": "parse_yaml",
        "name": "YAML解析",
        "name_en": "Parse YAML",
        "description": "将YAML字符串解析为对象",
        "category": "yaml",
        "subcategory": "parse",
        "api_endpoint": "/api/parse_yaml",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "YAML字符串"}
        ],
        "icon": "code"
    },
    "to_yaml": {
        "id": "to_yaml",
        "name": "YAML序列化",
        "name_en": "To YAML",
        "description": "将对象序列化为YAML字符串",
        "category": "yaml",
        "subcategory": "serialize",
        "api_endpoint": "/api/to_yaml",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "对象"}
        ],
        "icon": "code"
    },

    # ========== XML工具 ==========
    "parse_xml": {
        "id": "parse_xml",
        "name": "XML解析",
        "name_en": "Parse XML",
        "description": "将XML字符串解析为对象",
        "category": "xml",
        "subcategory": "parse",
        "api_endpoint": "/api/parse_xml",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "XML字符串"}
        ],
        "icon": "code"
    },
    "to_xml": {
        "id": "to_xml",
        "name": "XML序列化",
        "name_en": "To XML",
        "description": "将对象序列化为XML字符串",
        "category": "xml",
        "subcategory": "serialize",
        "api_endpoint": "/api/to_xml",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "object", "required": True, "description": "对象"},
            {"name": "root", "type": "string", "required": False, "description": "根元素名", "default": "root"}
        ],
        "icon": "code"
    },

    # ========== HTML工具 ==========
    "parse_html": {
        "id": "parse_html",
        "name": "HTML解析",
        "name_en": "Parse HTML",
        "description": "将HTML字符串解析",
        "category": "html",
        "subcategory": "parse",
        "api_endpoint": "/api/parse_html",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "HTML字符串"}
        ],
        "icon": "code"
    },
    "to_html": {
        "id": "to_html",
        "name": "HTML转换",
        "name_en": "To HTML",
        "description": "将文本转换为HTML",
        "category": "html",
        "subcategory": "convert",
        "api_endpoint": "/api/to_html",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "code"
    },

    # ========== 颜色工具 ==========
    "hex_to_rgb": {
        "id": "hex_to_rgb",
        "name": "HEX转RGB",
        "name_en": "HEX to RGB",
        "description": "将HEX颜色值转换为RGB",
        "category": "color",
        "subcategory": "convert",
        "api_endpoint": "/api/hex_to_rgb",
        "method": "POST",
        "params": [
            {"name": "hex", "type": "string", "required": True, "description": "HEX颜色值"}
        ],
        "icon": "palette"
    },
    "rgb_to_hex": {
        "id": "rgb_to_hex",
        "name": "RGB转HEX",
        "name_en": "RGB to HEX",
        "description": "将RGB值转换为HEX颜色",
        "category": "color",
        "subcategory": "convert",
        "api_endpoint": "/api/rgb_to_hex",
        "method": "POST",
        "params": [
            {"name": "r", "type": "number", "required": True, "description": "红色分量"},
            {"name": "g", "type": "number", "required": True, "description": "绿色分量"},
            {"name": "b", "type": "number", "required": True, "description": "蓝色分量"}
        ],
        "icon": "palette"
    },
    "rgb_to_hsl": {
        "id": "rgb_to_hsl",
        "name": "RGB转HSL",
        "name_en": "RGB to HSL",
        "description": "将RGB值转换为HSL",
        "category": "color",
        "subcategory": "convert",
        "api_endpoint": "/api/rgb_to_hsl",
        "method": "POST",
        "params": [
            {"name": "r", "type": "number", "required": True, "description": "红色分量"},
            {"name": "g", "type": "number", "required": True, "description": "绿色分量"},
            {"name": "b", "type": "number", "required": True, "description": "蓝色分量"}
        ],
        "icon": "palette"
    },
    "hsl_to_rgb": {
        "id": "hsl_to_rgb",
        "name": "HSL转RGB",
        "name_en": "HSL to RGB",
        "description": "将HSL值转换为RGB",
        "category": "color",
        "subcategory": "convert",
        "api_endpoint": "/api/hsl_to_rgb",
        "method": "POST",
        "params": [
            {"name": "h", "type": "number", "required": True, "description": "色调"},
            {"name": "s", "type": "number", "required": True, "description": "饱和度"},
            {"name": "l", "type": "number", "required": True, "description": "亮度"}
        ],
        "icon": "palette"
    },
    "lighten": {
        "id": "lighten",
        "name": "提亮颜色",
        "name_en": "Lighten Color",
        "description": "将颜色值调亮",
        "category": "color",
        "subcategory": "adjust",
        "api_endpoint": "/api/lighten",
        "method": "POST",
        "params": [
            {"name": "hex", "type": "string", "required": True, "description": "HEX颜色值"},
            {"name": "amount", "type": "number", "required": False, "description": "提亮量", "default": 10}
        ],
        "icon": "sun"
    },
    "darken": {
        "id": "darken",
        "name": "加深颜色",
        "name_en": "Darken Color",
        "description": "将颜色值调深",
        "category": "color",
        "subcategory": "adjust",
        "api_endpoint": "/api/darken",
        "method": "POST",
        "params": [
            {"name": "hex", "type": "string", "required": True, "description": "HEX颜色值"},
            {"name": "amount", "type": "number", "required": False, "description": "加深量", "default": 10}
        ],
        "icon": "moon"
    },
    "saturate": {
        "id": "saturate",
        "name": "饱和度调整",
        "name_en": "Saturate Color",
        "description": "调整颜色饱和度",
        "category": "color",
        "subcategory": "adjust",
        "api_endpoint": "/api/saturate",
        "method": "POST",
        "params": [
            {"name": "hex", "type": "string", "required": True, "description": "HEX颜色值"},
            {"name": "amount", "type": "number", "required": False, "description": "调整量", "default": 10}
        ],
        "icon": "palette"
    },
    "desaturate": {
        "id": "desaturate",
        "name": "去饱和",
        "name_en": "Desaturate Color",
        "description": "降低颜色饱和度",
        "category": "color",
        "subcategory": "adjust",
        "api_endpoint": "/api/desaturate",
        "method": "POST",
        "params": [
            {"name": "hex", "type": "string", "required": True, "description": "HEX颜色值"},
            {"name": "amount", "type": "number", "required": False, "description": "调整量", "default": 10}
        ],
        "icon": "palette"
    },
    "grayscale": {
        "id": "grayscale",
        "name": "灰度转换",
        "name_en": "Grayscale",
        "description": "将颜色转换为灰度",
        "category": "color",
        "subcategory": "convert",
        "api_endpoint": "/api/grayscale",
        "method": "POST",
        "params": [
            {"name": "hex", "type": "string", "required": True, "description": "HEX颜色值"}
        ],
        "icon": "palette"
    },
    "invert": {
        "id": "invert",
        "name": "反相颜色",
        "name_en": "Invert Color",
        "description": "将颜色反相",
        "category": "color",
        "subcategory": "convert",
        "api_endpoint": "/api/invert",
        "method": "POST",
        "params": [
            {"name": "hex", "type": "string", "required": True, "description": "HEX颜色值"}
        ],
        "icon": "refresh"
    },

    # ========== URL工具 ==========
    "parse_url": {
        "id": "parse_url",
        "name": "URL解析",
        "name_en": "Parse URL",
        "description": "解析URL字符串",
        "category": "url",
        "subcategory": "parse",
        "api_endpoint": "/api/parse_url",
        "method": "POST",
        "params": [
            {"name": "url", "type": "string", "required": True, "description": "URL字符串"}
        ],
        "icon": "link"
    },
    "build_url": {
        "id": "build_url",
        "name": "URL构建",
        "name_en": "Build URL",
        "description": "构建URL字符串",
        "category": "url",
        "subcategory": "build",
        "api_endpoint": "/api/build_url",
        "method": "POST",
        "params": [
            {"name": "scheme", "type": "string", "required": True, "description": "协议"},
            {"name": "host", "type": "string", "required": True, "description": "主机"},
            {"name": "path", "type": "string", "required": False, "description": "路径"},
            {"name": "query", "type": "object", "required": False, "description": "查询参数"}
        ],
        "icon": "link"
    },
    "get_query_params": {
        "id": "get_query_params",
        "name": "获取查询参数",
        "name_en": "Get Query Params",
        "description": "从URL中获取查询参数",
        "category": "url",
        "subcategory": "query",
        "api_endpoint": "/api/get_query_params",
        "method": "POST",
        "params": [
            {"name": "url", "type": "string", "required": True, "description": "URL字符串"}
        ],
        "icon": "search"
    },
    "add_query_param": {
        "id": "add_query_param",
        "name": "添加查询参数",
        "name_en": "Add Query Param",
        "description": "向URL添加查询参数",
        "category": "url",
        "subcategory": "query",
        "api_endpoint": "/api/add_query_param",
        "method": "POST",
        "params": [
            {"name": "url", "type": "string", "required": True, "description": "URL字符串"},
            {"name": "key", "type": "string", "required": True, "description": "参数名"},
            {"name": "value", "type": "string", "required": True, "description": "参数值"}
        ],
        "icon": "plus"
    },

    # ========== 文件路径工具 ==========
    "get_extension": {
        "id": "get_extension",
        "name": "获取扩展名",
        "name_en": "Get Extension",
        "description": "获取文件路径的扩展名",
        "category": "file",
        "subcategory": "path",
        "api_endpoint": "/api/get_extension",
        "method": "POST",
        "params": [
            {"name": "path", "type": "string", "required": True, "description": "文件路径"}
        ],
        "icon": "file"
    },
    "get_filename": {
        "id": "get_filename",
        "name": "获取文件名",
        "name_en": "Get Filename",
        "description": "获取文件路径的文件名",
        "category": "file",
        "subcategory": "path",
        "api_endpoint": "/api/get_filename",
        "method": "POST",
        "params": [
            {"name": "path", "type": "string", "required": True, "description": "文件路径"}
        ],
        "icon": "file"
    },
    "get_basename": {
        "id": "get_basename",
        "name": "获取基名",
        "name_en": "Get Basename",
        "description": "获取文件路径的基名（不含扩展名）",
        "category": "file",
        "subcategory": "path",
        "api_endpoint": "/api/get_basename",
        "method": "POST",
        "params": [
            {"name": "path", "type": "string", "required": True, "description": "文件路径"}
        ],
        "icon": "file"
    },
    "get_dirname": {
        "id": "get_dirname",
        "name": "获取目录名",
        "name_en": "Get Dirname",
        "description": "获取文件路径的目录名",
        "category": "file",
        "subcategory": "path",
        "api_endpoint": "/api/get_dirname",
        "method": "POST",
        "params": [
            {"name": "path", "type": "string", "required": True, "description": "文件路径"}
        ],
        "icon": "folder"
    },
    "join_path": {
        "id": "join_path",
        "name": "拼接路径",
        "name_en": "Join Path",
        "description": "拼接多个路径组件",
        "category": "file",
        "subcategory": "path",
        "api_endpoint": "/api/join_path",
        "method": "POST",
        "params": [
            {"name": "parts", "type": "array", "required": True, "description": "路径部分"}
        ],
        "icon": "link"
    },
    "normalize_path": {
        "id": "normalize_path",
        "name": "规范化路径",
        "name_en": "Normalize Path",
        "description": "规范化文件路径",
        "category": "file",
        "subcategory": "path",
        "api_endpoint": "/api/normalize_path",
        "method": "POST",
        "params": [
            {"name": "path", "type": "string", "required": True, "description": "文件路径"}
        ],
        "icon": "link"
    },

    # ========== 数学工具 ==========
    "percent_of": {
        "id": "percent_of",
        "name": "百分比计算",
        "name_en": "Percent Of",
        "description": "计算某数占总数的百分比",
        "category": "math",
        "subcategory": "percent",
        "api_endpoint": "/api/percent_of",
        "method": "POST",
        "params": [
            {"name": "value", "type": "number", "required": True, "description": "数值"},
            {"name": "total", "type": "number", "required": True, "description": "总数"}
        ],
        "icon": "percent"
    },
    "percent_change": {
        "id": "percent_change",
        "name": "百分比变化",
        "name_en": "Percent Change",
        "description": "计算百分比变化",
        "category": "math",
        "subcategory": "percent",
        "api_endpoint": "/api/percent_change",
        "method": "POST",
        "params": [
            {"name": "old_value", "type": "number", "required": True, "description": "旧值"},
            {"name": "new_value", "type": "number", "required": True, "description": "新值"}
        ],
        "icon": "trending-up"
    },
    "percent_diff": {
        "id": "percent_diff",
        "name": "百分比差异",
        "name_en": "Percent Difference",
        "description": "计算两个数之间的百分比差异",
        "category": "math",
        "subcategory": "percent",
        "api_endpoint": "/api/percent_diff",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "数值A"},
            {"name": "b", "type": "number", "required": True, "description": "数值B"}
        ],
        "icon": "percent"
    },
    "percentile": {
        "id": "percentile",
        "name": "百分位数",
        "name_en": "Percentile",
        "description": "计算数组的百分位数",
        "category": "math",
        "subcategory": "statistics",
        "api_endpoint": "/api/percentile",
        "method": "POST",
        "params": [
            {"name": "array", "type": "array", "required": True, "description": "数值数组"},
            {"name": "p", "type": "number", "required": True, "description": "百分位"}
        ],
        "icon": "percent"
    },
    "sin": {
        "id": "sin",
        "name": "正弦",
        "name_en": "Sine",
        "description": "计算正弦值",
        "category": "math",
        "subcategory": "trigonometry",
        "api_endpoint": "/api/sin",
        "method": "POST",
        "params": [
            {"name": "angle", "type": "number", "required": True, "description": "角度"}
        ],
        "icon": "triangle"
    },
    "cos": {
        "id": "cos",
        "name": "余弦",
        "name_en": "Cosine",
        "description": "计算余弦值",
        "category": "math",
        "subcategory": "trigonometry",
        "api_endpoint": "/api/cos",
        "method": "POST",
        "params": [
            {"name": "angle", "type": "number", "required": True, "description": "角度"}
        ],
        "icon": "triangle"
    },
    "tan": {
        "id": "tan",
        "name": "正切",
        "name_en": "Tangent",
        "description": "计算正切值",
        "category": "math",
        "subcategory": "trigonometry",
        "api_endpoint": "/api/tan",
        "method": "POST",
        "params": [
            {"name": "angle", "type": "number", "required": True, "description": "角度"}
        ],
        "icon": "triangle"
    },
    "asin": {
        "id": "asin",
        "name": "反正弦",
        "name_en": "Arc Sine",
        "description": "计算反正弦值",
        "category": "math",
        "subcategory": "trigonometry",
        "api_endpoint": "/api/asin",
        "method": "POST",
        "params": [
            {"name": "value", "type": "number", "required": True, "description": "数值"}
        ],
        "icon": "triangle"
    },
    "acos": {
        "id": "acos",
        "name": "反余弦",
        "name_en": "Arc Cosine",
        "description": "计算反余弦值",
        "category": "math",
        "subcategory": "trigonometry",
        "api_endpoint": "/api/acos",
        "method": "POST",
        "params": [
            {"name": "value", "type": "number", "required": True, "description": "数值"}
        ],
        "icon": "triangle"
    },
    "atan": {
        "id": "atan",
        "name": "反正切",
        "name_en": "Arc Tangent",
        "description": "计算反正切值",
        "category": "math",
        "subcategory": "trigonometry",
        "api_endpoint": "/api/atan",
        "method": "POST",
        "params": [
            {"name": "value", "type": "number", "required": True, "description": "数值"}
        ],
        "icon": "triangle"
    },
    "complex_add": {
        "id": "complex_add",
        "name": "复数加法",
        "name_en": "Complex Add",
        "description": "复数相加",
        "category": "math",
        "subcategory": "complex",
        "api_endpoint": "/api/complex_add",
        "method": "POST",
        "params": [
            {"name": "a", "type": "object", "required": True, "description": "复数A {real, imaginary}"},
            {"name": "b", "type": "object", "required": True, "description": "复数B {real, imaginary}"}
        ],
        "icon": "plus"
    },
    "complex_sub": {
        "id": "complex_sub",
        "name": "复数减法",
        "name_en": "Complex Subtract",
        "description": "复数相减",
        "category": "math",
        "subcategory": "complex",
        "api_endpoint": "/api/complex_sub",
        "method": "POST",
        "params": [
            {"name": "a", "type": "object", "required": True, "description": "复数A {real, imaginary}"},
            {"name": "b", "type": "object", "required": True, "description": "复数B {real, imaginary}"}
        ],
        "icon": "minus"
    },
    "complex_mul": {
        "id": "complex_mul",
        "name": "复数乘法",
        "name_en": "Complex Multiply",
        "description": "复数相乘",
        "category": "math",
        "subcategory": "complex",
        "api_endpoint": "/api/complex_mul",
        "method": "POST",
        "params": [
            {"name": "a", "type": "object", "required": True, "description": "复数A {real, imaginary}"},
            {"name": "b", "type": "object", "required": True, "description": "复数B {real, imaginary}"}
        ],
        "icon": "x"
    },
    "complex_div": {
        "id": "complex_div",
        "name": "复数除法",
        "name_en": "Complex Divide",
        "description": "复数相除",
        "category": "math",
        "subcategory": "complex",
        "api_endpoint": "/api/complex_div",
        "method": "POST",
        "params": [
            {"name": "a", "type": "object", "required": True, "description": "复数A {real, imaginary}"},
            {"name": "b", "type": "object", "required": True, "description": "复数B {real, imaginary}"}
        ],
        "icon": "divide"
    },
    "matrix_add": {
        "id": "matrix_add",
        "name": "矩阵加法",
        "name_en": "Matrix Add",
        "description": "矩阵相加",
        "category": "math",
        "subcategory": "matrix",
        "api_endpoint": "/api/matrix_add",
        "method": "POST",
        "params": [
            {"name": "a", "type": "array", "required": True, "description": "矩阵A"},
            {"name": "b", "type": "array", "required": True, "description": "矩阵B"}
        ],
        "icon": "grid"
    },
    "matrix_sub": {
        "id": "matrix_sub",
        "name": "矩阵减法",
        "name_en": "Matrix Subtract",
        "description": "矩阵相减",
        "category": "math",
        "subcategory": "matrix",
        "api_endpoint": "/api/matrix_sub",
        "method": "POST",
        "params": [
            {"name": "a", "type": "array", "required": True, "description": "矩阵A"},
            {"name": "b", "type": "array", "required": True, "description": "矩阵B"}
        ],
        "icon": "grid"
    },
    "matrix_mul": {
        "id": "matrix_mul",
        "name": "矩阵乘法",
        "name_en": "Matrix Multiply",
        "description": "矩阵相乘",
        "category": "math",
        "subcategory": "matrix",
        "api_endpoint": "/api/matrix_mul",
        "method": "POST",
        "params": [
            {"name": "a", "type": "array", "required": True, "description": "矩阵A"},
            {"name": "b", "type": "array", "required": True, "description": "矩阵B"}
        ],
        "icon": "grid"
    },
    "matrix_transpose": {
        "id": "matrix_transpose",
        "name": "矩阵转置",
        "name_en": "Matrix Transpose",
        "description": "矩阵转置",
        "category": "math",
        "subcategory": "matrix",
        "api_endpoint": "/api/matrix_transpose",
        "method": "POST",
        "params": [
            {"name": "matrix", "type": "array", "required": True, "description": "矩阵"}
        ],
        "icon": "grid"
    },
    "matrix_inverse": {
        "id": "matrix_inverse",
        "name": "矩阵求逆",
        "name_en": "Matrix Inverse",
        "description": "求矩阵的逆",
        "category": "math",
        "subcategory": "matrix",
        "api_endpoint": "/api/matrix_inverse",
        "method": "POST",
        "params": [
            {"name": "matrix", "type": "array", "required": True, "description": "矩阵"}
        ],
        "icon": "grid"
    },
    "matrix_determinant": {
        "id": "matrix_determinant",
        "name": "矩阵行列式",
        "name_en": "Matrix Determinant",
        "description": "计算矩阵行列式",
        "category": "math",
        "subcategory": "matrix",
        "api_endpoint": "/api/matrix_determinant",
        "method": "POST",
        "params": [
            {"name": "matrix", "type": "array", "required": True, "description": "矩阵"}
        ],
        "icon": "grid"
    },
    "vector_add": {
        "id": "vector_add",
        "name": "向量加法",
        "name_en": "Vector Add",
        "description": "向量相加",
        "category": "math",
        "subcategory": "vector",
        "api_endpoint": "/api/vector_add",
        "method": "POST",
        "params": [
            {"name": "a", "type": "array", "required": True, "description": "向量A"},
            {"name": "b", "type": "array", "required": True, "description": "向量B"}
        ],
        "icon": "git-compare"
    },
    "vector_sub": {
        "id": "vector_sub",
        "name": "向量减法",
        "name_en": "Vector Subtract",
        "description": "向量相减",
        "category": "math",
        "subcategory": "vector",
        "api_endpoint": "/api/vector_sub",
        "method": "POST",
        "params": [
            {"name": "a", "type": "array", "required": True, "description": "向量A"},
            {"name": "b", "type": "array", "required": True, "description": "向量B"}
        ],
        "icon": "git-compare"
    },
    "vector_dot": {
        "id": "vector_dot",
        "name": "向量点积",
        "name_en": "Vector Dot Product",
        "description": "计算向量点积",
        "category": "math",
        "subcategory": "vector",
        "api_endpoint": "/api/vector_dot",
        "method": "POST",
        "params": [
            {"name": "a", "type": "array", "required": True, "description": "向量A"},
            {"name": "b", "type": "array", "required": True, "description": "向量B"}
        ],
        "icon": "git-compare"
    },
    "vector_cross": {
        "id": "vector_cross",
        "name": "向量叉积",
        "name_en": "Vector Cross Product",
        "description": "计算向量叉积",
        "category": "math",
        "subcategory": "vector",
        "api_endpoint": "/api/vector_cross",
        "method": "POST",
        "params": [
            {"name": "a", "type": "array", "required": True, "description": "向量A"},
            {"name": "b", "type": "array", "required": True, "description": "向量B"}
        ],
        "icon": "git-compare"
    },
    "vector_magnitude": {
        "id": "vector_magnitude",
        "name": "向量模长",
        "name_en": "Vector Magnitude",
        "description": "计算向量模长",
        "category": "math",
        "subcategory": "vector",
        "api_endpoint": "/api/vector_magnitude",
        "method": "POST",
        "params": [
            {"name": "vector", "type": "array", "required": True, "description": "向量"}
        ],
        "icon": "maximize"
    },
    "vector_normalize": {
        "id": "vector_normalize",
        "name": "向量归一化",
        "name_en": "Vector Normalize",
        "description": "归一化向量",
        "category": "math",
        "subcategory": "vector",
        "api_endpoint": "/api/vector_normalize",
        "method": "POST",
        "params": [
            {"name": "vector", "type": "array", "required": True, "description": "向量"}
        ],
        "icon": "minimize"
    },

    # ========== 概率统计工具 ==========
    "random_normal": {
        "id": "random_normal",
        "name": "正态分布随机数",
        "name_en": "Normal Distribution",
        "description": "生成正态分布随机数",
        "category": "probability",
        "subcategory": "normal",
        "api_endpoint": "/api/random_normal",
        "method": "POST",
        "params": [
            {"name": "mean", "type": "number", "required": False, "description": "均值", "default": 0},
            {"name": "std", "type": "number", "required": False, "description": "标准差", "default": 1}
        ],
        "icon": "hash"
    },
    "random_uniform": {
        "id": "random_uniform",
        "name": "均匀分布随机数",
        "name_en": "Uniform Distribution",
        "description": "生成均匀分布随机数",
        "category": "probability",
        "subcategory": "uniform",
        "api_endpoint": "/api/random_uniform",
        "method": "POST",
        "params": [
            {"name": "min", "type": "number", "required": True, "description": "最小值"},
            {"name": "max", "type": "number", "required": True, "description": "最大值"}
        ],
        "icon": "hash"
    },
    "random_exponential": {
        "id": "random_exponential",
        "name": "指数分布随机数",
        "name_en": "Exponential Distribution",
        "description": "生成指数分布随机数",
        "category": "probability",
        "subcategory": "exponential",
        "api_endpoint": "/api/random_exponential",
        "method": "POST",
        "params": [
            {"name": "lambda", "type": "number", "required": True, "description": "lambda参数"}
        ],
        "icon": "hash"
    },
    "mean": {
        "id": "mean",
        "name": "平均值",
        "name_en": "Mean",
        "description": "计算平均值",
        "category": "statistics",
        "subcategory": "average",
        "api_endpoint": "/api/mean",
        "method": "POST",
        "params": [
            {"name": "array", "type": "array", "required": True, "description": "数值数组"}
        ],
        "icon": "percent"
    },
    "median": {
        "id": "median",
        "name": "中位数",
        "name_en": "Median",
        "description": "计算中位数",
        "category": "statistics",
        "subcategory": "middle",
        "api_endpoint": "/api/median",
        "method": "POST",
        "params": [
            {"name": "array", "type": "array", "required": True, "description": "数值数组"}
        ],
        "icon": "percent"
    },
    "mode": {
        "id": "mode",
        "name": "众数",
        "name_en": "Mode",
        "description": "计算众数",
        "category": "statistics",
        "subcategory": "frequency",
        "api_endpoint": "/api/mode",
        "method": "POST",
        "params": [
            {"name": "array", "type": "array", "required": True, "description": "数值数组"}
        ],
        "icon": "percent"
    },
    "variance": {
        "id": "variance",
        "name": "方差",
        "name_en": "Variance",
        "description": "计算方差",
        "category": "statistics",
        "subcategory": "dispersion",
        "api_endpoint": "/api/variance",
        "method": "POST",
        "params": [
            {"name": "array", "type": "array", "required": True, "description": "数值数组"}
        ],
        "icon": "percent"
    },
    "std_dev": {
        "id": "std_dev",
        "name": "标准差",
        "name_en": "Standard Deviation",
        "description": "计算标准差",
        "category": "statistics",
        "subcategory": "dispersion",
        "api_endpoint": "/api/std_dev",
        "method": "POST",
        "params": [
            {"name": "array", "type": "array", "required": True, "description": "数值数组"}
        ],
        "icon": "percent"
    },
    "skewness": {
        "id": "skewness",
        "name": "偏度",
        "name_en": "Skewness",
        "description": "计算偏度",
        "category": "statistics",
        "subcategory": "shape",
        "api_endpoint": "/api/skewness",
        "method": "POST",
        "params": [
            {"name": "array", "type": "array", "required": True, "description": "数值数组"}
        ],
        "icon": "percent"
    },
    "kurtosis": {
        "id": "kurtosis",
        "name": "峰度",
        "name_en": "Kurtosis",
        "description": "计算峰度",
        "category": "statistics",
        "subcategory": "shape",
        "api_endpoint": "/api/kurtosis",
        "method": "POST",
        "params": [
            {"name": "array", "type": "array", "required": True, "description": "数值数组"}
        ],
        "icon": "percent"
    },
    "linear_regression": {
        "id": "linear_regression",
        "name": "线性回归",
        "name_en": "Linear Regression",
        "description": "计算线性回归",
        "category": "regression",
        "subcategory": "linear",
        "api_endpoint": "/api/linear_regression",
        "method": "POST",
        "params": [
            {"name": "x", "type": "array", "required": True, "description": "X值数组"},
            {"name": "y", "type": "array", "required": True, "description": "Y值数组"}
        ],
        "icon": "trending-up"
    },
    "polynomial_regression": {
        "id": "polynomial_regression",
        "name": "多项式回归",
        "name_en": "Polynomial Regression",
        "description": "计算多项式回归",
        "category": "regression",
        "subcategory": "polynomial",
        "api_endpoint": "/api/polynomial_regression",
        "method": "POST",
        "params": [
            {"name": "x", "type": "array", "required": True, "description": "X值数组"},
            {"name": "y", "type": "array", "required": True, "description": "Y值数组"},
            {"name": "degree", "type": "number", "required": False, "description": "多项式次数", "default": 2}
        ],
        "icon": "trending-up"
    },
    "lerp": {
        "id": "lerp",
        "name": "线性插值",
        "name_en": "Linear Interpolation",
        "description": "线性插值",
        "category": "interpolation",
        "subcategory": "linear",
        "api_endpoint": "/api/lerp",
        "method": "POST",
        "params": [
            {"name": "a", "type": "number", "required": True, "description": "起始值"},
            {"name": "b", "type": "number", "required": True, "description": "结束值"},
            {"name": "t", "type": "number", "required": True, "description": "插值参数"}
        ],
        "icon": "git-merge"
    },
    "slerp": {
        "id": "slerp",
        "name": "球面线性插值",
        "name_en": "Spherical Lerp",
        "description": "球面线性插值",
        "category": "interpolation",
        "subcategory": "spherical",
        "api_endpoint": "/api/slerp",
        "method": "POST",
        "params": [
            {"name": "a", "type": "array", "required": True, "description": "起始向量"},
            {"name": "b", "type": "array", "required": True, "description": "结束向量"},
            {"name": "t", "type": "number", "required": True, "description": "插值参数"}
        ],
        "icon": "git-merge"
    },
    "bilinear_interpolate": {
        "id": "bilinear_interpolate",
        "name": "双线性插值",
        "name_en": "Bilinear Interpolation",
        "description": "双线性插值",
        "category": "interpolation",
        "subcategory": "bilinear",
        "api_endpoint": "/api/bilinear_interpolate",
        "method": "POST",
        "params": [
            {"name": "q11", "type": "number", "required": True, "description": "Q11值"},
            {"name": "q12", "type": "number", "required": True, "description": "Q12值"},
            {"name": "q21", "type": "number", "required": True, "description": "Q21值"},
            {"name": "q22", "type": "number", "required": True, "description": "Q22值"},
            {"name": "x", "type": "number", "required": True, "description": "X位置"},
            {"name": "y", "type": "number", "required": True, "description": "Y位置"}
        ],
        "icon": "git-merge"
    },
    "moving_average": {
        "id": "moving_average",
        "name": "移动平均",
        "name_en": "Moving Average",
        "description": "计算移动平均",
        "category": "smoothing",
        "subcategory": "average",
        "api_endpoint": "/api/moving_average",
        "method": "POST",
        "params": [
            {"name": "array", "type": "array", "required": True, "description": "数值数组"},
            {"name": "window", "type": "number", "required": True, "description": "窗口大小"}
        ],
        "icon": "activity"
    },
    "exponential_smooth": {
        "id": "exponential_smooth",
        "name": "指数平滑",
        "name_en": "Exponential Smoothing",
        "description": "指数平滑",
        "category": "smoothing",
        "subcategory": "exponential",
        "api_endpoint": "/api/exponential_smooth",
        "method": "POST",
        "params": [
            {"name": "array", "type": "array", "required": True, "description": "数值数组"},
            {"name": "alpha", "type": "number", "required": False, "description": "平滑系数", "default": 0.3}
        ],
        "icon": "activity"
    },
    "savitzky_golay": {
        "id": "savitzky_golay",
        "name": "Savitzky-Golay滤波",
        "name_en": "Savitzky-Golay Filter",
        "description": "Savitzky-Golay平滑滤波",
        "category": "smoothing",
        "subcategory": "savitzky_golay",
        "api_endpoint": "/api/savitzky_golay",
        "method": "POST",
        "params": [
            {"name": "array", "type": "array", "required": True, "description": "数值数组"},
            {"name": "window", "type": "number", "required": False, "description": "窗口大小", "default": 5},
            {"name": "order", "type": "number", "required": False, "description": "多项式阶数", "default": 2}
        ],
        "icon": "activity"
    },

    # ========== 网络工具 ==========
    "parse_url": {
        "id": "parse_url",
        "name": "URL解析",
        "name_en": "Parse URL",
        "description": "解析URL获取各组成部分",
        "category": "network",
        "subcategory": "url",
        "api_endpoint": "/api/parse_url",
        "method": "POST",
        "params": [
            {"name": "url", "type": "string", "required": True, "description": "URL字符串"}
        ],
        "icon": "link"
    },
    "build_url": {
        "id": "build_url",
        "name": "URL构建",
        "name_en": "Build URL",
        "description": "构建URL字符串",
        "category": "network",
        "subcategory": "url",
        "api_endpoint": "/api/build_url",
        "method": "POST",
        "params": [
            {"name": "scheme", "type": "string", "required": True, "description": "协议"},
            {"name": "host", "type": "string", "required": True, "description": "主机"},
            {"name": "path", "type": "string", "required": False, "description": "路径"},
            {"name": "query", "type": "object", "required": False, "description": "查询参数"}
        ],
        "icon": "link"
    },
    "get_query_params": {
        "id": "get_query_params",
        "name": "获取查询参数",
        "name_en": "Get Query Params",
        "description": "从URL中提取查询参数",
        "category": "network",
        "subcategory": "url",
        "api_endpoint": "/api/get_query_params",
        "method": "POST",
        "params": [
            {"name": "url", "type": "string", "required": True, "description": "URL字符串"}
        ],
        "icon": "search"
    },
    "add_query_param": {
        "id": "add_query_param",
        "name": "添加查询参数",
        "name_en": "Add Query Param",
        "description": "向URL添加查询参数",
        "category": "network",
        "subcategory": "url",
        "api_endpoint": "/api/add_query_param",
        "method": "POST",
        "params": [
            {"name": "url", "type": "string", "required": True, "description": "URL字符串"},
            {"name": "key", "type": "string", "required": True, "description": "参数名"},
            {"name": "value", "type": "string", "required": True, "description": "参数值"}
        ],
        "icon": "plus"
    },
    "is_valid_ip": {
        "id": "is_valid_ip",
        "name": "IP验证",
        "name_en": "Is Valid IP",
        "description": "验证IP地址格式",
        "category": "network",
        "subcategory": "ip",
        "api_endpoint": "/api/is_valid_ip",
        "method": "POST",
        "params": [
            {"name": "ip", "type": "string", "required": True, "description": "IP地址"}
        ],
        "icon": "check"
    },
    "ip_to_int": {
        "id": "ip_to_int",
        "name": "IP转整数",
        "name_en": "IP to Integer",
        "description": "将IP地址转换为整数",
        "category": "network",
        "subcategory": "ip",
        "api_endpoint": "/api/ip_to_int",
        "method": "POST",
        "params": [
            {"name": "ip", "type": "string", "required": True, "description": "IP地址"}
        ],
        "icon": "hash"
    },
    "int_to_ip": {
        "id": "int_to_ip",
        "name": "整数转IP",
        "name_en": "Integer to IP",
        "description": "将整数转换为IP地址",
        "category": "network",
        "subcategory": "ip",
        "api_endpoint": "/api/int_to_ip",
        "method": "POST",
        "params": [
            {"name": "num", "type": "number", "required": True, "description": "整数"}
        ],
        "icon": "hash"
    },
    "is_private_ip": {
        "id": "is_private_ip",
        "name": "私网IP检查",
        "name_en": "Is Private IP",
        "description": "检查是否为私网IP",
        "category": "network",
        "subcategory": "ip",
        "api_endpoint": "/api/is_private_ip",
        "method": "POST",
        "params": [
            {"name": "ip", "type": "string", "required": True, "description": "IP地址"}
        ],
        "icon": "check"
    },
    "dns_lookup": {
        "id": "dns_lookup",
        "name": "DNS查询",
        "name_en": "DNS Lookup",
        "description": "查询域名的DNS记录",
        "category": "network",
        "subcategory": "dns",
        "api_endpoint": "/api/dns_lookup",
        "method": "POST",
        "params": [
            {"name": "domain", "type": "string", "required": True, "description": "域名"}
        ],
        "icon": "search"
    },
    "reverse_dns": {
        "id": "reverse_dns",
        "name": "反向DNS",
        "name_en": "Reverse DNS",
        "description": "进行反向DNS查询",
        "category": "network",
        "subcategory": "dns",
        "api_endpoint": "/api/reverse_dns",
        "method": "POST",
        "params": [
            {"name": "ip", "type": "string", "required": True, "description": "IP地址"}
        ],
        "icon": "search"
    },
    "ping": {
        "id": "ping",
        "name": "Ping检测",
        "name_en": "Ping",
        "description": "检测主机是否可达",
        "category": "network",
        "subcategory": "ping",
        "api_endpoint": "/api/ping",
        "method": "POST",
        "params": [
            {"name": "host", "type": "string", "required": True, "description": "主机地址"}
        ],
        "icon": "activity"
    },
    "port_scan": {
        "id": "port_scan",
        "name": "端口扫描",
        "name_en": "Port Scan",
        "description": "扫描主机的端口",
        "category": "network",
        "subcategory": "scan",
        "api_endpoint": "/api/port_scan",
        "method": "POST",
        "params": [
            {"name": "host", "type": "string", "required": True, "description": "主机地址"},
            {"name": "ports", "type": "array", "required": False, "description": "端口列表"}
        ],
        "icon": "search"
    },
    "http_get": {
        "id": "http_get",
        "name": "HTTP GET",
        "name_en": "HTTP GET",
        "description": "发送HTTP GET请求",
        "category": "network",
        "subcategory": "http",
        "api_endpoint": "/api/http_get",
        "method": "POST",
        "params": [
            {"name": "url", "type": "string", "required": True, "description": "URL"}
        ],
        "icon": "globe"
    },
    "http_post": {
        "id": "http_post",
        "name": "HTTP POST",
        "name_en": "HTTP POST",
        "description": "发送HTTP POST请求",
        "category": "network",
        "subcategory": "http",
        "api_endpoint": "/api/http_post",
        "method": "POST",
        "params": [
            {"name": "url", "type": "string", "required": True, "description": "URL"},
            {"name": "data", "type": "object", "required": False, "description": "数据"}
        ],
        "icon": "globe"
    },
    "parse_headers": {
        "id": "parse_headers",
        "name": "解析HTTP头",
        "name_en": "Parse Headers",
        "description": "解析HTTP响应头",
        "category": "network",
        "subcategory": "http",
        "api_endpoint": "/api/parse_headers",
        "method": "POST",
        "params": [
            {"name": "headers", "type": "string", "required": True, "description": "HTTP头字符串"}
        ],
        "icon": "list"
    },
    "build_headers": {
        "id": "build_headers",
        "name": "构建HTTP头",
        "name_en": "Build Headers",
        "description": "构建HTTP请求头",
        "category": "network",
        "subcategory": "http",
        "api_endpoint": "/api/build_headers",
        "method": "POST",
        "params": [
            {"name": "headers", "type": "object", "required": True, "description": "头信息对象"}
        ],
        "icon": "list"
    },

    # ========== 邮件工具 ==========
    "is_valid_email": {
        "id": "is_valid_email",
        "name": "邮箱验证",
        "name_en": "Is Valid Email",
        "description": "验证邮箱格式",
        "category": "email",
        "subcategory": "validate",
        "api_endpoint": "/api/is_valid_email",
        "method": "POST",
        "params": [
            {"name": "email", "type": "string", "required": True, "description": "邮箱地址"}
        ],
        "icon": "check"
    },
    "parse_email": {
        "id": "parse_email",
        "name": "解析邮箱",
        "name_en": "Parse Email",
        "description": "解析邮箱地址",
        "category": "email",
        "subcategory": "parse",
        "api_endpoint": "/api/parse_email",
        "method": "POST",
        "params": [
            {"name": "email", "type": "string", "required": True, "description": "邮箱地址"}
        ],
        "icon": "mail"
    },
    "build_email": {
        "id": "build_email",
        "name": "构建邮箱",
        "name_en": "Build Email",
        "description": "构建邮箱地址",
        "category": "email",
        "subcategory": "build",
        "api_endpoint": "/api/build_email",
        "method": "POST",
        "params": [
            {"name": "local", "type": "string", "required": True, "description": "本地部分"},
            {"name": "domain", "type": "string", "required": True, "description": "域名"}
        ],
        "icon": "mail"
    },
    "extract_domain": {
        "id": "extract_domain",
        "name": "提取域名",
        "name_en": "Extract Domain",
        "description": "从邮箱提取域名",
        "category": "email",
        "subcategory": "extract",
        "api_endpoint": "/api/extract_domain",
        "method": "POST",
        "params": [
            {"name": "email", "type": "string", "required": True, "description": "邮箱地址"}
        ],
        "icon": "at-sign"
    },
    "mask_email": {
        "id": "mask_email",
        "name": "邮箱脱敏",
        "name_en": "Mask Email",
        "description": "隐藏邮箱部分字符",
        "category": "email",
        "subcategory": "mask",
        "api_endpoint": "/api/mask_email",
        "method": "POST",
        "params": [
            {"name": "email", "type": "string", "required": True, "description": "邮箱地址"}
        ],
        "icon": "eye-off"
    },

    # ========== 正则表达式工具 ==========
    "regex_match": {
        "id": "regex_match",
        "name": "正则匹配",
        "name_en": "Regex Match",
        "description": "检查字符串是否匹配正则",
        "category": "regex",
        "subcategory": "match",
        "api_endpoint": "/api/regex_match",
        "method": "POST",
        "params": [
            {"name": "pattern", "type": "string", "required": True, "description": "正则模式"},
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "check"
    },
    "regex_find": {
        "id": "regex_find",
        "name": "正则查找",
        "name_en": "Regex Find",
        "description": "查找所有匹配项",
        "category": "regex",
        "subcategory": "find",
        "api_endpoint": "/api/regex_find",
        "method": "POST",
        "params": [
            {"name": "pattern", "type": "string", "required": True, "description": "正则模式"},
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "search"
    },
    "regex_replace": {
        "id": "regex_replace",
        "name": "正则替换",
        "name_en": "Regex Replace",
        "description": "替换匹配的文本",
        "category": "regex",
        "subcategory": "replace",
        "api_endpoint": "/api/regex_replace",
        "method": "POST",
        "params": [
            {"name": "pattern", "type": "string", "required": True, "description": "正则模式"},
            {"name": "replacement", "type": "string", "required": True, "description": "替换文本"},
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "edit"
    },
    "regex_split": {
        "id": "regex_split",
        "name": "正则分割",
        "name_en": "Regex Split",
        "description": "用正则分割文本",
        "category": "regex",
        "subcategory": "split",
        "api_endpoint": "/api/regex_split",
        "method": "POST",
        "params": [
            {"name": "pattern", "type": "string", "required": True, "description": "正则模式"},
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "scissors"
    },
    "regex_groups": {
        "id": "regex_groups",
        "name": "正则捕获组",
        "name_en": "Regex Groups",
        "description": "获取捕获组",
        "category": "regex",
        "subcategory": "groups",
        "api_endpoint": "/api/regex_groups",
        "method": "POST",
        "params": [
            {"name": "pattern", "type": "string", "required": True, "description": "正则模式"},
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "list"
    },
    "is_email": {
        "id": "is_email",
        "name": "邮箱格式检查",
        "name_en": "Is Email",
        "description": "检查是否为邮箱格式",
        "category": "regex",
        "subcategory": "validate",
        "api_endpoint": "/api/is_email",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "check"
    },
    "is_url": {
        "id": "is_url",
        "name": "URL格式检查",
        "name_en": "Is URL",
        "description": "检查是否为URL格式",
        "category": "regex",
        "subcategory": "validate",
        "api_endpoint": "/api/is_url",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "check"
    },
    "is_phone": {
        "id": "is_phone",
        "name": "电话格式检查",
        "name_en": "Is Phone",
        "description": "检查是否为电话号码格式",
        "category": "regex",
        "subcategory": "validate",
        "api_endpoint": "/api/is_phone",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "check"
    },

    # ========== 压缩工具 ==========
    "compress_gzip": {
        "id": "compress_gzip",
        "name": "Gzip压缩",
        "name_en": "Gzip Compress",
        "description": "使用Gzip压缩数据",
        "category": "compression",
        "subcategory": "gzip",
        "api_endpoint": "/api/compress_gzip",
        "method": "POST",
        "params": [
            {"name": "data", "type": "string", "required": True, "description": "数据"}
        ],
        "icon": "archive"
    },
    "decompress_gzip": {
        "id": "decompress_gzip",
        "name": "Gzip解压",
        "name_en": "Gzip Decompress",
        "description": "解压Gzip数据",
        "category": "compression",
        "subcategory": "gzip",
        "api_endpoint": "/api/decompress_gzip",
        "method": "POST",
        "params": [
            {"name": "data", "type": "string", "required": True, "description": "压缩数据"}
        ],
        "icon": "archive"
    },
    "compress_zlib": {
        "id": "compress_zlib",
        "name": "Zlib压缩",
        "name_en": "Zlib Compress",
        "description": "使用Zlib压缩数据",
        "category": "compression",
        "subcategory": "zlib",
        "api_endpoint": "/api/compress_zlib",
        "method": "POST",
        "params": [
            {"name": "data", "type": "string", "required": True, "description": "数据"}
        ],
        "icon": "archive"
    },
    "decompress_zlib": {
        "id": "decompress_zlib",
        "name": "Zlib解压",
        "name_en": "Zlib Decompress",
        "description": "解压Zlib数据",
        "category": "compression",
        "subcategory": "zlib",
        "api_endpoint": "/api/decompress_zlib",
        "method": "POST",
        "params": [
            {"name": "data", "type": "string", "required": True, "description": "压缩数据"}
        ],
        "icon": "archive"
    },
    "compress_bz2": {
        "id": "compress_bz2",
        "name": "BZ2压缩",
        "name_en": "BZ2 Compress",
        "description": "使用BZ2压缩数据",
        "category": "compression",
        "subcategory": "bz2",
        "api_endpoint": "/api/compress_bz2",
        "method": "POST",
        "params": [
            {"name": "data", "type": "string", "required": True, "description": "数据"}
        ],
        "icon": "archive"
    },
    "decompress_bz2": {
        "id": "decompress_bz2",
        "name": "BZ2解压",
        "name_en": "BZ2 Decompress",
        "description": "解压BZ2数据",
        "category": "compression",
        "subcategory": "bz2",
        "api_endpoint": "/api/decompress_bz2",
        "method": "POST",
        "params": [
            {"name": "data", "type": "string", "required": True, "description": "压缩数据"}
        ],
        "icon": "archive"
    },
    "compress_lzma": {
        "id": "compress_lzma",
        "name": "LZMA压缩",
        "name_en": "LZMA Compress",
        "description": "使用LZMA压缩数据",
        "category": "compression",
        "subcategory": "lzma",
        "api_endpoint": "/api/compress_lzma",
        "method": "POST",
        "params": [
            {"name": "data", "type": "string", "required": True, "description": "数据"}
        ],
        "icon": "archive"
    },
    "decompress_lzma": {
        "id": "decompress_lzma",
        "name": "LZMA解压",
        "name_en": "LZMA Decompress",
        "description": "解压LZMA数据",
        "category": "compression",
        "subcategory": "lzma",
        "api_endpoint": "/api/decompress_lzma",
        "method": "POST",
        "params": [
            {"name": "data", "type": "string", "required": True, "description": "压缩数据"}
        ],
        "icon": "archive"
    },

    # ========== 国际化工具 ==========
    "detect_language": {
        "id": "detect_language",
        "name": "语言检测",
        "name_en": "Detect Language",
        "description": "检测文本语言",
        "category": "i18n",
        "subcategory": "detect",
        "api_endpoint": "/api/detect_language",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "globe"
    },
    "translate": {
        "id": "translate",
        "name": "文本翻译",
        "name_en": "Translate",
        "description": "翻译文本",
        "category": "i18n",
        "subcategory": "translate",
        "api_endpoint": "/api/translate",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"},
            {"name": "from_lang", "type": "string", "required": False, "description": "源语言"},
            {"name": "to_lang", "type": "string", "required": True, "description": "目标语言"}
        ],
        "icon": "globe"
    },
    "to_pinyin": {
        "id": "to_pinyin",
        "name": "转拼音",
        "name_en": "To Pinyin",
        "description": "将中文转换为拼音",
        "category": "i18n",
        "subcategory": "pinyin",
        "api_endpoint": "/api/to_pinyin",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "中文文本"}
        ],
        "icon": "type"
    },
    "to_traditional": {
        "id": "to_traditional",
        "name": "转繁体",
        "name_en": "To Traditional",
        "description": "将简体中文转换为繁体中文",
        "category": "i18n",
        "subcategory": "chinese",
        "api_endpoint": "/api/to_traditional",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "简体中文"}
        ],
        "icon": "type"
    },
    "to_simplified": {
        "id": "to_simplified",
        "name": "转简体",
        "name_en": "To Simplified",
        "description": "将繁体中文转换为简体中文",
        "category": "i18n",
        "subcategory": "chinese",
        "api_endpoint": "/api/to_simplified",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "繁体中文"}
        ],
        "icon": "type"
    },
    "locale_format": {
        "id": "locale_format",
        "name": "本地化格式化",
        "name_en": "Locale Format",
        "description": "根据区域格式化数字和日期",
        "category": "i18n",
        "subcategory": "format",
        "api_endpoint": "/api/locale_format",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "值"},
            {"name": "locale", "type": "string", "required": False, "description": "区域", "default": "en_US"}
        ],
        "icon": "globe"
    },

    # ========== 国际化工具 ==========
    "word_count": {
        "id": "word_count",
        "name": "字数统计",
        "name_en": "Word Count",
        "description": "统计文本字数",
        "category": "text",
        "subcategory": "count",
        "api_endpoint": "/api/word_count",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "hash"
    },
    "char_count": {
        "id": "char_count",
        "name": "字符数统计",
        "name_en": "Character Count",
        "description": "统计文本字符数",
        "category": "text",
        "subcategory": "count",
        "api_endpoint": "/api/char_count",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "hash"
    },
    "line_count": {
        "id": "line_count",
        "name": "行数统计",
        "name_en": "Line Count",
        "description": "统计文本行数",
        "category": "text",
        "subcategory": "count",
        "api_endpoint": "/api/line_count",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "hash"
    },
    "paragraph_count": {
        "id": "paragraph_count",
        "name": "段落数统计",
        "name_en": "Paragraph Count",
        "description": "统计文本段落数",
        "category": "text",
        "subcategory": "count",
        "api_endpoint": "/api/paragraph_count",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "hash"
    },
    "sentence_count": {
        "id": "sentence_count",
        "name": "句子数统计",
        "name_en": "Sentence Count",
        "description": "统计文本句子数",
        "category": "text",
        "subcategory": "count",
        "api_endpoint": "/api/sentence_count",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "hash"
    },
    "unique_words": {
        "id": "unique_words",
        "name": "去重词统计",
        "name_en": "Unique Words",
        "description": "统计不重复词数",
        "category": "text",
        "subcategory": "count",
        "api_endpoint": "/api/unique_words",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "hash"
    },
    "avg_word_length": {
        "id": "avg_word_length",
        "name": "平均词长",
        "name_en": "Average Word Length",
        "description": "计算平均词长度",
        "category": "text",
        "subcategory": "analysis",
        "api_endpoint": "/api/avg_word_length",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "percent"
    },
    "avg_sentence_length": {
        "id": "avg_sentence_length",
        "name": "平均句长",
        "name_en": "Average Sentence Length",
        "description": "计算平均句子长度",
        "category": "text",
        "subcategory": "analysis",
        "api_endpoint": "/api/avg_sentence_length",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "percent"
    },
    "readability_score": {
        "id": "readability_score",
        "name": "可读性评分",
        "name_en": "Readability Score",
        "description": "计算文本可读性评分",
        "category": "text",
        "subcategory": "analysis",
        "api_endpoint": "/api/readability_score",
        "method": "POST",
        "params": [
            {"name": "text", "type": "string", "required": True, "description": "文本"}
        ],
        "icon": "percent"
    },

    # ========== 调试工具 ==========
    "debug_print": {
        "id": "debug_print",
        "name": "调试打印",
        "name_en": "Debug Print",
        "description": "打印调试信息",
        "category": "debug",
        "subcategory": "print",
        "api_endpoint": "/api/debug_print",
        "method": "POST",
        "params": [
            {"name": "data", "type": "any", "required": True, "description": "数据"}
        ],
        "icon": "terminal"
    },
    "debug_var": {
        "id": "debug_var",
        "name": "变量检查",
        "name_en": "Debug Variable",
        "description": "检查变量类型和值",
        "category": "debug",
        "subcategory": "inspect",
        "api_endpoint": "/api/debug_var",
        "method": "POST",
        "params": [
            {"name": "name", "type": "string", "required": True, "description": "变量名"},
            {"name": "value", "type": "any", "required": True, "description": "变量值"}
        ],
        "icon": "search"
    },
    "debug_trace": {
        "id": "debug_trace",
        "name": "调用追踪",
        "name_en": "Trace Calls",
        "description": "追踪函数调用",
        "category": "debug",
        "subcategory": "trace",
        "api_endpoint": "/api/debug_trace",
        "method": "POST",
        "params": [
            {"name": "func", "type": "function", "required": True, "description": "函数"}
        ],
        "icon": "git-branch"
    },
    "debug_time": {
        "id": "debug_time",
        "name": "时间测量",
        "name_en": "Time Measure",
        "description": "测量代码执行时间",
        "category": "debug",
        "subcategory": "time",
        "api_endpoint": "/api/debug_time",
        "method": "POST",
        "params": [
            {"name": "func", "type": "function", "required": True, "description": "函数"}
        ],
        "icon": "clock"
    },
    "debug_memory": {
        "id": "debug_memory",
        "name": "内存检查",
        "name_en": "Memory Check",
        "description": "检查内存使用",
        "category": "debug",
        "subcategory": "memory",
        "api_endpoint": "/api/debug_memory",
        "method": "POST",
        "params": [],
        "icon": "database"
    },
    "breakpoint": {
        "id": "breakpoint",
        "name": "断点",
        "name_en": "Breakpoint",
        "description": "设置断点",
        "category": "debug",
        "subcategory": "breakpoint",
        "api_endpoint": "/api/breakpoint",
        "method": "POST",
        "params": [],
        "icon": "stop-circle"
    },

    # ========== 断言工具 ==========
    "assert_true": {
        "id": "assert_true",
        "name": "断言为真",
        "name_en": "Assert True",
        "description": "断言条件为真",
        "category": "assert",
        "subcategory": "boolean",
        "api_endpoint": "/api/assert_true",
        "method": "POST",
        "params": [
            {"name": "condition", "type": "boolean", "required": True, "description": "条件"},
            {"name": "message", "type": "string", "required": False, "description": "失败消息"}
        ],
        "icon": "check"
    },
    "assert_false": {
        "id": "assert_false",
        "name": "断言为假",
        "name_en": "Assert False",
        "description": "断言条件为假",
        "category": "assert",
        "subcategory": "boolean",
        "api_endpoint": "/api/assert_false",
        "method": "POST",
        "params": [
            {"name": "condition", "type": "boolean", "required": True, "description": "条件"},
            {"name": "message", "type": "string", "required": False, "description": "失败消息"}
        ],
        "icon": "check"
    },
    "assert_equal": {
        "id": "assert_equal",
        "name": "断言相等",
        "name_en": "Assert Equal",
        "description": "断言两个值相等",
        "category": "assert",
        "subcategory": "comparison",
        "api_endpoint": "/api/assert_equal",
        "method": "POST",
        "params": [
            {"name": "actual", "type": "any", "required": True, "description": "实际值"},
            {"name": "expected", "type": "any", "required": True, "description": "期望值"},
            {"name": "message", "type": "string", "required": False, "description": "失败消息"}
        ],
        "icon": "check"
    },
    "assert_not_equal": {
        "id": "assert_not_equal",
        "name": "断言不相等",
        "name_en": "Assert Not Equal",
        "description": "断言两个值不相等",
        "category": "assert",
        "subcategory": "comparison",
        "api_endpoint": "/api/assert_not_equal",
        "method": "POST",
        "params": [
            {"name": "actual", "type": "any", "required": True, "description": "实际值"},
            {"name": "expected", "type": "any", "required": True, "description": "期望值"},
            {"name": "message", "type": "string", "required": False, "description": "失败消息"}
        ],
        "icon": "check"
    },
    "assert_null": {
        "id": "assert_null",
        "name": "断言为空",
        "name_en": "Assert Null",
        "description": "断言值为空",
        "category": "assert",
        "subcategory": "null",
        "api_endpoint": "/api/assert_null",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "值"},
            {"name": "message", "type": "string", "required": False, "description": "失败消息"}
        ],
        "icon": "check"
    },
    "assert_not_null": {
        "id": "assert_not_null",
        "name": "断言非空",
        "name_en": "Assert Not Null",
        "description": "断言值非空",
        "category": "assert",
        "subcategory": "null",
        "api_endpoint": "/api/assert_not_null",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "值"},
            {"name": "message", "type": "string", "required": False, "description": "失败消息"}
        ],
        "icon": "check"
    },
    "assert_type": {
        "id": "assert_type",
        "name": "断言类型",
        "name_en": "Assert Type",
        "description": "断言值类型",
        "category": "assert",
        "subcategory": "type",
        "api_endpoint": "/api/assert_type",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "值"},
            {"name": "expected_type", "type": "string", "required": True, "description": "期望类型"},
            {"name": "message", "type": "string", "required": False, "description": "失败消息"}
        ],
        "icon": "check"
    },
    "assert_contains": {
        "id": "assert_contains",
        "name": "断言包含",
        "name_en": "Assert Contains",
        "description": "断言包含某值",
        "category": "assert",
        "subcategory": "contains",
        "api_endpoint": "/api/assert_contains",
        "method": "POST",
        "params": [
            {"name": "container", "type": "any", "required": True, "description": "容器"},
            {"name": "value", "type": "any", "required": True, "description": "值"},
            {"name": "message", "type": "string", "required": False, "description": "失败消息"}
        ],
        "icon": "check"
    },

    # ========== 测试工具 ==========
    "test_suite": {
        "id": "test_suite",
        "name": "测试套件",
        "name_en": "Test Suite",
        "description": "创建测试套件",
        "category": "test",
        "subcategory": "suite",
        "api_endpoint": "/api/test_suite",
        "method": "POST",
        "params": [
            {"name": "name", "type": "string", "required": True, "description": "名称"}
        ],
        "icon": "package"
    },
    "test_case": {
        "id": "test_case",
        "name": "测试用例",
        "name_en": "Test Case",
        "description": "创建测试用例",
        "category": "test",
        "subcategory": "case",
        "api_endpoint": "/api/test_case",
        "method": "POST",
        "params": [
            {"name": "name", "type": "string", "required": True, "description": "名称"},
            {"name": "func", "type": "function", "required": True, "description": "测试函数"}
        ],
        "icon": "file"
    },
    "run_tests": {
        "id": "run_tests",
        "name": "运行测试",
        "name_en": "Run Tests",
        "description": "运行所有测试",
        "category": "test",
        "subcategory": "run",
        "api_endpoint": "/api/run_tests",
        "method": "POST",
        "params": [],
        "icon": "play"
    },
    "test_report": {
        "id": "test_report",
        "name": "测试报告",
        "name_en": "Test Report",
        "description": "生成测试报告",
        "category": "test",
        "subcategory": "report",
        "api_endpoint": "/api/test_report",
        "method": "POST",
        "params": [],
        "icon": "file-text"
    },

    # ========== 异步工具 ==========
    "async_delay": {
        "id": "async_delay",
        "name": "异步延迟",
        "name_en": "Async Delay",
        "description": "异步延迟执行",
        "category": "async",
        "subcategory": "delay",
        "api_endpoint": "/api/async_delay",
        "method": "POST",
        "params": [
            {"name": "ms", "type": "number", "required": True, "description": "毫秒"}
        ],
        "icon": "clock"
    },
    "async_timeout": {
        "id": "async_timeout",
        "name": "异步超时",
        "name_en": "Async Timeout",
        "description": "设置异步操作超时",
        "category": "async",
        "subcategory": "timeout",
        "api_endpoint": "/api/async_timeout",
        "method": "POST",
        "params": [
            {"name": "func", "type": "function", "required": True, "description": "函数"},
            {"name": "ms", "type": "number", "required": True, "description": "超时毫秒"}
        ],
        "icon": "clock"
    },
    "async_retry": {
        "id": "async_retry",
        "name": "异步重试",
        "name_en": "Async Retry",
        "description": "异步重试操作",
        "category": "async",
        "subcategory": "retry",
        "api_endpoint": "/api/async_retry",
        "method": "POST",
        "params": [
            {"name": "func", "type": "function", "required": True, "description": "函数"},
            {"name": "max_attempts", "type": "number", "required": False, "description": "最大尝试次数", "default": 3}
        ],
        "icon": "refresh-cw"
    },
    "async_parallel": {
        "id": "async_parallel",
        "name": "并行执行",
        "name_en": "Async Parallel",
        "description": "并行执行多个异步函数",
        "category": "async",
        "subcategory": "parallel",
        "api_endpoint": "/api/async_parallel",
        "method": "POST",
        "params": [
            {"name": "funcs", "type": "array", "required": True, "description": "函数数组"}
        ],
        "icon": "layers"
    },
    "async_sequence": {
        "id": "async_sequence",
        "name": "顺序执行",
        "name_en": "Async Sequence",
        "description": "顺序执行多个异步函数",
        "category": "async",
        "subcategory": "sequence",
        "api_endpoint": "/api/async_sequence",
        "method": "POST",
        "params": [
            {"name": "funcs", "type": "array", "required": True, "description": "函数数组"}
        ],
        "icon": "list"
    },
    "async_waterfall": {
        "id": "async_waterfall",
        "name": "瀑布流",
        "name_en": "Async Waterfall",
        "description": "瀑布流执行，每个结果传递给下一个",
        "category": "async",
        "subcategory": "waterfall",
        "api_endpoint": "/api/async_waterfall",
        "method": "POST",
        "params": [
            {"name": "funcs", "type": "array", "required": True, "description": "函数数组"},
            {"name": "initial", "type": "any", "required": False, "description": "初始值"}
        ],
        "icon": "arrow-down"
    },
    "async_whilst": {
        "id": "async_whilst",
        "name": "异步循环条件",
        "name_en": "Async Whilst",
        "description": "当条件为真时重复执行",
        "category": "async",
        "subcategory": "loop",
        "api_endpoint": "/api/async_whilst",
        "method": "POST",
        "params": [
            {"name": "condition", "type": "function", "required": True, "description": "条件函数"},
            {"name": "func", "type": "function", "required": True, "description": "执行函数"}
        ],
        "icon": "repeat"
    },
    "async_until": {
        "id": "async_until",
        "name": "异步直到条件",
        "name_en": "Async Until",
        "description": "直到条件为真时重复执行",
        "category": "async",
        "subcategory": "loop",
        "api_endpoint": "/api/async_until",
        "method": "POST",
        "params": [
            {"name": "condition", "type": "function", "required": True, "description": "条件函数"},
            {"name": "func", "type": "function", "required": True, "description": "执行函数"}
        ],
        "icon": "repeat"
    },

    # ========== 日志工具 ==========
    "log_debug": {
        "id": "log_debug",
        "name": "调试日志",
        "name_en": "Debug Log",
        "description": "记录调试级别日志",
        "category": "log",
        "subcategory": "debug",
        "api_endpoint": "/api/log_debug",
        "method": "POST",
        "params": [
            {"name": "message", "type": "string", "required": True, "description": "消息"}
        ],
        "icon": "info"
    },
    "log_info": {
        "id": "log_info",
        "name": "信息日志",
        "name_en": "Info Log",
        "description": "记录信息级别日志",
        "category": "log",
        "subcategory": "info",
        "api_endpoint": "/api/log_info",
        "method": "POST",
        "params": [
            {"name": "message", "type": "string", "required": True, "description": "消息"}
        ],
        "icon": "info"
    },
    "log_warn": {
        "id": "log_warn",
        "name": "警告日志",
        "name_en": "Warn Log",
        "description": "记录警告级别日志",
        "category": "log",
        "subcategory": "warn",
        "api_endpoint": "/api/log_warn",
        "method": "POST",
        "params": [
            {"name": "message", "type": "string", "required": True, "description": "消息"}
        ],
        "icon": "alert-triangle"
    },
    "log_error": {
        "id": "log_error",
        "name": "错误日志",
        "name_en": "Error Log",
        "description": "记录错误级别日志",
        "category": "log",
        "subcategory": "error",
        "api_endpoint": "/api/log_error",
        "method": "POST",
        "params": [
            {"name": "message", "type": "string", "required": True, "description": "消息"}
        ],
        "icon": "alert-circle"
    },
    "log_fatal": {
        "id": "log_fatal",
        "name": "致命日志",
        "name_en": "Fatal Log",
        "description": "记录致命级别日志",
        "category": "log",
        "subcategory": "fatal",
        "api_endpoint": "/api/log_fatal",
        "method": "POST",
        "params": [
            {"name": "message", "type": "string", "required": True, "description": "消息"}
        ],
        "icon": "alert-octagon"
    },
    "log_get_level": {
        "id": "log_get_level",
        "name": "获取日志级别",
        "name_en": "Get Log Level",
        "description": "获取当前日志级别",
        "category": "log",
        "subcategory": "config",
        "api_endpoint": "/api/log_get_level",
        "method": "POST",
        "params": [],
        "icon": "settings"
    },
    "log_set_level": {
        "id": "log_set_level",
        "name": "设置日志级别",
        "name_en": "Set Log Level",
        "description": "设置日志级别",
        "category": "log",
        "subcategory": "config",
        "api_endpoint": "/api/log_set_level",
        "method": "POST",
        "params": [
            {"name": "level", "type": "string", "required": True, "description": "级别"}
        ],
        "icon": "settings"
    },
    "log_format": {
        "id": "log_format",
        "name": "日志格式化",
        "name_en": "Log Format",
        "description": "格式化日志消息",
        "category": "log",
        "subcategory": "format",
        "api_endpoint": "/api/log_format",
        "method": "POST",
        "params": [
            {"name": "level", "type": "string", "required": True, "description": "级别"},
            {"name": "message", "type": "string", "required": True, "description": "消息"},
            {"name": "context", "type": "object", "required": False, "description": "上下文"}
        ],
        "icon": "file-text"
    },

    # ========== 事件工具 ==========
    "event_on": {
        "id": "event_on",
        "name": "监听事件",
        "name_en": "Event On",
        "description": "注册事件监听器",
        "category": "event",
        "subcategory": "listen",
        "api_endpoint": "/api/event_on",
        "method": "POST",
        "params": [
            {"name": "event", "type": "string", "required": True, "description": "事件名"},
            {"name": "handler", "type": "function", "required": True, "description": "处理函数"}
        ],
        "icon": "bell"
    },
    "event_off": {
        "id": "event_off",
        "name": "取消监听",
        "name_en": "Event Off",
        "description": "取消事件监听器",
        "category": "event",
        "subcategory": "listen",
        "api_endpoint": "/api/event_off",
        "method": "POST",
        "params": [
            {"name": "event", "type": "string", "required": True, "description": "事件名"},
            {"name": "handler", "type": "function", "required": True, "description": "处理函数"}
        ],
        "icon": "bell-off"
    },
    "event_emit": {
        "id": "event_emit",
        "name": "触发事件",
        "name_en": "Event Emit",
        "description": "触发事件",
        "category": "event",
        "subcategory": "emit",
        "api_endpoint": "/api/event_emit",
        "method": "POST",
        "params": [
            {"name": "event", "type": "string", "required": True, "description": "事件名"},
            {"name": "data", "type": "any", "required": False, "description": "数据"}
        ],
        "icon": "radio"
    },
    "event_once": {
        "id": "event_once",
        "name": "单次监听",
        "name_en": "Event Once",
        "description": "注册单次事件监听器",
        "category": "event",
        "subcategory": "listen",
        "api_endpoint": "/api/event_once",
        "method": "POST",
        "params": [
            {"name": "event", "type": "string", "required": True, "description": "事件名"},
            {"name": "handler", "type": "function", "required": True, "description": "处理函数"}
        ],
        "icon": "bell"
    },
    "event_clear": {
        "id": "event_clear",
        "name": "清除事件",
        "name_en": "Event Clear",
        "description": "清除事件监听器",
        "category": "event",
        "subcategory": "clear",
        "api_endpoint": "/api/event_clear",
        "method": "POST",
        "params": [
            {"name": "event", "type": "string", "required": False, "description": "事件名"}
        ],
        "icon": "trash-2"
    },

    # ========== 缓存工具 ==========
    "cache_set": {
        "id": "cache_set",
        "name": "缓存设置",
        "name_en": "Cache Set",
        "description": "设置缓存值",
        "category": "cache",
        "subcategory": "set",
        "api_endpoint": "/api/cache_set",
        "method": "POST",
        "params": [
            {"name": "key", "type": "string", "required": True, "description": "键"},
            {"name": "value", "type": "any", "required": True, "description": "值"},
            {"name": "ttl", "type": "number", "required": False, "description": "过期秒数"}
        ],
        "icon": "database"
    },
    "cache_get": {
        "id": "cache_get",
        "name": "缓存获取",
        "name_en": "Cache Get",
        "description": "获取缓存值",
        "category": "cache",
        "subcategory": "get",
        "api_endpoint": "/api/cache_get",
        "method": "POST",
        "params": [
            {"name": "key", "type": "string", "required": True, "description": "键"}
        ],
        "icon": "database"
    },
    "cache_has": {
        "id": "cache_has",
        "name": "缓存存在",
        "name_en": "Cache Has",
        "description": "检查缓存是否存在",
        "category": "cache",
        "subcategory": "has",
        "api_endpoint": "/api/cache_has",
        "method": "POST",
        "params": [
            {"name": "key", "type": "string", "required": True, "description": "键"}
        ],
        "icon": "check"
    },
    "cache_delete": {
        "id": "cache_delete",
        "name": "缓存删除",
        "name_en": "Cache Delete",
        "description": "删除缓存",
        "category": "cache",
        "subcategory": "delete",
        "api_endpoint": "/api/cache_delete",
        "method": "POST",
        "params": [
            {"name": "key", "type": "string", "required": True, "description": "键"}
        ],
        "icon": "trash-2"
    },
    "cache_clear": {
        "id": "cache_clear",
        "name": "缓存清空",
        "name_en": "Cache Clear",
        "description": "清空所有缓存",
        "category": "cache",
        "subcategory": "clear",
        "api_endpoint": "/api/cache_clear",
        "method": "POST",
        "params": [],
        "icon": "trash"
    },
    "cache_keys": {
        "id": "cache_keys",
        "name": "缓存键列表",
        "name_en": "Cache Keys",
        "description": "获取所有缓存键",
        "category": "cache",
        "subcategory": "keys",
        "api_endpoint": "/api/cache_keys",
        "method": "POST",
        "params": [],
        "icon": "list"
    },
    "cache_ttl": {
        "id": "cache_ttl",
        "name": "缓存TTL",
        "name_en": "Cache TTL",
        "description": "获取缓存剩余生存时间",
        "category": "cache",
        "subcategory": "ttl",
        "api_endpoint": "/api/cache_ttl",
        "method": "POST",
        "params": [
            {"name": "key", "type": "string", "required": True, "description": "键"}
        ],
        "icon": "clock"
    },

    # ========== 流控工具 ==========
    "rate_limit": {
        "id": "rate_limit",
        "name": "限流",
        "name_en": "Rate Limit",
        "description": "限制调用频率",
        "category": "rate_limiter",
        "subcategory": "limit",
        "api_endpoint": "/api/rate_limit",
        "method": "POST",
        "params": [
            {"name": "key", "type": "string", "required": True, "description": "键"},
            {"name": "max_calls", "type": "number", "required": True, "description": "最大调用数"},
            {"name": "window", "type": "number", "required": True, "description": "时间窗口秒数"}
        ],
        "icon": "zap"
    },
    "rate_check": {
        "id": "rate_check",
        "name": "限流检查",
        "name_en": "Rate Check",
        "description": "检查是否超过限制",
        "category": "rate_limiter",
        "subcategory": "check",
        "api_endpoint": "/api/rate_check",
        "method": "POST",
        "params": [
            {"name": "key", "type": "string", "required": True, "description": "键"}
        ],
        "icon": "check"
    },
    "rate_reset": {
        "id": "rate_reset",
        "name": "限流重置",
        "name_en": "Rate Reset",
        "description": "重置限流计数器",
        "category": "rate_limiter",
        "subcategory": "reset",
        "api_endpoint": "/api/rate_reset",
        "method": "POST",
        "params": [
            {"name": "key", "type": "string", "required": True, "description": "键"}
        ],
        "icon": "refresh-cw"
    },

    # ========== 批处理工具 ==========
    "batch_process": {
        "id": "batch_process",
        "name": "批量处理",
        "name_en": "Batch Process",
        "description": "批量处理数据",
        "category": "batch",
        "subcategory": "process",
        "api_endpoint": "/api/batch_process",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数据项"},
            {"name": "func", "type": "function", "required": True, "description": "处理函数"}
        ],
        "icon": "layers"
    },
    "batch_map": {
        "id": "batch_map",
        "name": "批量映射",
        "name_en": "Batch Map",
        "description": "批量映射数据",
        "category": "batch",
        "subcategory": "map",
        "api_endpoint": "/api/batch_map",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数据项"},
            {"name": "func", "type": "function", "required": True, "description": "映射函数"}
        ],
        "icon": "git-merge"
    },
    "batch_filter": {
        "id": "batch_filter",
        "name": "批量过滤",
        "name_en": "Batch Filter",
        "description": "批量过滤数据",
        "category": "batch",
        "subcategory": "filter",
        "api_endpoint": "/api/batch_filter",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数据项"},
            {"name": "func", "type": "function", "required": True, "description": "过滤函数"}
        ],
        "icon": "filter"
    },
    "batch_reduce": {
        "id": "batch_reduce",
        "name": "批量聚合",
        "name_en": "Batch Reduce",
        "description": "批量聚合数据",
        "category": "batch",
        "subcategory": "reduce",
        "api_endpoint": "/api/batch_reduce",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数据项"},
            {"name": "func", "type": "function", "required": True, "description": "聚合函数"},
            {"name": "initial", "type": "any", "required": False, "description": "初始值"}
        ],
        "icon": "sliders"
    },
    "batch_chunk": {
        "id": "batch_chunk",
        "name": "批量分块",
        "name_en": "Batch Chunk",
        "description": "将数据分块",
        "category": "batch",
        "subcategory": "chunk",
        "api_endpoint": "/api/batch_chunk",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "数据项"},
            {"name": "size", "type": "number", "required": True, "description": "块大小"}
        ],
        "icon": "grid"
    },
    "batch_flatten": {
        "id": "batch_flatten",
        "name": "批量扁平化",
        "name_en": "Batch Flatten",
        "description": "扁平化嵌套数组",
        "category": "batch",
        "subcategory": "flatten",
        "api_endpoint": "/api/batch_flatten",
        "method": "POST",
        "params": [
            {"name": "items", "type": "array", "required": True, "description": "嵌套数组"}
        ],
        "icon": "minimize-2"
    },
    "batch_zip": {
        "id": "batch_zip",
        "name": "批量合并",
        "name_en": "Batch Zip",
        "description": "合并多个数组",
        "category": "batch",
        "subcategory": "zip",
        "api_endpoint": "/api/batch_zip",
        "method": "POST",
        "params": [
            {"name": "arrays", "type": "array", "required": True, "description": "数组列表"}
        ],
        "icon": "git-merge"
    },

    # ========== 管道工具 ==========
    "pipe": {
        "id": "pipe",
        "name": "管道",
        "name_en": "Pipe",
        "description": "将函数串联成管道",
        "category": "pipe",
        "subcategory": "pipe",
        "api_endpoint": "/api/pipe",
        "method": "POST",
        "params": [
            {"name": "funcs", "type": "array", "required": True, "description": "函数数组"},
            {"name": "value", "type": "any", "required": True, "description": "初始值"}
        ],
        "icon": "git-merge"
    },
    "compose": {
        "id": "compose",
        "name": "组合函数",
        "name_en": "Compose",
        "description": "组合多个函数",
        "category": "pipe",
        "subcategory": "compose",
        "api_endpoint": "/api/compose",
        "method": "POST",
        "params": [
            {"name": "funcs", "type": "array", "required": True, "description": "函数数组"}
        ],
        "icon": "git-merge"
    },
    "trace": {
        "id": "trace",
        "name": "追踪调用",
        "name_en": "Trace",
        "description": "追踪函数调用过程",
        "category": "pipe",
        "subcategory": "trace",
        "api_endpoint": "/api/trace",
        "method": "POST",
        "params": [
            {"name": "func", "type": "function", "required": True, "description": "函数"},
            {"name": "value", "type": "any", "required": True, "description": "值"}
        ],
        "icon": "git-branch"
    },
    "tap": {
        "id": "tap",
        "name": "分支处理",
        "name_en": "Tap",
        "description": "在管道中插入副作用",
        "category": "pipe",
        "subcategory": "tap",
        "api_endpoint": "/api/tap",
        "method": "POST",
        "params": [
            {"name": "func", "type": "function", "required": True, "description": "函数"},
            {"name": "value", "type": "any", "required": True, "description": "值"}
        ],
        "icon": "git-branch"
    },

    # ========== 异常处理工具 ==========
    "try_catch": {
        "id": "try_catch",
        "name": "尝试捕获",
        "name_en": "Try Catch",
        "description": "捕获异常",
        "category": "exception",
        "subcategory": "try",
        "api_endpoint": "/api/try_catch",
        "method": "POST",
        "params": [
            {"name": "func", "type": "function", "required": True, "description": "函数"},
            {"name": "catch", "type": "function", "required": False, "description": "捕获函数"}
        ],
        "icon": "shield"
    },
    "throw": {
        "id": "throw",
        "name": "抛出异常",
        "name_en": "Throw",
        "description": "抛出异常",
        "category": "exception",
        "subcategory": "throw",
        "api_endpoint": "/api/throw",
        "method": "POST",
        "params": [
            {"name": "message", "type": "string", "required": True, "description": "错误消息"}
        ],
        "icon": "alert-triangle"
    },
    "is_error": {
        "id": "is_error",
        "name": "是否为错误",
        "name_en": "Is Error",
        "description": "检查是否为错误对象",
        "category": "exception",
        "subcategory": "check",
        "api_endpoint": "/api/is_error",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "值"}
        ],
        "icon": "check"
    },
    "error_message": {
        "id": "error_message",
        "name": "错误消息",
        "name_en": "Error Message",
        "description": "获取错误消息",
        "category": "exception",
        "subcategory": "message",
        "api_endpoint": "/api/error_message",
        "method": "POST",
        "params": [
            {"name": "error", "type": "any", "required": True, "description": "错误对象"}
        ],
        "icon": "message-circle"
    },
    "error_stack": {
        "id": "error_stack",
        "name": "错误堆栈",
        "name_en": "Error Stack",
        "description": "获取错误堆栈",
        "category": "exception",
        "subcategory": "stack",
        "api_endpoint": "/api/error_stack",
        "method": "POST",
        "params": [
            {"name": "error", "type": "any", "required": True, "description": "错误对象"}
        ],
        "icon": "list"
    },

    # ========== 反射工具 ==========
    "typeof": {
        "id": "typeof",
        "name": "类型查询",
        "name_en": "Type Of",
        "description": "获取值的类型",
        "category": "reflect",
        "subcategory": "type",
        "api_endpoint": "/api/typeof",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "值"}
        ],
        "icon": "tag"
    },
    "to_type": {
        "id": "to_type",
        "name": "类型转换",
        "name_en": "To Type",
        "description": "转换为指定类型",
        "category": "reflect",
        "subcategory": "convert",
        "api_endpoint": "/api/to_type",
        "method": "POST",
        "params": [
            {"name": "value", "type": "any", "required": True, "description": "值"},
            {"name": "type", "type": "string", "required": True, "description": "目标类型"}
        ],
        "icon": "refresh-cw"
    },
    "has_method": {
        "id": "has_method",
        "name": "是否有方法",
        "name_en": "Has Method",
        "description": "检查对象是否有某方法",
        "category": "reflect",
        "subcategory": "method",
        "api_endpoint": "/api/has_method",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "any", "required": True, "description": "对象"},
            {"name": "name", "type": "string", "required": True, "description": "方法名"}
        ],
        "icon": "check"
    },
    "get_methods": {
        "id": "get_methods",
        "name": "获取方法列表",
        "name_en": "Get Methods",
        "description": "获取对象的所有方法",
        "category": "reflect",
        "subcategory": "method",
        "api_endpoint": "/api/get_methods",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "any", "required": True, "description": "对象"}
        ],
        "icon": "list"
    },
    "get_properties": {
        "id": "get_properties",
        "name": "获取属性列表",
        "name_en": "Get Properties",
        "description": "获取对象的所有属性",
        "category": "reflect",
        "subcategory": "property",
        "api_endpoint": "/api/get_properties",
        "method": "POST",
        "params": [
            {"name": "obj", "type": "any", "required": True, "description": "对象"}
        ],
        "icon": "list"
    },

    # ========== 数据结构工具 ==========
    "tree_create": {
        "id": "tree_create",
        "name": "创建树",
        "name_en": "Create Tree",
        "description": "创建新的树结构",
        "category": "tree",
        "subcategory": "create",
        "api_endpoint": "/api/tree_create",
        "method": "POST",
        "params": [
            {"name": "root", "type": "any", "required": True, "description": "根节点值"}
        ],
        "icon": "git-branch"
    },
    "tree_insert": {
        "id": "tree_insert",
        "name": "插入节点",
        "name_en": "Insert Node",
        "description": "在树中插入节点",
        "category": "tree",
        "subcategory": "insert",
        "api_endpoint": "/api/tree_insert",
        "method": "POST",
        "params": [
            {"name": "tree", "type": "object", "required": True, "description": "树"},
            {"name": "value", "type": "any", "required": True, "description": "值"}
        ],
        "icon": "plus"
    },
    "tree_delete": {
        "id": "tree_delete",
        "name": "删除节点",
        "name_en": "Delete Node",
        "description": "从树中删除节点",
        "category": "tree",
        "subcategory": "delete",
        "api_endpoint": "/api/tree_delete",
        "method": "POST",
        "params": [
            {"name": "tree", "type": "object", "required": True, "description": "树"},
            {"name": "value", "type": "any", "required": True, "description": "值"}
        ],
        "icon": "trash-2"
    },
    "tree_search": {
        "id": "tree_search",
        "name": "搜索节点",
        "name_en": "Search Node",
        "description": "在树中搜索节点",
        "category": "tree",
        "subcategory": "search",
        "api_endpoint": "/api/tree_search",
        "method": "POST",
        "params": [
            {"name": "tree", "type": "object", "required": True, "description": "树"},
            {"name": "value", "type": "any", "required": True, "description": "值"}
        ],
        "icon": "search"
    },
    "tree_traverse": {
        "id": "tree_traverse",
        "name": "遍历树",
        "name_en": "Traverse Tree",
        "description": "遍历树节点",
        "category": "tree",
        "subcategory": "traverse",
        "api_endpoint": "/api/tree_traverse",
        "method": "POST",
        "params": [
            {"name": "tree", "type": "object", "required": True, "description": "树"},
            {"name": "order", "type": "string", "required": False, "description": "遍历顺序", "default": "inorder"}
        ],
        "icon": "git-branch"
    },
    "tree_height": {
        "id": "tree_height",
        "name": "树高度",
        "name_en": "Tree Height",
        "description": "计算树的高度",
        "category": "tree",
        "subcategory": "property",
        "api_endpoint": "/api/tree_height",
        "method": "POST",
        "params": [
            {"name": "tree", "type": "object", "required": True, "description": "树"}
        ],
        "icon": "maximize"
    },
    "tree_size": {
        "id": "tree_size",
        "name": "树大小",
        "name_en": "Tree Size",
        "description": "计算树的节点数",
        "category": "tree",
        "subcategory": "property",
        "api_endpoint": "/api/tree_size",
        "method": "POST",
        "params": [
            {"name": "tree", "type": "object", "required": True, "description": "树"}
        ],
        "icon": "hash"
    },
    "tree_flatten": {
        "id": "tree_flatten",
        "name": "树扁平化",
        "name_en": "Flatten Tree",
        "description": "将树扁平化为数组",
        "category": "tree",
        "subcategory": "flatten",
        "api_endpoint": "/api/tree_flatten",
        "method": "POST",
        "params": [
            {"name": "tree", "type": "object", "required": True, "description": "树"}
        ],
        "icon": "minimize-2"
    },

    # ========== 图工具 ==========
    "graph_create": {
        "id": "graph_create",
        "name": "创建图",
        "name_en": "Create Graph",
        "description": "创建新的图结构",
        "category": "graph",
        "subcategory": "create",
        "api_endpoint": "/api/graph_create",
        "method": "POST",
        "params": [
            {"name": "directed", "type": "boolean", "required": False, "description": "是否有向", "default": False}
        ],
        "icon": "git-branch"
    },
    "graph_add_node": {
        "id": "graph_add_node",
        "name": "添加节点",
        "name_en": "Add Node",
        "description": "在图中添加节点",
        "category": "graph",
        "subcategory": "node",
        "api_endpoint": "/api/graph_add_node",
        "method": "POST",
        "params": [
            {"name": "graph", "type": "object", "required": True, "description": "图"},
            {"name": "node", "type": "any", "required": True, "description": "节点"}
        ],
        "icon": "plus"
    },
    "graph_add_edge": {
        "id": "graph_add_edge",
        "name": "添加边",
        "name_en": "Add Edge",
        "description": "在图中添加边",
        "category": "graph",
        "subcategory": "edge",
        "api_endpoint": "/api/graph_add_edge",
        "method": "POST",
        "params": [
            {"name": "graph", "type": "object", "required": True, "description": "图"},
            {"name": "from", "type": "any", "required": True, "description": "起始节点"},
            {"name": "to", "type": "any", "required": True, "description": "目标节点"},
            {"name": "weight", "type": "number", "required": False, "description": "权重"}
        ],
        "icon": "git-merge"
    },
    "graph_remove_node": {
        "id": "graph_remove_node",
        "name": "移除节点",
        "name_en": "Remove Node",
        "description": "从图中移除节点",
        "category": "graph",
        "subcategory": "node",
        "api_endpoint": "/api/graph_remove_node",
        "method": "POST",
        "params": [
            {"name": "graph", "type": "object", "required": True, "description": "图"},
            {"name": "node", "type": "any", "required": True, "description": "节点"}
        ],
        "icon": "trash-2"
    },
    "graph_bfs": {
        "id": "graph_bfs",
        "name": "广度优先",
        "name_en": "BFS",
        "description": "广度优先搜索",
        "category": "graph",
        "subcategory": "traverse",
        "api_endpoint": "/api/graph_bfs",
        "method": "POST",
        "params": [
            {"name": "graph", "type": "object", "required": True, "description": "图"},
            {"name": "start", "type": "any", "required": True, "description": "起始节点"}
        ],
        "icon": "git-branch"
    },
    "graph_dfs": {
        "id": "graph_dfs",
        "name": "深度优先",
        "name_en": "DFS",
        "description": "深度优先搜索",
        "category": "graph",
        "subcategory": "traverse",
        "api_endpoint": "/api/graph_dfs",
        "method": "POST",
        "params": [
            {"name": "graph", "type": "object", "required": True, "description": "图"},
            {"name": "start", "type": "any", "required": True, "description": "起始节点"}
        ],
        "icon": "git-branch"
    },
    "graph_shortest_path": {
        "id": "graph_shortest_path",
        "name": "最短路径",
        "name_en": "Shortest Path",
        "description": "计算最短路径",
        "category": "graph",
        "subcategory": "path",
        "api_endpoint": "/api/graph_shortest_path",
        "method": "POST",
        "params": [
            {"name": "graph", "type": "object", "required": True, "description": "图"},
            {"name": "from", "type": "any", "required": True, "description": "起始节点"},
            {"name": "to", "type": "any", "required": True, "description": "目标节点"}
        ],
        "icon": "git-branch"
    },
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
