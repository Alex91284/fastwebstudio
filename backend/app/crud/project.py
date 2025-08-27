from sqlalchemy.orm import Session
from app.models.project import Project   # ✅ Import correcto
from app.schemas import project as project_schema


def create_project(db: Session, project: project_schema.ProjectCreate, user_id: int):
    print(f"🟢 Creando proyecto para user_id={user_id}, datos={project.dict()}")  # Debug
    db_project = Project(**project.dict(), user_id=user_id)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


def get_projects_by_user(db: Session, user_id: int):
    print(f"📂 Buscando proyectos del user_id={user_id}")  # Debug
    return db.query(Project).filter(Project.user_id == user_id).all()


def get_projects(db: Session):
    return db.query(Project).all()


def get_project(db: Session, project_id: int):
    return db.query(Project).filter(Project.id == project_id).first()


def update_project(db: Session, project_id: int, updated: project_schema.ProjectCreate):
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
