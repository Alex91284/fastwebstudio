from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import project as project_schema
from app.crud import project as project_crud
from app.db.session import get_db

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.post("/", response_model=project_schema.ProjectOut)
def create_project(project: project_schema.ProjectCreate, db: Session = Depends(get_db)):
    return project_crud.create_project(db, project)

@router.get("/", response_model=list[project_schema.ProjectOut])
def get_projects(db: Session = Depends(get_db)):
    return project_crud.get_projects(db)

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
