from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas import component as component_schema
from app.crud import component as component_crud
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=component_schema.ComponentOut)
def create_component(component: component_schema.ComponentCreate, db: Session = Depends(get_db)):
    return component_crud.create_component(db, component)

@router.get("/page/{page_id}", response_model=List[component_schema.ComponentOut])
def list_components_by_page(page_id: int, db: Session = Depends(get_db)):
    return component_crud.get_components_by_page(db, page_id)

@router.get("/{component_id}", response_model=component_schema.ComponentOut)
def get_component(component_id: int, db: Session = Depends(get_db)):
    db_component = component_crud.get_component(db, component_id)
    if not db_component:
        raise HTTPException(status_code=404, detail="Component not found")
    return db_component

@router.put("/{component_id}", response_model=component_schema.ComponentOut)
def update_component(component_id: int, component: component_schema.ComponentUpdate, db: Session = Depends(get_db)):
    updated = component_crud.update_component(db, component_id, component)
    if not updated:
        raise HTTPException(status_code=404, detail="Component not found")
    return updated

@router.delete("/{component_id}")
def delete_component(component_id: int, db: Session = Depends(get_db)):
    deleted = component_crud.delete_component(db, component_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Component not found")
    return {"ok": True}
