from sqlalchemy.orm import Session
from app.models.component import Component
from app.schemas.component import ComponentCreate, ComponentUpdate

def create_component(db: Session, page_id: int, data: ComponentCreate):
    comp = Component(page_id=page_id, **data.dict())
    db.add(comp); db.commit(); db.refresh(comp)
    return comp

# def get_components_by_page(db: Session, page_id: int):
#     return db.query(Component).filter(Component.page_id == page_id).order_by(Component.order).all()

# def get_component(db: Session, component_id: int):
#     return db.query(Component).filter(Component.id == component_id).first()

def update_component(db: Session, comp_id: int, data: ComponentUpdate):
    comp = db.get(Component, comp_id)
    if not comp: return None
    for k, v in data.dict(exclude_none=True).items():
        setattr(comp, k, v)
    db.commit(); db.refresh(comp)
    return comp

def delete_component(db: Session, comp_id: int):
    comp = db.get(Component, comp_id)
    if comp:
        db.delete(comp); db.commit()
    return True
