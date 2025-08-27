from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Request, HTTPException
from jose import JWTError
from app.auth.auth_handler import decode_jwt

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        if credentials:
            print("🔐 TOKEN RECIBIDO:", credentials.credentials)
            
            payload = decode_jwt(credentials.credentials)
            print("📦 PAYLOAD DECODIFICADO:", payload)

            # 👇 Validamos que realmente exista "user_id" en el payload
            if not payload.get("user_id"):
                raise HTTPException(status_code=403, detail="Invalid or expired token")
            
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwt_token: str) -> bool:
        try:
            payload = decode_jwt(jwt_token)
            return bool(payload)
        except JWTError:
            return False
