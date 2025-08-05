from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    nombre: str
    email: EmailStr

class UserCreate(UserBase):
    name: str
    email: str
    password: str
    role: str

class UserUpdate(BaseModel):
    nombre: str | None = None
    email: EmailStr | None = None

class UserOut(UserBase):
    id: int

class UserLogin(BaseModel):
    email: str
    password: str


    class Config:
        from_attributes = True
