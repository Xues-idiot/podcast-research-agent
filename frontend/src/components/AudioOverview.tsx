"use client"

import { useState, useRef, useEffect } from "react"
import { motion } from "motion/react"
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card"
import { Play, Pause, Clock, User, Volume2, VolumeX } from "lucide-react"

interface AudioOverviewProps {
  audioOverview: {
    title: string
    script: string
    segments: Array<{
      speaker: string
      content: string
      duration_seconds: number
    }>
    total_duration_seconds: number
    style: string
    audio_url?: string
  }
}

export function AudioOverview({ audioOverview }: AudioOverviewProps) {
  const [isPlaying, setIsPlaying] = useState(false)
  const [isMuted, setIsMuted] = useState(false)
  const [currentSegment, setCurrentSegment] = useState(0)
  const audioRef = useRef<HTMLAudioElement | null>(null)

  const hasAudio = !!audioOverview.audio_url

  const formatDuration = (seconds: number) => {
    const mins = Math.floor(seconds / 60)
    const secs = seconds % 60
    return `${mins}:${secs.toString().padStart(2, "0")}`
  }

  const totalMins = Math.floor(audioOverview.total_duration_seconds / 60)

  useEffect(() => {
    if (audioRef.current) {
      audioRef.current.muted = isMuted
    }
  }, [isMuted])

  const togglePlay = () => {
    if (!audioRef.current) return
    if (isPlaying) {
      audioRef.current.pause()
    } else {
      audioRef.current.play()
    }
    setIsPlaying(!isPlaying)
  }

  const handleEnded = () => {
    setIsPlaying(false)
    setCurrentSegment(0)
  }

  const handleTimeUpdate = () => {
    if (!audioRef.current) return
    const currentTime = audioRef.current.currentTime
    const totalDuration = audioOverview.total_duration_seconds
    const segmentIndex = Math.floor((currentTime / totalDuration) * audioOverview.segments.length)
    setCurrentSegment(Math.min(segmentIndex, audioOverview.segments.length - 1))
  }

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4, delay: 0.6 }}
    >
      <Card className="border-l-4 border-l-[#9B59B6]">
        <CardHeader>
          <CardTitle className="flex items-center justify-between">
            <span className="flex items-center gap-2">
              <span className="text-2xl">🎙</span>
              AI播客讨论
              <span className="px-2 py-0.5 text-xs rounded-full bg-[#9B59B6]/10 text-[#9B59B6]">
                {audioOverview.style === "deep_dive" ? "深入讨论" :
                 audioOverview.style === "brief" ? "简短总结" :
                 audioOverview.style === "critique" ? "评论分析" : "辩论"}
              </span>
            </span>
            <div className="flex items-center gap-2 text-sm text-[#2C3E50]/50">
              <Clock className="w-4 h-4" />
              约{totalMins}分钟
            </div>
          </CardTitle>
        </CardHeader>
        <CardContent>
          {/* 标题 */}
          <h3 className="text-lg font-semibold text-[#2C3E50] mb-4">
            {audioOverview.title}
          </h3>

          {/* 音频播放控制 */}
          {hasAudio && (
            <div className="flex items-center gap-3 p-3 bg-[#9B59B6]/5 rounded-lg mb-4">
              <audio
                ref={audioRef}
                src={audioOverview.audio_url}
                onEnded={handleEnded}
                onTimeUpdate={handleTimeUpdate}
              />
              <button
                onClick={togglePlay}
                className="p-2 rounded-full bg-[#9B59B6] text-white hover:bg-[#8E44AD] transition-colors"
              >
                {isPlaying ? (
                  <Pause className="w-5 h-5" />
                ) : (
                  <Play className="w-5 h-5" />
                )}
              </button>
              <div className="flex-1">
                <p className="text-sm font-medium text-[#2C3E50]">
                  {isPlaying ? "正在播放..." : "点击播放AI播客"}
                </p>
                <p className="text-xs text-[#2C3E50]/50">
                  {audioOverview.segments[currentSegment]?.speaker} · {audioOverview.segments[currentSegment]?.content?.slice(0, 30)}...
                </p>
              </div>
              <button
                onClick={() => setIsMuted(!isMuted)}
                className="p-2 rounded-full hover:bg-[#9B59B6]/10 transition-colors"
              >
                {isMuted ? (
                  <VolumeX className="w-5 h-5 text-[#9B59B6]" />
                ) : (
                  <Volume2 className="w-5 h-5 text-[#9B59B6]" />
                )}
              </button>
            </div>
          )}

          {!hasAudio && (
            <div className="flex items-center gap-3 p-3 bg-[#9B59B6]/5 rounded-lg mb-4">
              <div className="p-2 rounded-full bg-[#9B59B6]/10">
                <Play className="w-5 h-5 text-[#9B59B6]" />
              </div>
              <div className="flex-1">
                <p className="text-sm font-medium text-[#2C3E50]">即将支持TTS播放</p>
                <p className="text-xs text-[#2C3E50]/50">当前显示脚本内容</p>
              </div>
            </div>
          )}

          {/* 对话片段 */}
          <div className="space-y-3 max-h-96 overflow-y-auto">
            {audioOverview.segments.map((segment, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, x: -10 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: index * 0.1 }}
                className={`flex gap-3 p-3 rounded-lg ${
                  segment.speaker === "Host A"
                    ? "bg-[#2C3E50]/5"
                    : "bg-[#E67E22]/5"
                }`}
              >
                <div className={`flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center ${
                  segment.speaker === "Host A"
                    ? "bg-[#2C3E50]/10"
                    : "bg-[#E67E22]/10"
                }`}>
                  <User className={`w-4 h-4 ${
                    segment.speaker === "Host A"
                      ? "text-[#2C3E50]"
                      : "text-[#E67E22]"
                  }`} />
                </div>
                <div className="flex-1">
                  <div className="flex items-center justify-between mb-1">
                    <span className={`text-sm font-medium ${
                      segment.speaker === "Host A"
                        ? "text-[#2C3E50]"
                        : "text-[#E67E22]"
                    }`}>
                      {segment.speaker}
                    </span>
                    <span className="text-xs text-[#2C3E50]/40">
                      {formatDuration(segment.duration_seconds)}
                    </span>
                  </div>
                  <p className="text-sm text-[#2C3E50]/80 leading-relaxed">
                    {segment.content}
                  </p>
                </div>
              </motion.div>
            ))}
          </div>
        </CardContent>
      </Card>
    </motion.div>
  )
}
