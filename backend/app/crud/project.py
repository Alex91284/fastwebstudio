from sqlalchemy.orm import Session
from app import models, schemas

def create_project(db: Session, project: schemas.ProjectCreate, user_id: int):
    db_project = models.Project(**project.dict(), user_id=user_id)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def get_projects_by_user(db: Session, user_id: int):
    return db.query(models.Project).filter(models.Project.user_id == user_id).all()

def get_projects(db: Session):
    return db.query(models.project.Project).all()

def get_project(db: Session, project_id: int):
    return db.query(models.project.Project).filter(models.project.Project.id == project_id).first()

def update_project(db: Session, project_id: int, updated: schemas.project.ProjectCreate):
    project = get_project(db, project_id)
    if project:
        for key, value in updated.model_dump().items():
            setattr(project, key, value)
        db.commit()
        db.refresh(project)
    return project

def delete_project(db: Session, project_id: int):
    project = get_project(db, project_id)
    if project:
        db.delete(project)
        db.commit()
    return project
