from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserOut
from app.crud import user
from app.db.session import get_db
from typing import List

router = APIRouter()

@router.post("/", response_model=UserOut)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    return user.create_user(db, user_data)

@router.get("/", response_model=List[UserOut])
def list_users(db: Session = Depends(get_db)):
    return user.get_users(db)
