import { Navigate } from "react-router-dom";
import { useAuthContext } from "../auth/AuthContext";

export default function ProtectedRoute({ children }) {
  const { token } = useAuthContext();
  if (!token) return <Navigate to="/login" />;
  return children;
}
