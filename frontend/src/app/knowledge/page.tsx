'use client'

import { useState, useEffect } from 'react'
import { motion } from 'motion/react'
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'
import { Input } from '@/components/ui/input'
import { Button } from '@/components/ui/button'
import { Mic, Search, Trash2, BookOpen, Clock, ArrowLeft } from 'lucide-react'
import { ThemeToggle } from '@/components/ThemeToggle'
import { API_BASE, getKnowledgePodcasts, searchKnowledge } from '@/lib/api'

interface Podcast {
  podcast_id: string
  title: string
  entry_count: number
  created_at: string
}

interface Entry {
  id?: string
  entry_id: string
  podcast_id: string
  content: string
  compiled?: string
  raw?: string
  start_time: number
  end_time: number
}

export default function KnowledgePage() {
  const [podcasts, setPodcasts] = useState<Podcast[]>([])
  const [selectedPodcast, setSelectedPodcast] = useState<string | null>(null)
  const [entries, setEntries] = useState<Entry[]>([])
  const [loading, setLoading] = useState(true)
  const [searchQuery, setSearchQuery] = useState('')

  useEffect(() => {
    fetchPodcasts()
  }, [])

  const fetchPodcasts = async () => {
    try {
      const podcasts = await getKnowledgePodcasts()
      setPodcasts(podcasts.map(p => ({
        podcast_id: p.id,
        title: p.title,
        entry_count: p.entry_count,
        created_at: p.created_at
      })))
    } catch (error) {
      console.error('Failed to fetch podcasts:', error)
    } finally {
      setLoading(false)
    }
  }

  const fetchEntries = async (podcastId: string) => {
    try {
      const res = await fetch(`${API_BASE}/knowledge/entries/${podcastId}`)
      const data = await res.json()
      setEntries(data.entries || [])
      setSelectedPodcast(podcastId)
    } catch (error) {
      console.error('Failed to fetch entries:', error)
    }
  }

  const searchEntries = async () => {
    if (!searchQuery.trim()) {
      if (selectedPodcast) {
        fetchEntries(selectedPodcast)
      }
      return
    }

    try {
      const results = await searchKnowledge(searchQuery, 10)
      setEntries(results.map(e => ({
        entry_id: e.id,
        podcast_id: e.podcast_id,
        content: e.content,
        compiled: e.content,
        start_time: e.timestamp || 0,
        end_time: 0
      })))
    } catch (error) {
      console.error('Failed to search:', error)
    }
  }

  const deletePodcast = async (podcastId: string) => {
    if (!confirm('确定要删除这个播客的知识库吗？')) return

    try {
      await fetch(`${API_BASE}/knowledge/entries/${podcastId}`, { method: 'DELETE' })
      fetchPodcasts()
      if (selectedPodcast === podcastId) {
        setSelectedPodcast(null)
        setEntries([])
      }
    } catch (error) {
      console.error('Failed to delete:', error)
    }
  }

  const formatTime = (seconds: number) => {
    const mins = Math.floor(seconds / 60)
    const secs = Math.floor(seconds % 60)
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`
  }

  if (loading) {
    return (
      <div className="min-h-screen bg-[#FAF8F5] flex items-center justify-center">
        <div className="text-[#2C3E50]/50">加载中...</div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-[#FAF8F5]">
      {/* Header */}
      <header className="bg-white border-b border-[#2C3E50]/10">
        <div className="max-w-5xl mx-auto px-6 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <a href="/podcast" className="flex items-center gap-2 text-[#2C3E50]/60 hover:text-[#E67E22] transition-colors">
                <ArrowLeft className="w-4 h-4" />
                <span className="text-sm">返回研究</span>
              </a>
            </div>
            <nav className="flex items-center gap-4">
              <ThemeToggle />
              <a href="/podcast" className="text-sm font-medium text-gray-600 hover:text-[#E67E22]">研究</a>
              <a href="/knowledge" className="text-sm font-medium text-[#2C3E50] hover:text-[#E67E22]">知识库</a>
              <a href="/export" className="text-sm font-medium text-gray-600 hover:text-[#E67E22]">导出</a>
              <a href="/history" className="text-sm font-medium text-gray-600 hover:text-[#E67E22]">历史</a>
            </nav>
          </div>
        </div>
      </header>

      <main className="max-w-5xl mx-auto px-6 py-8">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="mb-8"
        >
          <h1 className="text-2xl font-bold text-[#2C3E50] flex items-center gap-2">
            <BookOpen className="w-6 h-6 text-[#E67E22]" />
            知识库
          </h1>
          <p className="text-[#2C3E50]/60 mt-1">管理已研究的播客内容</p>
        </motion.div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Podcast List */}
          <motion.div
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: 0.1 }}
          >
            <Card>
              <CardHeader>
                <CardTitle className="text-lg">已研究的播客</CardTitle>
              </CardHeader>
              <CardContent>
                {podcasts.length === 0 ? (
                  <p className="text-[#2C3E50]/50 text-sm text-center py-4">暂无知识库，请先进行研究</p>
                ) : (
                  <div className="space-y-2">
                    {podcasts.map((podcast) => (
                      <motion.div
                        key={podcast.podcast_id}
                        whileHover={{ scale: 1.02 }}
                        whileTap={{ scale: 0.98 }}
                        className={`p-3 rounded-lg cursor-pointer transition ${
                          selectedPodcast === podcast.podcast_id
                            ? 'bg-[#E67E22]/10 border-l-2 border-l-[#E67E22]'
                            : 'hover:bg-[#FAF8F5]'
                        }`}
                        onClick={() => fetchEntries(podcast.podcast_id)}
                      >
                        <div className="flex items-center gap-2">
                          <Mic className="w-4 h-4 text-[#2C3E50]/50" />
                          <div className="flex-1 min-w-0">
                            <div className="font-medium text-[#2C3E50] truncate">
                              {podcast.title || podcast.podcast_id}
                            </div>
                            <div className="text-xs text-[#2C3E50]/50">
                              {podcast.entry_count} 个知识点
                            </div>
                          </div>
                        </div>
                      </motion.div>
                    ))}
                  </div>
                )}
              </CardContent>
            </Card>
          </motion.div>

          {/* Entries & Search */}
          <div className="lg:col-span-2 space-y-6">
            {/* Search */}
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.2 }}
            >
              <Card>
                <CardHeader>
                  <CardTitle className="flex items-center gap-2">
                    <Search className="w-5 h-5 text-[#E67E22]" />
                    搜索知识
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="flex gap-2">
                    <Input
                      type="text"
                      value={searchQuery}
                      onChange={(e) => setSearchQuery(e.target.value)}
                      onKeyDown={(e) => e.key === 'Enter' && searchEntries()}
                      placeholder="输入关键词搜索..."
                      className="flex-1"
                    />
                    <Button
                      onClick={searchEntries}
                      className="bg-[#E67E22] hover:bg-[#D35400]"
                    >
                      搜索
                    </Button>
                  </div>
                </CardContent>
              </Card>
            </motion.div>

            {/* Entries List */}
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.3 }}
            >
              <Card className="border-l-4 border-l-[#2C3E50]">
                <CardHeader>
                  <div className="flex items-center justify-between">
                    <CardTitle>
                      {selectedPodcast ? '知识点列表' : '选择一个播客查看'}
                    </CardTitle>
                    {selectedPodcast && (
                      <Button
                        variant="ghost"
                        size="sm"
                        onClick={() => deletePodcast(selectedPodcast)}
                        className="text-red-500 hover:text-red-600 hover:bg-red-50"
                      >
                        <Trash2 className="w-4 h-4 mr-1" />
                        删除
                      </Button>
                    )}
                  </div>
                </CardHeader>
                <CardContent>
                  {entries.length === 0 ? (
                    <p className="text-[#2C3E50]/50 text-center py-8">
                      {selectedPodcast ? '暂无知识点' : '请选择一个播客'}
                    </p>
                  ) : (
                    <div className="space-y-3 max-h-96 overflow-y-auto">
                      {entries.map((entry, index) => (
                        <motion.div
                          key={entry.id || index}
                          initial={{ opacity: 0, y: 10 }}
                          animate={{ opacity: 1, y: 0 }}
                          transition={{ delay: index * 0.05 }}
                          className="p-3 bg-[#FAF8F5] rounded-lg hover:bg-[#F5F5DC]/30 transition-colors"
                        >
                          <div className="flex items-start justify-between">
                            <div className="flex-1">
                              <div className="flex items-center gap-2 text-xs text-[#E67E22] mb-1">
                                <Clock className="w-3 h-3" />
                                [{entry.start_time ? formatTime(entry.start_time) : '?'} - {entry.end_time ? formatTime(entry.end_time) : '?'}]
                              </div>
                              <p className="text-[#2C3E50]/80 text-sm">{entry.compiled || entry.raw}</p>
                            </div>
                          </div>
                        </motion.div>
                      ))}
                    </div>
                  )}
                </CardContent>
              </Card>
            </motion.div>
          </div>
        </div>
      </main>
    </div>
  )
}
