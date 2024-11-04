from fastapi import APIRouter

from app.api.routes import auth, health, users

api_router = APIRouter()
api_router.include_router(health.router, tags=["health"])
api_router.include_router(auth.router, tags=["login"])
api_router.include_router(users.router, prefix="/user", tags=["user"])
