import { useState } from "react"
import { useNavigate, Link } from "react-router-dom"
import { useAuthContext } from "../auth/AuthContext"

export default function Login() {
  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")
  const { login } = useAuthContext()
  const navigate = useNavigate()
  const [error, setError] = useState("")

  const handleSubmit = async (e) => {
    e.preventDefault()
    try {
      const res = await fetch("http://localhost:8000/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
      })

      const data = await res.json()

      if (!res.ok) throw new Error(data.detail || "Login failed")

      login(data.token) // guarda el JWT
      navigate("/dashboard") // redirige al dashboard
    } catch (err) {
      setError(err.message)
    }
  }

  return (
    <div className="max-w-md p-4 mx-auto mt-10 bg-white rounded shadow">
      <h1 className="mb-4 text-xl font-bold">Iniciar sesión</h1>
      {error && <p className="mb-2 text-red-500">{error}</p>}
      <form onSubmit={handleSubmit} className="space-y-4">
        <input
          type="email"
          placeholder="Correo"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className="w-full p-2 border rounded"
          required
          autoComplete="email"
        />
        <input
          type="password"
          placeholder="Contraseña"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="w-full p-2 border rounded"
          required
          autoComplete="current-password"
        />
        <button className="w-full p-2 text-white bg-blue-500 rounded hover:bg-blue-600">
          Entrar
        </button>
      </form>
      <p>
        ¿No tienes cuenta?{" "}
        <Link to="/register">Regístrate aquí</Link>
      </p>
    </div>
  );
}
