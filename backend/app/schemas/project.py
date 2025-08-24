from pydantic import BaseModel

class ProjectBase(BaseModel):
    name: str
    description: str | None = None
    url: str | None = None

class ProjectCreate(ProjectBase):
    pass

class ProjectOut(ProjectBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
