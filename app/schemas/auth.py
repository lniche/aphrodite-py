from typing import Optional
from pydantic import BaseModel, Field


class LoginReq(BaseModel):
    phone: str = Field(..., example="13800138000")
    code: str = Field(..., example="1234")


class LoginResp(BaseModel):
    access_token: Optional[str] = Field(None,
                                        example="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...")


class SendVerifyCodeReq(BaseModel):
    phone: str = Field(..., example="13800138000")
