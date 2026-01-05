import { useEffect, useState } from "react"
import { useParams } from "react-router-dom"
import { getPublicSite } from "../services/sites"

function RenderComp({ c }){
  if(c.type==="text") return <p style={c.styles}>{c.props.text}</p>
  if(c.type==="image") return <img src={c.props.src} alt={c.props.alt||""} className="max-w-full" />
  if(c.type==="button") return <a href={c.props.href} style={c.styles}>{c.props.text}</a>
  return null
}

export default function PublicSite(){
  const { slug } = useParams()
  const [data, setData] = useState(null)

  useEffect(()=>{ (async()=> setData(await getPublicSite(slug)))(); }, [slug])

  if(!data) return <div className="p-6">Cargando…</div>

  const home = data.project.pages[0]
  return (
    <div className="max-w-4xl p-6 mx-auto space-y-4">
      {home.components.map(c => <RenderComp key={c.id} c={c} />)}
    </div>
  )
}
