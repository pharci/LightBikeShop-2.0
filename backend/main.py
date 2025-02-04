from routes import auth, site
from bot.bot import bot
from fastapi import FastAPI
from db.db import init_db
from routes import bot_rout
import os
from fastapi.middleware.cors import CORSMiddleware
from middlewares.cache import CacheControlMiddleware
import logging
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware.sessions import SessionMiddleware
from middlewares.auth import AuthMiddleware
from fastapi.responses import FileResponse
from fastadmin import fastapi_app as admin_app
from admin.views import setup_admin


app = FastAPI(debug=True)
app.mount("/admin", admin_app)

setup_admin()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(SessionMiddleware, secret_key=os.getenv("SECRET_KEY", "defaultsecret"))
app.add_middleware(AuthMiddleware)

app.include_router(bot_rout.router)
app.include_router(auth.router)
app.include_router(site.router)

@app.on_event("startup")
async def startup_event():
    print("Установка вебхука.")
    await init_db()
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_webhook(f"{os.getenv("WEBHOOK_URL")}/webhook")

    # from crud.user import createsuperuser
    # await createsuperuser("admin", "root")

@app.on_event("shutdown")
async def shutdown_event():
    await bot.delete_webhook(drop_pending_updates=True)



logging.basicConfig(level=logging.DEBUG)  # Для вывода всех логов
logger = logging.getLogger("uvicorn.error")

@app.middleware("http")
async def log_requests(request, call_next):
    logger.debug(f"Request: {request.method} {request.url}")
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        logger.exception(f"Unhandled error: {e}")
        raise