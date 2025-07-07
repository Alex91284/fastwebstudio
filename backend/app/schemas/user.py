from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    nombre: str
    email: EmailStr

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    nombre: str | None = None
    email: EmailStr | None = None

class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True
