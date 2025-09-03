import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { DndContext, useDraggable, useDroppable, closestCenter, PointerSensor, useSensor, useSensors } from "@dnd-kit/core";
import { useAuth } from "../auth/useAuth";
import { getFullProject } from "../services/projects";
import { addComponent, updateComponent, deleteComponent } from "../services/component.jsx";
import { useEditor } from "../store/editorStore";
import { publishSite, upsertSite } from "../services/sites";

const PALETTE = [
  { type: "text", label: "Texto", props:{ text:"Doble clic para editar"}, styles:{ fontSize:24, fontWeight:"bold" } },
  { type: "image", label: "Imagen", props:{ src:"https://placehold.co/600x300", alt:"" }, styles:{} },
  { type: "button", label: "Botón", props:{ text:"Click aquí", href:"#"}, styles:{ padding:"12px 18px", borderRadius:8, border:"1px solid #222" } },
];

function PaletteItem({ item }){
  const { attributes, listeners, setNodeRef } = useDraggable({ id: `palette-${item.type}`, data: item });
  return <div ref={setNodeRef} {...listeners} {...attributes} className="px-3 py-2 border rounded cursor-grab">{item.label}</div>;
}

function Canvas({ components, onDrop }){
  const { setNodeRef, isOver } = useDroppable({ id:"canvas" });
  return (
    <div
      ref={setNodeRef}
      onDrop={onDrop}
      className={`min-h-[60vh] bg-white rounded-xl border p-6 ${isOver ? 'ring-2 ring-blue-500' : ''}`}>
      {components.length===0 && <p className="text-gray-400">Arrastra componentes aquí…</p>}
        <div className="space-y-3">
          {components.map(c => <ComponentView key={c.id} comp={c} />)}
      </div>
    </div>
  );
}

function ComponentView({ comp }){
  const { token } = useAuth();
  const {  currentPageId, replaceComponents, pageById } = useEditor();
  const [editing, setEditing] = useState(false);
  const onDelete = async () => {
    await deleteComponent(token, comp.id);
    const page = pageById(currentPageId);
    replaceComponents(currentPageId, page.components.filter(x=>x.id!==comp.id));
  };

  if(comp.type==="text"){
    return (
      <div className="relative p-3 border rounded group">
        {editing ? (
          <input
            className="w-full outline-none"
            value={comp.props.text}
            onChange={async e=>{
              comp.props.text = e.target.value;
              await updateComponent(token, comp.id, { props: comp.props });
            }}
            onBlur={()=>setEditing(false)}
            autoFocus
          />
        ) : (
          <p style={comp.styles} onDoubleClick={()=>setEditing(true)}>{comp.props.text}</p>
        )}
        <button onClick={onDelete} className="absolute hidden px-2 text-xs text-white bg-red-600 rounded-full group-hover:block -top-2 -right-2">x</button>
      </div>
    );
  }
  if(comp.type==="image"){
    return (
      <div className="relative p-3 border rounded group">
        <img src={comp.props.src} alt={comp.props.alt || ""} className="max-w-full rounded"/>
        <button onClick={onDelete} className="absolute hidden px-2 text-xs text-white bg-red-600 rounded-full group-hover:block -top-2 -right-2">x</button>
      </div>
    );
  }
  if(comp.type==="button"){
    return (
      <div className="relative p-3 border rounded group">
        <a href={comp.props.href} style={comp.styles}>{comp.props.text}</a>
        <button onClick={onDelete} className="absolute hidden px-2 text-xs text-white bg-red-600 rounded-full group-hover:block -top-2 -right-2">x</button>
      </div>
    );
  }
  return null;
}

export default function Editor(){
  const { id } = useParams();
  const { token } = useAuth();
  const { project, setProject, currentPageId, setCurrentPage, pageById, replaceComponents } = useEditor();
  const sensors = useSensors(useSensor(PointerSensor));
  const [siteSlug, setSiteSlug] = useState("");

  useEffect(() => {
    (async () => {
      const data = await getFullProject(token, id);
      setProject(data);
      setSiteSlug(data?.site?.slug ?? "");
    })();
  }, [id, token, setProject]);

  const page = pageById(currentPageId) || { components: [] };

  const handleDragEnd = async (ev) => {
    const item = ev.active?.data?.current;
    if(ev.over?.id === "canvas" && item?.type){
      const created = await addComponent(token, page.id, {
        type: item.type, props: item.props, styles: item.styles, order: (page.components?.length ?? 0)
      });
      replaceComponents(page.id, [...(page.components || []), created]);
    }
  };

  const saveSite = async () => {
    await upsertSite(token, project.id, { name: project.name, slug: siteSlug });
    alert("Guardado. Puedes publicar.");
  };

  const publish = async () => {
    await publishSite(token, project.id);
    alert(`Publicado en /s/${siteSlug}`);
  };

  if(!project) return <div className="p-6">Cargando…</div>;

  return (
    <div className="grid grid-cols-12 gap-6 p-6">
      <aside className="col-span-3 space-y-3">
        <h3 className="font-semibold">Componentes</h3>
        <div className="space-y-2">
          {PALETTE.map(i => <PaletteItem key={i.type} item={i} />)}
        </div>

        <div className="mt-6 space-y-2">
          <h3 className="font-semibold">Páginas</h3>
          {project.pages.map(p => (
            <button key={p.id} onClick={()=>setCurrentPage(p.id)}
              className={`w-full text-left px-3 py-2 rounded border ${p.id===currentPageId?'bg-black text-white':''}`}>
              {p.name}
            </button>
          ))}
        </div>

        <div className="mt-6 space-y-2">
          <h3 className="font-semibold">Publicación</h3>
          <input className="w-full px-3 py-2 border rounded" placeholder="slug-del-sitio"
                 value={siteSlug} onChange={e=>setSiteSlug(e.target.value)} />
          <button onClick={saveSite} className="w-full px-3 py-2 text-white bg-gray-800 rounded">Guardar sitio</button>
          <button onClick={publish} className="w-full px-3 py-2 text-white bg-green-600 rounded">Publicar</button>
        </div>
      </aside>

      <main className="col-span-9">
        <h2 className="mb-3 text-xl font-semibold">{project.name} — {page?.name}</h2>
        <DndContext sensors={sensors} collisionDetection={closestCenter} onDragEnd={handleDragEnd}>
          <Canvas components={page?.components ?? []} />
        </DndContext>
      </main>
    </div>
  );
}
