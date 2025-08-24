import { useState } from "react"
import { useNavigate } from "react-router-dom"
import { useAuthContext } from "../auth/AuthContext"

export default function Register() {
  const navigate = useNavigate()
  const { login } = useAuthContext()

  const [form, setForm] = useState({
    name: "",
    email: "",
    password: "",
    role: ""
  })
  const [error, setError] = useState(null)
  const [loading, setLoading] = useState(false)

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value
    })
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setError(null)
    setLoading(true)

    try {
      const res = await fetch("http://localhost:8000/api/users/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(form)
      })

      if (!res.ok) {
        const err = await res.json()
        throw new Error(err.detail || "Error al registrar usuario")
      }

      const data = await res.json()
     
      login(data.token)
      navigate("/")
    } catch (err) {
      setError(err.message)
    }finally {
      setLoading(false)
    }
  }

  return (
    <div className="max-w-md p-6 mx-auto">
      <h2 className="mb-4 text-2xl font-bold">Registro</h2>
      <form onSubmit={handleSubmit} className="space-y-4">
        <input
          type="text"
          name="name"
          placeholder="Nombre"
          value={form.name}
          onChange={handleChange}
          autoComplete="username"
          className="w-full p-2 border"
          required
          // style={{ display: "block", width: "100%", marginBottom: 10 }}
        />
        <input
          type="email"
          name="email"
          placeholder="Correo electrónico"
          value={form.email}
          autoComplete="email"
          onChange={handleChange}
          className="w-full p-2 border"
          required
          // style={{ display: "block", width: "100%", marginBottom: 10 }}
        />
        <input
          type="password"
          name="password"
          placeholder="Contraseña"
          value={form.password}
          autoComplete="current-password"
          onChange={handleChange}
          className="w-full p-2 border"
          required
          // style={{ display: "block", width: "100%", marginBottom: 10 }}
        />
        <input
          type="role"
          name="role"
          placeholder="Rol"
          value={form.role}
          autoComplete="current-role"
          onChange={handleChange}
          className="w-full p-2 border"
          required
          // style={{ display: "block", width: "100%", marginBottom: 10 }}
        />
        {error && <p className="text-red-600">{error}</p>}
        <button
          type="submit"
          disabled={loading}
          className="px-4 py-2 text-white bg-green-600"
        >
          {loading ? "Registrando..." : "Registrarse"}
        </button>
      </form>

      {/* {error && <p style={{ color: "red", marginTop: 10 }}>{error}</p>} */}
      {/* {success && <p style={{ color: "green", marginTop: 10 }}>{success}</p>} */}
    </div>
  );
}
