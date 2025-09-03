from pydantic import BaseModel
from typing import Optional
from .project import ProjectFull

# class SiteBase(BaseModel):
#     name: str
#     domain: str
#     project_id: int

class SiteCreate(BaseModel):
    name: str
    slug: str
class SiteUpdate(BaseModel):
    name: Optional[str] = None
    slug: Optional[str] = None
    is_published: Optional[bool] = None

class SiteOut(BaseModel):
    id: int
    name: str
    slug: str
    is_published: bool
    class Config:
        from_attributes = True 

class PublicSite(BaseModel):
    site: SiteOut
    project: ProjectFull