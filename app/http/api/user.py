from typing import Optional
from fastapi import APIRouter, Depends

from app.http import deps
from app.http.deps import get_db
from app.models.user import User
from app.schemas.response import Result, StatusCode
from app.schemas.user import UpdateUser, GetUserResp

router = APIRouter(
    prefix="/v1/user"
)


@router.get("/{user_code}", dependencies=[Depends(get_db)])
def get_user(user_code: Optional[str] = None, auth_user: User = Depends(deps.get_auth_user)):
    if user_code:
        user_info = User.get_or_none(User.user_code == user_code)
        if not user_info:
            raise Result.err(StatusCode.ERR_DATA)
    else:
        user_info = auth_user
    response_data = GetUserResp(
        user_code=user_info.user_code,
        user_no=auth_user.user_no,
        email=auth_user.email,
        nickname=auth_user.nickname,
        phone=auth_user.phone,
    )
    return Result.ok(response_data)


@router.put("", dependencies=[Depends(get_db)])
def update_user(update_user: UpdateUser, auth_user: User = Depends(deps.get_auth_user)):
    if update_user.email is not None:
        auth_user.email = update_user.email
    if auth_user.nickname is not None:
        auth_user.nickname = update_user.nickname
    auth_user.save()
    return Result.ok()


@router.delete("", dependencies=[Depends(get_db)])
def delete_user(auth_user: User = Depends(deps.get_auth_user)):
    auth_user.status = 3
    auth_user.save()
    return Result.ok()
