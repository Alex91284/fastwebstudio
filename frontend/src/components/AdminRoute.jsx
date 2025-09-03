import { Navigate } from "react-router-dom";
import { useAuth } from "../auth/useAuth";

export default function AdminRoute({ children }) {
  const { user, loading } = useAuth();

  if (loading) {
    return <div>Cargando...</div>;
  }

  // Verifica si no está logueado
  if (!user) {
    return <Navigate to="/login" replace />;
  }

  // Verifica si no tiene rol admin
  if (user.role !== "admin") {
    return <Navigate to="/unauthorized" replace />;
  }

  return children;
}
