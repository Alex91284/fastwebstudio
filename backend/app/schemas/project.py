from pydantic import BaseModel
from typing import Optional


# 🔹 Base común para crear/actualizar proyectos
class ProjectBase(BaseModel):
    name: str
    description: Optional[str] = None
    url: Optional[str] = None


# 🔹 Esquema para creación de proyectos
class ProjectCreate(ProjectBase):
    pass


# 🔹 Esquema para respuesta de proyectos
class ProjectOut(ProjectBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
        orm_mode = True