import { useEffect, useState } from "react"
import {AuthContext} from "./AuthContext"
import {jwtDecode} from "jwt-decode"

export function AuthProvider({ children }) {
  const [token, setToken] = useState(null)
  const [user, setUser] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const storedToken = localStorage.getItem("token")
    if (storedToken) {
      setToken(storedToken)
      try {
        const decoded = jwtDecode(storedToken)
        setUser(decoded)
      } catch (error) {
        console.error("Invalid token", error)
        logout()
      }
    }
    setLoading(false)
  }, [])

  const login = (newToken) => {
    localStorage.setItem("token", newToken)
    setToken(newToken)
    const decoded = jwtDecode(newToken)
    setUser(decoded)
  }

  const logout = () => {
    localStorage.removeItem("token")
    setToken(null)
    setUser(null)
  }

  return (
    <AuthContext.Provider value={{ loading, token, user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}
