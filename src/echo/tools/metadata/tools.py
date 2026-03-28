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
