from sqlalchemy.orm import Session
from app.models.project import Project
from app.models.page import Page
from app.schemas.project import ProjectCreate

def create_project(db: Session, user_id: int, data: ProjectCreate) -> Project:
    project = Project(name=data.name, user_id=user_id)
    db.add(project); db.commit(); db.refresh(project)
    # página inicial
    first = Page(title="Inicio", slug="inicio", project_id=project.id, order=0)
    db.add(first); db.commit()
    return project

def get_projects_by_user(db: Session, user_id: int):
    return db.query(Project).filter(Project.user_id == user_id).all()


def get_projects(db: Session):
    return db.query(Project).all()


def get_project(db: Session, project_id: int):
    return db.query(Project).filter(Project.id == project_id).first()

def get_full_project(db: Session, project_id: int, user_id: int):
    return db.query(Project).filter(Project.id==project_id, Project.user_id==user_id).first()

def update_project(db: Session, project_id: int, updated: ProjectCreate):
    project = get_project(db, project_id)
    if project:
        print(f"✏️ Actualizando proyecto {project_id} con {updated.dict()}")  # Debug
        for key, value in updated.dict().items():
            setattr(project, key, value)
        db.commit()
        db.refresh(project)
    return project


def delete_project(db: Session, project_id: int):
    project = get_project(db, project_id)
    if project:
        print(f"🗑️ Eliminando proyecto {project_id}")  # Debug
        db.delete(project)
        db.commit()
    return project
