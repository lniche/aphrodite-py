from fastapi import APIRouter, Depends, Body
from starlette.responses import JSONResponse

from app.http.deps import get_db
from app.schemas.auth import Token
from app.schemas.response import Result
from app.services.auth import random_code_verifier
from app.services.auth.grant import PasswordGrant, CellphoneGrant
from app.services.auth.oauth2_schema import OAuth2PasswordRequest, OAuth2CellphoneRequest
from app.support.helper import is_chinese_cellphone
from app.models.user import User
from app.http import deps

router = APIRouter(
    prefix="/v1"
)


@router.post("/login", response_model=Token, dependencies=[Depends(get_db)])
def login(request_data: OAuth2CellphoneRequest):
    grant = CellphoneGrant(request_data)
    return grant.respond()


@router.post("/send-code")
def send_verification_code(phone: str = Body(..., embed=True)):
    if not is_chinese_cellphone(phone):
        return JSONResponse(status_code=422, content={"message": 'invalid phone'})

    code = random_code_verifier.make(phone)
    # TODO fake send
    return {"success": True}


@router.post("/logout", dependencies=[Depends(get_db)])
def login(auth_user: User = Depends(deps.get_auth_user)):

    return Result.ok("")
