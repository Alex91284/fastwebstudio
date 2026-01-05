import { Navigate } from "react-router-dom"
import { useAuthContext } from "../auth/AuthContext"

export default function AdminRoute({ children }) {
  const { user, loading } = useAuthContext()

  if (loading) {
    return <div>Cargando...</div>
  }

  // Verifica si no está logueado
  if (!user) {
    return <Navigate to="/login" replace />
  }

  // Verifica si no tiene rol admin
  if (user.role !== "admin") {
    return <Navigate to="/unauthorized" replace />
  }

  return children
}
