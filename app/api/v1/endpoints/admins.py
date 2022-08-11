from fastapi import APIRouter


router = APIRouter(prefix="/admins", tags=["Users"])


@router.get(path="/test",
             summary="Test",
             status_code=200)
async def registration():
    return {"msg": "hello world"}
