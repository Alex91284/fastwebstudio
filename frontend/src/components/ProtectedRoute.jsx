import { Navigate } from "react-router-dom"
import { useAuthContext } from "../auth/AuthContext"

export default function ProtectedRoute({ children }) {
  const { isAuth, loading } = useAuthContext()

  if (loading) {
    return <div>Cargando...</div> // O un spinner bonito
  }

  // Si no hay usuario logueado → redirige a login
  if (!isAuth) {
    return <Navigate to="/login" replace />
  }

  return children
}
