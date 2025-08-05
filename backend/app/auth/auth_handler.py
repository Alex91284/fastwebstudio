import os
import time
from typing import Dict
from jose import jwt
from passlib.context import CryptContext

# Clave secreta y algoritmo
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def sign_jwt(user: dict) -> Dict[str, str]:
    payload = {
        "user_id": user["id"],
        "name": user["name"],
        "email": user["email"],
        "role": user["role"],  
        "exp": time.time() + 3600  # Token válido por 1 hora
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token}

def decode_jwt(token: str) -> dict:
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except:
        return {}

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
