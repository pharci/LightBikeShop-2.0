import jwt
import datetime
import os

SECRET_KEY = os.getenv("SECRET_KEY", "defaultsecret")

def create_access_token(data: dict, expires_delta: datetime.timedelta = None):
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.datetime.utcnow() + expires_delta
    else:
        expire = datetime.datetime.utcnow() + datetime.timedelta(hours=1)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")

    return encoded_jwt

def decode_access_token(token: str):
    try:
        decoded_jwt = jwt.decode(token, SECRET_KEY, algorithms=["HS256"], options={"require": ["exp"]})
        
        if decoded_jwt["exp"] < datetime.utcnow().timestamp():
            raise jwt.ExpiredSignatureError("Token has expired")
        
        return decoded_jwt
    except jwt.ExpiredSignatureError:
        raise Exception("Token has expired")
    except jwt.InvalidTokenError:
        raise Exception("Invalid token")
    except Exception as e:
        # Обработка ошибок, если что-то пошло не так
        raise Exception(f"Error decoding token: {str(e)}")