import type { Metadata } from 'next'
import './globals.css'
import { ProgressBar } from '@/components/ProgressBar'

export const metadata: Metadata = {
  title: 'Echo - 播客研究Agent',
  description: '让知识回响，从播客/视频中提取有价值的信息',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="zh">
      <body className="antialiased">
        <ProgressBar />
        {children}
      </body>
    </html>
  )
}
