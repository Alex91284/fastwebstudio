from sqlalchemy.orm import Session
from app.schemas import component as schemas
from app import models

def create_component(db: Session, component: schemas.ComponentCreate):
    db_component = models.Component(**component.dict())
    db.add(db_component)
    db.commit()
    db.refresh(db_component)
    return db_component

def get_components_by_page(db: Session, page_id: int):
    return db.query(models.Component).filter(models.Component.page_id == page_id).order_by(models.Component.order).all()

def get_component(db: Session, component_id: int):
    return db.query(models.Component).filter(models.Component.id == component_id).first()

def update_component(db: Session, component_id: int, component: schemas.ComponentUpdate):
    db_component = get_component(db, component_id)
    if not db_component:
        return None
    for field, value in component.dict(exclude_unset=True).items():
        setattr(db_component, field, value)
    db.commit()
    db.refresh(db_component)
    return db_component

def delete_component(db: Session, component_id: int):
    db_component = get_component(db, component_id)
    if db_component:
        db.delete(db_component)
        db.commit()
    return db_component
