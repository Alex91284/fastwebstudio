from sqlalchemy.orm import Session
from app.models.page import Page
from app.schemas.page import PageCreate, PageUpdate

def create_page(db: Session, project_id: int, data: PageCreate):
    page = Page(name=data.name, slug=data.slug, project_id=project_id, order=999)
    db.add(page); db.commit(); db.refresh(page)
    return page

# def get_pages_by_project(db: Session, project_id: int):
#     return db.query(Page).filter(Page.project_id == project_id).all()

# def get_page(db: Session, page_id: int):
#     return db.query(Page).filter(Page.id == page_id).first()

def update_page(db: Session, page_id: int, data: PageUpdate):
    page = db.get(Page, page_id)
    if not page: return None
    for k, v in data.dict(exclude_none=True).items():
        setattr(page, k, v)
    db.commit(); db.refresh(page)
    return page

def delete_page(db: Session, page_id: int):
    page = db.get(Page, page_id)
    if page: 
        db.delete(page); db.commit()
    return True
