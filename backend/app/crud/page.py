from sqlalchemy.orm import Session
from app.models.page import Page
from app.schemas.page import PageCreate, PageUpdate

def create_page(db: Session, page_data: PageCreate) -> Page:
    page = Page(**page_data.dict())
    db.add(page)
    db.commit()
    db.refresh(page)
    return page

def get_pages_by_project(db: Session, project_id: int):
    return db.query(Page).filter(Page.project_id == project_id).all()

def get_page(db: Session, page_id: int):
    return db.query(Page).filter(Page.id == page_id).first()

def update_page(db: Session, page_id: int, data: PageUpdate):
    page = get_page(db, page_id)
    if page:
        for key, value in data.dict().items():
            setattr(page, key, value)
        db.commit()
        db.refresh(page)
    return page

def delete_page(db: Session, page_id: int):
    page = get_page(db, page_id)
    if page:
        db.delete(page)
        db.commit()
    return page
