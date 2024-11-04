from fastapi import APIRouter
from app.api.response import Result

router = APIRouter()


@router.get("/")
async def home() -> str:
    return "Thank you for using aphrodite!"


@router.get("/ping")
async def ping() -> Result:
    return Result.ok("pong")
