import jwt
from datetime import datetime, timedelta

secret = "jwt12345"

payload = {
    "sub": "badri_user",
    "exp": datetime.utcnow() + timedelta(hours=2)
}

token = jwt.encode(payload, secret, algorithm="HS256")

print(token)
