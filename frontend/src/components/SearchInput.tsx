"use client"

import { useState, useCallback } from "react"
import { motion, AnimatePresence } from "motion/react"
import { Search, X } from "lucide-react"

interface SearchResult {
  segmentIndex: number
  text: string
  start: number
  end: number
}

interface SearchInputProps {
  transcript?: {
    text: string
    segments?: Array<{ start: number; end: number; text: string }>
  }
  onResultClick?: (segmentIndex: number) => void
}

export function SearchInput({ transcript, onResultClick }: SearchInputProps) {
  const [query, setQuery] = useState("")
  const [results, setResults] = useState<SearchResult[]>([])

  const handleSearch = useCallback(
    (searchQuery: string) => {
      setQuery(searchQuery)

      if (!searchQuery.trim() || !transcript?.segments) {
        setResults([])
        return
      }

      const lowerQuery = searchQuery.toLowerCase()
      const found = transcript.segments
        .map((seg, index) => ({ segmentIndex: index, ...seg }))
        .filter((seg) => seg.text.toLowerCase().includes(lowerQuery))

      setResults(found)
    },
    [transcript]
  )

  const clearSearch = () => {
    setQuery("")
    setResults([])
  }

  const formatTime = (seconds: number) => {
    const mins = Math.floor(seconds / 60)
    const secs = Math.floor(seconds % 60)
    return `${mins}:${secs.toString().padStart(2, "0")}`
  }

  const escapeRegex = (str: string) => {
    return str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')
  }

  const highlightText = (text: string, query: string) => {
    if (!query) return text
    const parts = text.split(new RegExp(`(${escapeRegex(query)})`, 'gi'))
    return parts.map((part, i) =>
      part.toLowerCase() === query.toLowerCase()
        ? <mark key={i} className="bg-[#E67E22]/20 text-[#E67E22]">{part}</mark>
        : part
    )
  }

  return (
    <div className="relative">
      <div className="relative">
        <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-[#2C3E50]/40" />
        <input
          type="text"
          value={query}
          onChange={(e) => handleSearch(e.target.value)}
          placeholder="在转录文本中搜索..."
          className="w-full pl-10 pr-10 py-2.5 rounded-lg border border-[#2C3E50]/20 focus:border-[#2C3E50] focus:ring-2 focus:ring-[#2C3E50]/10 outline-none transition-all text-sm text-[#2C3E50] placeholder:text-[#2C3E50]/40"
        />
        {query && (
          <button
            onClick={clearSearch}
            className="absolute right-3 top-1/2 -translate-y-1/2 p-0.5 hover:bg-[#2C3E50]/10 rounded"
          >
            <X className="w-4 h-4 text-[#2C3E50]/40" />
          </button>
        )}
      </div>

      <AnimatePresence>
        {results.length > 0 && (
          <motion.div
            initial={{ opacity: 0, y: -10 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -10 }}
            className="absolute top-full left-0 right-0 mt-2 bg-white rounded-lg shadow-lg border border-[#2C3E50]/10 max-h-64 overflow-y-auto z-50"
          >
            <div className="p-2 text-xs text-[#2C3E50]/50 border-b border-[#2C3E50]/10">
              找到 {results.length} 个匹配
            </div>
            {results.map((result, index) => (
              <button
                key={index}
                onClick={() => {
                  onResultClick?.(result.segmentIndex)
                  clearSearch()
                }}
                className="w-full p-3 text-left hover:bg-[#FAF8F5] transition-colors border-b border-[#2C3E50]/5 last:border-b-0"
              >
                <div className="flex items-center gap-2 mb-1">
                  <span className="text-xs font-mono text-[#E67E22]">
                    {formatTime(result.start)}
                  </span>
                </div>
                <p className="text-sm text-[#2C3E50]/80 line-clamp-2">
                  {highlightText(result.text, query)}
                </p>
              </button>
            ))}
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  )
}