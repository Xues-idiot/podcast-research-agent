"use client"

import { motion } from "motion/react"
import { useEffect, useState } from "react"

interface VoiceAvatarProps {
  isPlaying: boolean
  size?: "sm" | "md" | "lg"
}

export function VoiceAvatar({ isPlaying, size = "md" }: VoiceAvatarProps) {
  const [pulseScale, setPulseScale] = useState(1)

  useEffect(() => {
    if (!isPlaying) {
      setPulseScale(1)
      return
    }

    const interval = setInterval(() => {
      setPulseScale((s) => (s === 1 ? 1.1 : 1))
    }, 500)

    return () => clearInterval(interval)
  }, [isPlaying])

  const sizeClasses = {
    sm: "w-8 h-8",
    md: "w-12 h-12",
    lg: "w-16 h-16",
  }

  const iconSizes = {
    sm: "w-4 h-4",
    md: "w-6 h-6",
    lg: "w-8 h-8",
  }

  return (
    <div className="relative flex items-center justify-center">
      {/* Pulse ring */}
      {isPlaying && (
        <motion.div
          className="absolute inset-0 rounded-full bg-[#E67E22]/20"
          animate={{
            scale: [1, 1.5, 1],
            opacity: [0.5, 0, 0.5],
          }}
          transition={{
            duration: 1.5,
            repeat: Infinity,
            ease: "easeInOut",
          }}
        />
      )}

      {/* Main avatar */}
      <motion.div
        className={`${sizeClasses[size]} rounded-full bg-gradient-to-br from-[#2C3E50] to-[#34495E] flex items-center justify-center shadow-lg`}
        animate={{
          scale: isPlaying ? pulseScale : 1,
        }}
        transition={{
          duration: 0.3,
        }}
      >
        {isPlaying ? (
          <motion.div
            className="flex items-center gap-0.5"
            animate={{ opacity: [1, 0.5, 1] }}
            transition={{ duration: 0.5, repeat: Infinity }}
          >
            <span className={`${iconSizes[size]} text-white font-bold`}>🎙</span>
          </motion.div>
        ) : (
          <span className={`${iconSizes[size]} text-white/70`}>🎧</span>
        )}
      </motion.div>

      {/* Status indicator */}
      <motion.div
        className="absolute -bottom-1 -right-1"
        initial={{ scale: 0 }}
        animate={{ scale: 1 }}
        transition={{ delay: 0.2 }}
      >
        <div
          className={`
            w-3 h-3 rounded-full border-2 border-white
            ${isPlaying ? "bg-green-500" : "bg-gray-400"}
          `}
        />
      </motion.div>
    </div>
  )
}