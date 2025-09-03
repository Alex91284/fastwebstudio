from sqlalchemy.orm import Session
from datetime import datetime
from app.models.site import Site
from app.models.project import Project
from app.schemas.site import SiteCreate, SiteUpdate

def get_sites(db: Session):
    return db.query(Site).all()

def get_site(db: Session, site_id: int):
    return db.query(Site).filter(Site.id == site_id).first()

def create_site(db: Session, site: SiteCreate):
    db_site = Site(**site.dict())
    db.add(db_site)
    db.commit()
    db.refresh(db_site)
    return db_site

def update_site(db: Session, site_id: int, site: SiteUpdate):
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

def upsert_site(db: Session, project_id: int, data: SiteCreate | SiteUpdate):
    site = db.query(Site).filter(Site.project_id==project_id).first()
    if not site:
        site = Site(project_id=project_id, name=data.name, slug=data.slug, is_published=False)
        db.add(site); db.commit(); db.refresh(site)
    else:
        for k, v in data.dict(exclude_none=True).items():
            setattr(site, k, v)
        db.commit(); db.refresh(site)
    return site

def publish_site(db: Session, project_id: int):
    site = db.query(Site).filter(Site.project_id==project_id).first()
    if not site: return None
    site.is_published = True
    site.published_at = datetime.utcnow()
    db.commit(); db.refresh(site)
    return site

def get_site_by_slug(db: Session, slug: str):
    return db.query(Site).filter(Site.slug==slug, Site.is_published==True).first()
