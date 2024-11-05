from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class UpdateUser(BaseModel):
    nickname: Optional[str] = Field(None, example="john")
    email: Optional[str] = Field(None, example="john@example.com")


class GetUserResp(BaseModel):
    user_code: Optional[str] = Field(None, example="A8000")
    user_no: Optional[str] = Field(None, example="100000")
    phone: Optional[str] = Field(None, example="13800138000")
    nickname: Optional[str] = Field(None, example="john")
    email: Optional[str] = Field(None, example="john@example.com")
