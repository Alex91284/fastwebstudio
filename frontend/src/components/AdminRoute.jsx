import { Navigate } from "react-router-dom"
import { useAuthContext } from "../auth/AuthContext"

export default function AdminRoute({ children }) {
  const { token, user, loading } = useAuthContext()

  if (loading) return <p>Cargando...</p>

  if (!token) return <Navigate to="/login" replace />

  return user?.role === "admin" ? children : <Navigate to="/unauthorized" replace />
}
