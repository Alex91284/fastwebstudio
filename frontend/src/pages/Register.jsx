import { useState } from "react"
import { useNavigate } from "react-router-dom"

export default function Register() {
  const navigate = useNavigate()
  const [form, setForm] = useState({ name: "", email: "", password: "" })
  const [error, setError] = useState("")
  const [success, setSuccess] = useState("")

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value })
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setError("")
    setSuccess("")

    try {
      const res = await fetch("http://localhost:8000/api/users", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          nombre: form.name,   
          email: form.email,
          password: form.password,
          role: "user"     
        })
      })

      if (!res.ok) {
        const err = await res.json()
        throw new Error(err.detail || "Error al registrar")
      }

      await res.json()
      setSuccess("Usuario creado exitosamente. Redirigiendo...")
      setTimeout(() => navigate("/login"), 1500)
    } catch (err) {
      setError(err.message)
    }
  }

  return (
    <div style={{ maxWidth: 400, margin: "0 auto", padding: 20 }}>
      <h2>Registro</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="name"
          placeholder="Nombre"
          value={form.name}
          autoComplete="username"
          onChange={handleChange}
          required
          style={{ display: "block", width: "100%", marginBottom: 10 }}
        />
        <input
          type="email"
          name="email"
          placeholder="Correo electrónico"
          value={form.email}
          autoComplete="email"
          onChange={handleChange}
          required
          style={{ display: "block", width: "100%", marginBottom: 10 }}
        />
        <input
          type="password"
          name="password"
          placeholder="Contraseña"
          value={form.password}
          autoComplete="current-password"
          onChange={handleChange}
          required
          style={{ display: "block", width: "100%", marginBottom: 10 }}
        />
        <button type="submit">Registrarse</button>
      </form>

      {error && <p style={{ color: "red", marginTop: 10 }}>{error}</p>}
      {success && <p style={{ color: "green", marginTop: 10 }}>{success}</p>}
    </div>
  );
}
