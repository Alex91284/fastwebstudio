import { useState, useEffect } from "react";
import { AuthContext } from "./AuthContext";

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null); 
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Aquí deberías validar el token guardado en localStorage o cookies
    const token = localStorage.getItem("token");
    if (token) {
      // TODO: llamar a tu backend para obtener datos del usuario
      setUser({ id: 1, name: "Demo User", role: "admin" }); // <-- EJEMPLO
    }
    setLoading(false);
  }, []);

  const login = (userData) => {
    setUser(userData);
    localStorage.setItem("token", userData.token);
  };

  const logout = () => {
    setUser(null);
    localStorage.removeItem("token");
  };

  return (
    <AuthContext.Provider value={{ user, loading, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}
