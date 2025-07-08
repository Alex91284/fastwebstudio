from sqlalchemy.orm import Session
from app.schemas import site as schemas
from app.models import site as models

def get_sites(db: Session):
    return db.query(models.Site).all()

def get_site(db: Session, site_id: int):
    return db.query(models.Site).filter(models.Site.id == site_id).first()

def create_site(db: Session, site: schemas.SiteCreate):
    db_site = models.Site(**site.dict())
    db.add(db_site)
    db.commit()
    db.refresh(db_site)
    return db_site

def update_site(db: Session, site_id: int, site: schemas.SiteUpdate):
    db_site = get_site(db, site_id)
    if db_site:
        for field, value in site.dict(exclude_unset=True).items():
            setattr(db_site, field, value)
        db.commit()
        db.refresh(db_site)
    return db_site

def delete_site(db: Session, site_id: int):
    db_site = get_site(db, site_id)
    if db_site:
        db.delete(db_site)
        db.commit()
    return db_site
