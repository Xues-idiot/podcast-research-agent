"use client"

import { motion } from "motion/react"

interface PlatformBadgeProps {
  platform: string
  size?: "sm" | "md" | "lg"
}

const platformConfig: Record<string, { emoji: string; label: string; color: string }> = {
  bilibili: { emoji: "📺", label: "B站", color: "#00A1D6" },
  youtube: { emoji: "▶️", label: "YouTube", color: "#FF0000" },
  douyin: { emoji: "🎵", label: "抖音", color: "#000000" },
  wechat: { emoji: "💬", label: "微信", color: "#07C160" },
  xiaohongshu: { emoji: "📕", label: "小红书", color: "#FF2442" },
  rss: { emoji: "📻", label: "RSS", color: "#F26522" },
  unknown: { emoji: "🔗", label: "链接", color: "#666666" },
}

export function PlatformBadge({ platform, size = "md" }: PlatformBadgeProps) {
  const config = platformConfig[platform] || platformConfig.unknown

  const sizeClasses = {
    sm: "px-2 py-0.5 text-xs",
    md: "px-3 py-1 text-sm",
    lg: "px-4 py-1.5 text-base",
  }

  return (
    <motion.span
      initial={{ scale: 0.9, opacity: 0 }}
      animate={{ scale: 1, opacity: 1 }}
      transition={{ duration: 0.2 }}
      className={`inline-flex items-center gap-1 rounded-full font-medium ${sizeClasses[size]}`}
      style={{
        backgroundColor: `${config.color}15`,
        color: config.color,
      }}
    >
      <span>{config.emoji}</span>
      <span>{config.label}</span>
    </motion.span>
  )
}
