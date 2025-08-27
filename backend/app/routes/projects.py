from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import project as project_schema
from app.crud import project as project_crud
from app.db.session import get_db
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import decode_jwt

router = APIRouter(prefix="/projects", tags=["Projects"])

# 📌 Crear proyecto asociado al usuario autenticado
@router.post("/", response_model=project_schema.ProjectOut, dependencies=[Depends(JWTBearer())])
def create_project(
    project: project_schema.ProjectCreate,
    db: Session = Depends(get_db),
    token: str = Depends(JWTBearer())
):
    payload = decode_jwt(token)
    print("📦 Payload create_project:", payload)

    user_id = payload.get("user_id")   # 👈 siempre user_id
    if not user_id:
        raise HTTPException(status_code=403, detail="Invalid or expired token")

    return project_crud.create_project(db, project, user_id)


# 📌 Listar proyectos del usuario autenticado
@router.get("/", response_model=list[project_schema.ProjectOut], dependencies=[Depends(JWTBearer())])
def get_projects(db: Session = Depends(get_db), token: str = Depends(JWTBearer())):
    payload = decode_jwt(token)
    print("📦 Payload get_projects:", payload)

    user_id = payload.get("user_id")   # 👈 siempre user_id
    if not user_id:
        raise HTTPException(status_code=403, detail="Invalid or expired token")

    return project_crud.get_projects_by_user(db, user_id)


# 📌 Obtener un proyecto por ID (solo si pertenece al usuario autenticado)
@router.get("/{project_id}", response_model=project_schema.ProjectOut, dependencies=[Depends(JWTBearer())])
def get_project(project_id: int, db: Session = Depends(get_db), token: str = Depends(JWTBearer())):
    payload = decode_jwt(token)
    print("📦 Payload get_project:", payload)

    user_id = payload.get("user_id")
    project = project_crud.get_project(db, project_id)

    if not project or project.user_id != user_id:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")

    return project


# 📌 Actualizar proyecto (solo dueño)
@router.put("/{project_id}", response_model=project_schema.ProjectOut, dependencies=[Depends(JWTBearer())])
def update_project(
    project_id: int,
    updated: project_schema.ProjectCreate,
    db: Session = Depends(get_db),
    token: str = Depends(JWTBearer())
):
    payload = decode_jwt(token)
    print("📦 Payload update_project:", payload)

    user_id = payload.get("user_id")
    project = project_crud.get_project(db, project_id)

    if not project or project.user_id != user_id:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")

    return project_crud.update_project(db, project_id, updated)


# 📌 Eliminar proyecto (solo dueño)
@router.delete("/{project_id}", dependencies=[Depends(JWTBearer())])
def delete_project(project_id: int, db: Session = Depends(get_db), token: str = Depends(JWTBearer())):
    payload = decode_jwt(token)
    print("📦 Payload delete_project:", payload)

    user_id = payload.get("user_id")
    project = project_crud.get_project(db, project_id)

    if not project or project.user_id != user_id:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")

    deleted = project_crud.delete_project(db, project_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")

    return {"detail": "Proyecto eliminado"}