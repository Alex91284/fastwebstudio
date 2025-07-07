from pydantic import BaseModel
from typing import Optional

class PageBase(BaseModel):
    title: str
    slug: str
    content: Optional[str] = None

class PageCreate(PageBase):
    project_id: int

class PageUpdate(PageBase):
    pass

class PageOut(PageBase):
    id: int
    project_id: int

    class Config:
        from_attributes = True
