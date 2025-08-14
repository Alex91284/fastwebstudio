from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    name: str
    email: str
    password: str
    role: str

class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None

class UserOut(UserBase):
    id: int

class UserLogin(BaseModel):
    email: str
    password: str


    class Config:
        from_attributes = True
