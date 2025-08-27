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
    role: "user", // mejor default; idealmente el backend lo fija
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
      const res = await fetch("http://localhost:8000/api/users/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form),
      });

      const data = await res.json();

      if (!res.ok) {
        throw new Error(data.detail || "Error al registrar usuario");
      }

      // el backend devuelve { access_token: "..." }
      const token = data.access_token ?? data.token;
      if (!token || typeof token !== "string") {
        throw new Error("El backend no devolvió un access_token válido");
      }

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
          autoComplete="username"
          className="w-full p-2 border"
          required
        />
        <input
          type="email"
          name="email"
          placeholder="Correo electrónico"
          value={form.email}
          onChange={handleChange}
          autoComplete="email"
          className="w-full p-2 border"
          required
        />
        <input
          type="password"
          name="password"
          placeholder="Contraseña"
          value={form.password}
          onChange={handleChange}
          autoComplete="new-password"
          className="w-full p-2 border"
          required
        />
        {/* Si quieres permitir cambiar rol, usa un select; si no, elimínalo */}
        <input
          type="text"
          name="role"
          placeholder="Rol"
          value={form.role}
          onChange={handleChange}
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
