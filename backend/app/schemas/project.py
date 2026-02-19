from pydantic import BaseModel
from typing import List, Optional
from .page import PageOut


# # 🔹 Base común para crear/actualizar proyectos
# class ProjectBase(BaseModel):
#     name: str
#     description: Optional[str] = None
#     url: Optional[str] = None


# 🔹 Esquema para creación de proyectos
class ProjectCreate(BaseModel):
    name: str


# 🔹 Esquema para respuesta de proyectos
class ProjectOut(BaseModel):
    id: int
    name: str
    class Config: 
        from_attributes = True
        from_attributes = True

class ProjectFull(BaseModel):
    id: int
    name: str
    pages: List[PageOut] = []
    class Config:
        from_attributes = True
        from_attributes = True