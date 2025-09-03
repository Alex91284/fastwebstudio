import { Navigate } from "react-router-dom";
import { useAuth } from "../auth/useAuth";

export default function ProtectedRoute({ children }) {
  const { user, loading } = useAuth();

  if (loading) {
    return <div>Cargando...</div>; // O un spinner bonito
  }

  // Si no hay usuario logueado → redirige a login
  if (!user) {
    return <Navigate to="/login" replace />;
  }

  return children;
}
