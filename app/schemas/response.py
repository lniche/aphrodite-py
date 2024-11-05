from tkinter import E
from typing import Any, Dict, Optional
from pydantic import BaseModel
import json


class StatusCode:
    # common errors
    OK = 0
    Err = -1
    ERR_BAD_REQUEST = 400
    ERR_UNAUTHORIZED = 401
    ERR_FORBIDDEN = 403
    ERR_NOT_FOUND = 404
    ERR_METHOD_NOT_ALLOWED = 405
    ERR_INTERNAL_SERVER_ERROR = 500
    # more biz errors
    ERR_DATA = 1001
    ERR_SERVICE = 1002

    @staticmethod
    def get_error_message(code: int) -> str:
        messages = {
            StatusCode.ERR_BAD_REQUEST: "Bad Request",
            StatusCode.ERR_UNAUTHORIZED: "Unauthorized",
            StatusCode.ERR_FORBIDDEN: "Forbidden",
            StatusCode.ERR_NOT_FOUND: "Not Found",
            StatusCode.ERR_METHOD_NOT_ALLOWED: "Method Not Allowed",
            StatusCode.ERR_INTERNAL_SERVER_ERROR: "Internal Server Error",
            StatusCode.ERR_DATA: "Data Error",
            StatusCode.ERR_SERVICE: "Service Error",
        }
        return messages.get(code, "Unknown Error")


class Result(BaseModel):
    code: int
    message: str
    data: Any

    @classmethod
    def ok(cls, data: Optional[Any] = None, message: str = "ok") -> "Result":
        return cls(code=StatusCode.OK, message=message, data=data)

    @classmethod
    def err(cls, status_code: Optional[Any] = None, message: str = "err") -> "Result":
        if status_code is None:
            status_code = StatusCode.ERR_INTERNAL_SERVER_ERROR
            message = StatusCode.get_error_message(status_code)
        return cls(code=status_code, message=message, data=None)
