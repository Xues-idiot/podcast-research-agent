import Link from 'next/link'
import { Mic, Sparkles, Clock, MessageCircle, BookOpen, Download, ArrowRight, Brain, Zap } from 'lucide-react'
import { ThemeToggle } from '@/components/ThemeToggle'

export default function Home() {
  return (
    <div className="min-h-screen bg-[#FAF8F5]">
      {/* Header */}
      <header className="bg-white border-b border-[#2C3E50]/10">
        <div className="max-w-5xl mx-auto px-6 py-4 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-[#2C3E50] to-[#34495E] flex items-center justify-center">
              <Mic className="w-5 h-5 text-white" />
            </div>
            <div>
              <h1 className="text-xl font-bold text-[#2C3E50]">Echo</h1>
              <p className="text-xs text-[#2C3E50]/60">播客研究Agent</p>
            </div>
          </div>
          <nav className="flex items-center gap-4">
            <ThemeToggle />
            <Link href="/podcast" className="text-sm font-medium text-[#2C3E50] hover:text-[#E67E22]">研究</Link>
            <Link href="/knowledge" className="text-sm font-medium text-gray-600 hover:text-[#E67E22]">知识库</Link>
            <Link href="/export" className="text-sm font-medium text-gray-600 hover:text-[#E67E22]">导出</Link>
            <Link href="/history" className="text-sm font-medium text-gray-600 hover:text-[#E67E22]">历史</Link>
          </nav>
        </div>
      </header>

      {/* Hero */}
      <main className="max-w-5xl mx-auto px-6 py-16">
        <div className="text-center mb-16">
          <h2 className="text-5xl font-bold text-[#2C3E50] mb-4">
            让播客内容<span className="text-[#E67E22]">真正</span>变成你的知识
          </h2>
          <p className="text-xl text-[#2C3E50]/70 max-w-2xl mx-auto mb-8">
            输入B站、YouTube链接或播客RSS，AI自动转录、提取要点、生成摘要、构建知识图谱
          </p>
          <Link
            href="/podcast"
            className="inline-flex items-center gap-2 px-8 py-4 bg-[#E67E22] text-white rounded-full text-lg font-medium hover:bg-[#D35400] transition-colors shadow-lg shadow-[#E67E22]/30"
          >
            开始研究
            <ArrowRight className="w-5 h-5" />
          </Link>
        </div>

        {/* Features */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-16">
          <FeatureCard
            icon={<Clock className="w-6 h-6" />}
            title="时间戳导航"
            description="点击要点时间戳，一键跳转到播客对应段落，精准回顾"
            color="#E67E22"
          />
          <FeatureCard
            icon={<MessageCircle className="w-6 h-6" />}
            title="对话式回顾"
            description="基于研究结果与AI对话，深入探讨播客内容"
            color="#2C3E50"
          />
          <FeatureCard
            icon={<BookOpen className="w-6 h-6" />}
            title="知识库管理"
            description="自动构建个人知识库，轻松搜索和回顾已研究内容"
            color="#9B59B6"
          />
          <FeatureCard
            icon={<Download className="w-6 h-6" />}
            title="多格式导出"
            description="支持JSON、Markdown、HTML、PDF、Anki等多种导出格式"
            color="#27AE60"
          />
          <FeatureCard
            icon={<Brain className="w-6 h-6" />}
            title="AI播客讨论"
            description="自动生成两个AI角色对播客内容的深入讨论"
            color="#3498DB"
          />
          <FeatureCard
            icon={<Sparkles className="w-6 h-6" />}
            title="智能摘要"
            description="自动提取关键要点和精华片段，高效获取核心信息"
            color="#E74C3C"
          />
        </div>

        {/* How it works */}
        <div className="bg-white rounded-2xl p-8 shadow-sm border border-[#2C3E50]/10">
          <h3 className="text-2xl font-bold text-[#2C3E50] text-center mb-8">研究流程</h3>
          <div className="flex flex-wrap justify-center gap-4">
            {[
              { step: '1', label: '输入链接' },
              { step: '2', label: 'AI转录' },
              { step: '3', label: '智能摘要' },
              { step: '4', label: '提取要点' },
              { step: '5', label: '构建图谱' },
              { step: '6', label: '知识关联' },
              { step: '7', label: '生成报告' },
              { step: '8', label: '问答对' },
            ].map((item, i) => (
              <div key={i} className="flex items-center gap-2">
                <div className="w-8 h-8 rounded-full bg-[#2C3E50] text-white flex items-center justify-center text-sm font-bold">
                  {item.step}
                </div>
                <span className="text-[#2C3E50]/70 text-sm">{item.label}</span>
                {i < 7 && <span className="text-[#2C3E50]/30 ml-2">→</span>}
              </div>
            ))}
          </div>
        </div>

        {/* CTA */}
        <div className="text-center mt-16">
          <p className="text-[#2C3E50]/50 mb-4">支持B站、YouTube视频和播客RSS链接</p>
          <Link
            href="/podcast"
            className="inline-flex items-center gap-2 px-6 py-3 bg-[#2C3E50] text-white rounded-full font-medium hover:bg-[#34495E] transition-colors"
          >
            <Zap className="w-4 h-4" />
            立即体验
          </Link>
        </div>
      </main>

      {/* Footer */}
      <footer className="border-t border-[#2C3E50]/10 bg-white mt-auto">
        <div className="max-w-5xl mx-auto px-6 py-4">
          <p className="text-center text-sm text-[#2C3E50]/50">
            Echo · 播客研究Agent · {new Date().getFullYear()}
          </p>
        </div>
      </footer>
    </div>
  )
}

function FeatureCard({ icon, title, description, color }: {
  icon: React.ReactNode
  title: string
  description: string
  color: string
}) {
  return (
    <div className="bg-white rounded-xl p-6 shadow-sm border border-[#2C3E50]/10 hover:shadow-md transition-shadow">
      <div
        className="w-12 h-12 rounded-lg flex items-center justify-center mb-4"
        style={{ backgroundColor: `${color}15`, color }}
      >
        {icon}
      </div>
      <h4 className="font-semibold text-[#2C3E50] mb-2">{title}</h4>
      <p className="text-sm text-[#2C3E50]/60">{description}</p>
    </div>
  )
}
