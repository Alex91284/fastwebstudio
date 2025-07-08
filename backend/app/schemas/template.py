from pydantic import BaseModel
from typing import Optional

class TemplateBase(BaseModel):
    name: str
    description: str | None = None

class TemplateCreate(TemplateBase):
    pass

class TemplateUpdate(TemplateBase):
    pass

class TemplateOut(TemplateBase):
    id: int

    class Config:
        from_attributes = True  # Pydantic v2
