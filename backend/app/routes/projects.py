from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import project as project_schema
from app.crud import project as project_crud
from app.db.session import get_db
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import decode_jwt

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.post("/", response_model=project_schema.ProjectOut, dependencies=[Depends(JWTBearer())])
def create_project(
    project: project_schema.ProjectCreate,
    token: str = Depends(JWTBearer()),
    db: Session = Depends(get_db),
    ):
    payload = decode_jwt(token)
    user_id = payload.get("user_id")
    if not user_id:
        raise HTTPException(status_code=403, detail="Token inválido o expirado")
    return project_crud.create_project(db, project, user_id)

@router.get("/", response_model=list[project_schema.ProjectOut], dependencies=[Depends(JWTBearer())])
def get_projects(
    token: str = Depends(JWTBearer()),
    db: Session = Depends(get_db)
):
    payload = decode_jwt(token)
    user_id = payload.get("user_id")
    if not user_id:
        raise HTTPException(status_code=403, detail="Token inválido o expirado")
    return project_crud.get_projects_by_user(db, user_id)

@router.get("/{project_id}", response_model=project_schema.ProjectOut)
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = project_crud.get_project(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    return project

@router.put("/{project_id}", response_model=project_schema.ProjectOut)
def update_project(project_id: int, updated: project_schema.ProjectCreate, db: Session = Depends(get_db)):
    result = project_crud.update_project(db, project_id, updated)
    if not result:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    return result

@router.delete("/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db)):
    deleted = project_crud.delete_project(db, project_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    return {"detail": "Proyecto eliminado"}
