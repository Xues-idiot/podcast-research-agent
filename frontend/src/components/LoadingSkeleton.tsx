"use client"

import { motion } from "motion/react"
import { Loader2 } from "lucide-react"

interface LoadingSkeletonProps {
  type?: "summary" | "keypoints" | "mindmap" | "full"
  stepHint?: string
}

export function LoadingSkeleton({ type = "full", stepHint }: LoadingSkeletonProps) {
  const shimmer = (
    <div className="relative overflow-hidden">
      <div
        className="absolute inset-0 -translate-x-full animate-[shimmer_1.5s_infinite]"
        style={{
          background: 'linear-gradient(90deg, transparent 0%, rgba(255,255,255,0.4) 50%, transparent 100%)',
        }}
      />
    </div>
  )

  const skeletonItem = (index: number, width = "w-full", height = "h-4") => (
    <motion.div
      key={index}
      initial={{ opacity: 0, x: -10 }}
      animate={{ opacity: 1, x: 0 }}
      transition={{ delay: index * 0.08 }}
      className={`${height} ${width} bg-gradient-to-r from-[#2C3E50]/10 via-[#2C3E50]/5 to-[#2C3E50]/10 rounded relative overflow-hidden`}
    >
      {shimmer}
    </motion.div>
  )

  if (type === "summary") {
    return (
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="bg-white rounded-xl p-6 border border-[#2C3E50]/10"
      >
        <div className="flex items-center gap-2 mb-4">
          <motion.div
            animate={{ rotate: 360 }}
            transition={{ duration: 2, repeat: Infinity, ease: "linear" }}
            className="w-6 h-6"
          >
            <Loader2 className="w-6 h-6 text-[#2C3E50]/40 animate-spin" />
          </motion.div>
          <div className="w-32 h-5 bg-[#2C3E50]/10 rounded animate-pulse relative overflow-hidden">
            {shimmer}
          </div>
        </div>
        <div className="space-y-3">
          {skeletonItem(0, "w-full")}
          {skeletonItem(1, "w-[95%]")}
          {skeletonItem(2, "w-[88%]")}
          {skeletonItem(3, "w-[92%]")}
          {skeletonItem(4, "w-[70%]")}
        </div>
      </motion.div>
    )
  }

  if (type === "keypoints") {
    return (
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="bg-white rounded-xl p-6 border border-[#2C3E50]/10"
      >
        <div className="flex items-center gap-2 mb-4">
          <motion.div
            animate={{ rotate: 360 }}
            transition={{ duration: 2, repeat: Infinity, ease: "linear" }}
            className="w-6 h-6"
          >
            <Loader2 className="w-6 h-6 text-[#E67E22]/40 animate-spin" />
          </motion.div>
          <div className="w-24 h-5 bg-[#E67E22]/10 rounded animate-pulse relative overflow-hidden">
            {shimmer}
          </div>
        </div>
        <div className="space-y-3">
          {[...Array(5)].map((_, i) => (
            <div key={i} className="flex items-start gap-3">
              <motion.div
                initial={{ scale: 0 }}
                animate={{ scale: 1 }}
                transition={{ delay: i * 0.1 }}
                className="w-5 h-5 bg-[#E67E22]/10 rounded-full animate-pulse relative overflow-hidden mt-0.5"
              >
                {shimmer}
              </motion.div>
              <div className="flex-1 space-y-2">
                {skeletonItem(i, "w-[80%]")}
                {skeletonItem(i + 5, "w-[60%]")}
              </div>
            </div>
          ))}
        </div>
      </motion.div>
    )
  }

  if (type === "mindmap") {
    return (
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="bg-white rounded-xl p-6 border border-[#2C3E50]/10"
      >
        <div className="flex items-center gap-2 mb-4">
          <motion.div
            animate={{ rotate: 360 }}
            transition={{ duration: 2, repeat: Infinity, ease: "linear" }}
            className="w-6 h-6"
          >
            <Loader2 className="w-6 h-6 text-[#2C3E50]/40 animate-spin" />
          </motion.div>
          <div className="w-28 h-5 bg-[#2C3E50]/10 rounded animate-pulse relative overflow-hidden">
            {shimmer}
          </div>
        </div>
        <div className="flex justify-center py-8">
          <motion.div
            animate={{ scale: [1, 1.1, 1] }}
            transition={{ duration: 2, repeat: Infinity }}
            className="w-32 h-32 bg-gradient-to-br from-[#2C3E50]/10 to-[#E67E22]/10 rounded-full flex items-center justify-center relative overflow-hidden"
          >
            {shimmer}
            <motion.div
              animate={{ opacity: [0.5, 1, 0.5] }}
              transition={{ duration: 1.5, repeat: Infinity }}
              className="w-16 h-16 bg-[#2C3E50]/20 rounded-full"
            />
          </motion.div>
        </div>
      </motion.div>
    )
  }

  // Full skeleton for entire page
  return (
    <div className="space-y-6">
      {stepHint && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          className="flex items-center justify-center gap-2 py-2 text-sm text-[#E67E22]"
        >
          <Loader2 className="w-4 h-4 animate-spin" />
          <span>{stepHint}</span>
        </motion.div>
      )}

      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="bg-white rounded-xl p-6 border border-[#2C3E50]/10"
      >
        <div className="flex items-center gap-2 mb-4">
          <motion.div
            animate={{ rotate: 360 }}
            transition={{ duration: 2, repeat: Infinity, ease: "linear" }}
            className="w-6 h-6"
          >
            <Loader2 className="w-6 h-6 text-[#2C3E50]/40 animate-spin" />
          </motion.div>
          <div className="w-32 h-5 bg-[#2C3E50]/10 rounded animate-pulse relative overflow-hidden">
            {shimmer}
          </div>
        </div>
        <div className="space-y-3">
          {skeletonItem(0, "w-full")}
          {skeletonItem(1, "w-[95%]")}
          {skeletonItem(2, "w-[88%]")}
          {skeletonItem(3, "w-[92%]")}
          {skeletonItem(4, "w-[70%]")}
        </div>
      </motion.div>

      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.1 }}
        className="bg-white rounded-xl p-6 border border-[#2C3E50]/10"
      >
        <div className="flex items-center gap-2 mb-4">
          <motion.div
            animate={{ rotate: 360 }}
            transition={{ duration: 2, repeat: Infinity, ease: "linear" }}
            className="w-6 h-6"
          >
            <Loader2 className="w-6 h-6 text-[#E67E22]/40 animate-spin" />
          </motion.div>
          <div className="w-24 h-5 bg-[#E67E22]/10 rounded animate-pulse relative overflow-hidden">
            {shimmer}
          </div>
        </div>
        <div className="space-y-3">
          {[...Array(4)].map((_, i) => (
            <div key={i} className="flex items-start gap-3">
              <motion.div
                initial={{ scale: 0 }}
                animate={{ scale: 1 }}
                transition={{ delay: i * 0.1 }}
                className="w-5 h-5 bg-[#E67E22]/10 rounded-full animate-pulse relative overflow-hidden mt-0.5"
              >
                {shimmer}
              </motion.div>
              <div className="flex-1 space-y-2">
                {skeletonItem(i, "w-[85%]")}
                {skeletonItem(i + 4, "w-[55%]")}
              </div>
            </div>
          ))}
        </div>
      </motion.div>

      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.2 }}
        className="bg-white rounded-xl p-6 border border-[#2C3E50]/10"
      >
        <div className="flex items-center gap-2 mb-4">
          <motion.div
            animate={{ rotate: 360 }}
            transition={{ duration: 2, repeat: Infinity, ease: "linear" }}
            className="w-6 h-6"
          >
            <Loader2 className="w-6 h-6 text-[#9B59B6]/40 animate-spin" />
          </motion.div>
          <div className="w-24 h-5 bg-[#9B59B6]/10 rounded animate-pulse relative overflow-hidden">
            {shimmer}
          </div>
        </div>
        <div className="flex justify-center py-6">
          <motion.div
            animate={{ scale: [1, 1.05, 1] }}
            transition={{ duration: 2, repeat: Infinity }}
            className="w-24 h-24 bg-gradient-to-br from-[#2C3E50]/10 to-[#E67E22]/10 rounded-full flex items-center justify-center relative overflow-hidden"
          >
            {shimmer}
            <motion.div
              animate={{ opacity: [0.3, 0.6, 0.3] }}
              transition={{ duration: 1.5, repeat: Infinity }}
              className="w-12 h-12 bg-[#2C3E50]/20 rounded-full"
            />
          </motion.div>
        </div>
      </motion.div>
    </div>
  )
}
