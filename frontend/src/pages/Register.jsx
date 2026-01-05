import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAuthContext } from "../auth/AuthContext";

export default function Register() {
  const navigate = useNavigate();
  const { login } = useAuthContext();

  const [form, setForm] = useState({
    name: "",
    email: "",
    password: "",
    role: "user", // Backend espera este campo
  });

  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setForm((prev) => ({ ...prev, [e.target.name]: e.target.value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setLoading(true);

    try {
      // Enviar datos exactamente como espera el backend
      const res = await fetch("http://localhost:8000/api/users/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          name: form.name.trim(),
          email: form.email.trim(),
          password: form.password,
          role: form.role.trim(),
        }),
      });

      const data = await res.json();

      if (!res.ok) {
        console.error("Error 422 detalle:", data);
        throw new Error(data.detail?.[0]?.msg || "Error al registrar usuario");
      }

      const token = data.access_token;
      if (!token) {
        throw new Error("El backend no devolvió un access_token válido");
      }

      // Guardar token y navegar al dashboard
      localStorage.setItem("token", token);
      login(token);
      navigate("/dashboard");
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

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
          required
          className="w-full p-2 border"
        />
        <input
          type="email"
          name="email"
          placeholder="Correo electrónico"
          value={form.email}
          onChange={handleChange}
          required
          className="w-full p-2 border"
        />
        <input
          type="password"
          name="password"
          placeholder="Contraseña"
          value={form.password}
          onChange={handleChange}
          required
          className="w-full p-2 border"
        />
        <input
          type="text"
          name="role"
          value={form.role}
          onChange={handleChange}
          autoComplete="current-password"
          className="w-full p-2 border"
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
    </div>
  );
}
