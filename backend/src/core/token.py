import jwt
import os
from datetime import datetime, timedelta
from fastapi import Cookie
import uuid
from core.responce import error_response


SECRET_KEY = os.getenv("SECRET_KEY", "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7")
ALGORITHM = os.getenv("ALGORITHM", "HS256")



def create_access_token(employee_id:uuid.UUID,role:str):
    try:
        payload = {
            "id": str(employee_id),
            "role":role,
            "exp": datetime.utcnow() + timedelta(minutes=30)
        }

        token = jwt.encode(
            payload,
            SECRET_KEY,
            algorithm=ALGORITHM
        )
        return token
    except Exception as e:
        print(e)

def get_current_user(access_token: str | None = Cookie(default=None)):
    # print(access_token)
    if access_token is None:
        raise error_response("Login First", 401)
    try:
        payload = jwt.decode(
            access_token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload
    except Exception as e:
        print(e,"hi")
        raise error_response("un autherized", 401)
