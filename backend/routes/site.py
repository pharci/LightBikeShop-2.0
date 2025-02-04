from fastapi import APIRouter, Request

from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from db.models import *
router = APIRouter()

@router.get("/api/message")
async def get_message():
    return {"message": "Привет из FastAPI!"}
