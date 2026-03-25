"use client"

import { useEffect, useState } from "react"
import { motion, AnimatePresence } from "motion/react"

export function ProgressBar() {
  const [loading, setLoading] = useState(false)
  const [progress, setProgress] = useState(0)
  const [mounted, setMounted] = useState(false)

  useEffect(() => {
    setMounted(true)

    // Listen for fetch events
    const handleFetchStart = () => {
      setLoading(true)
      setProgress(0)
    }

    const handleFetchEnd = () => {
      setProgress(100)
      setTimeout(() => {
        setLoading(false)
        setProgress(0)
      }, 200)
    }

    // Use XMLHttpRequest to intercept fetch
    const originalFetch = window.fetch
    window.fetch = async (...args) => {
      handleFetchStart()
      try {
        const response = await originalFetch(...args)
        handleFetchEnd()
        return response
      } catch (error) {
        handleFetchEnd()
        throw error
      }
    }

    // Simulate progress for streaming responses
    let progressInterval: NodeJS.Timeout | null = null
    const startProgress = () => {
      progressInterval = setInterval(() => {
        setProgress((prev) => {
          if (prev >= 90) return prev
          return prev + Math.random() * 10
        })
      }, 500)
    }

    const stopProgress = () => {
      if (progressInterval) {
        clearInterval(progressInterval)
        progressInterval = null
      }
    }

    return () => {
      window.fetch = originalFetch
      stopProgress()
    }
  }, [])

  if (!mounted) return null

  return (
    <AnimatePresence>
      {loading && (
        <motion.div
          initial={{ opacity: 0, y: -2 }}
          animate={{ opacity: 1, y: 0 }}
          exit={{ opacity: 0, y: -2 }}
          className="fixed top-0 left-0 right-0 z-50 h-1"
        >
          <div className="h-full bg-[#E67E22]/20">
            <motion.div
              className="h-full bg-[#E67E22]"
              initial={{ width: "0%" }}
              animate={{ width: `${progress}%` }}
              transition={{ duration: 0.3 }}
            />
          </div>
        </motion.div>
      )}
    </AnimatePresence>
  )
}
