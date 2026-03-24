"use client"

import { useEffect, useRef } from "react"
import { motion } from "motion/react"

interface WaveformProps {
  isPlaying: boolean
  audioData?: number[]
  color?: string
}

export function Waveform({ isPlaying, audioData, color = "#2C3E50" }: WaveformProps) {
  const canvasRef = useRef<HTMLCanvasElement>(null)
  const animationRef = useRef<number>()

  useEffect(() => {
    const canvas = canvasRef.current
    if (!canvas) return

    const ctx = canvas.getContext("2d")
    if (!ctx) return

    const draw = () => {
      const width = canvas.width
      const height = canvas.height
      ctx.clearRect(0, 0, width, height)

      const bars = 40
      const barWidth = width / bars - 2

      for (let i = 0; i < bars; i++) {
        let barHeight: number

        if (audioData && audioData[i] !== undefined) {
          barHeight = audioData[i] * height
        } else {
          barHeight = isPlaying
            ? Math.random() * height * 0.8 + height * 0.1
            : height * 0.15
        }

        const x = i * (barWidth + 2) + 1
        const y = (height - barHeight) / 2

        ctx.fillStyle = isPlaying ? color : `${color}40`
        ctx.beginPath()
        ctx.roundRect(x, y, barWidth, barHeight, barWidth / 2)
        ctx.fill()
      }

      if (isPlaying) {
        animationRef.current = requestAnimationFrame(draw)
      }
    }

    if (isPlaying) {
      draw()
    } else {
      draw()
    }

    return () => {
      if (animationRef.current) {
        cancelAnimationFrame(animationRef.current)
      }
    }
  }, [isPlaying, audioData, color])

  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      className="flex items-center justify-center"
    >
      <canvas
        ref={canvasRef}
        width={200}
        height={40}
        className="w-full max-w-[200px] h-10"
      />
    </motion.div>
  )
}