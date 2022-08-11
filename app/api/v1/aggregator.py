from fastapi import APIRouter

from app.api.v1.endpoints import admins

api_router = APIRouter(prefix="/v1")
api_router.include_router(admins.router)
