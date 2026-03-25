'use client'

import { useState, useEffect } from 'react'

interface Podcast {
  podcast_id: string
  title: string
  entry_count: number
  created_at: string
}

export default function KnowledgePage() {
  const [podcasts, setPodcasts] = useState<Podcast[]>([])
  const [selectedPodcast, setSelectedPodcast] = useState<string | null>(null)
  const [entries, setEntries] = useState<any[]>([])
  const [loading, setLoading] = useState(true)
  const [searchQuery, setSearchQuery] = useState('')

  useEffect(() => {
    fetchPodcasts()
  }, [])

  const fetchPodcasts = async () => {
    try {
      const res = await fetch('/api/knowledge/podcasts')
      const data = await res.json()
      setPodcasts(data.podcasts || [])
    } catch (error) {
      console.error('Failed to fetch podcasts:', error)
    } finally {
      setLoading(false)
    }
  }

  const fetchEntries = async (podcastId: string) => {
    try {
      const res = await fetch(`/api/knowledge/entries/${podcastId}`)
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
      const res = await fetch('/api/knowledge/search', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          query: searchQuery,
          podcast_id: selectedPodcast,
          top_k: 10
        })
      })
      const data = await res.json()
      setEntries(data.results || [])
    } catch (error) {
      console.error('Failed to search:', error)
    }
  }

  const deletePodcast = async (podcastId: string) => {
    if (!confirm('确定要删除这个播客的知识库吗？')) return

    try {
      await fetch(`/api/knowledge/entries/${podcastId}`, { method: 'DELETE' })
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
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-gray-500">加载中...</div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow-sm border-b">
        <div className="max-w-7xl mx-auto px-4 py-4 flex items-center justify-between">
          <div className="flex items-center gap-4">
            <a href="/podcast" className="text-gray-600 hover:text-gray-900">
              &larr; 返回研究
            </a>
            <h1 className="text-2xl font-bold text-gray-900">知识库</h1>
          </div>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-4 py-8">
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Podcast List */}
          <div className="bg-white rounded-lg shadow p-4">
            <h2 className="text-lg font-semibold mb-4">已研究的播客</h2>
            {podcasts.length === 0 ? (
              <p className="text-gray-500 text-sm">暂无知识库，请先进行研究</p>
            ) : (
              <div className="space-y-2">
                {podcasts.map((podcast) => (
                  <div
                    key={podcast.podcast_id}
                    className={`p-3 rounded-lg cursor-pointer transition ${
                      selectedPodcast === podcast.podcast_id
                        ? 'bg-blue-50 border-blue-200'
                        : 'hover:bg-gray-50'
                    }`}
                    onClick={() => fetchEntries(podcast.podcast_id)}
                  >
                    <div className="font-medium text-gray-900 truncate">
                      {podcast.title || podcast.podcast_id}
                    </div>
                    <div className="text-sm text-gray-500">
                      {podcast.entry_count} 个知识点
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>

          {/* Entries & Search */}
          <div className="lg:col-span-2 space-y-6">
            {/* Search */}
            <div className="bg-white rounded-lg shadow p-4">
              <h2 className="text-lg font-semibold mb-4">搜索知识</h2>
              <div className="flex gap-2">
                <input
                  type="text"
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  onKeyDown={(e) => e.key === 'Enter' && searchEntries()}
                  placeholder="输入关键词搜索..."
                  className="flex-1 px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
                <button
                  onClick={searchEntries}
                  className="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
                >
                  搜索
                </button>
              </div>
            </div>

            {/* Entries List */}
            <div className="bg-white rounded-lg shadow p-4">
              <div className="flex items-center justify-between mb-4">
                <h2 className="text-lg font-semibold">
                  {selectedPodcast ? '知识点列表' : '选择一个播客查看'}
                </h2>
                {selectedPodcast && (
                  <button
                    onClick={() => deletePodcast(selectedPodcast)}
                    className="text-red-600 hover:text-red-700 text-sm"
                  >
                    删除知识库
                  </button>
                )}
              </div>

              {entries.length === 0 ? (
                <p className="text-gray-500 text-center py-8">
                  {selectedPodcast ? '暂无知识点' : '请选择一个播客'}
                </p>
              ) : (
                <div className="space-y-3 max-h-96 overflow-y-auto">
                  {entries.map((entry, index) => (
                    <div
                      key={entry.id || index}
                      className="p-3 bg-gray-50 rounded-lg"
                    >
                      <div className="flex items-start justify-between">
                        <div className="flex-1">
                          <div className="text-xs text-gray-500 mb-1">
                            [{entry.start_time ? formatTime(entry.start_time) : '?'} - {entry.end_time ? formatTime(entry.end_time) : '?'}]
                          </div>
                          <p className="text-gray-700">{entry.compiled || entry.raw}</p>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </div>
          </div>
        </div>
      </main>
    </div>
  )
}
