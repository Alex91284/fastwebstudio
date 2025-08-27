import { useEffect, useState } from "react"
import { useNavigate } from "react-router-dom"

export default function Dashboard() {
  const [projects, setProjects] = useState([])
  const [name, setName] = useState("")
  const [description, setDescription] = useState("")
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState("")
  const navigate = useNavigate()

  const token = localStorage.getItem("token")

  // 🔹 Redirigir si no hay token
  useEffect(() => {
    if (!token) {
      navigate("/login")
    } else {
      fetchProjects()
    }
  }, [token])

  console.log("TOKEN FRONTEND:", token)

  // 🔹 Obtener proyectos del usuario logueado
  const fetchProjects = async () => {
    try {
      const res = await fetch("http://localhost:8000/api/projects/", {
        method: "GET",
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })
      
      if (!res.ok) throw new Error("Error al obtener proyectos")
      const data = await res.json()
      setProjects(data)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  // 🔹 Crear proyecto
  const handleCreate = async (e) => {
    e.preventDefault()
    try {
      const res = await fetch("http://localhost:8000/api/projects/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({ name, description }),
      })
      
      if (!res.ok) throw new Error("Error al crear proyecto")
      const newProject = await res.json()
      setProjects([...projects, newProject])
      setName("")
      setDescription("")
    } catch (err) {
      setError(err.message)
    }
  }

  // 🔹 Eliminar proyecto
  const handleDelete = async (id) => {
    if (!confirm("¿Seguro que quieres eliminar este proyecto?")) return
    try {
      const res = await fetch(`http://localhost:8000/api/projects/${id}`, {
        method: "DELETE",
        headers: { Authorization: `Bearer ${token}` },
      })
      if (!res.ok) throw new Error("Error al eliminar proyecto")
      setProjects(projects.filter((p) => p.id !== id))
    } catch (err) {
      setError(err.message)
    }
  }

  return (
    <div className="max-w-4xl p-4 mx-auto mt-10 bg-white rounded shadow">
      <h1 className="mb-4 text-2xl font-bold">Panel de Administración</h1>

      {error && <p className="text-red-500">{error}</p>}
      {loading ? (
        <p>Cargando proyectos...</p>
      ) : (
        <div>
          {/* Formulario para crear proyecto */}
          <form onSubmit={handleCreate} className="mb-6 space-y-3">
            <input
              type="text"
              placeholder="Nombre del proyecto"
              value={name}
              onChange={(e) => setName(e.target.value)}
              className="w-full p-2 border rounded"
              required
            />
            <textarea
              placeholder="Descripción"
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              className="w-full p-2 border rounded"
            />
            <button className="w-full p-2 text-white bg-blue-500 rounded hover:bg-blue-600">
              Crear Proyecto
            </button>
          </form>

          {/* Listado de proyectos */}
          <ul className="space-y-2">
            {projects.map((project) => (
              <li
                key={project.id}
                className="flex items-center justify-between p-3 border rounded"
              >
                <div>
                  <h2 className="font-semibold">{project.name}</h2>
                  <p className="text-sm text-gray-600">
                    {project.description}
                  </p>
                </div>
                <button
                  onClick={() => handleDelete(project.id)}
                  className="p-2 text-white bg-red-500 rounded hover:bg-red-600"
                >
                  Eliminar
                </button>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  )
}
