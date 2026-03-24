"use client"

import { motion } from "motion/react"

interface LoadingSkeletonProps {
  type?: "summary" | "keypoints" | "mindmap" | "full"
}

export function LoadingSkeleton({ type = "full" }: LoadingSkeletonProps) {
  const skeletonItem = (index: number, width = "w-full") => (
    <motion.div
      key={index}
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ delay: index * 0.1 }}
      className={`h-4 ${width} bg-[#2C3E50]/10 rounded animate-pulse`}
    />
  )

  if (type === "summary") {
    return (
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="bg-white rounded-xl p-6 border border-[#2C3E50]/10"
      >
        <div className="flex items-center gap-2 mb-4">
          <div className="w-6 h-6 bg-[#2C3E50]/20 rounded animate-pulse" />
          <div className="w-32 h-5 bg-[#2C3E50]/20 rounded animate-pulse" />
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
          <div className="w-6 h-6 bg-[#E67E22]/20 rounded animate-pulse" />
          <div className="w-24 h-5 bg-[#E67E22]/20 rounded animate-pulse" />
        </div>
        <div className="space-y-3">
          {[...Array(5)].map((_, i) => (
            <div key={i} className="flex items-start gap-3">
              <div className="w-5 h-5 bg-[#E67E22]/20 rounded-full animate-pulse mt-0.5" />
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
          <div className="w-6 h-6 bg-[#2C3E50]/20 rounded animate-pulse" />
          <div className="w-28 h-5 bg-[#2C3E50]/20 rounded animate-pulse" />
        </div>
        <div className="flex justify-center">
          <div className="w-32 h-32 bg-[#2C3E50]/10 rounded-full animate-pulse" />
        </div>
      </motion.div>
    )
  }

  // Full skeleton for entire page
  return (
    <div className="space-y-6">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="bg-white rounded-xl p-6 border border-[#2C3E50]/10"
      >
        <div className="flex items-center gap-2 mb-4">
          <div className="w-6 h-6 bg-[#2C3E50]/20 rounded animate-pulse" />
          <div className="w-32 h-5 bg-[#2C3E50]/20 rounded animate-pulse" />
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
          <div className="w-6 h-6 bg-[#E67E22]/20 rounded animate-pulse" />
          <div className="w-24 h-5 bg-[#E67E22]/20 rounded animate-pulse" />
        </div>
        <div className="space-y-3">
          {[...Array(4)].map((_, i) => (
            <div key={i} className="flex items-start gap-3">
              <div className="w-5 h-5 bg-[#E67E22]/20 rounded-full animate-pulse mt-0.5" />
              <div className="flex-1 space-y-2">
                {skeletonItem(i, "w-[85%]")}
                {skeletonItem(i + 4, "w-[55%]")}
              </div>
            </div>
          ))}
        </div>
      </motion.div>
    </div>
  )
}