from pydantic import BaseModel
from typing import Optional

class SiteBase(BaseModel):
    name: str
    domain: str
    project_id: int

class SiteCreate(SiteBase):
    pass

class SiteUpdate(BaseModel):
    name: Optional[str]
    domain: Optional[str]

class SiteOut(SiteBase):
    id: int

    class Config:
        from_attributes = True 
