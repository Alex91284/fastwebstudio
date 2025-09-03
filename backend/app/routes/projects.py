from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.project import ProjectCreate, ProjectOut, ProjectFull
from app.crud import project as project_crud
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import decode_jwt

router = APIRouter(prefix="/projects", tags=["Projects"])

# 📌 Crear proyecto asociado al usuario autenticado
@router.post("", response_model=ProjectOut, dependencies=[Depends(JWTBearer())])
def create_project(data: ProjectCreate, db: Session = Depends(get_db), token: str = Depends(JWTBearer())):
    user_id = decode_jwt(token).get("user_id")
    return project_crud.create_project(db, user_id, data)


# 📌 Listar proyectos del usuario autenticado
@router.get("", response_model=list[ProjectOut], dependencies=[Depends(JWTBearer())])
def list_my_projects(db: Session = Depends(get_db), token: str = Depends(JWTBearer())):
    user_id = decode_jwt(token).get("user_id")
    return project_crud.get_projects_by_user(db, user_id)


# 📌 Obtener un proyecto por ID (solo si pertenece al usuario autenticado)
@router.get("/{project_id}", response_model=ProjectOut, dependencies=[Depends(JWTBearer())])
def get_project(project_id: int, db: Session = Depends(get_db), token: str = Depends(JWTBearer())):
    payload = decode_jwt(token)
    print("📦 Payload get_project:", payload)

    user_id = payload.get("user_id")
    project = project_crud.get_project(db, project_id)

    if not project or project.user_id != user_id:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")

    return project


# 📌 Actualizar proyecto (solo dueño)
@router.put("/{project_id}", response_model=ProjectOut, dependencies=[Depends(JWTBearer())])
def update_project(
    project_id: int,
    updated: ProjectCreate,
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

# Obtener proyecto completo con páginas y componentes
@router.get("/{project_id}/full", response_model=ProjectFull, dependencies=[Depends(JWTBearer())])
def get_full(project_id: int, db: Session = Depends(get_db), token: str = Depends(JWTBearer())):
    user_id = decode_jwt(token).get("user_id")
    proj = project_crud.get_full_project(db, project_id, user_id)
    if not proj: raise HTTPException(404, "Project not found")
    return proj