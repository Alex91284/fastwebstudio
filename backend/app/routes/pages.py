from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.schemas.page import PageCreate, PageOut, PageUpdate
from app.crud import page as crud_page

router = APIRouter(prefix="/pages", tags=["Pages"])

@router.post("/", response_model=PageOut)
def create(page: PageCreate, db: Session = Depends(get_db)):
    return crud_page.create_page(db, page)

@router.get("/project/{project_id}", response_model=List[PageOut])
def list_by_project(project_id: int, db: Session = Depends(get_db)):
    return crud_page.get_pages_by_project(db, project_id)

@router.get("/{page_id}", response_model=PageOut)
def retrieve(page_id: int, db: Session = Depends(get_db)):
    page = crud_page.get_page(db, page_id)
    if not page:
        raise HTTPException(status_code=404, detail="Page not found")
    return page

@router.put("/{page_id}", response_model=PageOut)
def update(page_id: int, page_data: PageUpdate, db: Session = Depends(get_db)):
    return crud_page.update_page(db, page_id, page_data)

@router.delete("/{page_id}", response_model=PageOut)
def delete(page_id: int, db: Session = Depends(get_db)):
    return crud_page.delete_page(db, page_id)
