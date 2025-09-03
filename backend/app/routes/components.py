from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.component import ComponentCreate, ComponentUpdate, ComponentOut
from app.crud import component as comp_crud
from app.auth.auth_bearer import JWTBearer
from typing import List

router = APIRouter(prefix="/components", tags=["components"], dependencies=[Depends(JWTBearer())])

@router.post("/{page_id}", response_model=ComponentOut)
def create_component(page_id: int, data: ComponentCreate, db: Session = Depends(get_db)):
    return comp_crud.create_component(db, page_id, data)

@router.get("/page/{page_id}", response_model=List[ComponentOut])
def list_components_by_page(page_id: int, db: Session = Depends(get_db)):
    return comp_crud.get_components_by_page(db, page_id)

@router.get("/{component_id}", response_model=ComponentOut)
def get_component(component_id: int, db: Session = Depends(get_db)):
    db_component = comp_crud.get_component(db, component_id)
    if not db_component:
        raise HTTPException(status_code=404, detail="Component not found")
    return db_component

@router.put("/{component_id}", response_model=ComponentOut)
def update_component(component_id: int, data: ComponentUpdate, db: Session = Depends(get_db)):
    comp = comp_crud.update_component(db, component_id, data)
    if not comp: raise HTTPException(404, "Component not found")
    return comp

@router.delete("/{component_id}")
def delete_component(component_id: int, db: Session = Depends(get_db)):
    deleted = comp_crud.delete_component(db, component_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Component not found")
    return {"ok": True}
