from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/")
async def home() -> str:
    return "Thank you for using aphrodite!"


@router.get("/ping")
async def ping() -> str:
    return "pong"
