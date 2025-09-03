from pydantic import BaseModel
from typing import Any, Dict, Optional

# class ComponentBase(BaseModel):
#     type: str
#     content: str
#     order: int | None = None
#     page_id: int

class ComponentCreate(BaseModel):
    type: str
    order: int = 0
    parent_id: Optional[int] = None
    props: Dict[str, Any] = {}
    styles: Dict[str, Any] = {}

class ComponentUpdate(BaseModel):
    order: Optional[int] = None
    parent_id: Optional[int] = None
    props: Optional[dict] = None
    styles: Optional[dict] = None

class ComponentOut(BaseModel):
    id: int
    type: str
    order: int
    parent_id: int | None
    props: dict
    styles: dict
    page_id: int
    class Config:
        from_attributes = True
