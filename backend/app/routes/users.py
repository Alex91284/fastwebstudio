from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import decode_jwt, sign_jwt
from app.models.user import User
from app.schemas import user as schemas
from app.crud import user as crud_user

router = APIRouter(prefix="/users", tags=["Users"])

# -------------------------------
# 📌 Registro de usuario
# -------------------------------
@router.post("/", response_model=dict)  # 👈 devolvemos dict en vez de UserOut
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Crear usuario en DB
    new_user = crud_user.create_user(db, user)

    # Generar token JWT con la info del usuario
    token = sign_jwt({
        "id": new_user.id,
        "name": new_user.name,
        "email": new_user.email,
        "role": new_user.role,
    })

    # Devolver usuario + token (para que el frontend lo guarde)
    return {
        "access_token": token["access_token"],
        "user": {
            "id": new_user.id,
            "name": new_user.name,
            "email": new_user.email,
            "role": new_user.role
        }
    }

# -------------------------------
# 📌 Listar usuarios
# -------------------------------
@router.get("/", response_model=list[schemas.UserOut])
def list_users(db: Session = Depends(get_db)):
    return crud_user.get_users(db)

# -------------------------------
# 📌 Obtener un usuario por ID
# -------------------------------
@router.get("/{user_id}", response_model=schemas.UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = crud_user.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# -------------------------------
# 📌 Actualizar usuario
# -------------------------------
@router.put("/{user_id}", response_model=schemas.UserOut)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    updated = crud_user.update_user(db, user_id, user)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

# -------------------------------
# 📌 Eliminar usuario
# -------------------------------
@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted = crud_user.delete_user(db, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}

# -------------------------------
# 📌 Obtener info del usuario logueado
# -------------------------------
@router.get("/me", dependencies=[Depends(JWTBearer())])
def get_user_data(token: str = Depends(JWTBearer()), db: Session = Depends(get_db)):
    payload = decode_jwt(token)
    user_id = payload.get("user_id")
    if not user_id:
        raise HTTPException(status_code=403, detail="Invalid or expired token")

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "role": user.role,
    }
