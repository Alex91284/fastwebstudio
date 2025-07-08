from pydantic import BaseModel

class ComponentBase(BaseModel):
    type: str
    content: str
    order: int | None = None
    page_id: int

class ComponentCreate(ComponentBase):
    pass

class ComponentUpdate(BaseModel):
    type: str | None = None
    content: str | None = None
    order: int | None = None

class ComponentOut(ComponentBase):
    id: int

    class Config:
        from_attributes = True
