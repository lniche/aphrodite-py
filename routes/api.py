from fastapi import APIRouter
from app.http.api import auth
from app.http.api import user

api_router = APIRouter()

api_router.include_router(auth.router, tags=["Auth Module"])

api_router.include_router(user.router, tags=["User Module"])
