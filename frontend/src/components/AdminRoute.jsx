import { Navigate } from "react-router-dom"
import { useAuthContext } from "../auth/AuthContext"

export default function AdminRoute({ children }) {
  const { token, user } = useAuthContext()

  if (!token || !user) return <Navigate to="/login" replace />
  if (user.role !== "admin") return <Navigate to="/unauthorized" replace />

  return children
}
