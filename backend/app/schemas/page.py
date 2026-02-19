from pydantic import BaseModel
from typing import List, Optional
from .component import ComponentOut

# class PageBase(BaseModel):
#     title: str
#     slug: str
#     content: Optional[str] = None

class PageCreate(BaseModel):
    name: str
    slug: Optional[str] = None

class PageUpdate(BaseModel):
    name: Optional[str] = None
    slug: Optional[str] = None
    order: Optional[int] = None

class PageOut(BaseModel):
    id: int
    name: str
    slug: str | None
    order: int
    class Config:
        from_attributes = True
        from_attributes = True

class PageFull(PageOut):
    components: List[ComponentOut] = []