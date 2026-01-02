import { useEffect, useState } from 'react'
import './App.css'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

function App() {
  const [message, setMessage] = useState('Loading...')
  const [error, setError] = useState('')

  useEffect(() => {
    fetch(`${API_URL}/message`)
      .then(async (res) => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`)
        return res.json()
      })
      .then((data) => setMessage(data.message ?? JSON.stringify(data)))
      .catch((e) => setError(String(e)))
  }, [])

  return (
    <div style={{ padding: 24 }}>
      <h1>Frontend</h1>
      <h2>Backend message</h2>
      {error ? <pre>{error}</pre> : <p>{message}</p>}
      <p>API_URL: <code>{API_URL}</code></p>
    </div>
  )
}

export default App
