from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import site as schemas
from app.crud import site as crud
from app.db.session import get_db

router = APIRouter()

@router.get("/", response_model=list[schemas.SiteOut])
def list_sites(db: Session = Depends(get_db)):   
    return crud.get_sites(db)

@router.get("/{site_id}", response_model=schemas.SiteOut)
def get_site(site_id: int, db: Session = Depends(get_db)):
    site = crud.get_site(db, site_id)
    if not site:
        raise HTTPException(status_code=404, detail="Site not found")
    return site

@router.post("/", response_model=schemas.SiteOut)
def create_site(site: schemas.SiteCreate, db: Session = Depends(get_db)):
    return crud.create_site(db, site)

@router.put("/{site_id}", response_model=schemas.SiteOut)
def update_site(site_id: int, site: schemas.SiteUpdate, db: Session = Depends(get_db)):
    return crud.update_site(db, site_id, site)

@router.delete("/{site_id}", response_model=schemas.SiteOut)
def delete_site(site_id: int, db: Session = Depends(get_db)):
    return crud.delete_site(db, site_id)