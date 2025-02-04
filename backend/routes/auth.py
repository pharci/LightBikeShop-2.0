from fastapi import APIRouter, Depends, Request, HTTPException
from fastapi.responses import RedirectResponse, HTMLResponse
import hashlib
import hmac
import time
import jwt
from datetime import datetime, timedelta
from admin.access_token import create_access_token

from crud.user import get_user_by_username
from schemas.user import LoginData

from fastapi import Request

router = APIRouter()

# def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=30)) -> str:
#     to_encode = data.copy()
#     expire = datetime.utcnow() + expires_delta
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm="HS256")
#     return encoded_jwt

# def verify_telegram_data(telegram_data, token):
#     auth_date = telegram_data.get('auth_date')
#     hash_value = telegram_data.get('hash')
    
#     if not auth_date or not hash_value:
#         return False

#     data_check_string = '\n'.join(f"{k}={v}" for k, v in sorted(telegram_data.items()) if k != 'hash')

#     secret_key = hashlib.sha256(token.encode()).digest()
#     check_hash = hmac.new(secret_key, data_check_string.encode(), hashlib.sha256).hexdigest()

#     return hmac.compare_digest(check_hash, hash_value) and (int(time.time()) - int(auth_date)) < 86400

# @router.get("/login")
# async def login_via_telegram(request: Request):
#     telegram_data = request.query_params
#     if "hash" in telegram_data:
#         if not verify_telegram_data(telegram_data, token=settings.TELEGRAM_TOKEN):
#             raise HTTPException(status_code=403, detail="Telegram verification failed.")
        
#         if telegram_data.get("username"):
#             username = telegram_data.get("username")
#         else:
#             username = "Отсутствует"
        
#         user_data = UserCreate(user_id=telegram_data.get("id"), username=username, first_name=telegram_data.get("first_name"))
#         user = await get_or_create_user(user_data)

#         if not(user.is_staff or user.is_superuser):
#             raise HTTPException(status_code=403, detail="No access.")

#         token = create_access_token(data={"user_id": user.user_id, "first_name": user.first_name})

#         response = RedirectResponse("/admin")
#         response.set_cookie(key="access_token", value=token, httponly=True)
#         return response
    
#     return templates.TemplateResponse("login.html", {"request": request})

# @router.get("/login", response_class=HTMLResponse)
# async def main(request: Request):
#     return templates.TemplateResponse("accounts/login.html", {"request": request})

@router.post("/api/login")
async def login(data: LoginData, request: Request):
    user = await get_user_by_username(data.username)
    
    if user is None or not user.verify_password(data.password):
        raise HTTPException(status_code=401, detail="Неверный логин или пароль")
    
    user_data = {"id": user.id, "username": user.username}
    access_token = create_access_token(data=user_data)
    print(access_token, user_data)
    request.session.update({"token": access_token, "user": user_data})
    return {"user": user_data}

@router.get("/api/user")
async def login(request: Request):
    user = request.session.get("user")
    if not user:
        raise HTTPException(status_code=401, detail="Неавторизован")

    return {"user": user}

@router.get("api/logout")
async def logout(request: Request):
    request.session.clear()
    response = RedirectResponse("/login")
    return response