import { useEffect, useState } from "react"
import { useAuthContext } from "../auth/AuthContext"
import { listProjects, createProject } from "../services/projects"
import { Link } from "react-router-dom"

export default function Dashboard(){
  const { token } = useAuthContext()
  const [projects, setProjects] = useState([])
  const [name, setName] = useState("")

  useEffect(() => {
    (async () => setProjects(await listProjects(token)))()
  }, [token])

  const onCreate = async (e) => {
    e.preventDefault()
    const p = await createProject(token, name)
    setProjects(prev => [p, ...prev])
    setName("")
  };

  return (
    <div className="p-6 space-y-6">
      <form onSubmit={onCreate} className="flex gap-2">
        <input className="flex-1 px-3 py-2 border rounded" placeholder="Nombre del proyecto"
               value={name} onChange={e=>setName(e.target.value)} />
        <button className="px-4 py-2 text-white bg-black rounded">Crear</button>
      </form>

      <div className="grid gap-4 md:grid-cols-3">
        {projects.map(p => (
          <div key={p.id} className="p-4 border rounded-xl">
            <h3 className="font-semibold">{p.name}</h3>
            <Link to={`/editor/${p.id}`} className="text-blue-600 underline">Abrir editor</Link>
          </div>
        ))}
      </div>
    </div>
  )
}
