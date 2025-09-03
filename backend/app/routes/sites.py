from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.site import SiteCreate, SiteUpdate, SiteOut, PublicSite
from app.crud import site as site_crud
from app.crud import project as project_crud
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import decode_jwt

router = APIRouter(prefix="/sites", tags=["sites"])

@router.get("/", response_model=list[SiteOut])
def list_sites(db: Session = Depends(get_db)):   
    return site_crud.get_sites(db)

@router.get("/{site_id}", response_model=SiteOut)
def get_site(site_id: int, db: Session = Depends(get_db)):
    site = site_crud.get_site(db, site_id)
    if not site:
        raise HTTPException(status_code=404, detail="Site not found")
    return site

@router.post("/", response_model=SiteOut)
def create_site(site: SiteCreate, db: Session = Depends(get_db)):
    return site_crud.create_site(db, site)

@router.put("/{site_id}", response_model=SiteOut)
def update_site(site_id: int, site: SiteUpdate, db: Session = Depends(get_db)):
    return site_crud.update_site(db, site_id, site)

@router.delete("/{site_id}", response_model=SiteOut)
def delete_site(site_id: int, db: Session = Depends(get_db)):
    return site_crud.delete_site(db, site_id)