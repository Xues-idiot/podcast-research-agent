"use client"

import { useEffect, useState } from "react"
import { motion, AnimatePresence } from "motion/react"
import { checkHealth } from "@/lib/api"
import { Wifi, WifiOff } from "lucide-react"

export function ApiStatus() {
  const [connected, setConnected] = useState<boolean | null>(null)

  useEffect(() => {
    const check = async () => {
      const isConnected = await checkHealth()
      setConnected(isConnected)
    }

    check()
    const interval = setInterval(check, 30000) // 每30秒检查一次

    return () => clearInterval(interval)
  }, [])

  return (
    <motion.div
      initial={{ opacity: 0, y: -10 }}
      animate={{ opacity: 1, y: 0 }}
      className="flex items-center gap-2"
    >
      <AnimatePresence mode="wait">
        {connected === null ? (
          <motion.span
            key="loading"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="text-xs text-[#2C3E50]/50"
          >
            检测中...
          </motion.span>
        ) : connected ? (
          <motion.span
            key="connected"
            initial={{ opacity: 0, scale: 0.8 }}
            animate={{ opacity: 1, scale: 1 }}
            exit={{ opacity: 0 }}
            className="flex items-center gap-1 text-xs text-green-600"
          >
            <Wifi className="w-3 h-3" />
            API已连接
          </motion.span>
        ) : (
          <motion.span
            key="disconnected"
            initial={{ opacity: 0, scale: 0.8 }}
            animate={{ opacity: 1, scale: 1 }}
            exit={{ opacity: 0 }}
            className="flex items-center gap-1 text-xs text-red-500"
          >
            <WifiOff className="w-3 h-3" />
            API未连接
          </motion.span>
        )}
      </AnimatePresence>
    </motion.div>
  )
}
