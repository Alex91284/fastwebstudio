import { Navigate } from "react-router-dom"
import { useAuthContext } from "../auth/AuthContext"

export default function ProtectedRoute({ children }) {
  const { token, loading } = useAuthContext()

  if (loading) return <div>Cargando...</div>
 return token ? children : <Navigate to="/login" replace />
}
