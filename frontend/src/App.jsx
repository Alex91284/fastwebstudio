import { useEffect, useState } from "react"

function App() {
  const [msg, setMsg] = useState("Cargando...")

  useEffect(() => {
    fetch("http://localhost:8000/api/ping")
      .then(res => res.json())
      .then(data => setMsg(data.message))
      .catch(() => setMsg("Error conectando con el backend"))
  }, [])

  return (
    <div style={{ padding: 50 }}>
      <h1>FastWebStudio</h1>
      <p>{msg}</p>
    </div>
  )
}

export default App
