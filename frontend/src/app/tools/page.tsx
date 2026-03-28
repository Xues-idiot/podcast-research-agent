"use client"

import { useState, useEffect } from "react"
import { motion, AnimatePresence } from "motion/react"
import { Search, X, ChevronRight, Loader2 } from "lucide-react"
import { toolsApi, ToolCategory, Tool } from "@/lib/tools-api"

const ICON_MAP: Record<string, string> = {
  mic: "🎙️",
  calculator: "🧮",
  database: "🗄️",
  "refresh-cw": "🔄",
  "check-circle": "✅",
  calendar: "📅",
  folder: "📁",
  code: "💻",
  shuffle: "🎲",
  hash: "#️⃣",
  link: "🔗",
  lock: "🔒",
  mail: "📧",
  phone: "📞",
  "credit-card": "💳",
  globe: "🌍",
  clock: "🕐",
  "hard-drive": "💾",
  file: "📋",
  "file-text": "📄",
  search: "🔍",
  "bar-chart": "📊",
  percent: "📈",
  check: "✔️",
  list: "📋",
  book: "📖",
  circle: "⭕",
  "share-2": "🔗",
  "help-circle": "❓",
  scissors: "✂️",
  tag: "🏷️",
  eraser: "🧹",
  "bar-chart-2": "📊",
  star: "⭐"
}

function getIcon(iconName: string): string {
  return ICON_MAP[iconName] || "🔧"
}

export default function ToolsPage() {
  const [categories, setCategories] = useState<ToolCategory[]>([])
  const [selectedCategory, setSelectedCategory] = useState<string | null>(null)
  const [tools, setTools] = useState<Tool[]>([])
  const [selectedTool, setSelectedTool] = useState<Tool | null>(null)
  const [searchQuery, setSearchQuery] = useState("")
  const [loading, setLoading] = useState(true)
  const [searchResults, setSearchResults] = useState<Tool[]>([])
  const [isSearching, setIsSearching] = useState(false)

  useEffect(() => {
    loadCategories()
  }, [])

  useEffect(() => {
    if (searchQuery.trim()) {
      handleSearch()
    } else {
      setSearchResults([])
      setIsSearching(false)
    }
  }, [searchQuery])

  async function loadCategories() {
    try {
      const data = await toolsApi.getCategories()
      setCategories(data.categories || [])
    } catch (error) {
      console.error("Failed to load categories:", error)
    } finally {
      setLoading(false)
    }
  }

  async function loadCategoryTools(categoryId: string) {
    try {
      const data = await toolsApi.getCategoryTools(categoryId)
      setTools(data.tools || [])
    } catch (error) {
      console.error("Failed to load tools:", error)
    }
  }

  async function handleSearch() {
    if (!searchQuery.trim()) return
    setIsSearching(true)
    try {
      const data = await toolsApi.searchTools(searchQuery)
      setSearchResults(data.results || [])
    } catch (error) {
      console.error("Failed to search tools:", error)
    } finally {
      setIsSearching(false)
    }
  }

  function handleCategoryClick(categoryId: string) {
    setSelectedCategory(categoryId)
    setSelectedTool(null)
    loadCategoryTools(categoryId)
  }

  function handleBackToCategories() {
    setSelectedCategory(null)
    setTools([])
    setSelectedTool(null)
  }

  const displayTools = searchQuery.trim() ? searchResults : tools

  return (
    <div className="min-h-screen bg-[#FAF8F5]">
      {/* Header */}
      <header className="bg-white border-b border-[#2C3E50]/10 sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-6 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-4">
              <button
                onClick={() => window.location.href = '/'}
                className="text-[#2C3E50] hover:text-[#E67E22] transition-colors"
              >
                <span className="text-2xl font-bold">Echo</span>
              </button>
              <span className="text-[#2C3E50]/40">|</span>
              <h1 className="text-xl font-semibold text-[#2C3E50]">工具中心</h1>
            </div>
            <nav className="flex items-center gap-6">
              <a href="/podcast" className="text-[#2C3E50]/70 hover:text-[#E67E22] transition-colors">
                研究
              </a>
              <a href="/knowledge" className="text-[#2C3E50]/70 hover:text-[#E67E22] transition-colors">
                知识库
              </a>
              <a href="/tools" className="text-[#E67E22] font-medium">
                工具中心
              </a>
            </nav>
          </div>
        </div>
      </header>

      {/* Search Bar */}
      <div className="max-w-7xl mx-auto px-6 py-8">
        <div className="relative">
          <Search className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-[#2C3E50]/40" />
          <input
            type="text"
            placeholder="搜索工具..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="w-full pl-12 pr-4 py-3 bg-white border border-[#2C3E50]/10 rounded-xl text-[#2C3E50] placeholder-[#2C3E50]/40 focus:outline-none focus:border-[#E67E22] focus:ring-2 focus:ring-[#E67E22]/20 transition-all"
          />
          {searchQuery && (
            <button
              onClick={() => setSearchQuery("")}
              className="absolute right-4 top-1/2 -translate-y-1/2 text-[#2C3E50]/40 hover:text-[#2C3E50] transition-colors"
            >
              <X className="w-5 h-5" />
            </button>
          )}
        </div>
      </div>

      {/* Main Content */}
      <div className="max-w-7xl mx-auto px-6 pb-12">
        {loading ? (
          <div className="flex items-center justify-center py-20">
            <Loader2 className="w-8 h-8 text-[#E67E22] animate-spin" />
          </div>
        ) : (
          <AnimatePresence mode="wait">
            {/* Search Results */}
            {searchQuery.trim() ? (
              <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                exit={{ opacity: 0 }}
                className="space-y-6"
              >
                <div className="flex items-center justify-between">
                  <h2 className="text-lg font-medium text-[#2C3E50]">
                    搜索结果 ({searchResults.length})
                  </h2>
                  <button
                    onClick={() => setSearchQuery("")}
                    className="text-sm text-[#E67E22] hover:underline"
                  >
                    清除搜索
                  </button>
                </div>
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
                  {isSearching ? (
                    <div className="col-span-full flex items-center justify-center py-12">
                      <Loader2 className="w-6 h-6 text-[#E67E22] animate-spin" />
                    </div>
                  ) : searchResults.length === 0 ? (
                    <p className="col-span-full text-center text-[#2C3E50]/60 py-12">
                      未找到相关工具
                    </p>
                  ) : (
                    searchResults.map((tool) => (
                      <ToolCard
                        key={tool.id}
                        tool={tool}
                        onClick={() => setSelectedTool(tool)}
                      />
                    ))
                  )}
                </div>
              </motion.div>
            ) : selectedCategory ? (
              /* Category Tools View */
              <motion.div
                key="category-view"
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -20 }}
              >
                <div className="flex items-center gap-2 mb-6">
                  <button
                    onClick={handleBackToCategories}
                    className="text-[#E67E22] hover:underline text-sm"
                  >
                    全部分类
                  </button>
                  <ChevronRight className="w-4 h-4 text-[#2C3E50]/40" />
                  <span className="text-[#2C3E50] font-medium">
                    {categories.find(c => c.id === selectedCategory)?.name}
                  </span>
                </div>
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
                  {tools.map((tool) => (
                    <ToolCard
                      key={tool.id}
                      tool={tool}
                      onClick={() => setSelectedTool(tool)}
                    />
                  ))}
                </div>
              </motion.div>
            ) : (
              /* Categories Grid View */
              <motion.div
                key="categories-view"
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                exit={{ opacity: 0 }}
              >
                <h2 className="text-lg font-medium text-[#2C3E50] mb-6">
                  全部分类
                </h2>
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
                  {categories.map((category) => (
                    <CategoryCard
                      key={category.id}
                      category={category}
                      onClick={() => handleCategoryClick(category.id)}
                    />
                  ))}
                </div>
              </motion.div>
            )}
          </AnimatePresence>
        )}
      </div>

      {/* Tool Detail Modal */}
      <AnimatePresence>
        {selectedTool && (
          <ToolDetailModal
            tool={selectedTool}
            onClose={() => setSelectedTool(null)}
          />
        )}
      </AnimatePresence>
    </div>
  )
}

function CategoryCard({
  category,
  onClick
}: {
  category: ToolCategory
  onClick: () => void
}) {
  return (
    <motion.button
      whileHover={{ y: -4, shadow: "0 10px 40px rgba(0,0,0,0.1)" }}
      whileTap={{ scale: 0.98 }}
      onClick={onClick}
      className="bg-white rounded-2xl p-6 text-left border border-[#2C3E50]/10 hover:border-[#E67E22]/30 transition-all group"
    >
      <div
        className="w-12 h-12 rounded-xl flex items-center justify-center text-2xl mb-4"
        style={{ backgroundColor: `${category.color}15` }}
      >
        {getIcon(category.icon)}
      </div>
      <h3 className="text-[#2C3E50] font-semibold mb-1">{category.name}</h3>
      <p className="text-[#2C3E50]/60 text-sm mb-3">{category.description}</p>
      <div className="flex items-center justify-between">
        <span className="text-[#E67E22] font-medium">{category.tool_count}+</span>
        <span className="text-[#2C3E50]/40 text-sm group-hover:text-[#E67E22] transition-colors">
          查看 →
        </span>
      </div>
    </motion.button>
  )
}

function ToolCard({
  tool,
  onClick
}: {
  tool: Tool
  onClick: () => void
}) {
  return (
    <motion.button
      whileHover={{ y: -4, shadow: "0 10px 40px rgba(0,0,0,0.1)" }}
      whileTap={{ scale: 0.98 }}
      onClick={onClick}
      className="bg-white rounded-2xl p-5 text-left border border-[#2C3E50]/10 hover:border-[#E67E22]/30 transition-all group"
    >
      <div className="flex items-start justify-between mb-3">
        <span className="text-2xl">{getIcon(tool.icon)}</span>
        <span className="text-xs text-[#2C3E50]/40 bg-[#2C3E50]/5 px-2 py-1 rounded">
          {tool.method}
        </span>
      </div>
      <h4 className="text-[#2C3E50] font-semibold mb-1">{tool.name}</h4>
      <p className="text-[#2C3E50]/60 text-sm line-clamp-2">{tool.description}</p>
    </motion.button>
  )
}

function ToolDetailModal({
  tool,
  onClose
}: {
  tool: Tool
  onClose: () => void
}) {
  const [params, setParams] = useState<Record<string, string>>({})
  const [result, setResult] = useState<any>(null)
  const [loading, setLoading] = useState(false)

  async function handleExecute() {
    setLoading(true)
    try {
      const data = await toolsApi.executeTool(tool.id, params)
      setResult(data)
    } catch (error) {
      console.error("Execute failed:", error)
    } finally {
      setLoading(false)
    }
  }

  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      className="fixed inset-0 bg-black/50 z-50 flex items-center justify-center p-6"
      onClick={onClose}
    >
      <motion.div
        initial={{ scale: 0.95, opacity: 0 }}
        animate={{ scale: 1, opacity: 1 }}
        exit={{ scale: 0.95, opacity: 0 }}
        onClick={(e) => e.stopPropagation()}
        className="bg-white rounded-2xl max-w-lg w-full max-h-[80vh] overflow-y-auto"
      >
        <div className="p-6 border-b border-[#2C3E50]/10">
          <div className="flex items-start justify-between">
            <div>
              <span className="text-3xl mb-2 block">{getIcon(tool.icon)}</span>
              <h3 className="text-xl font-semibold text-[#2C3E50]">{tool.name}</h3>
              <p className="text-[#2C3E50]/60 text-sm mt-1">{tool.name_en}</p>
            </div>
            <button
              onClick={onClose}
              className="text-[#2C3E50]/40 hover:text-[#2C3E50] transition-colors"
            >
              <X className="w-6 h-6" />
            </button>
          </div>
        </div>

        <div className="p-6 space-y-6">
          <p className="text-[#2C3E50]">{tool.description}</p>

          <div>
            <label className="block text-sm font-medium text-[#2C3E50] mb-2">
              API 端点
            </label>
            <code className="block bg-[#2C3E50]/5 text-[#2C3E50] px-3 py-2 rounded-lg text-sm">
              {tool.method} {tool.api_endpoint}
            </code>
          </div>

          {tool.params.length > 0 && (
            <div>
              <label className="block text-sm font-medium text-[#2C3E50] mb-3">
                参数
              </label>
              <div className="space-y-3">
                {tool.params.map((param) => (
                  <div key={param.name}>
                    <label className="block text-sm text-[#2C3E50]/70 mb-1">
                      {param.name}
                      {param.required && <span className="text-[#E67E22]"> *</span>}
                    </label>
                    <input
                      type={param.type === "number" ? "number" : "text"}
                      placeholder={param.description}
                      value={params[param.name] || ""}
                      onChange={(e) => setParams({ ...params, [param.name]: e.target.value })}
                      className="w-full px-3 py-2 bg-[#FAF8F5] border border-[#2C3E50]/10 rounded-lg text-[#2C3E50] placeholder-[#2C3E50]/40 focus:outline-none focus:border-[#E67E22] transition-all text-sm"
                    />
                  </div>
                ))}
              </div>
            </div>
          )}

          {result && (
            <div>
              <label className="block text-sm font-medium text-[#2C3E50] mb-2">
                执行结果
              </label>
              <pre className="bg-[#2C3E50]/5 text-[#2C3E50] px-3 py-2 rounded-lg text-sm overflow-auto max-h-40">
                {JSON.stringify(result, null, 2)}
              </pre>
            </div>
          )}
        </div>

        <div className="p-6 border-t border-[#2C3E50]/10">
          <button
            onClick={handleExecute}
            disabled={loading || tool.params.filter(p => p.required).length > 0}
            className="w-full py-3 bg-[#E67E22] hover:bg-[#d4721f] disabled:bg-[#2C3E50]/20 disabled:cursor-not-allowed text-white font-medium rounded-xl transition-colors flex items-center justify-center gap-2"
          >
            {loading && <Loader2 className="w-4 h-4 animate-spin" />}
            {loading ? "执行中..." : "执行工具"}
          </button>
        </div>
      </motion.div>
    </motion.div>
  )
}