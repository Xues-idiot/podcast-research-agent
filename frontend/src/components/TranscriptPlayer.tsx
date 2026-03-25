"use client"

import { useState, useEffect, useRef } from "react"
import { motion } from "motion/react"
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card"
import { Play, Pause, SkipBack, SkipForward, Copy, Check } from "lucide-react"

interface TranscriptPlayerProps {
  transcript: {
    text: string
    segments?: Array<{ start: number; end: number; text: string }>
    language?: string
  }
  /** 外部传入的时间戳（秒），用于跳转高亮 */
  highlightTimestamp?: number
  /** 跳转回调 */
  onTimestampClick?: (timestamp: number) => void
}

const PLAYBACK_SPEEDS = [0.5, 0.75, 1, 1.25, 1.5, 2]

export function TranscriptPlayer({ transcript, highlightTimestamp, onTimestampClick }: TranscriptPlayerProps) {
  const [isPlaying, setIsPlaying] = useState(false)
  const [currentSegment, setCurrentSegment] = useState(0)
  const [playbackSpeed, setPlaybackSpeed] = useState(1)
  const [copiedIndex, setCopiedIndex] = useState<number | null>(null)
  const segmentRefs = useRef<(HTMLDivElement | null)[]>([])

  const segments = transcript.segments || []

  // 当highlightTimestamp变化时，自动滚动到对应片段
  useEffect(() => {
    if (highlightTimestamp !== undefined && segments.length > 0) {
      const idx = segments.findIndex(
        seg => seg.start <= highlightTimestamp && seg.end >= highlightTimestamp
      )
      if (idx >= 0) {
        setCurrentSegment(idx)
        // 滚动到对应片段
        setTimeout(() => {
          segmentRefs.current[idx]?.scrollIntoView({ behavior: "smooth", block: "center" })
        }, 100)
      }
    }
  }, [highlightTimestamp, segments])

  const copyToClipboard = async (text: string, index: number) => {
    try {
      await navigator.clipboard.writeText(text)
      setCopiedIndex(index)
      setTimeout(() => setCopiedIndex(null), 2000)
    } catch (err) {
      console.error("Failed to copy:", err)
    }
  }

  const formatTime = (seconds: number) => {
    const mins = Math.floor(seconds / 60)
    const secs = Math.floor(seconds % 60)
    return `${mins}:${secs.toString().padStart(2, "0")}`
  }

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4, delay: 0.1 }}
    >
      <Card className="border-l-4 border-l-[#2C3E50]">
        <CardHeader>
          <CardTitle className="flex items-center justify-between">
            <span className="flex items-center gap-2">
              <span className="text-2xl">📝</span>
              转录文本
              {transcript.language && (
                <span className="px-2 py-0.5 text-xs rounded-full bg-[#2C3E50]/10 text-[#2C3E50]">
                  {transcript.language.toUpperCase()}
                </span>
              )}
            </span>
            <span className="text-sm font-normal text-[#2C3E50]/50">
              {segments.length > 0 ? `${segments.length} 段` : "全文"}
            </span>
          </CardTitle>
        </CardHeader>
        <CardContent>
          {/* 播放控制 */}
          {segments.length > 0 && (
            <div className="flex items-center gap-4 mb-4 p-3 bg-[#FAF8F5] rounded-lg">
              <button
                onClick={() => setCurrentSegment(Math.max(0, currentSegment - 1))}
                className="p-2 rounded-full hover:bg-[#2C3E50]/10 transition-colors"
              >
                <SkipBack className="w-4 h-4" />
              </button>

              <button
                onClick={() => setIsPlaying(!isPlaying)}
                className="p-3 rounded-full bg-[#2C3E50] text-white hover:bg-[#34495E] transition-colors"
              >
                {isPlaying ? (
                  <Pause className="w-5 h-5" />
                ) : (
                  <Play className="w-5 h-5" />
                )}
              </button>

              <button
                onClick={() => setCurrentSegment(Math.min(segments.length - 1, currentSegment + 1))}
                className="p-2 rounded-full hover:bg-[#2C3E50]/10 transition-colors"
              >
                <SkipForward className="w-4 h-4" />
              </button>

              <div className="flex-1 text-center text-sm text-[#2C3E50]/70">
                {segments[currentSegment] && (
                  <span>
                    {formatTime(segments[currentSegment].start)} - {formatTime(segments[currentSegment].end)}
                  </span>
                )}
              </div>

              {/* 播放速度控制 */}
              <select
                value={playbackSpeed}
                onChange={(e) => setPlaybackSpeed(Number(e.target.value))}
                className="px-2 py-1 text-sm rounded border border-[#2C3E50]/20 bg-white cursor-pointer"
              >
                {PLAYBACK_SPEEDS.map((speed) => (
                  <option key={speed} value={speed}>
                    {speed}x
                  </option>
                ))}
              </select>
            </div>
          )}

          {/* 文本内容 */}
          <div className="max-h-96 overflow-y-auto space-y-3">
            {segments.length > 0 ? (
              segments.map((segment, index) => (
                <motion.div
                  key={index}
                  ref={(el) => { segmentRefs.current[index] = el }}
                  initial={{ opacity: 0 }}
                  animate={{ opacity: currentSegment === index ? 1 : 0.6 }}
                  onClick={() => setCurrentSegment(index)}
                  className={`p-3 rounded-lg cursor-pointer transition-colors group ${
                    currentSegment === index
                      ? "bg-[#2C3E50]/10 border-l-2 border-[#2C3E50]"
                      : "hover:bg-[#FAF8F5]"
                  }`}
                >
                  <div className="flex items-start justify-between gap-2">
                    <div className="flex-1">
                      <span className="text-xs text-[#E67E22] font-mono mr-2">
                        {formatTime(segment.start)}
                      </span>
                      <span className="text-[#2C3E50]/80">{segment.text}</span>
                    </div>
                    <button
                      onClick={(e) => {
                        e.stopPropagation()
                        copyToClipboard(segment.text, index)
                      }}
                      className="p-1.5 rounded opacity-0 group-hover:opacity-100 hover:bg-[#2C3E50]/10 transition-all"
                      title="复制文本"
                    >
                      {copiedIndex === index ? (
                        <Check className="w-4 h-4 text-green-600" />
                      ) : (
                        <Copy className="w-4 h-4 text-[#2C3E50]/50" />
                      )}
                    </button>
                  </div>
                </motion.div>
              ))
            ) : (
              <p className="text-[#2C3E50]/80 leading-relaxed whitespace-pre-wrap">
                {transcript.text}
              </p>
            )}
          </div>
        </CardContent>
      </Card>
    </motion.div>
  )
}
