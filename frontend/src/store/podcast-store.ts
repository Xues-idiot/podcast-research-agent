import { create } from 'zustand'
import type { ResearchResult } from '@/lib/api'

type Status = 'idle' | 'loading' | 'success' | 'error'

interface PodcastState {
  // 状态
  status: Status
  url: string
  platform: string
  taskId: string | null
  error: string | null
  result: ResearchResult | null

  // 进度
  progress: number
  currentStep: string

  // 操作
  setUrl: (url: string) => void
  setPlatform: (platform: string) => void
  setStatus: (status: Status) => void
  setTaskId: (taskId: string) => void
  setError: (error: string | null) => void
  setResult: (result: ResearchResult | null) => void
  setProgress: (progress: number) => void
  setCurrentStep: (step: string) => void
  reset: () => void
}

const initialState = {
  status: 'idle' as Status,
  url: '',
  platform: 'unknown',
  taskId: null,
  error: null,
  result: null,
  progress: 0,
  currentStep: '',
}

// 简单的平台检测
function detectPlatform(url: string): string {
  const lower = url.toLowerCase()
  if (lower.includes('bilibili.com') || lower.includes('b23.tv')) return 'bilibili'
  if (lower.includes('youtube.com') || lower.includes('youtu.be')) return 'youtube'
  if (lower.includes('douyin.com') || lower.includes('huoshan.com')) return 'douyin'
  if (lower.includes('weixin.qq.com')) return 'wechat'
  if (lower.includes('xiaohongshu.com') || lower.includes('xhslink.com')) return 'xiaohongshu'
  if (lower.includes('.xml') || lower.includes('.rss') || lower.includes('feed')) return 'rss'
  return 'unknown'
}

export const usePodcastStore = create<PodcastState>((set) => ({
  ...initialState,

  setUrl: (url) => set({ url, platform: detectPlatform(url) }),
  setPlatform: (platform) => set({ platform }),
  setStatus: (status) => set({ status }),
  setTaskId: (taskId) => set({ taskId }),
  setError: (error) => set({ error, status: 'error' }),
  setResult: (result) => set({ result, status: 'success' }),
  setProgress: (progress) => set({ progress }),
  setCurrentStep: (currentStep) => set({ currentStep }),
  reset: () => set(initialState),
}))
