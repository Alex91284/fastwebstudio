import { useState, useEffect } from "react"
import { AuthContext } from "./AuthContext"

export function AuthProvider({ children }) {
  const [token, setToken] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const storedToken = localStorage.getItem("token")
    if (storedToken) {
      setToken(storedToken)
    }
    setLoading(false)
  }, [])

  const login = (jwt) => {
    localStorage.setItem("token", jwt)
    setToken(jwt)
  }

  const logout = () => {
    localStorage.removeItem("token")
    setToken(null)
  }

  return (
    <AuthContext.Provider value={{ token, isAuth: !!token, loading, login, logout }}>
      {children}
    </AuthContext.Provider>
  )
}
