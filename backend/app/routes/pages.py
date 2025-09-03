from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.page import PageCreate, PageUpdate, PageFull, PageOut
from app.models.page import Page
from app.crud import page as page_crud
from app.auth.auth_bearer import JWTBearer

router = APIRouter(prefix="/pages", tags=["Pages"])

@router.post("/{project_id}", response_model=PageOut)
def create_page(project_id: int, data: PageCreate, db: Session = Depends(get_db)):
    return page_crud.create_page(db, project_id, data)


# @router.get("/project/{project_id}", response_model=List[PageOut])
# def list_by_project(project_id: int, db: Session = Depends(get_db)):
#     return crud_page.get_pages_by_project(db, project_id)

# @router.get("/{page_id}", response_model=PageOut)
# def retrieve(page_id: int, db: Session = Depends(get_db)):
#     page = crud_page.get_page(db, page_id)
#     if not page:
#         raise HTTPException(status_code=404, detail="Page not found")
#     return page

@router.put("/{page_id}", response_model=PageOut)
def update_page(page_id: int, data: PageUpdate, db: Session = Depends(get_db)):
    page = page_crud.update_page(db, page_id, data)
    if not page: raise HTTPException(404, "Page not found")
    return page

@router.delete("/{page_id}")
def delete_page(page_id: int, db: Session = Depends(get_db)):
    page_crud.delete_page(db, page_id)
    return {"ok": True}
