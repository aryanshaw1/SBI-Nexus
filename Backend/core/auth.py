from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "sbi_nexus_secret_key"
ALGORITHM = "HS256"

def create_access_token(data: dict):
    payload = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=15)

    payload.update({"exp": expire})

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )