from db.models.user import User
from crud.user import get_user_by_username, get_user_by_id
from admin.access_token import create_access_token

from sqladmin.authentication import AuthenticationBackend

from fastapi import HTTPException, Request, status

class AdminAuth(AuthenticationBackend):
    def __init__(self, secret_key: str):
        self.secret_key = secret_key
        self.middlewares = []

    async def login(self, request: Request) -> bool:
        form = await request.form()
        username, password = form["username"], form["password"]
        user = await get_user_by_username(username)

        if user is None or not user.verify_password(password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Неверный логин или пароль"
            )
            
        user_data = {"id": user.id, "username": user.username}
        access_token = create_access_token(data=user_data)
        request.session.update({"token": access_token, "user": user_data})
        return True

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        user = request.session.get("user")

        if not user:
            return False
        
        user = await get_user_by_id(user["id"])

        if user is None or not (user.is_staff or user.is_superuser):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="У пользователя нет прав для доступа."
            )
        
        return True
    
authentication_backend = AdminAuth(secret_key="asdasd")