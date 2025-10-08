import { useEffect, useState } from 'react'
import './index.css'
import { getSignals } from './api'

function App() {
  const [data, setData] = useState({})
  useEffect(() => {
    getSignals().then(setData)
  }, [])
  return (
    <main className="p-6 font-sans">
      <h1 className="text-2xl font-bold mb-4">⚡ Live Squeeze Radar</h1>
      <table className="border-collapse">
        <thead><tr><th>Ticker</th><th>Squeeze?</th></tr></thead>
        <tbody>
          {Object.entries(data).map(([k,v]) => (
            <tr key={k}><td>{k}</td><td>{v ? '🔥' : '—'}</td></tr>
          ))}
        </tbody>
      </table>
      <p className="text-sm mt-4 opacity-60">Auto-refreshes every 5 min.</p>
    </main>
  )
}

export default App
