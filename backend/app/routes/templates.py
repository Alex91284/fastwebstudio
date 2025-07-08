from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas import template as template_schema
from app.crud import template as template_crud
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=template_schema.TemplateOut)
def create_template(
    template: template_schema.TemplateCreate,
    db: Session = Depends(get_db)
):
    return template_crud.create_template(db, template)

@router.get("/", response_model=List[template_schema.TemplateOut])
def read_templates(db: Session = Depends(get_db)):
    return template_crud.get_templates(db)

@router.get("/{template_id}", response_model=template_schema.TemplateOut)
def read_template(template_id: int, db: Session = Depends(get_db)):
    db_template = template_crud.get_template(db, template_id)
    if not db_template:
        raise HTTPException(status_code=404, detail="Template not found")
    return db_template

@router.put("/{template_id}", response_model=template_schema.TemplateOut)
def update_template(
    template_id: int,
    updated_data: template_schema.TemplateUpdate,
    db: Session = Depends(get_db)
):
    return template_crud.update_template(db, template_id, updated_data)

@router.delete("/{template_id}")
def delete_template(template_id: int, db: Session = Depends(get_db)):
    return template_crud.delete_template(db, template_id)
