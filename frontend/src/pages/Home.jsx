import { useNavigate } from "react-router-dom"
import { useAuthContext } from "../auth/AuthContext"

export default function Home() {
  const navigate = useNavigate()
  const { token, logout } = useAuthContext()

  return (
    <div className="p-6">
      <h2 className="mb-4 text-2xl font-bold">Home Page</h2>
      <p>Token actual: {token || "Ninguno"}</p>

      {!token && (
        <div className="space-x-2">
          <button
            className="px-4 py-2 text-white bg-blue-600"
            onClick={() => navigate("/login")}
          >
            Iniciar sesión
          </button>
          <button
            className="px-4 py-2 text-white bg-green-600"
            onClick={() => navigate("/register")}
          >
            Registrarse
          </button>
        </div>
      )}

      {token && (
        <button
          className="px-4 py-2 text-white bg-red-600"
          onClick={logout}
        >
          Cerrar sesión
        </button>
      )}
    </div>
  )
}
