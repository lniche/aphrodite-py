import datetime
from typing import Optional
from fastapi import APIRouter, Depends, Body, Request
from starlette.responses import JSONResponse

from app.http.deps import get_db
from app.schemas.auth import LoginReq, LoginResp, SendVerifyCodeReq
from app.schemas.response import Result
from app.services.auth import random_code_verifier
from app.support.helper import is_chinese_cellphone
from app.models.user import User
from app.http import deps

from datetime import timedelta

from app.exceptions.exception import AuthenticationError
from app.models.user import User
from app.services.auth import jwt_helper, hashing, random_code_verifier
from app.support.helper import alphanumeric_random
from config.auth import settings
import logging

router = APIRouter(
    prefix="/v1"
)


@router.post("/login", response_model=LoginResp, dependencies=[Depends(get_db)])
def login(request: Request, req: LoginReq):
    phone = req.phone
    code = req.code
    if not random_code_verifier.check(phone, code):
        raise AuthenticationError(message='Incorrect verification code')
    client_ip = request.client.host
    token = create_token_response_from_user(user)
    user = User.get_or_none(User.phone == phone)
    if not user:
        nickname = 'SUGAR_' + user.phone[-4:]
        user = User.create(
            nickname=nickname,
            login_at=datetime.now(),
            login_token=token,
            client_ip=client_ip,
            phone=phone
        )
    else:
        user.login_at = datetime.now()
        user.login_token = token
        user.client_ip = client_ip
        user.save()

    response_data = LoginResp(
        access_token=token
    )
    return Result.ok(response_data)


@router.post("/send-code")
def send_verification_code(req: SendVerifyCodeReq):
    phone = req.phone
    if not is_chinese_cellphone(phone):
        return Result.err("invalid phone")
    code = random_code_verifier.make(phone)
    logging.info(f"Send verification code: {code} to phone: {phone}")
    # TODO fake send
    return Result.ok()


@router.post("/logout", dependencies=[Depends(get_db)])
def logout(auth_user: User = Depends(deps.get_auth_user)):
    auth_user.login_token = ""
    auth_user.save()
    return Result.ok()


def create_token_response_from_user(user):
    expires_delta = timedelta(minutes=settings.JWT_TTL)
    expires_in = int(expires_delta.total_seconds())
    token = jwt_helper.create_access_token(user.id, expires_delta)

    return token
