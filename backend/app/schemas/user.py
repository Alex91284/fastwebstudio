from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str
    role: str

class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None

class UserOut(UserBase):
    id: int
    role: str

class UserLogin(BaseModel):
    email: str
    password: str


    class Config:
        from_attributes = True
