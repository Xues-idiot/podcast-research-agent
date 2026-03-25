"use client"

import { useState } from "react"
import { motion } from "motion/react"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Search, Loader2, AlertCircle, Tv2, Youtube, Music, MessageSquare, BookMarked, Rss } from "lucide-react"
import { usePodcastStore } from "@/store/podcast-store"

interface URLInputProps {
  onSubmit: (url: string) => Promise<void>
}

const PLATFORM_PATTERNS = [
  { name: "B站", patterns: ["bilibili.com", "b23.tv"], icon: Tv2, color: "#FF6B9D" },
  { name: "YouTube", patterns: ["youtube.com", "youtu.be"], icon: Youtube, color: "#FF0000" },
  { name: "抖音", patterns: ["douyin.com", "huoshan.com"], icon: Music, color: "#000000" },
  { name: "喜马拉雅", patterns: ["ximalaya.com", "ting.room"], icon: MessageSquare, color: "#FF6B00" },
  { name: "小宇宙", patterns: ["xiaoyuzhou.app"], icon: BookMarked, color: "#4A90D9" },
  { name: "RSS", patterns: [".xml", ".rss", "feed"], icon: Rss, color: "#FF9900" },
]

function detectPlatform(url: string) {
  const lower = url.toLowerCase()
  for (const platform of PLATFORM_PATTERNS) {
    for (const pattern of platform.patterns) {
      if (lower.includes(pattern)) {
        return platform
      }
    }
  }
  return null
}

export function URLInput({ onSubmit }: URLInputProps) {
  const [loading, setLoading] = useState(false)
  const { url, setUrl, status } = usePodcastStore()

  const platform = url.trim() ? detectPlatform(url) : null
  const isUnknownPlatform = url.trim() && !platform

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!url.trim() || loading) return

    setLoading(true)
    try {
      await onSubmit(url)
    } finally {
      setLoading(false)
    }
  }

  const isLoading = loading || status === "loading"

  return (
    <motion.form
      onSubmit={handleSubmit}
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4 }}
      className="flex w-full max-w-2xl gap-3"
    >
      <div className="relative flex-1">
        <Search className="absolute left-4 top-1/2 h-5 w-5 -translate-y-1/2 text-[#2C3E50]/50 z-10" />
        <Input
          type="url"
          placeholder="输入B站/YouTube视频链接或播客RSS地址... (按 / 聚焦)"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          className="pl-12 h-12 text-base pr-24"
          disabled={isLoading}
        />
        {/* Platform badge */}
        {platform && (
          <motion.div
            initial={{ scale: 0.8, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            className="absolute right-3 top-1/2 -translate-y-1/2 flex items-center gap-1.5 px-2 py-1 rounded-full text-xs font-medium"
            style={{ backgroundColor: `${platform.color}20`, color: platform.color }}
          >
            <platform.icon className="w-3.5 h-3.5" />
            {platform.name}
          </motion.div>
        )}
        {isUnknownPlatform && (
          <div className="absolute -bottom-6 left-0 flex items-center gap-1 text-xs text-yellow-600">
            <AlertCircle className="w-3 h-3" />
            <span>未知平台，可能无法处理</span>
          </div>
        )}
      </div>
      <Button
        type="submit"
        size="lg"
        disabled={isLoading || !url.trim()}
        className="bg-[#E67E22] hover:bg-[#D35400]"
      >
        {isLoading ? (
          <>
            <Loader2 className="h-5 w-5 animate-spin" />
            研究中...
          </>
        ) : (
          <>
            <Search className="h-5 w-5" />
            开始研究
          </>
        )}
      </Button>
    </motion.form>
  )
}
