from fastapi import APIRouter, Depends

from app.http import deps
from app.http.deps import get_db
from app.models.user import User
from app.schemas.response import Result
from app.schemas.user import UserDetail

router = APIRouter(
    prefix="/v1/user"
)


@router.get("", response_model=UserDetail, dependencies=[Depends(get_db)])
def get_user(auth_user: User = Depends(deps.get_auth_user)):
    return auth_user


@router.put("", dependencies=[Depends(get_db)])
def update_user(auth_user: User = Depends(deps.get_auth_user)):

    return Result.ok("")


@router.delete("", dependencies=[Depends(get_db)])
def delete_user(auth_user: User = Depends(deps.get_auth_user)):

    return Result.ok("")
