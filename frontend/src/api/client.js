export const API_URL =
  import.meta.env.VITE_API_URL ?? "http://localhost:8000/api"

export const api = async (url, { method = "GET", body, token } = {}) => {
  try {
    const res = await fetch(`${API_URL}${url}`, {
      method,
      headers: {
        "Content-Type": "application/json",
        ...(token ? { Authorization: `Bearer ${token}` } : {}),
      },
      body: body ? JSON.stringify(body) : undefined,
    })

    // 🔹 Si no está OK, intentamos parsear el error en JSON
    if (!res.ok) {
      let errorMessage = "Error en la petición"
      try {
        const errorData = await res.json()
        errorMessage = errorData.detail || JSON.stringify(errorData)
      } catch {
        errorMessage = await res.text()
      }
      throw new Error(errorMessage)
    }

    return res.json()
  } catch (err) {
    console.error("❌ Error en API:", err.message)
    throw err
  }
}
