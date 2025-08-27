import os
from dotenv import load_dotenv
import time
from typing import Dict
from jose import jwt, JWTError, ExpiredSignatureError
from passlib.context import CryptContext

load_dotenv()

# Clave secreta y algoritmo
SECRET_KEY = os.getenv("SECRET_KEY", "mi_clave_secreta_default")
ALGORITHM = os.getenv("ALGORITHM", "HS256")

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

# 🔹 Firmar JWT
def sign_jwt(user: dict) -> Dict[str, str]:
    payload = {
        "user_id": user["id"],
        "name": user["name"],
        "email": user["email"],
        "role": user["role"],
        "exp": int (time.time()) + 3600  # Token válido por 1 hora
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token}

# 🔹 Decodificar JWT
def decode_jwt(token: str) -> dict:
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print("✅ PAYLOAD DECODIFICADO:", decoded)  # 👈 Debug
        return decoded
    except ExpiredSignatureError:
        print("❌ TOKEN EXPIRADO")
        return {}
    except JWTError as e:
        print("❌ ERROR JWT:", e)
        return {}
    except Exception as e:
        print("❌ ERROR GENERAL DECODIFICANDO TOKEN:", e)
        return {}

# 🔹 Manejo de contraseñas
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
