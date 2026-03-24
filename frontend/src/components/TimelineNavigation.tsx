"use client"

import { useState, useEffect } from "react"
import { motion, AnimatePresence } from "motion/react"
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Play, Pause, SkipBack, SkipForward, Clock, ChevronDown, ChevronUp } from "lucide-react"

interface TimelineEntry {
  timestamp: number
  formatted: string
  content: string
  entry_id: string
  type: string
  relevance: number
}

interface TimelineNavigationProps {
  podcastId: string
  totalDuration: number
  currentTime: number
  onSeek: (timestamp: number) => void
  onPlayPause: () => void
  isPlaying: boolean
  entries?: Array<{
    start_time: number
    end_time: number
    id: string
    compiled: string
    raw: string
  }>
  keypoints?: Array<{ id: number; content: string; importance: string }>
}

export function TimelineNavigation({
  podcastId,
  totalDuration,
  currentTime,
  onSeek,
  onPlayPause,
  isPlaying,
  entries = [],
  keypoints = [],
}: TimelineNavigationProps) {
  const [moments, setMoments] = useState<TimelineEntry[]>([])
  const [isExpanded, setIsExpanded] = useState(false)
  const [isLoading, setIsLoading] = useState(false)

  // 注册播客时间戳数据
  useEffect(() => {
    const registerEntries = async () => {
      if (!podcastId || entries.length === 0) return

      try {
        await fetch("/api/navigation/register", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            podcast_id: podcastId,
            entries: entries,
          }),
        })
      } catch (error) {
        console.error("Failed to register entries:", error)
      }
    }

    registerEntries()
  }, [podcastId, entries])

  // 获取关键时刻
  useEffect(() => {
    const fetchKeyMoments = async () => {
      if (!podcastId) return

      setIsLoading(true)
      try {
        const response = await fetch(`/api/navigation/moments/${podcastId}?num_moments=10`)
        if (response.ok) {
          const data = await response.json()
          setMoments(data.moments || [])
        }
      } catch (error) {
        console.error("Failed to fetch moments:", error)
      } finally {
        setIsLoading(false)
      }
    }

    fetchKeyMoments()
  }, [podcastId])

  const formatTime = (seconds: number): string => {
    if (seconds < 0) return "00:00"
    const hours = Math.floor(seconds / 3600)
    const minutes = Math.floor((seconds % 3600) / 60)
    const secs = Math.floor(seconds % 60)

    if (hours > 0) {
      return `${hours.toString().padStart(2, "0")}:${minutes.toString().padStart(2, "0")}:${secs.toString().padStart(2, "0")}`
    }
    return `${minutes.toString().padStart(2, "0")}:${secs.toString().padStart(2, "0")}`
  }

  const handleJumpToMoment = async (timestamp: number) => {
    try {
      // 调用后端跳转API获取上下文
      const response = await fetch("/api/navigation/jump", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          podcast_id: podcastId,
          timestamp: timestamp,
          window_seconds: 30.0,
        }),
      })

      if (response.ok) {
        const data = await response.json()
        // 触发跳转到该时间戳
        onSeek(data.target_timestamp)
      }
    } catch (error) {
      console.error("Jump failed:", error)
      // 即使API调用失败，也直接跳转
      onSeek(timestamp)
    }
  }

  const handleSkip = (seconds: number) => {
    const newTime = Math.max(0, Math.min(totalDuration, currentTime + seconds))
    onSeek(newTime)
  }

  const progress = totalDuration > 0 ? (currentTime / totalDuration) * 100 : 0

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4, delay: 0.3 }}
    >
      <Card className="border-l-4 border-l-[#3498DB]">
        <CardHeader>
          <CardTitle className="flex items-center justify-between">
            <span className="flex items-center gap-2">
              <Clock className="w-5 h-5 text-[#3498DB]" />
              时间戳导航
            </span>
            <Button
              variant="ghost"
              size="sm"
              onClick={() => setIsExpanded(!isExpanded)}
            >
              {isExpanded ? <ChevronUp className="w-4 h-4" /> : <ChevronDown className="w-4 h-4" />}
            </Button>
          </CardTitle>
        </CardHeader>

        <CardContent>
          {/* 播放控制条 */}
          <div className="space-y-3">
            {/* 进度条 */}
            <div className="relative">
              <div className="h-2 bg-[#ECF0F1] rounded-full overflow-hidden">
                <motion.div
                  className="h-full bg-[#3498DB] rounded-full"
                  initial={{ width: 0 }}
                  animate={{ width: `${progress}%` }}
                  transition={{ duration: 0.3 }}
                />
              </div>
              {/* 时间戳标记 */}
              <div className="absolute top-0 left-0 right-0 h-2 pointer-events-none">
                {moments.map((moment, idx) => (
                  <div
                    key={idx}
                    className="absolute top-1/2 -translate-y-1/2 w-1 h-3 bg-[#E67E22] rounded-full cursor-pointer hover:bg-[#D35400] hover:scale-125 transition-all"
                    style={{ left: `${(moment.timestamp / totalDuration) * 100}%` }}
                    title={formatTime(moment.timestamp)}
                    onClick={() => handleJumpToMoment(moment.timestamp)}
                  />
                ))}
              </div>
            </div>

            {/* 时间显示 */}
            <div className="flex justify-between text-sm text-[#7F8C8D]">
              <span>{formatTime(currentTime)}</span>
              <span>{formatTime(totalDuration)}</span>
            </div>

            {/* 播放控制按钮 */}
            <div className="flex items-center justify-center gap-3">
              <Button
                variant="ghost"
                size="sm"
                onClick={() => handleSkip(-10)}
                title="快退10秒"
              >
                <SkipBack className="w-4 h-4" />
              </Button>

              <Button
                variant="ghost"
                size="sm"
                onClick={() => handleSkip(-5)}
                title="快退5秒"
              >
                <SkipBack className="w-3 h-3" />
              </Button>

              <Button
                onClick={onPlayPause}
                className="bg-[#3498DB] hover:bg-[#2980B9] text-white rounded-full w-12 h-12 flex items-center justify-center"
              >
                {isPlaying ? <Pause className="w-5 h-5" /> : <Play className="w-5 h-5 ml-0.5" />}
              </Button>

              <Button
                variant="ghost"
                size="sm"
                onClick={() => handleSkip(5)}
                title="快进5秒"
              >
                <SkipForward className="w-3 h-3" />
              </Button>

              <Button
                variant="ghost"
                size="sm"
                onClick={() => handleSkip(10)}
                title="快进10秒"
              >
                <SkipForward className="w-4 h-4" />
              </Button>
            </div>
          </div>

          {/* 关键时刻列表 */}
          <AnimatePresence>
            {isExpanded && (
              <motion.div
                initial={{ height: 0, opacity: 0 }}
                animate={{ height: "auto", opacity: 1 }}
                exit={{ height: 0, opacity: 0 }}
                transition={{ duration: 0.3 }}
                className="overflow-hidden"
              >
                <div className="mt-4 pt-4 border-t border-[#ECF0F1]">
                  <h4 className="text-sm font-medium text-[#2C3E50] mb-3">关键时刻</h4>

                  {isLoading ? (
                    <div className="text-center text-[#7F8C8D] py-4">加载中...</div>
                  ) : moments.length === 0 ? (
                    <div className="text-center text-[#7F8C8D] py-4">暂无关键时刻</div>
                  ) : (
                    <div className="space-y-2 max-h-60 overflow-y-auto">
                      {moments.map((moment, idx) => (
                        <motion.div
                          key={idx}
                          initial={{ opacity: 0, x: -10 }}
                          animate={{ opacity: 1, x: 0 }}
                          transition={{ delay: idx * 0.05 }}
                          className={`flex items-start gap-3 p-2 rounded-lg cursor-pointer hover:bg-[#F8F9FA] transition-colors ${
                            Math.abs(currentTime - moment.timestamp) < 5 ? "bg-[#EBF5FB] border border-[#3498DB]" : ""
                          }`}
                          onClick={() => handleJumpToMoment(moment.timestamp)}
                        >
                          <span className="flex-shrink-0 text-[#E67E22] font-mono text-sm bg-[#FEF5E7] px-2 py-0.5 rounded">
                            {moment.formatted}
                          </span>
                          <p className="text-sm text-[#2C3E50] line-clamp-2 flex-1">
                            {moment.content}
                          </p>
                          <span className={`flex-shrink-0 text-xs px-1.5 py-0.5 rounded ${
                            moment.type === "keypoint" ? "bg-[#E8F8F5] text-[#1ABC9C]" :
                            moment.type === "qa" ? "bg-[#EBF5FB] text-[#3498DB]" :
                            "bg-[#F5EEF8] text-[#9B59B6]"
                          }`}>
                            {moment.type}
                          </span>
                        </motion.div>
                      ))}
                    </div>
                  )}
                </div>
              </motion.div>
            )}
          </AnimatePresence>
        </CardContent>
      </Card>
    </motion.div>
  )
}
