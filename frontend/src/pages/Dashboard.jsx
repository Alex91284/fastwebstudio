import { useEffect, useState } from "react"
import { useNavigate } from "react-router-dom"
import { jwtDecode } from "jwt-decode" // 👈 instala con: npm install jwt-decode

export default function Dashboard() {
  const [user, setUser] = useState(null)
  const [usersList, setUsersList] = useState([])
  const navigate = useNavigate()

  useEffect(() => {
    const token = localStorage.getItem("token")
    if (!token) {
      navigate("/login") // si no hay token redirige
      return
    }

    try {
      const decoded = jwtDecode(token) // 👈 decodificar JWT
      setUser(decoded)

      // 🔥 Traer lista de usuarios desde backend protegido
      fetch("http://localhost:8000/users", {
        headers: {
          "Authorization": `Bearer ${token}`
        }
      })
        .then(res => {
          if (!res.ok) throw new Error("Error al cargar usuarios")
          return res.json()
        })
        .then(data => setUsersList(data))
        .catch(err => console.error(err))

    } catch (err) {
      console.error("Token inválido", err)
      localStorage.removeItem("token")
      navigate("/login")
    }
  }, [navigate])

  const handleLogout = () => {
    localStorage.removeItem("token")
    navigate("/login")
  }

  return (
    <div className="max-w-3xl p-6 mx-auto mt-10 bg-white rounded shadow">
      <h1 className="mb-4 text-2xl font-bold">Dashboard</h1>

      {user && (
        <div className="mb-4">
          <p><strong>Nombre:</strong> {user.name}</p>
          <p><strong>Email:</strong> {user.email}</p>
          <p><strong>Rol:</strong> {user.role}</p>
        </div>
      )}

      <button 
        onClick={handleLogout} 
        className="px-4 py-2 mb-6 text-white bg-red-500 rounded hover:bg-red-600"
      >
        Cerrar sesión
      </button>

      <h2 className="mb-2 text-xl font-semibold">Usuarios registrados</h2>
      <ul className="pl-5 list-disc">
        {usersList.map(u => (
          <li key={u.id}>
            {u.name} - {u.email} ({u.role})
          </li>
        ))}
      </ul>
    </div>
  )
}
