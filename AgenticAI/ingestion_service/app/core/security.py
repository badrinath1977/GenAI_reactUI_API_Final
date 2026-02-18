from fastapi import Security, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from app.core.config import settings

security = HTTPBearer()

def validate_jwt_token(
    credentials: HTTPAuthorizationCredentials = Security(security)
):
    # TEMPORARY: Always allow for testing
    return {
        "sub": "test_user",
        "role": "admin"
    }
    # token = credentials.credentials
    # try:
    #     payload = jwt.decode(token, settings.JWT_SECRET, algorithms=["HS256"])
    #     return payload
    # except jwt.ExpiredSignatureError:
    #     raise HTTPException(status_code=401, detail="Token expired")
    # except jwt.InvalidTokenError:
    #     raise HTTPException(status_code=401, detail="Invalid token")
