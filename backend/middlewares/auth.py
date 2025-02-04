from fastapi import Request
from fastapi.responses import RedirectResponse
from starlette.middleware.base import BaseHTTPMiddleware
import jwt
import os
from datetime import datetime

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.url.path in ["/login", "/admin"]:
            response = await call_next(request)
            return response

        token = request.cookies.get("token")

        if not token:
            response = await call_next(request)
            return response

        try:
            decoded_jwt = jwt.decode(token, os.getenv("SECRET_KEY", "defaultsecret"), algorithms=["HS256"], options={"require": ["exp"]})
            exp_timestamp = decoded_jwt["exp"]
            current_timestamp = datetime.utcnow().timestamp()

            if exp_timestamp < current_timestamp:
                request.session.clear()
                return RedirectResponse(url="/login")
            
            request.state.user = decoded_jwt

        except Exception as e:
            return RedirectResponse(url="/login")
        
        response = await call_next(request)
        return response